# Module 4 — Real-World Application and Industry Use Cases

> **Framework:** NIST AI RMF (AI RMF 1.0)
> **Module:** 4 of 10
> **Status:** ✅ Complete

---

## The six implementation phases

A GRC engineer implements NIST AI RMF in six phases:

| Phase | NIST function | What you build |
|---|---|---|
| 1 — Build the foundation | GOVERN | Policies, roles, committees, accountability |
| 2 — Find all AI systems | MAP | AI system inventory, risk identification |
| 3 — Assess every risk | MEASURE | Risk assessments, bias tests, heat maps |
| 4 — Treat and monitor | MANAGE | Controls, treatment plans, monitoring |
| 5 — Run governance daily | All | Intake workflows, dashboards, reporting cadence |
| 6 — Mature and improve | All | Audits, lessons learned, policy updates |

---

## Step-by-step walkthrough — Meridian Health System

**Scenario:** Hospital network deploying AI-powered patient triage tool in emergency departments.

### Phase 1 — GOVERN

**Step 1: Create AI Governance Policy**
- Every clinical AI must be reviewed and approved before deployment
- A named AI Risk Owner must be assigned
- All systems must be inventoried
- Patients have the right to know when AI is involved in their care

**Step 2: Form AI Governance Committee**
- Chair: Chief Medical Officer
- Members: CISO, Chief Privacy Officer, General Counsel, Director of Clinical Operations, Patient Advocate, Data Science Lead
- Authority: Approve, reject, or require modifications to any AI system

**Step 3: Assign roles to every system**
- AI Risk Owner — executive accountable for safe operation
- AI System Manager — operational lead
- AI Control Owner — GRC engineer maintaining controls and evidence

**Step 4: Build awareness and training**
- Clinical staff: 2-hour training on what the AI does, its limitations, override process, escalation
- Engineers: Secure AI development training

---

### Phase 2 — MAP (Discovery)

**Step 5: AI discovery survey**
Meridian surveys all departments: do you use any software that makes automated recommendations, predictions, or decisions?

Result: 31 AI systems found — nobody had a complete picture before.

**Step 6: Build AI system inventory**
Every system documented with: name, vendor, purpose, inputs, outputs, decision type, users, affected population, regulatory applicability, risk classification, risk owner.

**Step 7: Risk identification**
For the triage AI — 14 distinct risks identified:
- Bias: training data from predominantly urban hospitals
- Safety: incorrect triage score could delay critical care
- Explainability: physicians cannot see why a score was assigned
- Privacy: patient data transmitted to third-party vendor cloud
- Vendor: MedLogic Inc. has no published AI governance program

---

### Phase 3 — MEASURE (Assessment)

**Step 8: AI risk assessment**
Each of 14 risks formally assessed: description, likelihood, severity, rating, trustworthy AI property affected, lifecycle stage, evidence reviewed.

**Step 9: Fairness and performance testing**
- Accuracy tested across demographic groups (age, sex, race, language)
- Performance tested on Meridian's specific patient population
- Stress tests run for incomplete data inputs
- Adversarial inputs tested

**Step 10: Risk heat map**
Result: 2 Critical, 5 High, 5 Medium, 2 Low. Both Critical risks must be resolved before any deployment.

---

### Phase 4 — MANAGE (Treatment and monitoring)

**Step 11: Treatment decisions**
- Bias in training data → Mitigate: vendor must augment training data; defer 60 days
- No explainability → Mitigate: vendor adds score rationale display
- Vendor data transmission → Mitigate + Transfer: BAA required; encryption; liability clause
- Minor vendor risk → Accept: document; monitor quarterly

**Step 12: Control implementation**
22 controls built across: data governance, bias/fairness, human oversight, security, monitoring, incident response.

**Step 13: Monitoring configured**
Daily dashboard tracking: accuracy vs. final diagnosis, override rate, score distribution by demographic group, availability and errors, incidents.

**Step 14: Deployment approval**
After vendor delivers improvements, AI Review Board reviews evidence package and issues formal signed approval.

---

## Five patterns every GRC engineer must know

