# Reference Card — Human Oversight Levels

> **Source:** NIST AI RMF 1.0
> **Use:** Determining appropriate oversight for each AI system; designing oversight controls

---

## The three levels

### Level 1 — Human IN the loop
**Definition:** A human reviews and approves every AI output before it takes effect.
The AI makes a recommendation. The human decides.

**Characteristics:**
- AI output is advisory only
- No autonomous action without human sign-off
- Human can modify, reject, or override every output
- Full audit trail of human decisions

**Use when:**
- Decisions directly affect individuals' rights, health, safety, or finances
- Errors are difficult or impossible to reverse
- Regulatory requirements mandate human decision-making
- The AI system is new or unproven in the deployment context

**Examples:**
- Clinical AI recommending a medication dose — doctor reviews and prescribes
- Loan denial flagged by AI — human loan officer makes the final decision
- Job applicant ranked low by AI — human recruiter reviews before rejection
- Benefits eligibility determined by AI — caseworker reviews before notification

**GRC controls required:**
- Override mechanism must be documented and functional
- Human review completion must be logged
- Override rate must be monitored (high rate = AI not trusted; very low rate = humans may be rubber-stamping)
- Training for all humans in the review role

---

### Level 2 — Human ON the loop
**Definition:** The AI acts autonomously but a human monitors outputs and can intervene.
The human does not review every decision but watches for patterns and anomalies.

**Characteristics:**
- AI takes action immediately on most outputs
- Human monitors dashboards and alerts in near-real-time
- Human can reverse or escalate decisions after the fact
- Intervention thresholds are defined and monitored

**Use when:**
- Volume is too high for per-decision human review
- Errors are reversible within a reasonable timeframe
- A monitoring system can reliably flag anomalies
- The AI system is well-validated and has an established track record

**Examples:**
- Fraud detection system blocks suspicious transactions — analyst reviews flagged cases daily
- Content moderation AI removes posts — human moderators review appeals
- Automated loan approval — all approvals auto-processed, denials queued for human review
- Security alerting AI — SOC analyst monitors alert dashboard, investigates high-priority alerts

**GRC controls required:**
- Real-time monitoring dashboard
- Alert thresholds defined and documented
- Intervention SLA (how quickly can a human reverse a decision?)
- Escalation path for anomalies
- Regular review of intervention rate and patterns

---

### Level 3 — Human OUT of the loop
**Definition:** The AI acts fully autonomously with no human review of individual decisions.
Humans may set parameters or review aggregate performance, but do not review each output.

**Characteristics:**
- Fully automated decision-making at the individual level
- Human involvement limited to system configuration and performance review
- No per-decision override at time of decision
- Relies entirely on the quality of the AI model and safeguards built in

**Use when:**
- Decisions are low-stakes and easily reversible
- Speed requirements make human review impractical
- Volume is extremely high
- The system is extremely well-validated with low error rates

**Examples:**
- Spam filter categorizing emails
- High-frequency trading algorithms
- Real-time ad bidding
- Autocomplete suggestions

**GRC controls required:**
- Aggregate performance monitoring
- Statistical sampling of outputs for quality review
- Customer/user recourse mechanism (ability to contest or override)
- Clear disclosure that decisions are fully automated
- Regular independent model validation

**Warning:** Applying this level to high-stakes decisions (credit, employment, healthcare,
criminal justice, benefits) is a significant governance risk and may violate regulations
(EU AI Act, ECOA, FCRA). Document the rationale explicitly if used in medium-stakes contexts.

---

## Oversight level decision guide

Use this when classifying a new AI system:

```
Is this system making decisions that directly affect
individuals' rights, health, finances, or safety?
│
├── YES → Is this a regulated domain (lending, healthcare,
│          employment, criminal justice, benefits)?
│          │
│          ├── YES → Human IN the loop required
│          │
│          └── NO → Are errors easily reversible?
│                   │
│                   ├── YES → Human ON the loop acceptable
│                   │
│                   └── NO → Human IN the loop recommended
│
└── NO → Is the volume manageable for human review?
          │
          ├── YES → Consider Human IN or ON the loop
          │
          └── NO → Human OUT of loop acceptable
                   with strong monitoring
```

---

## Oversight level by risk tier

| Risk tier | Recommended minimum oversight level |
|---|---|
| Tier 1 — Critical | Human IN the loop |
| Tier 2 — High | Human IN or ON the loop (justified exception required for OUT) |
| Tier 3 — Medium | Human ON the loop minimum |
| Tier 4 — Low | Human OUT of loop acceptable with monitoring |

---

## Evidence required for each level

| Level | Evidence GRC engineer must maintain |
|---|---|
| In the loop | Human review log, override log, override rate trend, reviewer training records |
| On the loop | Monitoring dashboard, alert threshold documentation, intervention log, SLA compliance records |
| Out of loop | Aggregate performance reports, sampling results, recourse mechanism documentation, model validation records |
