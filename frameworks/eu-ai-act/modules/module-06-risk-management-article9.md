# Module 6 — EU AI Act Risk Management Systems Under Article 9
## The substantive analytical engine inside the conformity assessment process

> **Framework:** EU AI Act — Regulation (EU) 2024/1689
> **Module:** 6 of 10 (estimated)
> **Status:** ✅ Complete

---

## Why this module is distinct from Module 4

Module 4 covered the procedural machinery a high-risk system has to pass
through before market entry: technical documentation, the assessment
pathway, declarations, registration, and post-market monitoring. This
module covers what actually has to be happening substantively inside
that process — Article 9's risk management system requirement, the
analytical content the Annex IV technical documentation has to
demonstrate is genuinely operating, not just describe.

It's a useful distinction to hold clearly: Module 4 is about the
approval process. This module is about the risk thinking that process is
designed to verify actually exists.

## The continuity requirement: the exception inside an otherwise front-loaded model

Module 4 established that most high-risk compliance work concentrates
before a system launches. Article 9 is the meaningful exception inside
that pattern. It explicitly requires the risk management system to
operate as a continuous, iterative process across the AI system's entire
lifecycle — planned and run as regular, systematic updates, not a single
assessment completed once before launch and then filed alongside the
rest of the technical documentation.

This makes Article 9 the closest thing in the entire EU AI Act to ISO
42001's Clause 6 risk assessment and Clause 9 performance evaluation
operating together as a continuous loop, covered in earlier modules of
that framework's curriculum. The distinction worth being precise about:
this continuous-operation requirement lives specifically within Article
9's risk management system, not across the whole conformity assessment
process described in Module 4, which remains substantially front-loaded
in its other components — technical documentation compilation,
assessment pathway selection, registration.

## Risk identification: intended use and reasonably foreseeable misuse

Article 9 requires identifying and analyzing the known and reasonably
foreseeable risks the high-risk AI system could pose. This has two
components that are easy to collapse into one but are meaningfully
distinct.

**Risks under intended use** — how the system behaves and what harms it
could cause when used exactly as designed and described.

**Risks under reasonably foreseeable misuse** — how the system could be
used in ways its provider did not intend, but reasonably should have
anticipated given the system's actual capabilities and deployment
context. This is a wider net than intended-use analysis alone, and it's
a common shortcut in risk assessment work generally to evaluate a system
only against its stated purpose and stop there. Article 9 explicitly
closes that gap — not by requiring providers to anticipate every
conceivable misuse, but by requiring genuine consideration of misuse a
reasonable provider, familiar with the system's actual capabilities,
would foresee as plausible.

Article 9 also includes a specific, named requirement to consider risks
to vulnerable groups, including children. This doesn't arrive as a
generic instruction to "consider all affected stakeholders" the way
Module 9 of the ISO 42001 curriculum approached impact assessment
through broad stakeholder mapping — it's called out explicitly, because
the Act treats certain populations as warranting deliberate, named risk
consideration rather than leaving their inclusion to a general
stakeholder exercise that might or might not surface them.

## Risk estimation and evaluation

Once identified, risks have to be estimated and evaluated — assessing
both the likelihood of occurrence and the severity of potential harm,
conceptually parallel to the likelihood-times-impact scoring covered in
ISO 42001's Clause 6, though the EU AI Act does not prescribe a specific
scoring methodology the way an organization's own ISO 42001 risk
methodology document would. The evaluation has to account for the
system's intended purpose and the context in which it's actually expected
to be deployed.

## Mitigation: design and development measures, not disclosure

This is one of the more important substantive requirements in Article 9,
and it's worth being precise about the distinction it draws. A provider
cannot satisfy this requirement by simply identifying a risk and
documenting it as a known limitation. Article 9 requires risk management
measures that genuinely eliminate or reduce the identified risk through
the system's actual design and development — technical interventions,
not paperwork acknowledging the risk exists.

