# Module 9 — ISO/IEC 42001:2023 AI System Impact Assessments and Annex B Implementation Guidance
## Who is affected, and how the standard tells you to find out

> **Framework:** ISO/IEC 42001:2023 — AI Management System (AIMS)
> **Module:** 9 of 10
> **Status:** ✅ Complete

---

## How this module connects to Module 3

Module 3 catalogued what Annex A requires — the controls an organization
selects, implements, and documents in its Statement of Applicability. One
of those controls, AI system impact assessment, deserves its own module
because of how it's structured: it's a single named control, but
satisfying it well depends heavily on Annex B, the standard's own
implementation guidance for Annex A controls. Annex A says what to do.
Annex B says how to do it in a way that will actually hold up under audit
scrutiny and, more importantly, actually protect the people an AI system
affects.

## Impact assessment versus risk assessment: a distinction worth holding precisely

It's easy to conflate the AI system impact assessment with the Clause 6
risk assessment covered in Module 5, because both involve evaluating an AI
system before or during deployment. They ask different questions.

The Clause 6 risk assessment asks: what could go wrong with this AI
system, from the organization's perspective? It scores likelihood and
impact, and selects a treatment — modify, avoid, share, or retain.

The AI system impact assessment asks a related but distinct question: who
outside the organization is affected by this system, and in what way? A
risk assessment might conclude a hiring model carries medium risk and
select bias-testing controls as treatment. The impact assessment is the
document that actually walks through who is affected by that hiring
model — rejected candidates, current employees whose performance reviews
might eventually be informed by similar tooling, potentially regulators
with oversight authority over employment practices — and characterizes
each group's specific exposure.

Put simply: the risk assessment is about exposure to the organization. The
impact assessment is about exposure of the people the system touches. Both
are required, and an organization that completes one and treats it as
covering the other has a gap an auditor is likely to find.

## What Annex B actually adds

Annex A states the requirement to conduct AI system impact assessments
without prescribing exactly how. Annex B supplies the practical detail
that turns a vague requirement into something concrete enough to implement
and concrete enough for an auditor to evaluate against.

For a hiring-decision use case, Annex B guidance points toward documented
fairness testing across protected characteristics, and a defined path for
a rejected candidate to contest an automated decision — not just a general
acknowledgment that bias is theoretically possible. For a lending decision,
Annex B guidance points toward explainability sufficient to support
adverse action notices, because that intersects an existing legal
requirement (in many jurisdictions, lenders must be able to explain credit
denials), not just general AI governance best practice. For content
moderation, the guidance leans toward appeal mechanisms and periodic
accuracy review across different content types and languages, because the
impact in that domain touches freedom of expression and access to
information in ways a generic accuracy metric won't capture.

This is the part of the standard that turns "we thought about fairness"
into "we can show you exactly what we tested, and how someone affected by
this system can push back on a decision." An impact assessment without
this level of specificity tends to read as a formality rather than
evidence of genuine governance.

## Stakeholder mapping: where thin impact assessments usually fail

A common failure mode is writing an impact assessment that only considers
the direct user of a system — the recruiter using a hiring tool, the loan
officer reviewing a credit score output. Annex B guidance pushes the
assessment outward to a broader set of stakeholder groups:

- **Direct users** — the people operating the AI system day to day
- **People affected by the system's decisions** — who often never interact
  with the system directly and may not even know it was involved in a
  decision about them
- **Employees whose work changes because of the system** — including
  people whose own performance is now evaluated differently because of
  AI-assisted tooling
- **The general public** — particularly relevant for systems touching
  content moderation, public services, or broader rights and freedoms

A thorough impact assessment identifies which of these groups are
genuinely relevant to a given AI system before determining which impact
categories apply, rather than defaulting to whichever stakeholder group is
easiest to think about — almost always the direct user, almost never the
person on the receiving end of a decision they didn't ask for.

## Impact categories Annex B points toward

