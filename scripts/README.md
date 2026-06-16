# AI GRC Engineering Scripts

> Working Python automation built on the NIST AI RMF methodology documented
> in `frameworks/nist-ai-rmf/`. These scripts engineer the manual GRC
> processes from Modules 5-7 into repeatable, auditable systems.

---

## Scripts in this folder

| Script | Purpose | Module reference |
|---|---|---|
| `risk_rating.py` | Encodes the likelihood-severity heat map as a function | Module 5 |
| `generate_risk_register.py` | Generates a scored, formatted risk register from a CSV | Module 5 |
| `risk_tier_classifier.py` | Classifies an AI system intake into a risk tier (1-4) | Module 4 |
| `check_evidence_staleness.py` | Flags overdue control evidence before an auditor does | Module 7 |
| `package_evidence.py` | Packages audit-ready evidence with a manifest | Module 7 |

---

## Requirements

```bash
pip install pandas openpyxl
```

---

## Quick start

**Calculate a single risk rating:**
```bash
python risk_rating.py
```

**Generate a risk register from a CSV:**
```bash
python generate_risk_register.py identified_risks.csv risk_register.xlsx
```

**Classify a system's risk tier:**
```bash
python risk_tier_classifier.py
```

**Check for overdue evidence:**
```bash
python check_evidence_staleness.py evidence_inventory.csv status_report.xlsx
```

**Package evidence for an audit request:**
```bash
python package_evidence.py benefits_eligibility_ai ./evidence ./control_mapping.json ./audit_packages
```

---

## Sample CSV format for `generate_risk_register.py`

```csv
risk_id,risk_type,description,likelihood,severity,trustworthy_ai_property
RISK-001,Bias & discrimination,Training data underrepresents rural patients,High,Critical,Fair & unbiased
RISK-002,Explainability,Model cannot explain individual decisions,Medium,High,Explainable
RISK-003,Privacy,System transmits PII to third-party vendor without BAA,High,High,Privacy-enhanced
```

## Sample CSV format for `check_evidence_staleness.py`

```csv
control_id,control_name,evidence_type,last_updated,frequency_days,owner
BF-002,Quarterly bias audit,Audit report,2026-01-15,90,GRC Engineer
HO-002,Override rate monitoring,Monthly report,2026-05-01,30,GRC Engineer
```

---

*BridgeCore AI LLC — AI Governance Practice*
