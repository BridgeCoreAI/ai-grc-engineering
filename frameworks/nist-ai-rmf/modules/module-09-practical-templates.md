# Module 9 — Practical Templates
## The complete deliverable library

> **Framework:** NIST AI Risk Management Framework (AI RMF 1.0)
> **Module:** 9 of 10
> **Status:** ✅ Complete

---

## How this module is different

Every prior module taught a concept through explanation. This module is a
reference library — pulled from during a real engagement at the moment a
specific template is needed, rather than read start to finish.

The engagement flow these templates support:

```
Intake → Inventory → Assess → Control → Monitor → Report
```

---

## Template 1 — AI Impact Assessment (OMB M-24-10 aligned)

The single most federally specific template in this library — not just good
practice, but a **legal requirement** under OMB Memorandum M-24-10 for any
AI system that is rights-impacting or safety-impacting.

### Section A — System Identification
```
System name:                    _______________________
Agency / component:             _______________________
Chief AI Officer sign-off:      _______________________
Assessment date:                _______________________
Assessor name and title:        _______________________
```

### Section B — Impact Determination
```
RIGHTS-IMPACTING if the system is used to make or meaningfully inform a
decision about:
[ ] Eligibility for, or denial/revocation of, public benefits
[ ] Eligibility for, or denial of, government services
[ ] Civil rights or civil liberties
[ ] Equal opportunity (housing, education, employment)
[ ] Access to or conditions of employment
[ ] Educational opportunity
[ ] Healthcare access or treatment decisions
[ ] Criminal justice outcomes
[ ] Immigration status determinations

SAFETY-IMPACTING if failure or error could result in:
[ ] Loss of life or significant injury
[ ] Critical infrastructure failure
[ ] National security compromise
[ ] Significant environmental harm
```

### Section C — Minimum Risk Management Practices
Required if Section B is triggered. Any "No" requires a documented waiver
from the agency's Chief AI Officer with justification.

```
[ ] Completed an AI impact assessment before deployment        Yes / No
[ ] Tested for performance in a real-world context              Yes / No
[ ] Independently evaluated the AI                               Yes / No
[ ] Conducted ongoing monitoring                                 Yes / No
[ ] Mitigated emerging risks to rights and safety                Yes / No
[ ] Ensured human oversight and accountability                   Yes / No
[ ] Provided appropriate transparency to the public               Yes / No
[ ] Ensured options to opt-out where appropriate                  Yes / No
[ ] Conducted ongoing testing for disparate impact                Yes / No
```

### Section D — Waiver Documentation
```
Practice not implemented:        _______________________
Justification:                   _______________________
Risk acceptance approved by:     _______________________ (must be CAIO)
Compensating measure:            _______________________
Review date for re-assessment:   _______________________
```

### Section E — Public Disclosure Requirements
```
[ ] System added to agency's public AI use case inventory
[ ] Plain-language description published
[ ] Determination (rights-impacting / safety-impacting) disclosed
[ ] Minimum practices status disclosed
[ ] Waiver justification disclosed (if applicable)
```

**Why this matters most in a federal pitch:** an agency that cannot produce
this document for a rights-impacting or safety-impacting system is, by
definition, out of compliance with a binding OMB requirement. Offering to
build and maintain this template is offering direct compliance risk
reduction — an easier conversation than abstract "AI governance" language.

---

## Template 2 — AI Vendor Review Checklist

Operationalizes Module 6's vendor risk controls (VR-001, VR-002, VR-003)
into a scored evaluation a GRC engineer runs during an actual vendor call.

