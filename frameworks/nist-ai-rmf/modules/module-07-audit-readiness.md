# Module 7 — Audit Readiness & Evidence
## What to keep · How to organize it · How to survive an audit

> **Framework:** NIST AI Risk Management Framework (AI RMF 1.0)
> **Module:** 7 of 10
> **Status:** ✅ Complete

---

## Why this module matters most for federal work

Every prior module answers "how do we govern AI responsibly?" Module 7 answers
a different question: **"how do we prove it?"**

Federal agencies are not penalized for having risks — every AI system has risks.
They are penalized for being unable to demonstrate those risks were identified,
assessed, and managed. The IG, GAO, and OMB expect evidence of a functioning
governance process, not perfection.

This is where BridgeCore's value proposition becomes concrete: not just AI
governance consulting, but an evidence-generating system that survives scrutiny.

---

## The four types of federal AI oversight

### Inspector General (IG) audits

Independent audits, evaluations, and investigations conducted by each agency's
Office of Inspector General. AI is an increasing OIG focus area due to:
- Algorithmic bias risk in benefits, law enforcement, hiring decisions
- Data privacy concerns with AI processing of citizen data
- Procurement irregularities in AI vendor contracts
- Lack of documented governance processes

**What OIG audits examine:**
- Whether an AI governance policy exists and is followed
- Whether AI systems are inventoried and risk-classified
- Whether risk assessments were conducted before deployment
- Whether human oversight requirements are met and evidenced
- Whether vendor contracts include required AI governance clauses
- Whether incidents were properly reported and remediated

**Typical process:** Notification letter + PBC (Provided By Client) document
list → entrance conference → fieldwork (document review, interviews) →
draft report for management response → final report.

### GAO reviews

Conducted at the request of Congress or under statutory mandate. Broader and
more public than OIG audits — findings often become public reports affecting
agency reputation and funding.

**What GAO examines:**
- Compliance with OMB AI guidance government-wide
- Cross-agency AI governance maturity comparison
- Federal AI Use Case Inventory completeness
- Impact assessments for rights-impacting and safety-impacting systems

### OMB compliance reporting (M-24-10)

A recurring compliance obligation, not a traditional audit. Agencies must:
- Maintain a public AI use case inventory
- Designate a Chief AI Officer
- Conduct impact assessments for safety-impacting and rights-impacting systems
- Implement minimum risk management practices for those systems
- Report annually on AI governance maturity

### Third-party / customer assurance reviews

Not government audits, but operate similarly — customers verifying an AI
vendor's governance program meets procurement standards before contracting.

---

## The eight core evidence categories

### Category 1 — AI system inventory
The foundational artifact every audit starts with. Must contain for every system:
system name, owner, business purpose, risk classification, rights/safety-impacting
status, vendor or internal status, last risk assessment date, last validation date,
deployment status, and links to full documentation.

**Why it matters most:** An incomplete inventory is the single most damaging
audit finding. It suggests ungoverned AI systems may exist without anyone's
knowledge — and can trigger a much broader, more invasive audit.

### Category 2 — Risk assessments
Complete Module 5-style assessments. Auditors sample systems and review depth.
They check: was the assessment pre- or post-deployment? Are ratings evidence-based?
Were the right people involved? Were Critical/High risks actually treated?

### Category 3 — Testing results
Fairness, security, performance, and adversarial robustness results.

**The evidence quality test:** Could an independent reviewer understand exactly
what was tested, what method was used, what the results were, and whether they
met a defined threshold? Vague or undated results are flagged as insufficient
even if testing occurred.

### Category 4 — Approval records
Signed governance committee decisions. Audit-proof records are: dated and
signed by actual decision-makers, reference the specific assessment reviewed,
state the actual decision and conditions, and show conditions tracked to closure.

### Category 5 — Human oversight records
Override logs, review documentation, training records. Receives particular
scrutiny because human oversight is explicitly required by OMB M-24-10 for
rights-impacting and safety-impacting systems. Auditors may request live
demonstration of override functionality.

### Category 6 — Monitoring logs
Performance dashboards, drift detection, bias audit results post-deployment.

**Key insight:** Pre-deployment assessment is now table stakes. Post-deployment
monitoring is what differentiates mature governance programs. Excellent
pre-deployment documentation with no monitoring evidence still gets negative findings.

### Category 7 — Incident reports
Documentation of incidents, near-misses, root cause analysis, remediation.

**Counter-intuitive principle:** Documented incidents are not automatically
a negative finding. What damages outcomes is (a) incidents with no documentation
— suggesting concealment — or (b) documented incidents with no remediation
evidence — suggesting the organization doesn't learn from failures.

### Category 8 — Audit trails
Logs of governance actions — who approved deployment, who changed the model,
who reviewed quarterly audits, who accepted residual risk, and when. This is
the most neglected category because it requires disciplined documentation of
routine governance activity, not just high-visibility risk assessment.

---

## The evidence quality standard

| Quality | Test | Example |
|---|---|---|
| Specific | Not vague | "Fairness testing conducted 3/14/26 using four-fifths rule across 5 demographic categories; 0.91 ratio, exceeds 0.80 threshold" vs. "model was tested for bias" |
| Dated and attributable | Has a date and named owner | Undated evidence cannot establish a timeline |
| Independently verifiable | Methodology and data shown, not just assertion | Could someone outside the building team reach the same conclusion? |
| Consistent across sources | No contradictions between documents | Risk register says "High," exec summary says "minor concern" = a finding itself |
| Retained for required period | Correct retention schedule applied | Destroying evidence too early is itself a compliance failure |

---

## Building the audit-ready evidence package

