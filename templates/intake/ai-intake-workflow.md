# Template — AI Intake Workflow

> **Version:** 1.0
> **Based on:** NIST AI RMF 1.0 — GOVERN and MAP functions
> **Use:** Required process for every new AI system — whether built internally or procured from a vendor

---

## Purpose

No AI system should be deployed without completing this workflow.
It ensures every system is governed, assessed, and approved before going live —
and that ongoing monitoring is in place from day one.

---

## Stage 1 — Submission & Initial Intake

**Who triggers this:** Any team wanting to build, buy, or deploy an AI system.

**What happens:**
The requesting team completes the AI Intake Form (below) and submits it to the GRC team.
The GRC team acknowledges receipt within 2 business days and opens a governance ticket.

**Required inputs:**
- [ ] Intake form fully completed
- [ ] System name and plain-language purpose
- [ ] Requestor name and department
- [ ] Executive sponsor named
- [ ] Vendor name (if third-party) or internal build team
- [ ] Proposed go-live date

**Output:** Governance ticket opened. Risk pre-screen triggered.

**Gate:** Incomplete forms returned to requestor. No intake proceeds without an executive sponsor.

---

## AI Intake Form

```
SECTION 1 — SYSTEM IDENTIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
System / project name:      ________________________________
Requestor name:             ________________________________
Requestor department:       ________________________________
Executive sponsor:          ________________________________
Date submitted:             ________________________________
Proposed go-live date:      ________________________________

SECTION 2 — SYSTEM DESCRIPTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
What does this AI system do? (plain language, one paragraph)


What problem does it solve?


SECTION 3 — TECHNICAL PROFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Build type:
  [ ] Internal build
  [ ] Third-party vendor (vendor name: ___________________)
  [ ] Open-source model (model name: ___________________)
  [ ] Embedded in existing software (system name: ________)

Decision autonomy:
  [ ] Human in the loop (human approves every output)
  [ ] Human on the loop (human monitors, can intervene)
  [ ] Fully autonomous (no human review of individual outputs)

SECTION 4 — IMPACT PROFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Who is primarily affected by this AI?
  [ ] Internal staff only
  [ ] Customers / public
  [ ] Patients
  [ ] Job applicants / employees
  [ ] Government beneficiaries
  [ ] Other: _______________________________________________

Estimated number of people affected per month:
  [ ] Under 100
  [ ] 100 – 1,000
  [ ] 1,000 – 10,000
  [ ] 10,000 – 100,000
  [ ] Over 100,000

Does this system use personal or sensitive data? (check all that apply)
  [ ] Health / medical data
  [ ] Financial data
  [ ] Personal identifiers (name, SSN, date of birth)
  [ ] Biometric data (fingerprints, facial images, voice)
  [ ] Location data
  [ ] Employment records
  [ ] No personal data

SECTION 5 — REGULATORY PROFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Are you aware of regulations that may apply? (check all that apply)
  [ ] HIPAA (health data)
  [ ] FCRA (credit reporting)
  [ ] ECOA (equal credit opportunity)
  [ ] EEOC / Title VII (employment discrimination)
  [ ] GDPR / CCPA (privacy)
  [ ] FDA (medical devices / clinical decision support)
  [ ] State AI laws
  [ ] None identified
  [ ] Unknown — regulatory review needed

SECTION 6 — SPONSOR ATTESTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I confirm that the information above is accurate and I am
sponsoring this AI system through the governance process.

Executive sponsor name:     ________________________________
Title:                      ________________________________
Signature:                  ________________________________
Date:                       ________________________________
```

---

## Stage 2 — Risk Classification

**Who:** GRC engineer

**What happens:**
The GRC engineer reviews the submission and assigns a risk tier.

| Tier | Classification | Criteria |
|---|---|---|
| Tier 1 | Critical | Autonomous decisions + high-stakes population + sensitive data OR regulated domain |
| Tier 2 | High | Significant impact on individuals + limited human oversight |
| Tier 3 | Medium | Advisory outputs only + limited affected population |
| Tier 4 | Low | Internal tools + no personal data + easily reversible |

**Output:** Risk tier assigned. Review track communicated. Estimated timeline provided.

**Gate:** Tier 1 and 2 require full AI Review Board approval. Tier 3–4 may be delegated to GRC lead.

---

## Stage 3 — Multi-Disciplinary Review

**Who:** Specialist reviewers (routed by GRC engineer based on risk tier)

| Review | Required for | Reviewer |
|---|---|---|
| Legal & regulatory review | Tier 1, 2, 3 | Legal counsel |
| Privacy & data review (PIA) | Tier 1, 2, 3 | Privacy officer |
| Security review | Tier 1, 2, 3 | CISO / security team |
| Bias & fairness review | Tier 1, 2 | GRC engineer + data scientist |
| Vendor assessment | Tier 1, 2, 3 (vendor systems only) | GRC / procurement |

**Output:** All review checklists completed and signed. Issues documented with remediation actions.

**Gate:** All reviews must close before the system advances. Open issues block progression.

---

## Stage 4 — AI Risk Assessment

**Who:** GRC engineer (lead), with AI risk owner and specialist reviewers

**What happens:**
Full risk assessment conducted using the AI Risk Assessment Template.
All risks rated, registered, and assigned treatment plans.

**Output:** Completed risk register. Risk heat map. Risk treatment plan. Control requirements.

**Gate:** Critical-rated risks must have approved treatment plans before approval. Unresolvable Critical risks → rejection or redesign required.

---

## Stage 5 — Governance Committee Approval

**Who:** AI Review Board

**What happens:**
The full evidence package is reviewed. Formal deployment decision issued.

| Decision | Meaning |
|---|---|
| Approved | Proceed to deployment |
| Rejected | Returned to requestor with required changes |
| Conditional | Specific items must be resolved within defined timeline |

**Output:** Signed approval, rejection, or conditional approval record filed.

---

## Stage 6 — Deployment & Ongoing Monitoring

**Who:** AI system manager + GRC engineer

**What happens:**
System added to AI inventory. Monitoring activated. Risk owner confirmed.

**Ongoing governance schedule:**

| Cadence | Activity |
|---|---|
| Daily | Performance dashboard review |
| Monthly | Override rate and demographic distribution review |
| Quarterly | Formal fairness audit |
| Annually | Full AI risk reassessment; renewal decision by AI Review Board |
| On material change | Re-entry at Stage 2 (new data, new use case, significant model update) |

**Output:** System live under continuous governance. Monitoring active. Schedule established.

---

## Document control

| Field | Value |
|---|---|
| Version | 1.0 |
| Last reviewed | — |
| Next review due | — |
| Owner | GRC Lead |
| Approved by | — |
