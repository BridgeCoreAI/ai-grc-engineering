# Module 8 — GRC Engineering & Automation
## From documents to systems

> **Framework:** NIST AI Risk Management Framework (AI RMF 1.0)
> **Module:** 8 of 10
> **Status:** ✅ Complete

---

## The mindset shift

A GRC analyst writes a risk assessment in Word. A GRC engineer writes a script
that generates the risk assessment, scores every risk consistently using the
same logic every time, and produces the same document in minutes instead of hours.

A GRC analyst manually checks whether a control was operated correctly. A GRC
engineer builds a system that automatically flags when a control's evidence is
missing or overdue — before an auditor ever asks the question.

This is not about replacing judgment with automation. Risk identification,
treatment decisions, and escalation still require human expertise. It is about
automating the repetitive, error-prone, time-consuming parts so human expertise
gets applied where it actually matters.

---

## The engineering chain

```
Policy → Control → Workflow → Script → Dashboard → Report
```

Same chain as the GRC governance chain from Module 6 — now expressed in code.

---

## Five things a GRC engineer builds

### 1. Risk register engine
Encodes the Module 5 likelihood-severity matrix as code. Takes a CSV of
identified risks and produces a scored, sorted, formatted risk register.

**Why it matters:** Once the rating matrix exists as code, it can never be
applied inconsistently. See `scripts/risk_rating.py` and
`scripts/generate_risk_register.py` in this repository.

### 2. Risk tier classifier
Encodes the Module 4 intake classification logic. Takes intake responses
(decision autonomy, affected population, population size, sensitive data) and
returns a defensible, auditable Tier 1-4 classification applied identically
every time. See `scripts/risk_tier_classifier.py`.

### 3. CI validation pipeline
A GitHub Actions workflow that validates governance documentation on every
commit — checking required fields, valid ratings, and evidence currency. Applies
continuous integration principles directly to GRC documentation. See
`.github/workflows/validate-governance-docs.yml`.

### 4. Evidence staleness tracker
Reads an evidence inventory and flags any control evidence that is overdue
based on its required refresh frequency — catching gaps before an auditor does.
See `scripts/check_evidence_staleness.py`.

### 5. Evidence packager
Assembles all evidence for a specific AI system into an audit-ready ZIP archive
with a manifest mapping every document to its control. Turns a 48-hour audit
document request into a same-day response. See `scripts/package_evidence.py`.

---

## Engineering principle 1 — turn the risk rating matrix into code

```python
def calculate_risk_rating(likelihood, severity):
    """
    Calculates a composite risk rating from likelihood and severity scores
    per the NIST AI RMF heat map.
    """
    matrix = {
        ('Low', 'Low'): 'Accept',
        ('Low', 'Medium'): 'Accept',
        ('Low', 'High'): 'Low',
        ('Low', 'Critical'): 'Medium',
        ('Medium', 'Low'): 'Low',
        ('Medium', 'Medium'): 'Low',
        ('Medium', 'High'): 'Medium',
        ('Medium', 'Critical'): 'High',
        ('High', 'Low'): 'Low',
        ('High', 'Medium'): 'Medium',
        ('High', 'High'): 'High',
        ('High', 'Critical'): 'Critical',
    }
    rating = matrix.get((likelihood, severity))
    if rating is None:
        raise ValueError(f"Invalid combination: {likelihood}, {severity}")
    return rating
```

A junior analyst manually filling a spreadsheet might mis-rate a risk due to a
typo. The function cannot make that mistake. This is the foundation every
other automation in this module builds on.

---

## Engineering principle 2 — automate the risk register

```python
import pandas as pd
from datetime import datetime

def generate_risk_register(input_csv_path, output_path):
    """
    Reads a CSV of identified risks and generates a scored risk register.
    Expected columns: risk_id, risk_type, description, likelihood, severity
    """
    df = pd.read_csv(input_csv_path)
    df['composite_rating'] = df.apply(
        lambda row: calculate_risk_rating(row['likelihood'], row['severity']),
        axis=1
    )
    rating_order = {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3, 'Accept': 4}
    df['sort_order'] = df['composite_rating'].map(rating_order)
    df = df.sort_values('sort_order').drop('sort_order', axis=1)
    df['assessment_date'] = datetime.now().strftime('%Y-%m-%d')

    summary = df['composite_rating'].value_counts().to_dict()
    print(f"Risk Register Summary: {summary}")

    df.to_excel(output_path, index=False, sheet_name='Risk Register')
    return df, summary
```

