# Module 5 — The AI Risk Assessment: Deep Dive

> **Framework:** NIST AI Risk Management Framework (AI RMF 1.0)
> **Module:** 5 of 10
> **Status:** ✅ Complete

---

## What this module covers

The AI risk assessment is the most important hands-on skill in AI GRC work.
It is the primary document that proves an organization is governing AI responsibly —
to regulators, auditors, executives, and the public.

This module covers the complete eight-step process: how to prepare, who to involve,
what questions to ask, how to rate every risk, how to collect evidence, how to
document findings, how to escalate, and how to track remediation to closure.

---

## The mindset shift

A risk assessment is not a form-filling exercise. It is a **structured investigation**.

Your job as a GRC engineer is to:
- Ask hard questions and push back on comfortable answers
- Document what you find honestly — even when inconvenient
- Rate risks based on evidence, not on what teams want to hear
- Surface problems early enough to fix them

The best risk assessments are uncomfortable for the people being assessed.
That discomfort is a signal that real risks are being found.

---

## The eight steps

| Step | Name | Key output |
|---|---|---|
| 1 | Prepare | Assessment plan, document request, session schedule |
| 2 | Profile the system | Completed system profile (Section A of risk assessment) |
| 3 | Identify risks | Risk list covering all ten risk types |
| 4 | Rate each risk | Risk register with likelihood, severity, and composite ratings |
| 5 | Collect evidence | Evidence file organized by risk type |
| 6 | Draft treatment plans | Treatment plan for every Medium+ risk |
| 7 | Escalate and approve | Formal governance committee decision, signed approval record |
| 8 | Track and monitor | Remediation tracker, monthly status reporting |

---

## Step 1 — Prepare

### Documents to request before the first session

| Document | What it tells you |
|---|---|
| System requirements or product brief | What the AI was built to do — were governance requirements included? |
| Architecture diagram | How data flows — where risks can enter |
| Training data description | Source, size, demographic coverage |
| Model documentation | Algorithm, training approach, test results |
| Vendor documentation | Model card, security docs, governance program |
| Previous assessments | What was found before — was it resolved? |
| Regulatory landscape summary | What laws apply |

**If the team cannot provide these documents — that is itself a finding.**
An undocumented AI system is an ungoverned AI system.

### Session structure for Tier 1–2 systems

| Session | Attendees | Focus |
|---|---|---|
| Technical deep-dive | GRC engineer, data scientist, ML engineer | Architecture, data, model behavior |
| Risk identification | GRC engineer, risk owner, legal, privacy, security | All ten risk types |
| Treatment and sign-off | GRC engineer, risk owner, AI Review Board | Findings, decisions, approval |

---

## Step 2 — Profile the system

### Questions that build the system profile

**Purpose:**
- What problem does this AI solve? Why AI over a simpler solution?
- What does it output — score, recommendation, decision, content?
- What action does the output trigger? Automatic or human-reviewed?
- What happens if the output is wrong? Who bears the consequences?

**Data:**
- What data trained this model? Where did it come from? When?
- Does training data include personal information?
- How representative is it of the population the model will serve?
- Who has access to training data and model weights?

**Decisions:**
- Does the AI make the final decision or support a human decision?
- How often does it make recommendations or decisions?
- Can outputs be appealed or corrected?

**The single most important question:**
> *"What is the worst realistic thing that could happen if this AI makes
> a wrong decision — and who does it happen to?"*

---

## Step 3 — Identify risks

### How to open a risk identification session

Set the ground rules first:

> *"The goal of this session is not to find fault with your work. It is to identify
> risks so we can manage them. The more honest we are now, the better protected
> everyone is later. Nothing said here means the project is cancelled."*

This framing matters. Engineers fear their projects will be blocked.
Make it safe to surface problems.

### Master question list by risk type

**Bias & discrimination**
- Who does this AI make decisions about? Are any members of protected groups?
- What variables does the model use? Are any proxies for protected characteristics?
- Was training data tested for demographic representativeness?
- Has the model been tested for disparate impact across demographic groups?
- If the model gets it wrong, does it get it wrong equally across all groups?

**Safety**
- What is the worst realistic outcome if the model produces a wrong output?
- Is the system involved in physical safety, medical decisions, or financial security?
- What is the failure mode — silent failure or alert?
- Is there a mechanism to catch errors before they cause harm?

**Security**
- Is the model accessible via an API? Is that API authenticated?
- Has anyone tested whether the model can be fooled by crafted inputs?
- Who can modify the model — change weights, retrain, update?
- What happens if the data feed is disrupted or poisoned?

