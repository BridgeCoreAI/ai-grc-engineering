# Reference Card — AI Risk Types

> **Source:** NIST AI RMF 1.0
> **Use:** Risk identification during MAP function; populating the risk register

---

## The ten AI risk types

| Risk type | What it means | Real-world example | High-risk industries |
|---|---|---|---|
| **Bias & discrimination** | AI systematically disadvantages people based on protected characteristics | Hiring AI approves fewer female applicants with identical qualifications | HR, lending, insurance, criminal justice |
| **Safety** | AI causes physical, psychological, or financial harm | Autonomous vehicle fails to detect pedestrian in rain | Healthcare, automotive, aviation, defense |
| **Security** | AI is attacked, manipulated, or compromised | Fraud model fooled by adversarial transaction inputs | Banking, cybersecurity, government |
| **Privacy** | AI exposes, misuses, or enables surveillance of personal data | Facial recognition identifies individuals without consent | Healthcare, retail, law enforcement |
| **Reliability & performance** | AI produces inconsistent, inaccurate, or degraded outputs | Medical imaging AI performs well on new scanners but poorly on older models | Healthcare, manufacturing, finance |
| **Explainability** | AI cannot explain its decisions in understandable terms | Credit denial with no reason provided | Lending, insurance, HR, healthcare |
| **Accountability** | No clear responsibility when AI causes harm | Vendor-deployed AI causes harm; contract has no liability clause | All industries |
| **Regulatory & legal** | AI violates laws or regulations | Loan AI uses ZIP code as a proxy for race, violating ECOA | Lending, insurance, HR, healthcare |
| **Reputational** | AI causes public embarrassment or loss of trust | Chatbot produces offensive or factually wrong responses that go viral | Customer service, media, retail |
| **Third-party / vendor** | AI vendor or supplier introduces risk the organization cannot directly control | Third-party AI tool has critical unpatched security vulnerability | All industries with vendor AI |

---

## Risk type → trustworthy AI property mapping

| Risk type | Primary property affected |
|---|---|
| Bias & discrimination | Fair & unbiased |
| Safety | Safe |
| Security | Secure & resilient |
| Privacy | Privacy-enhanced |
| Reliability & performance | Safe, Explainable |
| Explainability | Explainable, Accountable |
| Accountability | Accountable, Transparent |
| Regulatory & legal | Fair, Accountable, Transparent |
| Reputational | Transparent, Safe |
| Third-party / vendor | All properties (depends on vendor) |

---

## Risk identification questions by type

Use these questions during MAP function risk identification sessions.

### Bias & discrimination
- Was the training data representative of all demographic groups?
- Are any input features proxies for protected characteristics?
- Has the model been tested for disparate impact across demographic groups?
- Are there regulatory requirements for equitable treatment (ECOA, EEOC, FHA)?

### Safety
- What is the worst realistic outcome if the AI makes a wrong decision?
- Is the AI involved in decisions affecting physical safety, health, or financial security?
- Is there a human override mechanism for critical errors?
- What happens if the AI fails completely?

### Security
- Is the model accessible via a public or semi-public API?
- Has adversarial robustness been tested?
- Who has access to model weights, training data, and output logs?
- Is there a process for detecting and responding to model poisoning attacks?

### Privacy
- What personal data does the system process?
- What is the legal basis for processing that data?
- Could the model output be used to infer information not explicitly provided?
- Is there a data subject request process?

### Reliability & performance
- What is the acceptable error rate for this system?
- Has performance been tested across all environments where the system will run?
- What happens to decisions made during system downtime or degraded performance?
- Is there a model retraining process when performance drops?

### Explainability
- Can the model explain individual decisions in plain language?
- Are affected individuals or regulators entitled to an explanation?
- Is there a process for reviewing contested AI decisions?

### Accountability
- Who is the named AI Risk Owner for this system?
- What happens if the system causes harm — who is responsible?
- Are all decisions about the system logged and auditable?
- If a vendor built the AI, what does the contract say about liability?

### Regulatory & legal
- What laws and regulations apply to this AI system and its decisions?
- Has legal counsel reviewed the system for compliance?
- Does the system operate across multiple jurisdictions with different requirements?

### Reputational
- Could AI outputs be shared publicly or go viral if they are wrong or offensive?
- Is there a review process for AI-generated content before it reaches users?
- Is there a public communications plan for AI incidents?

### Third-party / vendor
- Does the vendor have a published AI governance program?
- Can you audit the vendor's AI system or review fairness testing results?
- Does the contract require vendor notification of model changes?
- What happens to your data if the vendor relationship ends?

---

## Common risk combinations

Some risks frequently appear together. When you identify one, check for the others:

| If you find... | Also check for... |
|---|---|
| Bias risk | Regulatory risk, explainability risk, accountability risk |
| Security risk | Privacy risk, reliability risk, third-party risk |
| Explainability risk | Accountability risk, regulatory risk |
| Third-party risk | Security risk, privacy risk, accountability risk |
| Safety risk | Accountability risk, regulatory risk, reliability risk |
