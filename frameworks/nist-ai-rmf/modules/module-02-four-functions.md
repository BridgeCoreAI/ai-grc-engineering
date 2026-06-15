# Module 2 — The Four Core Functions: GOVERN · MAP · MEASURE · MANAGE

> **Framework:** NIST AI Risk Management Framework (AI RMF 1.0)
> **Module:** 2 of 10
> **Status:** ✅ Complete

---

## The big picture

The NIST AI RMF is organized around four core functions. Together they form a
continuous cycle — not a one-time checklist.

```
GOVERN → sets the foundation for everything else
   ↓
MAP → discover risks
   ↓
MEASURE → evaluate how serious they are
   ↓
MANAGE → treat and monitor them
   ↓
(loop back to MAP as the AI evolves)
```

**GOVERN** is the foundation. Without it, the other three functions will fail
because nobody will be accountable for doing them.

---

## Function 1 — GOVERN

### What it means
GOVERN builds the organizational infrastructure for AI risk management.
It establishes policies, roles, committees, values, and accountability chains
**before** any AI system is deployed.

Without GOVERN: no policy, no risk owner, no training, no committee to approve
or reject AI systems. Technical testing alone cannot fix this.

### The six GV subcategories

| Subcategory | Plain meaning |
|---|---|
| GV-1: Policies and processes | Written AI risk policies exist and are actively used |
| GV-2: Accountability and roles | Clear owners exist for every AI system |
| GV-3: Culture and awareness | Employees understand AI risks; responsible AI is cultural |
| GV-4: Organizational teams | Cross-functional teams (legal, tech, compliance, HR) are involved |
| GV-5: External AI policies | Policies cover vendor/third-party AI, not just internal systems |
| GV-6: Policies are updated | Governance processes are reviewed as AI and regulations evolve |

### Real-world GOVERN example
**MedCore Healthcare** creates:
- AI Governance Policy (how systems are approved, monitored, retired)
- AI Governance Committee (CMO, CISO, General Counsel, data ethicist)
- AI Risk Owner for every clinical system
- Mandatory AI literacy training for clinical and engineering staff
- Vendor policy requiring external AI suppliers to meet MedCore standards

### GRC engineer output
AI Governance Policy · AI Review Board charter · RACI matrix ·
Training completion records · Executive sign-off documentation

---

## Function 2 — MAP

### What it means
MAP is the discovery phase. You cannot manage a risk you do not know exists.
MAP forces the question: what AI systems do we have, what do they do,
who is affected, and what could go wrong?

### The five MP subcategories

| Subcategory | Plain meaning |
|---|---|
| MP-1: Organizational context | Mission, risk tolerance, regulatory environment |
| MP-2: AI system context | What does this AI do? Who built it? What data does it use? |
| MP-3: Impact analysis | Who could be harmed? How severe would the harm be? |
| MP-4: Risk identification | What are the actual risks? Bias, errors, privacy, security? |
| MP-5: Trustworthiness scoring | How trustworthy is this system before any controls are added? |

### Key output: AI system inventory
The most important GRC artifact produced by MAP.
For every AI system, document:

| Field | Example |
|---|---|
| System name | ED Triage Assist v2.1 |
| Vendor / builder | MedLogic Inc. |
| Purpose | Scores patient acuity to prioritize treatment |
| Data inputs | Vital signs, chief complaint, patient history, age |
| Data outputs | Triage score (1–5), recommended action |
| Decision type | Decision support — physician reviews and can override |
| Affected population | All ED patients (~200/day) |
| Regulatory applicability | FDA, HIPAA |
| Risk classification | High |
| AI Risk Owner | Dr. Sarah Chen, CMO |

### GRC engineer output
AI system inventory · Risk identification report · Data flow diagram

---

## Function 3 — MEASURE

### What it means
MAP tells you what risks exist. MEASURE tells you how serious they are.
It is the assessment and testing phase — assigning likelihood and severity ratings
to every identified risk.

### The four MS subcategories