**What this replaces:** a 45-minute clerical task (typing risks, looking up
ratings, sorting, counting for the executive summary) becomes a 3-second
script execution with zero arithmetic errors.

---

## Engineering principle 3 — automate risk tier classification

```python
def classify_risk_tier(decision_autonomy, affected_population,
                        population_size, contains_sensitive_data):
    """
    Classifies an AI system into a risk tier based on intake responses.
    Returns: tier (1-4), score, and review_track
    """
    score = 0
    autonomy_scores = {'out_of_loop': 3, 'on_the_loop': 2, 'in_the_loop': 1}
    score += autonomy_scores.get(decision_autonomy, 0)

    high_impact = ['customers_public', 'patients', 'job_applicants',
                   'government_beneficiaries']
    if affected_population in high_impact:
        score += 2

    size_scores = {'over_100000': 2, '10000_to_100000': 2,
                    '1000_to_10000': 1, '100_to_1000': 0, 'under_100': 0}
    score += size_scores.get(population_size, 0)

    if contains_sensitive_data:
        score += 2

    if score >= 7:
        return {'tier': 1, 'label': 'Critical', 'score': score,
                'review_track': 'Full AI Review Board approval required.'}
    elif score >= 5:
        return {'tier': 2, 'label': 'High', 'score': score,
                'review_track': 'Full AI Review Board approval required.'}
    elif score >= 3:
        return {'tier': 3, 'label': 'Medium', 'score': score,
                'review_track': 'GRC lead approval sufficient.'}
    else:
        return {'tier': 4, 'label': 'Low', 'score': score,
                'review_track': 'Expedited review.'}
```

**Federal application:** this function becomes the engine behind an actual
AI intake portal — replacing inconsistent manual classification, where
different reviewers might classify the same system differently, with a
single, defensible, auditable standard applied identically every time.

---

## Engineering principle 4 — the evidence staleness tracker

```python
import pandas as pd
from datetime import datetime

def check_evidence_staleness(evidence_inventory_path, output_path):
    """
    Flags evidence that is overdue based on its required refresh frequency.
    Expected columns: control_id, control_name, evidence_type,
    last_updated, frequency_days, owner
    """
    df = pd.read_csv(evidence_inventory_path, parse_dates=['last_updated'])
    today = datetime.now()
    df['days_since_update'] = (today - df['last_updated']).dt.days

    def get_status(row):
        days_overdue = row['days_since_update'] - row['frequency_days']
        if days_overdue > 30:
            return 'CRITICAL - Severely Overdue'
        elif days_overdue > 0:
            return 'OVERDUE'
        elif row['frequency_days'] - row['days_since_update'] <= 7:
            return 'DUE SOON'
        else:
            return 'CURRENT'

    df['status'] = df.apply(get_status, axis=1)
    needs_attention = df[df['status'] != 'CURRENT'].sort_values(
        'days_since_update', ascending=False
    )

    print(f"Total controls tracked: {len(df)}")
    print(f"Controls needing attention: {len(needs_attention)}")

    df.to_excel(output_path, index=False, sheet_name='Evidence Status')
    return df, needs_attention
```

**Why this is the single highest-value script:** this is exactly the tool
that prevents the Module 7 worked example scenario — a quarterly bias audit
planned but not executed for two quarters. Run weekly, it gives early warning
the moment evidence becomes overdue, instead of discovering the gap during
pre-audit self-assessment with limited time to remediate.

---

## Engineering principle 5 — GitHub Actions for continuous governance validation

```yaml
# .github/workflows/validate-governance-docs.yml
name: Validate AI Governance Documentation

on:
  push:
    paths:
      - 'risk-assessments/**'
      - 'control-evidence/**'

jobs:
  validate-risk-assessments:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install pandas openpyxl
      - name: Validate risk register completeness
        run: python scripts/validate_risk_register.py
      - name: Check for missing required fields
        run: python scripts/check_required_fields.py
      - name: Flag overdue evidence
        run: python scripts/check_evidence_staleness.py
```

**What this achieves:** every time anyone updates a risk assessment or adds
evidence, this workflow runs automatically and checks required fields, valid
ratings, and evidence currency. Continuous governance validation — the same
principle as continuous integration in software engineering, applied to GRC.

