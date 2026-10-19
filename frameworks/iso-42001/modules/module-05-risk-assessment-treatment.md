# Module 5 — ISO/IEC 42001:2023 AI Risk Assessment and Treatment Under Clause 6
## Where the framework stops being described and starts being operated

> **Framework:** ISO/IEC 42001:2023 — AI Management System (AIMS)
> **Module:** 5 of 10
> **Status:** ✅ Complete

---

## Why Clause 6 is the operational core

Everything in Clauses 4 and 5 — setting organizational context, establishing
leadership commitment, defining scope — is preparation. Clause 6 is where an
organization actually picks up AI risks, scores them, decides what to do about
them, and creates the paper trail that will survive an audit. The standard
requires this to be systematic, documented, and repeatable, not a one-off
exercise completed before the stage 2 audit and then quietly shelved.

For a GRC engineer, Clause 6 is the deliverable. It is where the technical
work of understanding an organization's AI systems meets the governance work of
deciding what risk is acceptable and what controls are required. Being able to
lead a Clause 6 assessment — and explain the reasoning to leadership, auditors,
and clients — is one of the most practical skills ISO 42001 builds.

## The mandatory sequence: methodology before assessment

The first thing Clause 6.1.2 requires is not a risk assessment. It is a
documented risk assessment methodology — a written specification of how
assessments will be conducted, covering:

- The criteria for deciding what constitutes an acceptable risk
- The scales used to score likelihood and impact
- How the two scores combine to produce an overall risk level
- Who is authorized to review and approve risk assessment outcomes

This document matters independently of any individual assessment result.
A stage 1 auditor reads it to determine whether the organization has a
coherent approach before checking whether that approach has been applied.
If the methodology is vague or missing, every downstream risk assessment
is unsupported, which creates a gap that can rise to the level of a major
nonconformity even if the individual assessments are otherwise thorough.

Only once the methodology exists does the organization apply it: identifying
AI-specific risks, scoring each one, and deciding on a treatment.

## AI-specific risk identification

The risks Clause 6 is designed to surface are not generic IT risks. They
arise from the specific characteristics of AI systems — properties that
make AI risks different from the risks that ISO 27001 was built to address:

- Bias and discrimination in model outputs, particularly in high-stakes
  decisions like hiring, lending, or law enforcement
- Model drift: performance degradation over time as real-world data
  distributions shift away from training data
- Data quality failures, including personal data in training sets without
  legal basis, or training data that embeds historical biases
- Lack of explainability: decisions that cannot be understood or contested
  by the people they affect
- Third-party AI vendor dependencies, where the organization uses AI
  systems it does not control and may not fully understand
- Dual-use risk: AI capabilities developed for one purpose being repurposed
  in ways that generate new harms

A useful framing: in cybersecurity risk assessment, the AI system is typically
an asset being protected from threats. In ISO 42001 risk assessment under
Clause 6, the AI system can itself be the threat — a model that produces
biased outputs is not being attacked, it is functioning as designed while
generating harm. This shift in the risk object is what makes AI risk
assessment genuinely distinct from information security risk assessment,
and the ability to articulate that distinction clearly is one of the
markers of a competent AI GRC practitioner.

## Scoring: likelihood and impact

Most organizations implement a 5×5 risk matrix:
- Likelihood: 1 (rare) to 5 (almost certain)
- Impact: 1 (negligible) to 5 (catastrophic)
- Risk score: Likelihood × Impact (1–25)
- Levels: Low (1–4), Medium (5–12), High (13–25)

The numbers are not fixed by the standard — what matters is that the
methodology defines them explicitly and applies them consistently. A 3×3
matrix is equally conformant if it is documented and applied with discipline.

What the standard does require is that any risk scoring above the defined
acceptance threshold triggers a treatment decision. Risks that fall below
the threshold can be retained (accepted as-is), but that acceptance still
needs to be documented — "we looked at this risk and decided it was within
appetite" is a different audit finding from "we never looked at this risk."

## The four treatment options

Clause 6.1.3 requires the organization to select and apply treatment for
risks that exceed the acceptance threshold. Four options are available, and
each has different implications:

**Modify.** Apply controls to reduce likelihood, impact, or both. This is
the most common treatment path and the one that connects directly into the
Annex A catalog from Module 3. Applicable controls are documented in the
Statement of Applicability and implemented, with evidence of implementation
retained for audit.

**Avoid.** Stop or decline to start the AI use case entirely. This is the
right treatment when residual risk — the risk remaining after all
practicable controls are applied — still exceeds what the organization can
accept. Choosing to avoid a risk is a legitimate and sometimes courageous
governance decision; it is not a failure.

**Share.** Transfer risk to an insurer, a supplier, or through contractual
arrangements. Third-party AI vendor contracts that include liability
provisions, SLAs, or explicit AI governance obligations are a form of risk
sharing. The risk does not disappear — it is redistributed — but the
organization's direct exposure is reduced.