Where a risk cannot be fully eliminated through design, adequate
mitigation and control measures are still required to reduce it as far
as reasonably possible. Only the risk that genuinely remains after these
measures have been applied — the residual risk — moves to the next
stage, rather than treating disclosure as an acceptable substitute for
attempting mitigation in the first place.

## Testing and validation: what separates a system from a document

Designing a mitigation measure isn't sufficient on its own. Article 9
requires testing that confirms the mitigation actually performs as
intended under conditions reasonably representative of the system's
actual deployment. This is what separates a genuine risk management
system from a risk management document — the difference between
asserting a mitigation works and demonstrating it does.

This testing connects directly back to the testing results required in
Annex IV's technical documentation, covered in Module 4. The testing
happening here, under Article 9's substantive risk management
requirement, is what generates the actual evidence that documentation
has to contain. The two modules describe the same underlying activity
from different angles: Module 4 covers what has to be filed; this module
covers what has to actually be done to produce something worth filing.

## Residual risk communication

After identification, evaluation, mitigation, and testing, whatever risk
genuinely remains — the residual risk — has to be communicated to users
and deployers. This is the final stage of the cycle, and it closes the
loop back to risk identification: residual risk that emerges from one
cycle becomes an input to ongoing monitoring and the next iteration of
the continuous process described above.

## What this means for GRC engineering work in practice

Article 9 is where a GRC engineer's actual analytical work concentrates
for a high-risk AI system engagement — the substantive risk thinking,
not just the procedural checklist. Building a genuine Article 9 risk
management system requires the same kind of disciplined methodology
covered in ISO 42001's Clause 6 risk assessment work, adapted to the
EU AI Act's specific requirements: explicit consideration of foreseeable
misuse, named attention to vulnerable groups, design-level mitigation
rather than disclosure-only treatment, and testing that produces real
evidence rather than asserted conclusions. The skill set transfers
substantially between the two frameworks, even though the legal
consequences of getting it wrong are structured very differently, as
covered in Module 5's penalty discussion.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Article 9 | The provision requiring a continuous risk management system for high-risk AI systems |
| Reasonably foreseeable misuse | Use of a system outside its intended purpose that a provider could reasonably anticipate given its actual capabilities |
| Vulnerable groups | Populations, including children, that Article 9 specifically names as requiring deliberate risk consideration |
| Mitigation through design | Risk reduction achieved through the system's actual technical design, distinct from disclosure or documentation alone |
| Residual risk | The risk that remains after mitigation measures have been applied and tested |

## Practice questions

1. How does Article 9's continuity requirement differ from the largely
   front-loaded structure of conformity assessment described in Module 4?
2. Why does risk identification under Article 9 need to cover both
   intended use and reasonably foreseeable misuse?
3. Why does Article 9 name vulnerable groups, including children,
   specifically rather than relying on general stakeholder consideration?
4. Why is documenting a known risk insufficient to satisfy Article 9's
   mitigation requirement on its own?
5. How does the testing and validation stage connect back to the
   technical documentation requirements covered in Module 4?
6. What happens to residual risk once mitigation and testing are
   complete?

## How to explain it in an interview

> "Article 9 is the substantive risk engine underneath the conformity
> assessment process from Module 4 — it's not the approval paperwork,
> it's the actual risk thinking that paperwork has to demonstrate is
> real. The biggest thing that sets it apart is that it's explicitly
> required to be continuous across the system's whole lifecycle, which
> is the one part of an otherwise front-loaded compliance process that
> actually resembles ISO 42001's ongoing risk and monitoring cycle. It
> covers both intended use and reasonably foreseeable misuse, and it
> specifically names vulnerable groups like children rather than leaving
> that to general stakeholder mapping. The part I'd flag as most
> important: mitigation has to happen through actual design and
> development changes, not just by writing the risk down as a known
> limitation, and it has to be tested to confirm it actually works.
> Only what's left after that — the genuine residual risk — gets
> disclosed to users."

---

*Previous: [Module 5 — Governance Bodies, Enforcement, and Penalties](module-05-governance-enforcement-penalties.md)*
*Next: Module 7 — Data Governance and Human Oversight Requirements (coming soon)*