---

## Engineering principle 6 — the evidence packager for audit response

```python
import os, shutil, zipfile, json
from datetime import datetime

def package_evidence_for_audit(system_name, evidence_root_path,
                                  control_mapping_path, output_dir):
    """
    Packages all evidence for an AI system into an audit-ready ZIP with
    a manifest mapping every document to its control.
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    package_name = f"{system_name}_evidence_package_{timestamp}"
    package_path = os.path.join(output_dir, package_name)
    os.makedirs(package_path, exist_ok=True)

    with open(control_mapping_path, 'r') as f:
        control_mapping = json.load(f)

    manifest = {'system_name': system_name, 'package_generated': timestamp,
                'documents': []}

    system_evidence_path = os.path.join(evidence_root_path, system_name)
    if os.path.exists(system_evidence_path):
        for category in os.listdir(system_evidence_path):
            category_path = os.path.join(system_evidence_path, category)
            if os.path.isdir(category_path):
                dest = os.path.join(package_path, category)
                shutil.copytree(category_path, dest)
                for file in os.listdir(category_path):
                    manifest['documents'].append({
                        'filename': file, 'category': category,
                        'mapped_control': control_mapping.get(category, 'Unmapped')
                    })

    manifest_path = os.path.join(package_path, 'MANIFEST.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

    zip_path = f"{package_path}.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, package_path)
                zipf.write(file_path, arcname)

    print(f"Evidence package created: {zip_path}")
    return zip_path, manifest
```

**Federal scenario this solves:** an auditor's PBC list requests "all evidence
related to the bias risk assessment for the benefits eligibility AI system,
within 48 hours." This script generates a complete, organized,
manifest-documented package in seconds instead of a manual document hunt.

---

## Putting it all together — the operational pipeline

| Stage | What happens | Automated? |
|---|---|---|
| Intake | New AI system proposed | Risk tier classifier runs automatically |
| Assessment | Risks identified through structured sessions | **Stays human — requires expert judgment** |
| Scoring | Identified risks rated and registered | Risk register generator runs automatically |
| Control | Controls selected from library, assigned to owners | Evidence inventory tracker monitors automatically |
| Continuous validation | Every repo update checked | GitHub Actions workflow runs automatically |
| Audit response | Evidence requested by auditor | Evidence packager runs automatically |

This is the complete engineering layer underneath Modules 5, 6, and 7 —
turning manual GRC processes into a repeatable, auditable, scalable system.
This is what makes BridgeCore an "AI GRC engineering" practice rather than a
traditional compliance consultancy.

---

## Key terms

| Term | Plain meaning |
|---|---|
| GRC engineering | Translating governance, risk, and compliance requirements into automated, repeatable technical systems |
| Continuous validation | Automatically checking governance documentation for completeness on every change |
| Evidence staleness | When evidence has not been refreshed within its required frequency window |
| Manifest | Document listing every file in an evidence package and its mapped control |
| Pipeline | A connected sequence of automated steps processing data from input to output |
| CI/CD for governance | Applying continuous integration principles to compliance documentation |

---

## Practice questions

1. What is the fundamental difference between a GRC analyst's work and a GRC engineer's work?
2. Why does encoding the risk rating matrix as a function eliminate a category of error?
3. What does the evidence staleness checker prevent, per the Module 7 worked example?
4. Why should validation trigger on every push rather than running manually monthly?
5. In the operational pipeline, which stage should NOT be automated, and why?
6. What does a manifest file accomplish that a simple folder of files does not?

---

## How to explain it in an interview

> "GRC engineering is the discipline of translating governance requirements
> into automated, repeatable technical systems rather than relying on manual
> documents and spreadsheets. I build Python scripts that encode risk-scoring
> logic so ratings are never applied inconsistently, automated evidence
> staleness checkers that flag overdue controls before an auditor finds the
> gap, GitHub Actions workflows that validate governance documentation on
> every commit, and evidence packaging scripts that turn a 48-hour audit
> document request into a same-day response. Risk identification and
> treatment decisions require human judgment and stay human — but everything
> downstream of that judgment should be engineered into a system that runs
> the same way every time."

---

*Previous: [Module 7 — Audit Readiness & Evidence](module-07-audit-readiness.md)*
*Next: Module 9 — Practical Templates (coming soon)*
