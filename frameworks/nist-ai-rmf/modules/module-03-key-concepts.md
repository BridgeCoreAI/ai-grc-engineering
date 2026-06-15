# Module 3 — Key Concepts: Trustworthy AI, Lifecycle, Risk Types, and Impact

> **Framework:** NIST AI Risk Management Framework (AI RMF 1.0)
> **Module:** 3 of 10
> **Status:** ✅ Complete

---

## Concept 1 — The Seven Properties of Trustworthy AI

NIST does not just say "make AI safe." It breaks trustworthiness into seven
specific properties. Each is a different lens for evaluating an AI system —
and a different category of risk if that property is missing.

| Property | Core question | Missing = risk of... |
|---|---|---|
| **Safe** | Does it avoid causing harm? | Physical, psychological, financial, or societal harm |
| **Secure & resilient** | Is it protected from attacks and able to recover? | Adversarial manipulation, system failure |
| **Explainable** | Can it explain why it made a specific decision? | Inability to review or contest AI decisions |
| **Transparent** | Is honest information available about how it works? | Hidden limitations, undisclosed use of AI |
| **Fair & unbiased** | Does it treat all groups equitably? | Discriminatory outcomes, EEOC violations |
| **Privacy-enhanced** | Does it protect personal data? | Data exposure, consent violations, surveillance |
| **Accountable** | Is someone clearly responsible when things go wrong? | No liability, no remediation path |

### Critical GRC insight
These seven properties are **not** a checklist you tick once. They are ongoing
commitments requiring continuous controls, testing, and monitoring. A GRC
engineer builds the systems that prove — with evidence — that each property
is maintained throughout the AI system's entire life.

### Explainability vs. Transparency — the critical distinction

| | Explainability | Transparency |
|---|---|---|
| **What it covers** | Why this specific AI output was produced | How the AI system works overall |
| **Type** | Technical property of the model | Organizational behavior |
| **Example** | "Loan denied because debt-to-income ratio exceeded 43%" | Model card published describing training data and limitations |
| **Who it serves** | Individual affected by a specific decision | Regulators, auditors, users, the public |

You can have a transparent organization running an unexplainable model.
You can have an explainable model that the organization keeps completely secret.
Good governance requires **both**.

---

## Concept 2 — The AI Lifecycle

Risk management must happen at **every stage** of an AI system's life —
not just before launch. The NIST AI RMF explicitly covers all six stages.

### The six lifecycle stages

| Stage | Name | Key GRC activities | Common risks |
|---|---|---|---|
| 1 | Plan & design | Define governance requirements; involve GRC from day one | Building something that should not be built |
| 2 | Collect & process data | Data quality review; privacy impact; lineage documentation | Biased training data; privacy violations; poor data quality |
| 3 | Build & train | Feature review for proxy variables; secure development | Bias encoded in model; overfitting; insecure practices |
| 4 | Verify & validate | Fairness testing; security testing; approval gate | Undetected bias; performance gaps; compliance failures |
| 5 | Deploy | Deployment controls; staged rollout; rollback plans | Premature launch; missing documentation |
| 6 | Operate & monitor | Drift detection; incident response; decommissioning | Model drift; emerging bias; undetected failures |

### Where bias most commonly enters
Stage 2 (data collection) — biased training data is the single most common
source of AI discrimination. If the training data does not represent all groups
fairly, the model learns and amplifies those imbalances.

### Model drift — why monitoring is non-negotiable
Even a well-tested model can become risky over time as real-world data changes.
This is called **model drift**. A model that was fair at launch can become
unfair six months later if the population it serves changes. This is why
ongoing monitoring is a governance requirement, not an optional extra.

---

## Concept 3 — Types of AI Risk

| Risk type | What it means | Real example |
|---|---|---|
| Bias & discrimination | AI treats some groups worse than others | Hiring AI rejects more female candidates |
| Safety | AI causes physical or psychological harm | Autonomous vehicle fails to detect pedestrian |
| Security | AI is attacked, manipulated, or compromised | Fraud model fooled by adversarial inputs |
| Privacy | AI exposes or misuses personal data | Facial recognition without consent |
| Reliability & performance | AI produces inconsistent or inaccurate outputs | Medical AI performs poorly on older scanner models |
| Explainability | AI cannot explain its decisions | Credit denial with no reason given |
| Accountability | Nobody is clearly responsible for AI harm | Vendor contract has no liability clause |
| Regulatory & legal | AI violates laws or regulations | Loan AI violates Equal Credit Opportunity Act |
| Reputational | AI causes public embarrassment | Chatbot produces offensive responses |
| Third-party / vendor | Vendor AI introduces risk you cannot directly control | Third-party tool has critical unpatched vulnerability |

---

## Concept 4 — Impact Assessment

NIST places heavy emphasis on impact — the real-world consequences of AI failure.
This shapes how GRC teams prioritize risk.

### Three dimensions of impact

**Who is impacted?**
- Individuals — specific people affected by AI decisions (loan applicants, patients, job seekers)
- Organizations — the company deploying the AI (legal liability, financial loss, reputation)
- Society — broader effects on communities, public health, democratic processes

**How severe?**
- Reversible vs. irreversible harm
- Narrow (one person) vs. widespread (millions)
- Immediate vs. long-term

**How likely?**
- Even catastrophic potential may be acceptable if likelihood is extremely low
- A moderate, highly-likely, widespread harm may be the highest priority

### The risk heat map