```
SECTION 1 — GOVERNANCE PROGRAM MATURITY        Score (0-5): ____
[ ] Published AI governance policy
[ ] Named individual responsible for AI risk
[ ] Can describe AI risk assessment process
[ ] Federal/regulated industry experience

SECTION 2 — TRANSPARENCY                       Score (0-5): ____
[ ] Provides model card or equivalent
[ ] Discloses training data sources/characteristics
[ ] Discloses known model limitations
[ ] Will disclose architecture under NDA

SECTION 3 — FAIRNESS AND TESTING                Score (0-5): ____
[ ] Conducted fairness/bias testing
[ ] Willing to share results
[ ] Allows independent fairness testing access
[ ] Documented remediation process for found bias

SECTION 4 — SECURITY                            Score (0-5): ____
[ ] Third-party security assessment (SOC 2, FedRAMP)
[ ] Tested for adversarial robustness
[ ] Documented incident response process
[ ] Will support agency security assessment requirements

SECTION 5 — CONTRACTUAL TERMS                   Score (0-5): ____
[ ] Audit rights included
[ ] Model change notification (minimum 30 days)
[ ] Data handling and ownership terms
[ ] Liability and indemnification clauses
[ ] AI-specific governance obligations

OVERALL: Total score ____ / 25
24-25: Low risk — proceed
18-23: Medium risk — proceed with enhanced monitoring
12-17: High risk — requires remediation plan before contracting
Below 12: Critical risk — do not proceed without vendor changes
```

---

## Template 3 — Human Oversight Checklist

Operationalizes Module 6's human oversight controls into a field test a
GRC engineer runs against a live system, not just a documentation review.

```
PART 1 — DOES THE OVERRIDE MECHANISM ACTUALLY WORK?
(Request a live demonstration — do not accept documentation alone)
[ ] Reviewer was shown a live override of an AI decision
[ ] Override took effect within an acceptable timeframe
[ ] Override was logged automatically
[ ] The person performing override had appropriate authority/training

PART 2 — IS THE OVERRIDE MECHANISM ACCESSIBLE?
[ ] Frontline staff (not just admins) can initiate review/override
[ ] No excessive technical barriers prevent timely override
[ ] No excessive escalation layers for time-sensitive decisions

PART 3 — OVERRIDE RATE ANALYSIS
Current rate: ____%   Baseline: ____%   Variance: ____%
[ ] Rate within expected range
[ ] If unusually HIGH (>30%): investigated for AI reliability issue
[ ] If unusually LOW (<1% on high-stakes system): investigated for
    rubber-stamping / lack of genuine review

PART 4 — TRAINING VERIFICATION
[ ] All staff with override authority completed required training
[ ] Training covers system limitations and known failure modes
[ ] Training records current within renewal period
[ ] Spot interview confirms staff understand escalation path

PART 5 — DETERMINATION
Required oversight level: __________
Observed oversight level: __________
[ ] MATCH — appropriate for risk level
[ ] GAP — insufficient; escalate immediately
```

---

## Template 4 — AI Audit Readiness Checklist

Operationalizes the eight evidence categories from Module 7 into a
self-assessment run before any real audit notification arrives.

```
Rate each category: STRONG (audit-proof evidence) / WEAK (gaps remain) /
MISSING (no evidence exists)

1. AI SYSTEM INVENTORY                  [ STRONG / WEAK / MISSING ]
2. RISK ASSESSMENTS                     [ STRONG / WEAK / MISSING ]
3. TESTING RESULTS                      [ STRONG / WEAK / MISSING ]
4. APPROVAL RECORDS                     [ STRONG / WEAK / MISSING ]
5. HUMAN OVERSIGHT RECORDS              [ STRONG / WEAK / MISSING ]
6. MONITORING LOGS                      [ STRONG / WEAK / MISSING ]
7. INCIDENT REPORTS                     [ STRONG / WEAK / MISSING ]
8. AUDIT TRAILS                         [ STRONG / WEAK / MISSING ]

REMEDIATION PLAN for any WEAK/MISSING category:
Category | Action | Owner | Due date

OVERALL DETERMINATION:
[ ] READY — would withstand audit scrutiny today
[ ] CONDITIONALLY READY — minor gaps, remediation in progress
[ ] NOT READY — significant gaps requiring immediate attention
```

---

## Template 5 — Control Mapping Matrix (cross-framework)

Proves BridgeCore's methodology generalizes beyond NIST AI RMF alone —
directly relevant once ISO 42001 and EU AI Act modules are complete.

