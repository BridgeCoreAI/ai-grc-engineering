# Module 1 — EU AI Act Overview
## Binding law, not a framework you opt into

> **Framework:** EU AI Act — Regulation (EU) 2024/1689
> **Module:** 1 of 10 (estimated)
> **Status:** ✅ Complete

---

## The fundamental difference: this is law, not guidance

The two frameworks covered earlier in this curriculum — NIST AI RMF and
ISO/IEC 42001:2023 — are things an organization chooses to engage with.
NIST AI RMF is voluntary guidance with no enforcement mechanism at all.
ISO 42001 is a certifiable management system standard an organization
opts into, pursuing certification because it provides value — to clients,
to regulators, to its own risk posture — not because the law requires it.

The EU AI Act is different in kind, not just degree. It is binding
regulation — formally Regulation (EU) 2024/1689 — with the legal force of
EU law. It does not ask an organization to adopt anything. If an
organization's AI systems fall within the Act's scope, the obligations
apply whether or not the organization ever decided to engage with the
Act at all. Noncompliance carries real financial penalties, not just
reputational or commercial consequences: fines for the most serious
violations can reach into the tens of millions of euros or a percentage
of global annual turnover, whichever is higher, similar in structure to
GDPR's penalty regime.

This distinction is the first thing worth being able to articulate
clearly, because it changes the nature of every piece of GRC engineering
work that follows. With ISO 42001, the question is "how do we build a
system that will pass certification." With the EU AI Act, the question is
"are we legally compliant," and the answer carries legal exposure
regardless of whether anyone ever audits the answer.

## Scope: who this actually applies to

The Act has broad extraterritorial reach, modeled on the same logic GDPR
established for data protection. It applies to:

- Providers placing AI systems on the EU market, regardless of where the
  provider is established
- Deployers of AI systems located within the EU
- Providers and deployers located outside the EU, if the AI system's
  output is used within the EU

This means a US-based company building an AI hiring tool used by a
European subsidiary, or an AI system whose outputs affect people located
in the EU even if the system itself runs entirely outside EU
infrastructure, can fall within scope. "We're not based in Europe" is not
by itself an exemption — the relevant question is where the system is
placed on the market or where its effects land, not where the company
is headquartered.

## The risk-tier structure: the organizing logic of the entire Act

Unlike ISO 42001, where every certified organization satisfies the same
seven core clauses regardless of what AI it builds, the EU AI Act's
obligations are conditional on classification. The tier an AI system
falls into determines almost everything else about what's legally
required. There are four tiers.

**Unacceptable risk — banned outright.** Certain AI practices are
prohibited entirely, with no compliance pathway available. Examples
include government social scoring systems, real-time remote biometric
identification in publicly accessible spaces for law enforcement purposes
(subject to narrow exceptions), AI systems designed to manipulate people
through subliminal or deceptive techniques that exploit vulnerabilities,
and emotion recognition systems used in workplaces or educational
institutions. There is no equivalent in ISO 42001's risk treatment
framework — Clause 6's "avoid" treatment is a choice an organization
makes; here, the choice has already been made by the regulation itself.

**High-risk — heavily regulated.** AI systems used in specified
high-stakes domains — employment and worker management, access to
essential services like credit scoring, critical infrastructure
management, law enforcement, migration and asylum processing, education
and vocational training access, and certain medical devices — face
extensive obligations. These include risk management systems, data
governance requirements, technical documentation, human oversight
provisions, a conformity assessment process before the system can be
placed on the market, and registration in an EU-wide database. This is
the tier where the bulk of substantive GRC engineering work under the Act
actually lives, and it has surface similarities to ISO 42001 certification
(documentation, risk management, oversight) while being legally mandatory
rather than voluntary, on a timeline set by the regulation rather than by
client preference.

**Limited risk — transparency obligations.** AI systems that interact
with people in ways that could be mistaken for human interaction —
chatbots, deepfake generators, AI-generated content more broadly — trigger
a disclosure requirement: people must be informed they are interacting
with an AI system, or that content they're viewing was AI-generated. No
conformity assessment is required, but the obligation is mandatory and
applies extremely broadly across consumer-facing AI products. This tier
is easy to underestimate precisely because the individual obligation
looks small.