**Privacy**
- What personal data does the system process?
- What is the legal basis for processing it?
- Could model outputs reveal information not explicitly provided?
- Does the system comply with GDPR, CCPA, HIPAA, or other applicable laws?

**Explainability**
- Can you explain in plain language why the model produced a specific output?
- Are affected individuals entitled to an explanation under law?
- If a regulator asked why the model made a specific decision, could you answer?

**Accountability**
- Who is the named AI Risk Owner?
- If this system causes harm tomorrow — who gets the call?
- Are decisions about this system logged and auditable?

**Vendor**
- Who built this model — internal team or external vendor?
- Have you seen the vendor's AI governance documentation?
- Can you audit the vendor or access fairness testing results?
- Does the contract require notification of model changes?

### Documenting risks as you go

Capture each risk immediately with:
- One-sentence description of the specific risk
- Risk type
- Trustworthy AI property affected
- Lifecycle stage where it originates
- Who raised it and when
- Evidence already available

**Do not rate risks during identification.** Separate identification from rating —
mixing them causes teams to anchor on low ratings to avoid scrutiny.

---

## Step 4 — Rate each risk

### The rating dimensions

**Likelihood**
- Low: unlikely given current context
- Medium: possible — some conditions exist
- High: probable — conditions clearly exist, or this has happened before

**Severity**
- Low: minor, reversible, affects few people
- Medium: moderate harm, manageable, bounded group
- High: serious harm, difficult to reverse, many people affected
- Critical: severe or irreversible harm, potentially widespread

### Risk rating matrix

| Severity \ Likelihood | Low | Medium | High |
|---|---|---|---|
| Critical | Medium | High | **CRITICAL** |
| High | Low | Medium | High |
| Medium | Low | Low | Medium |
| Low | Accept | Accept | Low |

### How to write a good rating justification

**Good:**
> "Rated HIGH likelihood because training data has confirmed underrepresentation
> of patients over 75 — evidenced by the demographic breakdown in the data quality
> report dated [date]. Rated HIGH severity because incorrect triage scores for this
> group could delay critical care. Composite rating: HIGH."

**Poor:**
> "This might be a problem."

The justification is what an auditor reads. It must be specific, evidence-based,
and defensible.

### Common rating mistakes

| Mistake | Why it is a problem |
|---|---|
| Anchoring low to protect the project | Produces misleading assessments; exposes organization to unmanaged risk |
| Conflating likelihood with severity | These are independent — rate them separately |
| Rating the control, not the risk | Rate inherent risk first; note residual risk separately |
| Not adjusting for scale | A 1% error rate on 10M daily decisions = 100,000 daily errors |

---

## Step 5 — Collect evidence

### Evidence quality hierarchy

1. Independent third-party testing results — **strongest**
2. Internal testing with documented methodology
3. Vendor-provided documentation
4. Team attestations and interviews
5. Analogies from similar systems — **weakest**

If your only evidence is "the team says it is fine" — that is a gap, not evidence.

### Evidence by risk type

| Risk type | Evidence to collect |
|---|---|
| Bias & discrimination | Fairness testing report, demographic training data breakdown, proxy variable analysis |
| Safety | Failure mode analysis, incident history, safety testing results |
| Security | Penetration test results, access control logs, adversarial robustness results |
| Privacy | Privacy impact assessment, data flow diagram, legal basis documentation |
| Explainability | Sample model outputs with explanations, explainability tool documentation |
| Accountability | Risk ownership assignment, governance minutes, approval records |
| Regulatory | Legal review memo, regulatory landscape analysis, compliance checklist |
| Vendor | Due diligence questionnaire, responses, contract review, model card |

---

## Step 6 — Draft treatment plans

### Treatment plan structure

```
Risk ID:          RISK-001
Risk description: Training data underrepresents patients over 75,
                  creating risk of incorrect triage scores for this group
Risk rating:      HIGH
Treatment choice: Mitigate
Treatment action: (1) Vendor to augment training data with minimum 15%
                  representation of patients over 75 by [date].
                  (2) Pre-deployment fairness testing to include
                  age-stratified performance analysis.
                  (3) Quarterly monitoring of triage score accuracy
                  for patients over 75 post-deployment.
Control owner:    Dr. Sarah Chen, CMO
Target date:      [date]
Residual risk:    Medium — acceptable with monitoring in place
Accepted by:      [Risk owner signature]
```

### Escalation triggers — stop the assessment immediately

- Any Critical risk with no viable treatment plan
- Evidence of active harm in a deployed system
- Regulatory violations creating immediate legal exposure
- Vendor refusal to provide required information
- System operating with no risk owner assigned