| Subcategory | Plain meaning |
|---|---|
| MS-1: Risk analysis approach | What methodology is used to analyze and prioritize risks? |
| MS-2: Risk evaluation | Rate each risk for likelihood, severity, and who is impacted |
| MS-3: Trustworthiness metrics | Track fairness, accuracy, robustness, explainability scores |
| MS-4: Risk feedback loops | Measurement findings feed back into MAP to improve risk identification |

### Risk rating approach

| Likelihood \ Severity | Low | Medium | High | Critical |
|---|---|---|---|---|
| High | Low | Medium | High | CRITICAL |
| Medium | Low | Low | Medium | High |
| Low | Accept | Accept | Low | Medium |

### GRC engineer output
Completed AI risk assessment · Fairness testing results ·
Performance test report · Risk heat map · Risk register

---

## Function 4 — MANAGE

### What it means
MANAGE acts on everything the first three functions produced.
It is where risks get treated, controls get implemented, and
monitoring becomes a continuous operational discipline.

### The four MG subcategories

| Subcategory | Plain meaning |
|---|---|
| MG-1: Risk prioritization | Which risks get addressed first? |
| MG-2: Risk treatment | Mitigate, transfer, accept, or avoid |
| MG-3: Residual risk | What risk remains after controls? Is it acceptable? |
| MG-4: Monitoring and response | Watch the system continuously; detect, escalate, respond |

### The four risk treatment options

| Treatment | Meaning | Example |
|---|---|---|
| Mitigate | Add controls to reduce the risk | Add human review for all loan denials |
| Transfer | Shift risk to a third party | Buy cyber insurance; add vendor liability clause |
| Accept | Acknowledge and monitor without action | Low risk, cost of control exceeds impact |
| Avoid | Do not deploy the system | Risk is too high and cannot be reduced |

### GRC engineer output
Risk treatment plan · Control library · Monitoring schedule ·
Incident response plan · Ongoing governance cadence

---

## Mini case study — all four functions applied

**ClearPath Insurance** wants to use AI to predict customer claim likelihood for renewal pricing.

| Function | What happened |
|---|---|
| GOVERN | Chief Risk Officer named as AI Risk Executive. AI Review Board formed (legal, compliance, actuarial, IT). Board must approve all AI used in pricing. |
| MAP | GRC team catalogs the model. Inputs: claims history, driving records, credit scores, ZIP code. Risks identified: ZIP code as racial proxy (redlining), explainability gaps, regulatory exposure. |
| MEASURE | Fairness tests run. ZIP code correlation with demographic data confirmed. Explainability gap rated HIGH. Model accuracy rated MEDIUM. Two CRITICAL risks identified. |
| MANAGE | ZIP code removed as input. Explainability module added. Quarterly fairness audit established. Monitoring dashboard configured. Annual independent model validation required. |

---

## Key terms

| Term | Meaning |
|---|---|
| Subcategory | A specific activity within one of the four functions |
| AI risk register | Document listing all risks with ratings and treatment plans |
| Risk treatment | The decision on what to do: mitigate, transfer, accept, or avoid |
| Residual risk | Risk remaining after controls are applied |
| Continuous monitoring | Ongoing watching of a deployed AI system |
| AI system inventory | Register of all AI systems with attributes and risk classifications |
| Risk owner | Named person accountable for managing a specific risk |

---

## Practice questions

1. Name the four functions and explain each in one sentence
2. Which function is the foundation? Why?
3. What is the difference between MAP and MEASURE?
4. Name the four risk treatment options with examples
5. What artifact does a GRC engineer produce at the end of MAP?
6. Why does the cycle loop back to MAP after MANAGE?

---

## How to explain it in an interview

> "The NIST AI RMF has four core functions. GOVERN sets the organizational foundation —
> policies, roles, and accountability. MAP identifies AI systems and their risks.
> MEASURE evaluates how serious those risks are through testing and analysis.
> MANAGE treats the risks with controls and monitors AI systems continuously.
> The functions form a cycle because AI systems evolve and new risks emerge over time.
> As a GRC engineer, I translate each function into workflows, evidence, and controls
> that the organization can actually operate."

---

*Previous: [Module 1 — Overview](module-01-overview.md)*
*Next: [Module 3 — Key Concepts](module-03-key-concepts.md)*
