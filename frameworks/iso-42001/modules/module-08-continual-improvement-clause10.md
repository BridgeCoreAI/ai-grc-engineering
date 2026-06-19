# Module 8 — ISO/IEC 42001:2023 Continual Improvement Under Clause 10
## The Act phase: turning findings into lasting change

> **Framework:** ISO/IEC 42001:2023 — AI Management System (AIMS)
> **Module:** 8 of 10
> **Status:** ✅ Complete

---

## Why Clause 10 is small but decisive

Clause 10, Continual Improvement, is the shortest clause in ISO 42001 by
word count, but it determines whether everything built across Clauses 4
through 9 actually compounds over time or simply remains static once
initial certification is achieved. It is the Act phase of the PDCA cycle
introduced in Module 1: Plan happens in Clause 6, Do happens in Clause 8,
Check happens in Clause 9, and Act happens here.

Clause 10 has two distinct parts that are easy to conflate but serve
different purposes: corrective action, which is reactive and addresses a
specific identified problem, and continual improvement, which is proactive
and addresses the AIMS as a whole, independent of any particular failure.

## Corrective action: a defined sequence, not a quick fix

When a nonconformity is identified — through internal audit findings from
Module 7's Clause 9.2, through monitoring data revealing a control isn't
working, through an incident, or through findings carried over from an
external surveillance audit — the instinct is often to fix the immediate
symptom and move on. Clause 10 requires more discipline than that, and
skipping steps in this sequence is one of the most common audit findings
in this part of the standard.

**Root cause analysis comes first.** Before any fix is implemented, the
organization has to understand why the nonconformity occurred, not just
what occurred. A missing AI literacy training record (the kind of
requirement covered in Module 2's discussion of Clause 7) is not
adequately explained by "we forgot to log it." The actual root cause might
be that the AIMS has no automated reminder mechanism, or that the person
who owned the training program changed roles without a handoff process.
Treating the symptom — backfilling the missing record — without addressing
the root cause means the same nonconformity is likely to recur.

**A corrective action plan follows**, with a defined owner and a deadline.
This plan is what gets tracked through to closure, the same way
internal audit findings are tracked under Clause 9.2.

**Implementation and verification come last**, and verification is a
distinct step from implementation. The organization has to confirm the
corrective action actually resolved the nonconformity, not simply that the
action was carried out. A corrective action that was implemented but never
verified leaves an open question an auditor will ask directly: how do you
know this won't happen again?

An organization that jumps straight from "nonconformity found" to "fixed"
without a documented root cause analysis step has a paper trail that
typically does not satisfy Clause 10 in practice, even if the underlying
problem was genuinely resolved.

## Continual improvement: proactive, not just reactive

The second part of Clause 10 is easy to treat as an aspirational slogan
rather than an auditable requirement, but it is a distinct obligation. Continual
improvement is not triggered by a nonconformity — it is the standard
requiring the organization to actively look for ways to improve the AIMS
even when nothing is currently broken.

In practice, this shows up as things like:

- Recalibrating a risk scoring methodology after several years of data
  revealed it was systematically over- or under-weighting certain risk
  types
- Expanding monitoring coverage to a category of AI risk that wasn't fully
  anticipated when the AIMS was first designed
- Simplifying a control that, in practice, turned out to be more
  bureaucratic overhead than actual risk reduction
- Updating the risk assessment methodology to account for a newly
  significant AI risk category, like agentic AI systems or new
  regulatory developments

The distinction matters in an audit context. An organization that can only
point to corrective actions — always reacting to findings that someone
else surfaced — has not demonstrated continual improvement as a practice
in its own right. Auditors specifically look for evidence the organization
is improving the AIMS proactively, independent of being prompted by a
nonconformity.

## Where the loop actually closes

The structural point that ties the entire ten-module arc together: Clause
10 does not generate a separate body of documentation. Its outputs are
changes to documents and practices established everywhere else in the
standard.

A corrective action that traces back to a gap in the risk assessment
methodology doesn't simply close out in a Clause 10 tracker — it should
trigger an actual revision to the risk methodology or risk register
covered in Module 5's discussion of Clause 6. A continual improvement
initiative that changes how monitoring is conducted should appear as a
concrete revision to the operational controls covered in Module 6's
discussion of Clause 8. If a corrective action plan is closed out but
nothing in the underlying AIMS documentation actually changed, the loop
has not genuinely closed — only the tracker has been updated.

This is also why Clause 10 is the shortest clause in the standard. It is
not generating new artifacts of its own; it is the mechanism by which
findings and improvement opportunities get translated into modifications
of the artifacts that already exist across Clauses 6 through 9.

## How this plays out across a full audit cycle

Connecting this back to Module 4's certification and audit cycle: every
surveillance audit and recertification audit is, in part, a check on
whether Clause 10 is functioning. An auditor revisiting an organization a
year after a previous finding will look specifically for evidence that the
corrective action was not just completed but verified, and that — where
relevant — the underlying methodology or control was actually updated, not
just patched in the instance that was caught. A pattern of recurring
similar findings across multiple audit cycles is one of the strongest
signals that Clause 10 is not functioning as intended, regardless of how
quickly individual corrective actions get closed.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Corrective action | A reactive process to address a specific identified nonconformity |
| Root cause analysis | Determining why a nonconformity occurred, not just what occurred |
| Continual improvement | A proactive practice of improving the AIMS independent of any specific nonconformity |
| Verification | Confirming a corrective action actually resolved the nonconformity, distinct from confirming it was implemented |
| Closed loop | The principle that Clause 10 outputs must result in actual changes to documents and practices elsewhere in the AIMS |

## Practice questions

1. What is the difference in purpose between corrective action and
   continual improvement?
2. Why does Clause 10 require root cause analysis before a corrective
   action plan is built?
3. What is the difference between implementing a corrective action and
   verifying it?
4. Give an example of a continual improvement activity that would not be
   triggered by any specific nonconformity.
5. Why is it said that Clause 10 doesn't generate its own body of
   documentation?
6. What pattern across multiple audit cycles signals that Clause 10 is
   not functioning as intended?

## How to explain it in an interview

> "Clause 10 is the Act phase of PDCA, and it's actually two different
> things people often collapse into one. Corrective action is reactive —
> a nonconformity gets found, you do root cause analysis to understand
> why it happened, build a plan with an owner and deadline, implement it,
> and then verify it actually worked, not just that it was done.
> Continual improvement is separate and proactive — it's the requirement
> that the organization keeps improving the AIMS even when nothing's
> currently broken, recalibrating a risk methodology or tightening
> monitoring coverage because of what's been learned over time. The thing
> that ties it together is that Clause 10 doesn't have its own
> documentation — its outputs are actual changes to the risk register,
> the SoA, the operational controls established everywhere else in the
> standard. If a corrective action gets marked closed but nothing in the
> underlying documentation changed, the loop hasn't really closed."

---

*Previous: [Module 7 — Performance Evaluation Under Clause 9](module-07-performance-evaluation-clause9.md)*
*Next: Module 9 — AI System Impact Assessments and Annex B Implementation Guidance (coming soon)*