---

## Step 7 — Escalate and get approval

### The escalation path

```
GRC engineer identifies finding
         ↓
Discussed with AI risk owner
         ↓
Risk owner accepts or escalates to AI Review Board
         ↓
Board reviews full assessment
         ↓
Decision: Approve / Reject / Conditional approval
         ↓
Decision recorded, signed, and filed
```

### Presenting findings to leadership — three layers

| Layer | Audience | Content |
|---|---|---|
| Layer 1 — Executive summary | Leadership, board | One page: system, overall rating, top 3 risks, recommendation |
| Layer 2 — Risk register | Risk owner, GRC team | All risks with ratings, owners, treatment decisions |
| Layer 3 — Full assessment | Auditors, regulators | Complete documentation, all evidence referenced |

Leadership decides on Layer 1.
Auditors review Layer 3.
Everyone tracks Layer 2.

---

## Step 8 — Track remediation

### Remediation tracker fields

| Field | What to capture |
|---|---|
| Risk ID | Unique identifier |
| Finding | One-sentence description |
| Rating | Critical / High / Medium / Low |
| Treatment | Mitigate / Transfer / Accept / Avoid |
| Action required | Specific step to close this finding |
| Owner | Named individual accountable for closure |
| Target date | Resolution deadline |
| Status | Open / In progress / Closed / Overdue |
| Closure evidence | What proves this is genuinely resolved |

### What "closed" actually means

A finding is not closed when someone says it is fixed.
It is closed when there is **verifiable evidence** that the treatment action
was completed and the risk is reduced to the agreed residual level.

---

## Worked example — HealthFirst AI Triage Assessment

| Step | What happened |
|---|---|
| Prepare | Requested model card, training data demographics, architecture diagram, HIPAA docs. Three sessions scheduled. |
| Profile | Scores patients 1–5. Decision support — physician reviews all. 200 patients/day. Vendor-built. FDA and HIPAA regulated. |
| Identify | 14 risks surfaced. Top: training data 73% urban (underrepresents rural), no explainability, no BAA with vendor, no change notification clause. |
| Rate | Training data bias → CRITICAL. No BAA → HIGH. No change notification → HIGH. No explainability → MEDIUM. |
| Evidence | Vendor demographic report, HIPAA BAA gap checklist, contract legal review, sample outputs with no explanation text. |
| Treatment | CRITICAL: augment data, defer 60 days, re-run fairness tests. HIGH (BAA): execute before any data transmission. HIGH (contract): amendment required before go-live. MEDIUM: vendor adds explanation text in 30 days. |
| Escalate | One-page summary to AI Review Board. Decision: conditional approval — CRITICAL and HIGH must be resolved first. |
| Track | Remediation tracker opened. Monthly board updates. CRITICAL closed day 58 after vendor delivers augmented dataset and new fairness results reviewed and approved. |

---

## Key terms

| Term | Plain meaning |
|---|---|
| Inherent risk | Risk level before any controls are applied |
| Residual risk | Risk level after controls are applied |
| Risk identification session | Structured meeting to surface all potential risks |
| Treatment plan | Documented decision on what action to take for a specific risk |
| Remediation tracker | Log of all open findings being worked to closure |
| Escalation trigger | Condition requiring immediate escalation before assessment completes |
| Executive summary | One-page findings overview for leadership |
| Closure evidence | Documentation proving a finding is genuinely resolved |

---

## Practice questions

1. What is the difference between inherent risk and residual risk?
2. Why should risk identification and rating happen in separate sessions?
3. Name three escalation triggers that stop an assessment immediately
4. What does "closed" actually mean for a risk finding?
5. How do you present risk assessment findings to executive leadership?
6. What evidence would you collect for a bias risk?
7. Why is "the team says it is fine" not sufficient evidence?
8. What is the most important single question to ask when profiling an AI system?

---

## How to explain it in an interview

> "When I conduct an AI risk assessment I follow an eight-step process: prepare by
> gathering documentation and scheduling structured sessions, build a complete system
> profile, run a facilitated risk identification session covering all ten risk types,
> rate each risk on likelihood and severity using a heat map, collect evidence to
> support every rating, draft treatment plans for all medium and above risks, escalate
> findings to the governance committee for formal approval, and track remediation to
> verified closure. The most important discipline is separating identification from
> rating, and never accepting 'the team says it is fine' as evidence. Every finding
> needs a justification an auditor can read and trust."

---

*Previous: [Module 4 — Real-World Application](module-04-real-world-application.md)*
*Next: Module 6 — Governance Controls*
