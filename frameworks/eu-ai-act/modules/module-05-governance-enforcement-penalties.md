# Module 5 — EU AI Act Governance Bodies, Enforcement, and Penalties
## Who enforces the Act, and what noncompliance actually costs

> **Framework:** EU AI Act — Regulation (EU) 2024/1689
> **Module:** 5 of 10 (estimated)
> **Status:** ✅ Complete

---

## Why this module matters

Module 4 covered what conformity assessment requires. This module covers
what happens when it doesn't happen — the governance structure responsible
for enforcement, and the actual financial exposure noncompliance creates.
This is the module that gives every other piece of this curriculum its
practical weight: classification, transparency obligations, and conformity
assessment all matter because there are real bodies with real authority to
investigate and penalize failures to meet them.

## The governance structure is layered, with different bodies doing different jobs

Unlike ISO 42001, where a single certification body handles an
organization's entire certification relationship, EU AI Act enforcement is
distributed across several distinct bodies, each with a different
function.

**The EU AI Office** sits inside the European Commission and has
specific responsibility for overseeing General-Purpose AI model
providers — the actors covered in Module 3 — along with coordinating
enforcement consistency across the whole EU and developing guidance and
codes of practice. This is the body most directly relevant to anything
involving foundation model providers specifically.

**National market surveillance authorities** are where most day-to-day
enforcement actually happens. Each EU member state designates its own
authority responsible for enforcing the Act within its territory:
investigating complaints, conducting inspections, and issuing penalties
for the majority of violations. This means there is no single enforcer
the way there's a single certification body per ISO 42001 engagement —
there are potentially as many separate national authorities as there are
EU member states, each operating within their own jurisdiction. For a GRC
engineer scoping client work, an early and non-obvious question is which
national authority actually has jurisdiction over a given client's AI
system — this isn't automatic the way "your chosen certification body" is
in ISO 42001 work.

**Notifying authorities** are a narrower, more technical layer. These are
the national bodies responsible for assessing and formally designating
which organizations qualify as notified bodies — the independent external
assessors covered in Module 4 who conduct conformity assessment for
certain high-risk system categories. Notifying authorities don't enforce
the Act against AI providers directly; they oversee the assessors who do
part of that work.

**The European Artificial Intelligence Board** sits above the national
layer as a harmonization mechanism. Composed of representatives from each
member state, it coordinates consistent application and interpretation of
the Act across the EU and advises the European Commission. Its existence
reflects a real risk in any law enforced at the national level across
multiple jurisdictions: without active coordination, different member
states could interpret and enforce identical provisions inconsistently,
undermining the Act's intended uniformity across the EU single market.

## The three-tier penalty structure, and why it deliberately mirrors GDPR

Article 99 establishes a three-tier penalty structure that closely follows
the model GDPR established for data protection violations — a structural
choice that signals how seriously the EU intends this regulation to be
enforced.

**Prohibited practices violations** — breaches of Article 5's banned
practices list, covered in Module 2 — carry the steepest penalties: up to
€35 million or 7% of total worldwide annual turnover, whichever is
higher. Notably, this is actually a higher percentage ceiling than GDPR's
maximum tier of 4% of turnover, a clear signal that violating the
prohibited practices list is treated as more severe than most data
protection violations under EU law.

**Other obligations** — including the high-risk system requirements
covered in Module 4, such as failing to complete conformity assessment or
failing to register in the EU database — carry penalties up to €15
million or 3% of global annual turnover, whichever is higher.

**Incorrect or incomplete information to authorities** carries penalties
up to €7.5 million or 1% of global annual turnover, whichever is higher.
This exists as its own distinct violation category specifically to
discourage organizations from obscuring or misrepresenting their actual
compliance status once a regulatory inquiry has begun — providing
authorities with false or incomplete information is penalized separately
from whatever underlying violation prompted the inquiry in the first
place.

## Why "whichever is higher" matters more for some companies than others