While the exact categories an organization uses can be adapted to its
context, Annex B guidance generally points toward considering:

- **Fairness and non-discrimination** — could the system produce disparate
  outcomes across protected groups
- **Transparency and explainability** — can an affected person understand
  why a particular decision was made
- **Legal and regulatory exposure** — does the use case intersect existing
  law, such as employment, lending, or data protection regulation
- **Accuracy and reliability** — what is the real-world cost of an
  incorrect output in this specific context
- **Rights and freedoms** — does the system affect expression, privacy, or
  access to services
- **Workforce impact** — does the system change how employees work, are
  evaluated, or are managed

Not every category applies to every system. A low-stakes internal
productivity tool, like a code assistant used only by engineers, carries
real accuracy and workforce-impact considerations but minimal exposure on
fairness or rights and freedoms. A hiring or lending system touches nearly
all of them. Part of doing the impact assessment well is being able to
justify why a category was scoped out, not just listing the categories
that were scoped in.

## Where the output goes

An AI system impact assessment is not a standalone document that gets
filed and forgotten. Its findings feed directly into two places already
covered in earlier modules:

It becomes supporting evidence for the relevant Annex A control claims in
the Statement of Applicability covered in Module 5 — if the SoA claims
fairness controls are implemented for a hiring system, the impact
assessment is part of the evidence trail an auditor will expect to see
behind that claim.

It can also change the Clause 6 risk treatment decision. A risk that
looked acceptable when evaluated purely through organizational exposure —
low likelihood of legal liability, manageable reputational risk — can look
substantially different once the impact assessment documents the actual
effect on the people the system makes decisions about. It is entirely
possible for an impact assessment to surface a concern significant enough
to shift a treatment decision from modify to avoid, even after a risk
assessment alone would have concluded modify was sufficient.

---

## Key terms

| Term | Plain meaning |
|---|---|
| AI system impact assessment | An Annex A control assessing who is affected by an AI system and how, distinct from organizational risk assessment |
| Annex B | The standard's implementation guidance explaining how to satisfy Annex A controls in practice |
| Stakeholder mapping | Identifying all groups affected by an AI system, not just its direct users |
| Affected party | A person impacted by an AI system's decisions, who may never interact with the system directly |
| Adverse action explainability | The level of explainability needed to justify a negative decision to the person it affects, often a legal requirement in lending |

## Practice questions

1. How does an AI system impact assessment differ from a Clause 6 risk
   assessment, even though both evaluate an AI system before deployment?
2. What role does Annex B play relative to Annex A?
3. Why does stakeholder mapping typically need to extend beyond a system's
   direct users?
4. Give an example of an impact category that would be highly relevant to
   a lending decision but less relevant to an internal code assistant.
5. How can the findings of an impact assessment change a risk treatment
   decision made under Clause 6?
6. Why might an organization justify excluding certain impact categories
   for a given AI system rather than addressing all of them?

## How to explain it in an interview

> "AI system impact assessment is an Annex A control, but it's a
> different question from the Clause 6 risk assessment. Risk assessment
> asks what could go wrong for the organization. Impact assessment asks
> who outside the organization is affected by the system and how — the
> people a hiring model rejects, the people a credit model denies, not
> just the recruiter or loan officer using the tool. Annex B is what makes
> this concrete: it's the standard's own implementation guidance, and for
> something like a hiring decision it points toward documented fairness
> testing and a real contestability path, not just an acknowledgment that
> bias is possible. The output isn't standalone — it becomes evidence
> behind your SoA control claims, and it can genuinely change a Clause 6
> treatment decision, because a risk that looks acceptable from a pure
> organizational-exposure lens can look very different once you document
> the actual impact on the people the system touches."

---

*Previous: [Module 8 — Continual Improvement Under Clause 10](module-08-continual-improvement-clause10.md)*
*This is the final module in the public ISO 42001 curriculum.*