| BridgeCore Control | NIST AI RMF | ISO/IEC 42001 | EU AI Act | OMB M-24-10 |
|---|---|---|---|---|
| BF-001 (Fairness test) | MEASURE 2.x | 8.2 | Art. 10, 15 | Disparate impact testing |
| HO-001 (Override) | GOVERN 1.x, MANAGE 4.x | 8.4 | Art. 14 | Human oversight |
| TR-001 (Model card) | GOVERN 4.x, MAP 5.x | 8.3 | Art. 13 | Transparency |
| SC-001 (Security) | MANAGE 4.x | 8.5 | Art. 15 | Security baseline |
| VR-001 (Vendor DD) | GOVERN 5.x | 8.6 | Art. 16, 28 | Vendor management |

*This matrix expands as ISO 42001 and EU AI Act modules are completed.*

**Strategic value:** a federal client rarely operates under a single
framework. A single control implementation satisfying multiple frameworks
simultaneously is a major efficiency and cost argument in any proposal.

---

## The remaining templates — quick reference

| Template | One-line purpose |
|---|---|
| AI System Intake Form | Standardized submission for any new AI system (built in Module 4) |
| AI System Inventory | Master register tracking every AI system organization-wide |
| Incident Response Checklist | Step-by-step actions when an AI incident is detected |
| Risk Acceptance Form | Formal sign-off when residual risk is accepted, not treated |
| Exception Management Log | Tracks every instance a control could not be performed as designed |
| Evidence Checklist | What evidence to collect per control, by Module 7's eight categories |
| Compliance Dashboard Structure | Layout, metrics, data sources for executive governance dashboard |
| AI Risk Register Template | Formal version of what `generate_risk_register.py` produces automatically |
| AI Control Library | Full Module 6 control catalog as a standalone reference document |
| AI Governance Workflow | Complete six-stage process diagram from intake through monitoring |

---

## GRC engineering application — templates as specifications, not endpoints

Every template here is designed to feed directly into a Module 8 script, or
to be generated automatically by one. The Impact Assessment's Section B
determination logic could become a function exactly like
`classify_risk_tier()`. The Vendor Review Checklist's scoring system could
become an automated scoring function the same way the risk rating matrix
became `calculate_risk_rating()`.

**The deeper lesson:** a template is not the end product. It is the
specification for the next automation to build. As a GRC engineering
practice matures, fewer documents are filled in by hand — more are
generated, scored, and validated by code, with humans reviewing outputs
rather than completing blank forms.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Rights-impacting AI | OMB designation triggering mandatory minimum risk practices |
| Safety-impacting AI | OMB designation for harm-to-health/safety contexts |
| Waiver | Documented exception to a required minimum practice, CAIO-approved |
| Cross-framework mapping | One control satisfying multiple regulatory frameworks simultaneously |
| Template-as-specification | A manual template defines requirements for future automation |

---

## Practice questions

1. What two conditions trigger "rights-impacting" status under OMB M-24-10? Name three examples of each.
2. Why must human oversight verification include a live demonstration, not just documentation review?
3. What does a vendor review score between 12 and 17 require before contracting?
4. Why is mapping one control to multiple frameworks a strategic advantage in a federal proposal?
5. What is the relationship between a template and the Module 8 automation scripts?

---

## Hands-on exercise

Take the AI system from your Module 7 evidence inventory exercise. Complete
the Audit Readiness Self-Assessment template in full, including a
remediation plan for any category rated WEAK or MISSING. This produces a
real, usable deliverable for your BridgeCore portfolio.

---

## How to explain it in an interview

> "I maintain a library of operational templates that translate every NIST
> AI RMF function into a document a client team can actually use — an OMB
> M-24-10 aligned impact assessment, a vendor due diligence checklist, a
> human oversight verification protocol requiring live demonstration rather
> than just documentation review, and a cross-framework control mapping
> matrix. The key principle is that templates aren't the end product —
> they're specifications for the next automation. As a GRC engineering
> practice matures, manual templates get replaced by scripts that generate,
> score, and validate the same information automatically."

---

*Previous: [Module 8 — GRC Engineering & Automation](module-08-grc-engineering.md)*
*This is the final module in the public NIST AI RMF curriculum.*
