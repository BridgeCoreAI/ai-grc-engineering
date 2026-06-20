# Module 8 — EU AI Act Phased Implementation Timeline and the Digital Omnibus
## Why "when does the EU AI Act apply" doesn't have one answer

> **Framework:** EU AI Act — Regulation (EU) 2024/1689
> **Module:** 8 of 10 (estimated)
> **Status:** ✅ Complete
> **Note:** This module reflects the timeline as understood in June 2026,
> including a significant recent legislative development. Given how
> recently this changed, verify current status before relying on these
> dates for a live client engagement — implementation timelines for
> active EU legislation can continue to shift.

---

## Why a single regulation has multiple "go-live" dates

A natural assumption is that a law has one effective date — it passes,
and then it applies. The EU AI Act doesn't work this way. It entered into
force on 1 August 2024, but "entry into force" is not the same as
"obligations become applicable." The Act uses a phased implementation
structure, where different categories of obligation become legally
applicable at different points after entry into force, giving
organizations, member states, and the EU's own governance bodies time to
prepare for increasingly demanding requirements.

This phased structure connects directly to material covered in earlier
modules: the prohibited practices from Module 2, the governance bodies
from Module 5, the GPAI obligations from Module 3, and the high-risk
system requirements from Modules 4, 6, and 7 don't all switch on at once.
Knowing which obligations are live at any given point in time is itself a
compliance question a GRC engineer needs to be able to answer precisely
for a client.

## The phased timeline, as currently understood

**1 August 2024 — entry into force.** The Act formally became EU law as
Regulation (EU) 2024/1689. This date starts the phased implementation
clock but did not, on its own, make any substantive obligations
immediately applicable.

**2 February 2025 — prohibited practices and AI literacy obligations
applicable.** Article 5's banned practices, covered in detail in Module
2, became the first substantive obligations to take legal effect — only
six months after entry into force, the shortest runway of any category,
reflecting the severity the EU assigned this tier. AI literacy
obligations, requiring organizations to ensure staff interacting with AI
systems have sufficient understanding of them, also became applicable at
this point.

**2 August 2025 — governance bodies and General-Purpose AI obligations
applicable.** EU member states were required to have designated their
national competent authorities — the market surveillance authorities and
notifying authorities covered in Module 5 — by this date, along with
reporting their institutional readiness to the Commission. General-Purpose
AI provider obligations from Module 3 also became applicable here,
notably before the heaviest high-risk system requirements, so the
governance infrastructure needed to actually enforce those requirements
exists before they land.

**2 August 2026 — originally scheduled for most remaining obligations,
including high-risk requirements and Article 50 transparency rules.**
Under the Act as originally published, this was meant to be the major
milestone: the bulk of high-risk AI system obligations from Modules 4, 6,
and 7, along with Article 50's transparency obligations from Module 3,
were scheduled to become applicable here.

**2 August 2027 — originally scheduled for the final phase.** This was
meant to bring the remaining scope into full applicability: high-risk AI
systems that are themselves safety components of products already
regulated under separate EU product legislation (such as machinery or
medical devices), and full compliance for GPAI models placed on the
market before August 2025.

## The Digital Omnibus: a significant, very recent shift

As of June 2026, the timeline above has been materially affected by a
new piece of EU legislative activity called the Digital Omnibus package.
The Council of the European Union and the European Parliament reached a
provisional agreement on this package on 7 May 2026 — only weeks before
this module was written.

The most consequential change: the major high-risk obligations deadline,
originally set for 2 August 2026, has been pushed back to December 2027
under this agreement. A related long-stop date for product-embedded
high-risk systems has also shifted, to 2 August 2028. The stated
rationale tied to this shift involves linking the effective date of
high-risk compliance obligations to the actual availability of supporting
technical standards and conformity assessment tools — recognizing that
much of the detailed technical infrastructure the high-risk obligations
depend on wasn't fully ready on the original schedule.

This is worth treating as a live, evolving situation rather than a
settled fact, for two reasons specific to where things stand in June
2026. First, this is a provisional political agreement between the
Council and Parliament, not yet fully adopted and published EU
legislation — the formal legal text incorporating this delay was still
working through final adoption procedures as of this module's writing.
Second, because this changed so recently, any client-facing compliance
planning should explicitly verify the current legal status of the Digital
Omnibus amendment before treating December 2027 as a confirmed date,
rather than relying on this module as a permanent reference.

## What this means for GRC engineering work in practice

This phased and, as of now, partially shifting timeline has two practical
implications for client-facing compliance work.

**Classification and scoping work doesn't wait for enforcement
deadlines.** Even though the heaviest high-risk obligations now have a
later applicability date, the underlying work covered in Modules 2, 4, 6,
and 7 — classification, conformity assessment preparation, risk
management system design, data governance, and human oversight design —
still needs lead time to execute well. A pushed-back legal deadline is
not the same as a recommendation to delay the underlying work; it changes
when noncompliance becomes legally enforceable, not how long the actual
implementation work realistically takes.

**Timeline literacy is itself a service a GRC engineer provides.** A
regulation with multiple staggered applicability dates, now further
complicated by a recent and still-finalizing legislative amendment, is
exactly the kind of complexity clients need help navigating. Being able
to say precisely which obligations are currently live, which are
scheduled, and which dates are genuinely settled versus provisionally
agreed and still pending formal adoption is a distinct and valuable skill
separate from understanding the substantive obligations themselves.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Entry into force | The date a regulation formally becomes EU law, distinct from when its obligations become applicable |
| Applicability date | The date a specific category of obligation becomes legally enforceable |
| Digital Omnibus | A 2026 EU legislative package amending, among other things, the AI Act's high-risk obligations timeline |
| Provisional agreement | A political agreement between the Council and Parliament not yet formally adopted as final law |
| Long-stop date | A final compliance deadline for a specific narrower category of system, distinct from the general applicability date |

## Practice questions

1. Why does "entry into force" not mean the same thing as "obligations
   become applicable" under the EU AI Act?
2. Why did prohibited practices become applicable before any other
   category of obligation?
3. Why did governance body designation and GPAI obligations become
   applicable before the high-risk system requirements?
4. What changed under the Digital Omnibus package, and when was that
   change agreed?
5. Why is it important to distinguish a "provisional agreement" from
   finalized, published EU law when advising a client?
6. Does a delayed enforcement deadline mean a GRC engineer should advise
   a client to delay their underlying compliance work? Why or why not?

## How to explain it in an interview

> "The EU AI Act doesn't have one go-live date, it's phased — prohibited
> practices became applicable first, just six months after entry into
> force, then governance bodies and GPAI obligations, with high-risk
> system requirements originally scheduled to follow. The thing I'd
> flag as a current event rather than settled history: there's a
> package called the Digital Omnibus that the Council and Parliament
> provisionally agreed on in May 2026, which actually pushed the major
> high-risk obligations deadline back from August 2026 to December
> 2027, tied to giving more time for the technical standards those
> obligations depend on to actually be ready. It's a good example of why
> this space requires staying current rather than memorizing a fixed
> timeline — and a provisionally agreed change isn't the same as
> finalized law, so part of doing this work well is being precise about
> which dates are confirmed versus still moving. But a later legal
> deadline doesn't mean the underlying compliance work should wait —
> classification, risk management design, conformity assessment prep,
> all of that still takes real lead time regardless of when the
> enforcement clock actually starts."

---

*Previous: [Module 7 — Data Governance and Human Oversight Requirements](module-07-data-governance-human-oversight.md)*
*Next: Module 9 — Comparing EU AI Act, ISO 42001, and NIST AI RMF (coming soon)*