The "whichever is higher" calculation between the fixed euro amount and
the percentage of global turnover means the practical exposure differs
enormously by company size. For a large multinational provider, the
percentage figure typically dominates — 7% of a company with tens of
billions in global revenue is a far larger number than the €35 million
fixed ceiling. For a smaller company, the relationship inverts: 7% of a
modest revenue base might be a trivial sum compared to the fixed €35
million ceiling, which would otherwise expose a small business to a fine
vastly disproportionate to its actual size and ability to pay.

## The SME adjustment: the calculation logic flips for smaller providers

To address this disproportionality, the Act includes a specific
adjustment for small and medium enterprises, including startups.
For SMEs, penalties use whichever amount is lower between the fixed sum
and the percentage of turnover — the opposite logic from the standard
calculation applied to larger providers. This prevents a small AI startup
from facing a flat multi-million-euro exposure that bears no relationship
to its actual revenue, while still preserving meaningful financial
consequences scaled to the company's actual size.

This is a meaningful detail for any GRC engagement involving a smaller AI
company client. The penalty exposure calculus genuinely changes depending
on company size — it is not simply a smaller version of the same number,
it is calculated using the opposite comparison logic entirely.

## How this connects to the rest of the curriculum

This module is the reason classification work in Module 2, transparency
obligations in Module 3, and conformity assessment in Module 4 all
matter in a legally binding way rather than as best-practice guidance.
Misclassifying a high-risk system as limited-risk, as flagged in Module
2, isn't just a documentation gap — under this module's penalty
structure, it's exposure to the "other obligations" tier, up to €15
million or 3% of global turnover. Building a system that crosses an
Article 5 prohibited line isn't a risk to be modified, avoided, shared,
or retained the way ISO 42001's Clause 6 treats risk — it's exposure to
the Act's most severe penalty tier, with no available compliance pathway
to begin with.

---

## Key terms

| Term | Plain meaning |
|---|---|
| EU AI Office | The body within the European Commission overseeing GPAI providers and coordinating EU-wide enforcement |
| Market surveillance authority | The national body in each EU member state responsible for day-to-day enforcement |
| Notifying authority | The national body responsible for designating which organizations qualify as notified bodies |
| European Artificial Intelligence Board | The cross-member-state body coordinating consistent application of the Act |
| Article 99 | The provision establishing the Act's three-tier penalty structure |
| SME adjustment | The reversed "whichever is lower" penalty calculation applied to small and medium enterprises |

## Practice questions

1. Why doesn't the EU AI Act have a single enforcement body the way ISO
   42001 has a single certification body per engagement?
2. What is the difference in role between a national market surveillance
   authority and a notifying authority?
3. Why is the maximum penalty percentage for prohibited practices
   violations higher than GDPR's maximum penalty percentage?
4. Why does "whichever is higher" benefit regulators more when dealing
   with large multinational companies than with small ones?
5. How does the SME penalty calculation differ from the standard
   calculation, and why does that difference exist?
6. Why is providing incorrect information to authorities treated as its
   own separate, penalizable violation category?

## How to explain it in an interview

> "Enforcement under the EU AI Act is layered and distributed in a way
> that's genuinely different from ISO 42001's single certification body
> model. The EU AI Office handles GPAI providers specifically, but most
> day-to-day enforcement actually happens at the national level — each
> member state has its own market surveillance authority, which means
> there isn't one single enforcer, there are potentially dozens. The
> penalty structure mirrors GDPR deliberately: three tiers, each
> calculated as whichever is higher between a fixed euro amount and a
> percentage of global turnover. Prohibited practices violations actually
> carry a higher percentage ceiling than GDPR's maximum tier — seven
> percent versus GDPR's four — which tells you how seriously the EU
> treats Article 5 violations specifically. The detail worth knowing for
> client work is the SME adjustment: for smaller companies, the
> calculation flips to whichever amount is lower, not higher, specifically
> so a startup doesn't face a flat thirty-five million euro exposure that
> has nothing to do with its actual size."

---

*Previous: [Module 4 — Conformity Assessment for High-Risk AI Systems](module-04-conformity-assessment.md)*
*Next: Module 6 — Risk Management Systems Under Article 9*