| Pattern | What it means |
|---|---|
| Vendor opacity is a governance blocker | If you cannot assess it, you cannot govern it. Contracts must require transparency. |
| Bias is almost always present | In 5 of 6 industry cases, demographic disparities were found. Fairness testing is non-negotiable. |
| Human oversight gaps create the highest risk | The worst risk profiles had the least human oversight. Autonomous AI in high-stakes domains is a red flag. |
| Monitoring is where governance lives or dies | Organizations that set up monitoring before deployment caught problems early. Those that did not were blindsided. |
| Documentation is the difference between governance and theater | Every organization needed evidence for regulators, auditors, and leadership. Without documentation, governance is invisible. |

---

## Industry use cases — summary

### Healthcare: Radiology AI (chest X-ray pneumonia detection)
- Key risk: 94% sensitivity overall but only 87% on older scanner models
- Control: Monthly accuracy audit; re-validation after scanner updates
- Evidence: Clinical validation report, radiologist oversight log

### Banking: Fraud detection AI
- Key risk: 6,900 legitimate transactions blocked daily (0.3% false positive rate); disproportionate impact on international corridors
- Control: 24-hour human dispute review SLA; quarterly corridor performance audit
- Evidence: Dispute log, false positive monitoring dashboard

### Cybersecurity: SOC threat detection AI
- Key risk: 40% false positive rate causing analyst fatigue; trained on different industry data
- Control: Analyst feedback loop for retraining; alert fatigue monitoring
- Evidence: False positive log, red team exercise reports

### Human resources: Resume screening AI
- Key risk: Vendor opacity — cannot assess model features; suspected heavy weighting of university name and employer prestige
- Control: Suspend pending vendor disclosure; add human review of top 20 candidates regardless of AI ranking
- Evidence: Vendor disclosure request, legal review memo, EEOC compliance assessment

### Government: Benefits eligibility AI
- Key risk: 23% higher denial rate for applicants in certain zip codes; eviction history as circular proxy variable
- Control: Remove eviction history; 100% caseworker review; formal appeals process
- Evidence: Equity audit reports, caseworker override log, appeals log

### Customer service: Telecoms chatbot
- Key risk: 12-point satisfaction gap vs. human agents; lower resolution rates for non-native English speakers
- Control: Weekly accuracy sampling; language equity monitoring; always-available escalation to human
- Evidence: CSAT dashboard, accuracy audit results, language equity report

---

## GRC engineering artifacts from Module 4

| Artifact | Purpose | Where it lives |
|---|---|---|
| AI system inventory | Complete register of all AI systems with risk profiles | Central GRC system or spreadsheet |
| AI risk assessment | Formal risk document for each system | Filed per system, version-controlled |
| Risk heat map | Visual priority ranking of all risks | Included in risk assessment |
| Risk treatment plan | Decisions on what to do about each risk | Attached to risk assessment |
| Control library | Pre-approved controls mapped to risk types | Shared GRC resource |
| Monitoring dashboard | Live view of AI system health | Dashboard tool (Power BI, Streamlit) |
| Deployment approval record | Signed evidence of governance sign-off | Filed per system |

---

## Practice questions

1. What happens during the AI discovery phase — and why does it surprise organizations?
2. What is an approval gate and where should one exist in the AI lifecycle?
3. Why is vendor opacity a critical governance risk?
4. What does a high override rate tell a GRC engineer?
5. Name three monitoring metrics every deployed AI system should track
6. Which of the six industry use cases had the most serious governance gap and why?
7. What five patterns appear across almost all AI governance engagements?

---

## How to explain it in an interview

> "When I implement NIST AI RMF for an organization, I follow a six-phase approach:
> build the governance foundation, discover and inventory all AI systems, conduct
> structured risk assessments, build a control environment, operationalize governance
> as a daily function, and continuously improve through audits and lessons learned.
> The most important lesson is that AI risk management is not a pre-deployment gate —
> it is a continuous program requiring daily monitoring, quarterly audits, and annual
> reassessments. In every engagement, the five biggest issues I look for are vendor
> opacity, demographic bias, insufficient human oversight, missing monitoring, and
> inadequate documentation."

---

*Previous: [Module 3 — Key Concepts](module-03-key-concepts.md)*
*Next: Module 5 — AI Risk Assessment (coming soon)*