**Minimal risk — largely unregulated.** The vast majority of AI systems
currently in use — spam filters, AI-enabled video games, inventory
management systems — carry no specific obligations under the Act at all.

## Why classification is the first and most consequential step

Because obligations are entirely conditional on tier, the single most
important early step in any EU AI Act compliance engagement is
classification: determining which tier a given AI system actually falls
into. Misclassifying a high-risk system as limited-risk doesn't just
create an administrative gap — it means an organization skips conformity
assessment, risk management documentation, and registration entirely for
a system that legally required all three. This is structurally different
from ISO 42001, where most readiness gaps are about depth and evidence
within a known set of clauses. Under the EU AI Act, the first gap that
can occur is getting the classification itself wrong.

## General-Purpose AI: a separate problem the tier system doesn't solve

One structural piece worth flagging now, ahead of the dedicated module
that will cover it later in this curriculum: General-Purpose AI (GPAI)
models — foundation models capable of being deployed across many
different downstream use cases — don't fit cleanly into the four-tier
system described above. A foundation model isn't inherently a hiring
tool or a chatbot; it becomes one depending on how a downstream developer
deploys it. The Act addresses this with a separate set of obligations
specifically for GPAI model providers, layered on top of the risk-tier
system rather than replacing it. This is a governance problem neither
NIST AI RMF nor ISO 42001 had to solve at the time they were written,
because neither was built around legally binding, tiered obligations in
the first place.

## How this compares to the two frameworks already covered

| | NIST AI RMF | ISO/IEC 42001 | EU AI Act |
|---|---|---|---|
| Nature | Voluntary guidance | Voluntary, certifiable standard | Binding law |
| Applies to | Whoever chooses to adopt it | Whoever pursues certification | Anyone in scope, regardless of choice |
| Structure | Four functions (Govern, Map, Measure, Manage) | Ten clauses, PDCA cycle | Four risk tiers, conditional obligations |
| Enforcement | None | Certification body audit | Government regulators, financial penalties |
| Obligations | Same guidance for everyone | Same clauses for every certified org | Different obligations depending on system's risk tier |

---

## Key terms

| Term | Plain meaning |
|---|---|
| Regulation (EU) 2024/1689 | The formal legal citation for the EU AI Act |
| Provider | An organization placing an AI system on the EU market |
| Deployer | An organization using an AI system within the EU |
| Risk tier | The classification (unacceptable, high, limited, minimal) determining an AI system's legal obligations |
| Conformity assessment | The mandatory pre-market evaluation process required for high-risk AI systems |
| General-Purpose AI (GPAI) | Foundation models with broad downstream applicability, subject to separate obligations layered on the tier system |

## Practice questions

1. How does the EU AI Act's legal nature differ from NIST AI RMF's and
   ISO 42001's?
2. Can a company headquartered outside the EU fall within the Act's
   scope? Under what condition?
3. Why is risk-tier classification described as the most consequential
   early step in an EU AI Act compliance engagement?
4. Name two practices that fall into the unacceptable risk tier.
5. Why don't General-Purpose AI models fit cleanly into the four-tier
   classification system?
6. What does the limited-risk tier require, and why is it easy to
   underestimate?

## How to explain it in an interview

> "The biggest thing to understand about the EU AI Act is that it isn't
> a framework you adopt, it's a law you're bound by. NIST AI RMF is
> voluntary, ISO 42001 is a standard you choose to get certified
> against — the EU AI Act applies whether or not you ever engaged with
> it, with real financial penalties for noncompliance. The whole
> structure is built around four risk tiers — unacceptable, high,
> limited, and minimal — and unlike ISO 42001 where every certified
> organization meets the same set of clauses, here your obligations are
> entirely conditional on which tier your AI system falls into. That
> makes classification the single most important early step: get it
> wrong, and you might skip conformity assessment and risk management
> documentation entirely for a system that legally required both. The
> piece that doesn't fit neatly into any of this is General-Purpose AI —
> foundation models get their own separate obligations because they
> don't belong to just one risk tier, they become whatever a downstream
> deployer turns them into."

---

*Next: Module 2 — Prohibited Practices and the High-Risk Classification System (coming soon)*
