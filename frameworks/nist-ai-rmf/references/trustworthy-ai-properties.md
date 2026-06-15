# Reference Card — The Seven Properties of Trustworthy AI

> **Source:** NIST AI RMF 1.0
> **Use:** Quick lookup during risk assessments, control design, and audit prep

---

## The seven properties at a glance

| # | Property | Core question | GRC control category |
|---|---|---|---|
| 1 | Safe | Does it avoid causing harm to people or the world? | Safety controls, testing, human oversight |
| 2 | Secure & resilient | Is it protected from attack and able to recover? | Cybersecurity controls, resilience planning |
| 3 | Explainable | Can it explain why it made a specific decision? | Explainability requirements, model documentation |
| 4 | Transparent | Is honest information available about how it works? | Model cards, disclosure policies, audit rights |
| 5 | Fair & unbiased | Does it treat all groups of people equitably? | Bias testing, fairness audits, proxy variable review |
| 6 | Privacy-enhanced | Does it protect personal data and individual rights? | Privacy impact assessments, data minimization |
| 7 | Accountable | Is someone clearly responsible when something goes wrong? | Risk ownership, governance structures, audit trails |

---

## Property deep-dives

### 1. Safe
- The AI does not cause physical, psychological, financial, or societal harm
- Includes direct harm (wrong medical recommendation) and indirect harm (biased housing decision)
- **Evidence required:** Safety testing results, incident log, human oversight records
- **Red flags:** No safety testing conducted; autonomous decisions in high-stakes domains with no override

### 2. Secure & resilient
- Protected against adversarial attacks (inputs crafted to fool the model)
- Can continue operating or recover gracefully from disruptions
- **Evidence required:** Security assessment report, adversarial robustness test results, business continuity plan
- **Red flags:** Model accessible via unauthenticated API; no recovery procedure documented

### 3. Explainable
- Individual decisions can be explained in plain language to the people they affect
- Separate from transparency (which is organizational) — this is model-level
- **Evidence required:** Explainability module documentation, sample explanation outputs, user testing results
- **Red flags:** Black-box model making high-stakes decisions; no reason provided for adverse outcomes

### 4. Transparent
- Organization openly discloses how the AI system works, what data it uses, and what its limitations are
- Model cards are the primary transparency artifact
- **Evidence required:** Published model card, AI disclosure notices, audit trail of system changes
- **Red flags:** No public documentation; vendor refuses to disclose model details; hidden AI use in consumer products

### 5. Fair & unbiased
- Outputs do not systematically disadvantage people based on protected characteristics
- Bias can enter at data collection, feature selection, model training, or evaluation
- **Evidence required:** Pre-deployment fairness test report, demographic performance breakdown, proxy variable review, periodic bias audit results
- **Red flags:** No fairness testing; proxy variables used without review; disparate impact found but not remediated

### 6. Privacy-enhanced
- Personal data is collected lawfully, used minimally, protected appropriately, and subject to individual rights
- AI creates specific privacy risks: inference attacks, re-identification, large-scale profiling
- **Evidence required:** Privacy impact assessment, data minimization log, consent records, data subject request log
- **Red flags:** No PIA conducted; personal data used beyond original purpose; no consent mechanism

### 7. Accountable
- Named individuals are responsible for the AI system's safe and compliant operation
- Decisions about the system are logged and auditable
- There is a clear escalation path and incident response process
- **Evidence required:** RACI matrix, risk ownership assignments, governance committee minutes, approval records, incident log
- **Red flags:** No named risk owner; no audit trail of decisions; "the algorithm did it" response to incidents

---

## Using this in a risk assessment

For each AI system in your inventory, rate each property:

| Property | Current state | Gap identified | Control required |
|---|---|---|---|
| Safe | ☐ Strong ☐ Adequate ☐ Weak ☐ Missing | | |
| Secure & resilient | ☐ Strong ☐ Adequate ☐ Weak ☐ Missing | | |
| Explainable | ☐ Strong ☐ Adequate ☐ Weak ☐ Missing | | |
| Transparent | ☐ Strong ☐ Adequate ☐ Weak ☐ Missing | | |
| Fair & unbiased | ☐ Strong ☐ Adequate ☐ Weak ☐ Missing | | |
| Privacy-enhanced | ☐ Strong ☐ Adequate ☐ Weak ☐ Missing | | |
| Accountable | ☐ Strong ☐ Adequate ☐ Weak ☐ Missing | | |

Any property rated **Weak** or **Missing** for a Tier 1 or Tier 2 system
requires a risk entry in the risk register and a treatment plan.