| Severity \ Likelihood | Low | Medium | High |
|---|---|---|---|
| Critical | Medium priority | High priority | **CRITICAL** |
| High | Low priority | Medium priority | High priority |
| Medium | Accept/monitor | Accept/monitor | Medium priority |
| Low | Accept/monitor | Accept/monitor | Low priority |

---

## Concept 5 — Human Oversight Levels

| Level | What it means | When to use |
|---|---|---|
| Human **in** the loop | Human reviews and approves every AI decision before it takes effect | High-stakes: clinical diagnosis, loan denial, criminal justice |
| Human **on** the loop | AI acts autonomously but human monitors and can intervene | Medium-stakes: fraud flagging, content moderation |
| Human **out** of the loop | AI acts fully autonomously, no human review | Low-stakes or speed-critical: spam filters, HFT |

**GRC rule:** The appropriate oversight level depends on the stakes.
High-risk AI systems (affecting health, liberty, finances, employment)
generally require **in the loop** or **on the loop**.

As a GRC engineer, you must:
1. Document the current oversight level for every AI system
2. Assess whether that level is appropriate for the risk
3. Build controls that enforce the required level

---

## Concept 6 — Proxy Variables

A proxy variable is an input that is not a protected characteristic
(race, gender, age, religion) but strongly correlates with one.

**Examples:**
| Proxy variable | Likely correlated with |
|---|---|
| ZIP code | Race (due to historical residential segregation) |
| University name | Socioeconomic background, race |
| Gap in employment history | Gender (caregiving), disability |
| Credit score | Race, socioeconomic background |
| Commute distance | Race (due to housing patterns) |

Using a proxy variable in a model can produce discriminatory outcomes
even when protected characteristics are never directly used.
GRC engineers must require a **proxy variable review** as part of every
AI risk assessment for systems making decisions about people.

---

## Mini case study — all six concepts applied

**TalentFirst** resume screening AI — scoring and ranking job applicants

| Concept | Assessment |
|---|---|
| Trustworthy AI | Safe: Medium. Secure: Low. **Explainable: CRITICAL.** **Transparent: HIGH.** **Fair: CRITICAL.** Privacy: High. Accountable: High. |
| Lifecycle risk | Stage 2: training data from historical hires — biased toward majority demographic groups. Stage 3: university name used as feature (proxy variable). Stage 4: no fairness testing conducted. Stage 6: no demographic monitoring. |
| Risk types | Bias risk: CRITICAL. Accountability risk: HIGH. Explainability risk: HIGH. Regulatory risk: HIGH (EEOC). |
| Impact | Severity: HIGH (employment decisions affect livelihoods). Likelihood: HIGH (bias already embedded). Scope: WIDESPREAD (thousands/month). Rating: **CRITICAL**. |
| Human oversight | Current level: out of the loop. Required level: **in the loop** for all low-scored candidates. |
| Proxy variables | University name correlates with socioeconomic background and race. **Must be removed before deployment.** |

**GRC recommendations:**
- Human review for all bottom-quartile scores before sending to clients
- Remove university name as a feature
- Re-train on de-biased dataset
- Assign AI Risk Owner
- Publish model card
- Implement quarterly fairness audits
- Add explainability module

---

## Key terms — full glossary for Module 3

| Term | Plain meaning |
|---|---|
| Trustworthy AI | AI that is safe, secure, explainable, transparent, fair, privacy-protective, and accountable |
| AI lifecycle | Every stage from planning through retirement |
| Model drift | Performance degradation over time as real-world data changes |
| Adversarial attack | Deliberate attempt to fool an AI model with specially crafted inputs |
| Bias | Systematic unfairness in AI outputs toward certain groups |
| Proxy variable | A variable that is not a protected characteristic but correlates with one |
| Risk heat map | Grid visualizing risks by likelihood and severity |
| Human in the loop | Human approves every AI decision before it takes effect |
| Model card | Document describing an AI model's purpose, data, performance, and limitations |
| Data lineage | Record of where data came from, how it was processed, and how it was used |

---

## Practice questions

1. Name the seven properties of trustworthy AI — explain each in one sentence
2. What is the difference between explainability and transparency?
3. Name three types of AI risk with a real example of each
4. What is model drift and why does it matter for GRC?
5. At which lifecycle stage is bias most commonly introduced?
6. What is a proxy variable? Give a real-world example
7. What are the three human oversight levels? When is each appropriate?
8. How do you score a risk using the impact-likelihood matrix?

---

## Hands-on exercise

Pick any AI system you use in daily life (recommendation engine, chatbot, spam filter).

1. Assess it against all seven trustworthy AI properties — which are strong? Which are weak?
2. Identify which lifecycle stage carries the highest risk for that system
3. Name two risk types that apply
4. Decide what human oversight level it has — and whether that is appropriate

Write your answers as a one-page document. This is the foundation of every
AI risk assessment you will ever conduct.

---

## How to explain it in an interview

> "NIST AI RMF is built around the concept of trustworthy AI — seven properties
> every responsible AI system should demonstrate. As a GRC engineer, I operationalize
> these by mapping them to controls, testing requirements, and monitoring activities
> across the AI lifecycle. I assess risks by type and impact, use a likelihood-severity
> matrix to prioritize, and ensure the right level of human oversight is in place.
> The key insight is that governance is continuous — not a one-time pre-deployment gate."

---

*Previous: [Module 2 — Four Functions](module-02-four-functions.md)*
*Next: [Module 4 — Real-World Application](module-04-real-world-application.md)*