**Retain.** Accept the risk as-is, with formal documentation and sign-off.
Retention is only appropriate for risks that fall within the defined
acceptance threshold. It is not a catch-all for risks the organization
does not have capacity to address; using it that way is a major
nonconformity waiting to be discovered.

## The Statement of Applicability

The SoA is the document that links risk assessment to control implementation.
Every control in Annex A must be addressed in the SoA — either:

- Marked as applicable, with an explanation of how it is implemented and
  a pointer to the evidence, or
- Excluded, with a documented justification for why it is not relevant to
  this organization's scope and AI systems.

The SoA is not a one-time deliverable. It is a living document that gets
updated whenever new AI systems enter scope, when risk assessment outcomes
change, when controls are added or removed, or when the audit cycle
surfaces gaps. An outdated SoA — one that claims controls are implemented
that actually aren't, or that excludes controls now made relevant by new
AI deployments — is one of the most common sources of major nonconformities
in stage 2 audits.

An important discipline: the SoA is the bridge between the risk register
and the audit evidence. Auditors will use it to trace from a documented
risk through the treatment decision to the specific Annex A control, and
then to the evidence that the control is actually operating. Any gap in
that chain — a control listed in the SoA with no corresponding evidence —
is the kind of finding that can block certification.

## Clause 6 and the PDCA cycle

Clause 6 sits in the Plan phase of the PDCA cycle introduced in Module 1.
Risk assessment and treatment planning happen before implementation — you
Plan what controls are needed, Do the implementation in Clause 8, Check
whether the controls are working through monitoring and internal audit in
Clause 9, and Act on deficiencies through management review and continual
improvement in Clause 10. The risk register and SoA are living Plan-phase
documents that feed every subsequent phase.

This circularity is intentional. ISO 42001 is a management system standard,
not a checklist — its underlying assumption is that risk landscapes evolve,
AI systems change, and governance has to keep up. Clause 6 is not a
milestone you pass; it is a recurring practice.

## How this differs from ISO 27001 risk assessment

The structure of Clause 6 in ISO 42001 deliberately mirrors the equivalent
clause in ISO 27001, which makes adoption easier for organizations that
already have an information security management system. But the differences
are substantial:

- The risk object is different: AI systems are not just assets to protect,
  they can also be sources of harm
- The harm types are different: bias, unfair treatment, lack of explainability,
  and inappropriate automation of consequential decisions are not
  cybersecurity concepts
- The stakeholders affected are different: the people harmed by a biased
  AI system are often outside the organization, not just the organization's
  own data or operations
- The controls are different: Annex A includes controls like human oversight,
  impact assessments, and AI objective setting that have no direct equivalent
  in ISO 27001's Annex A

Organizations with ISO 27001 certification do not get a free pass on Clause
6 of ISO 42001 — they need to run a separate, AI-specific risk assessment
process, though they can leverage the same methodological infrastructure.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Risk assessment methodology | A documented specification of how risks will be identified, scored, and accepted — required before any individual risk assessment |
| Risk acceptance criteria | The threshold below which a risk is acceptable without treatment — must be defined in the methodology |
| Risk score | Likelihood × Impact, producing a numeric level used to compare and prioritize risks |
| Modify | Treatment option: apply controls to reduce likelihood or impact |
| Avoid | Treatment option: stop or decline the AI use case |
| Share | Treatment option: transfer risk through contracts, insurance, or supplier obligations |
| Retain | Treatment option: formally accept the risk as-is, documented and approved |
| Statement of Applicability (SoA) | The document listing every Annex A control as applicable (with implementation detail) or excluded (with justification) |
| Residual risk | The risk remaining after controls are applied — the level that must fall within acceptance criteria for treatment to be complete |

## Practice questions

1. Why does the standard require a risk assessment methodology before the
   risk assessment itself?
2. Name three AI-specific risk types that would not typically appear in an
   ISO 27001 risk assessment.
3. What distinguishes the "retain" treatment option from simply ignoring a
   risk?
4. An organization's SoA lists a control as applicable but there is no
   evidence of implementation. What kind of audit finding does this
   likely produce?
5. How does the risk object in AI risk assessment differ from the risk
   object in information security risk assessment?
6. Where does Clause 6 sit in the PDCA cycle, and what happens to the
   risk register outputs in subsequent phases?

## How to explain it in an interview

> "Clause 6 is where the rubber meets the road in ISO 42001. Before you
> can assess any risk, you need a documented methodology — a written
> definition of your scoring scales, acceptance criteria, and approval
> authority. Then you identify AI-specific risks, which is different from
> information security risk assessment because the AI system itself can be
> the source of harm, not just an asset being protected. You score each
> risk, apply one of four treatments — modify, avoid, share, or retain —
> and document the whole thing in a risk register and a Statement of
> Applicability that maps every Annex A control to either an implemented
> control or a documented exclusion. The SoA is the document auditors
> use to trace from risk to treatment to evidence, so gaps there are
> usually where major nonconformities show up."

---

*Previous: [Module 4 — Certification Process and Audit Cycle](module-04-certification-audit-cycle.md)*
*Next: Module 6 — Operational Controls and Clause 8*