### Step 1 — Map evidence to control library
For every Module 6 control, identify exactly what evidence it generates,
where it is stored, and who owns keeping it current. This is your
**evidence inventory** — a master mapping of control to evidence location.

### Step 2 — Establish a central evidence repository

```
AI-Governance-Evidence/
├── 01-System-Inventory/
├── 02-Risk-Assessments/
│   └── [System-Name]/
├── 03-Testing-Results/
│   └── [System-Name]/
├── 04-Approval-Records/
├── 05-Human-Oversight/
│   └── [System-Name]/
├── 06-Monitoring-Logs/
│   └── [System-Name]/
├── 07-Incident-Reports/
└── 08-Audit-Trails/
```

### Step 3 — Conduct a pre-audit self-assessment
Walk through OMB M-24-10 requirements and publicly available IG audit
programs from other agencies. Confirm evidence exists for each requirement
before any real audit begins.

### Step 4 — Identify and remediate gaps before the auditor does
Two choices for any gap: generate missing evidence now if time allows, or
prepare an honest explanation and remediation plan if not.

**The worst outcome:** being surprised by your own gaps in real time, in
front of the auditor.

### Step 5 — Prepare key personnel for interviews
Ensure the AI Risk Owner, system managers, and staff understand their
accountabilities, where evidence lives, and how to answer honestly —
not coached talking points, which backfire if inconsistent with documents.

---

## What happens during an actual audit

| Phase | What happens | GRC engineer's role |
|---|---|---|
| Entrance conference | Auditors explain scope, objectives, timeline | Arrive with evidence repository already organized |
| Fieldwork — document requests | Formal requests, often 24-48 hour turnaround | Fulfill requests same-day from existing repository |
| Fieldwork — interviews | Staff interviewed to verify documented process matches practice | Prepare staff to describe actual process accurately |
| Draft findings | Auditors share preliminary findings | Coordinate management response |
| Management response | Agency formally replies before report is finalized | Correct factual errors, commit to corrective action plan |
| Final report | Findings, recommendations, corrective action plan published | Track every action to closure via remediation tracker |

**A strong management response includes:**
- Acknowledgment of valid findings without excessive defensiveness
- Correction of factual inaccuracies with supporting evidence
- A specific, dated corrective action plan
- A named responsible owner for each corrective action

---

## Worked example — BridgeCore supporting a federal OIG audit

**Scenario:** Federal agency notified of upcoming OIG audit of its AI benefits
eligibility screening system, following media reports of bias at other agencies.

| Phase | BridgeCore action |
|---|---|
| Pre-audit (weeks -4 to -1) | Rapid self-assessment finds strong risk assessment docs but weak monitoring — quarterly bias audits planned but not run for 2 quarters |
| Gap remediation | Runs overdue audits immediately with 4 weeks lead time; documents findings; prepares honest narrative with corrective process and automated reminder system |
| Evidence assembly | Organized into standard folder structure, cross-referenced to OIG's typical audit program |
| Entrance conference | GRC lead attends with Chief AI Officer; repository ready within hours of any request |
| Fieldwork | Document requests fulfilled same-day; staff interviews go smoothly due to prior preparation |
| Outcome | Bias audit lapse is a finding — but accompanied by evidence of proactive correction and prevention. Transforms "no monitoring exists" into "monitoring had a gap, now remediated" |

**The value BridgeCore delivers:** not the absence of findings, but
evidence-backed, well-managed findings demonstrating a self-correcting
governance program.

---

## Key terms

| Term | Plain meaning |
|---|---|
| PBC list | "Provided By Client" — auditor's formal document request list |
| Entrance conference | Opening meeting where auditors explain scope and process |
| Fieldwork | Active audit phase — document review and interviews |
| Management response | Agency's formal reply to draft audit findings |
| Corrective action plan | Documented commitment to remediate a finding, with owner and timeline |
| Rights-impacting AI | OMB designation for AI affecting individuals' legal rights or benefits |
| Safety-impacting AI | OMB designation for AI where failure could harm health or safety |
| Audit trail | Log of governance actions and decisions — distinct from AI output logs |
| Evidence inventory | Master mapping of every control to its evidence location and owner |

---

## Practice questions

1. What is the difference between an OIG audit and a GAO review?
2. Why is an incomplete AI system inventory the most damaging audit finding?
3. What five qualities make evidence "audit-proof" rather than just "documented"?
4. Why might documented incidents actually help, rather than hurt, an audit outcome?
5. What is a management response and why does it matter?
6. Why do auditors increasingly focus on post-deployment monitoring evidence?
7. What is the worst possible moment to discover an evidence gap?

---

## Hands-on exercise

Using the AI system risk assessment from Module 5's exercise, build a
one-page evidence inventory: which of the eight categories have strong
evidence, which are weak or missing, and a specific remediation plan for
each gap. This is the exact exercise a GRC engineer runs before any real
federal audit.

---

## How to explain it in an interview

> "Audit readiness means building evidence infrastructure once and reusing
> it across every type of oversight — IG audits, GAO reviews, OMB compliance
> reporting, and customer assurance reviews. I organize evidence into eight
> categories: system inventory, risk assessments, testing results, approval
> records, human oversight logs, monitoring logs, incident reports, and audit
> trails. For every piece of evidence I apply five quality tests: specific,
> dated, attributable, independently verifiable, and consistent across
> documentation. The goal isn't avoiding all findings — mature organizations
> have findings. The goal is ensuring every finding comes with evidence of a
> functioning, self-correcting governance process."

---

*Previous: [Module 6 — Governance Controls](module-06-governance-controls.md)*
*Next: Module 8 — GRC Engineering and Automation (coming soon)*
