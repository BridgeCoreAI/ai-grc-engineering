# Module 4 — EU AI Act Conformity Assessment for High-Risk AI Systems
## What the pre-market approval process actually requires

> **Framework:** EU AI Act — Regulation (EU) 2024/1689
> **Module:** 4 of 10 (estimated)
> **Status:** ✅ Complete

---

## Why this module matters

Module 2 established that high-risk classification under Annex III
triggers a mandatory pre-market process before a system can be placed on
the EU market. This module covers what that process actually requires:
technical documentation, the choice between internal control and external
assessment, formal declarations and marking, public registration, and
ongoing post-market monitoring. This is the practical core of high-risk
compliance work — the sequence a GRC engineer will actually walk a client
through.

## Step 1: Technical documentation under Annex IV

Before any conformity assessment can begin, the provider has to compile
detailed technical documentation. This is the foundational artifact
everything downstream in the process references and verifies against.
Annex IV's required content includes:

- A general description of the system and its intended purpose
- Design specifications, including the system's architecture
- The development methodology used
- Characteristics of the training, validation, and testing data
- The risk management measures applied to the system
- Testing results demonstrating the system meets the Act's accuracy,
  robustness, and cybersecurity requirements

A useful but imperfect comparison: this documentation plays a role
similar to the Statement of Applicability in ISO 42001, in that both are
the artifact an external party checks claims against. The difference is
in how each document comes to exist. The SoA, as covered in earlier ISO
42001 modules, is built iteratively across an ongoing AIMS lifecycle and
gets revised as Clause 10's corrective actions feed back into it. Annex
IV's technical documentation has to exist in essentially complete form
before assessment can even start — it is a pre-market gate, not a living
document that matures gradually over years of operation.

This documentation also doesn't get filed away once conformity is
confirmed. It has to be kept current and made available to relevant
authorities for the system's entire operational lifetime, which means a
provider needs an actual ongoing process for maintaining it accurately,
not a one-time compilation exercise completed before launch and then
forgotten.

## Step 2: The assessment pathway is determined by system type, not provider preference

High-risk systems follow one of two assessment pathways, and which
pathway applies is specified by the Act based on the system's
classification — it is not a choice the provider gets to make based on
preference or cost.

**Internal control** is the pathway for most high-risk systems. The
provider self-assesses conformity against the Act's requirements and
takes on legal responsibility for the accuracy of that assessment.
"Self-assessment" can sound like the lighter compliance option, and in
terms of process it is less procedurally burdensome than external review
— but it raises the stakes of getting the underlying technical
documentation genuinely right, because there is no independent third
party catching errors before the system reaches the market. The legal
exposure for an inaccurate self-assessment sits entirely with the
provider.

**Notified body assessment** is required for a narrower set of
particularly high-stakes system types, including certain biometric
identification systems. Here, an independent, externally accredited
organization — a notified body — conducts the conformity assessment
rather than the provider doing it internally. This is conceptually
closer to the external certification body role in ISO 42001's audit
process, though the legal context and stakes are different: ISO 42001
certification is voluntary; notified body assessment for these specific
high-risk categories is a mandatory legal requirement with no internal
control alternative available.

## Step 3: The substantive requirements being assessed

Regardless of which pathway applies, the assessment verifies the system
against the Act's substantive requirements:

- A documented risk management system specific to the AI system
- Data governance covering training, validation, and testing datasets
- The technical documentation from Step 1
- Record-keeping and logging capabilities
- Transparency provisions enabling deployers and users to understand the
  system's operation
- Human oversight mechanisms appropriate to the system's risk level
- Accuracy, robustness, and cybersecurity standards appropriate to the
  system's intended purpose

This is the substantive checklist the technical file from Step 1 has to
actually demonstrate, with evidence, rather than merely describe in
narrative form.

## Step 4: Declaration of conformity and CE marking

Once conformity is confirmed, the provider issues a formal EU declaration
of conformity and affixes CE marking to the system. This extends a
decades-old EU product compliance mechanism — used across machinery,
medical devices, and electronics — to AI systems for the first time.

This is worth being precise about for anyone coming to AI governance from
a software or AI background rather than a product compliance background.
CE marking is not a badge or a marketing claim; it is a formal, legally
binding declaration that the product meets EU regulatory requirements.
Affixing CE marking to a high-risk AI system without genuine underlying
conformity is not treated as a paperwork error — it carries the same
legal seriousness as any other false CE marking claim under existing EU
product law, which represents a different category of legal exposure
than most AI teams are accustomed to considering.

## Step 5: Registration in the EU database (Article 71)

Before a high-risk system can be placed on the market, the provider must
register it in a centralized, publicly accessible EU database, recording
the system's stated purpose, the provider's identifying details, and the
outcome of the conformity assessment.

This creates a transparency mechanism with no real equivalent in either
of the two frameworks covered earlier in this curriculum. ISO 42001's
audit evidence and NIST AI RMF's documentation are both internal to the
organization, or visible only to its certification body. The EU database
is public — anyone can look up which high-risk AI systems are registered,
who provides them, and what they are stated to do. A high-risk AI
system's basic existence and characteristics become a matter of public
record before it is even deployed, which is a genuinely different
governance posture than the internal-evidence model both prior frameworks
operate under.

## Step 6: Post-market monitoring — where the model finally resembles ISO 42001

Conformity assessment is not a one-time event that concludes once the
system launches. Providers must continuously monitor the system's
real-world performance after deployment and report serious incidents to
relevant authorities.

This is the part of the process that most closely parallels ISO 42001's
continuous operating model — specifically Clause 8's operational
monitoring and Clause 9's performance evaluation, covered in earlier
modules of that framework's curriculum. The structural difference is
sequencing, not substance: ISO 42001 treats monitoring as part of one
continuous loop running from the start of a system's operational life.
The EU AI Act treats post-market monitoring as a distinct phase that
begins only after a much heavier, front-loaded approval process — Steps
1 through 5 above — has already concluded.

## What this means for scoping GRC engineering work

The conformity assessment process described in this module is where most
of the substantive, billable work in EU AI Act compliance for high-risk
systems actually concentrates. Unlike ISO 42001 engagements, where work
is spread relatively evenly across a continuous improvement cycle, EU AI
Act high-risk compliance work is heavily front-loaded: building Annex IV
technical documentation, determining the correct assessment pathway,
preparing for whichever assessment applies, and managing EU database
registration are all concentrated before a system can launch at all. Post-
market monitoring work continues afterward, but it is a smaller, ongoing
slice relative to the pre-market effort — the inverse of how effort
distributes across an ISO 42001 implementation.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Annex IV | The Act's required content list for a high-risk system's technical documentation |
| Internal control | The self-assessment conformity pathway available to most high-risk system types |
| Notified body | An independent, accredited third party required to conduct conformity assessment for a narrower set of higher-stakes system types |
| EU declaration of conformity | The formal statement issued by a provider confirming a system meets the Act's requirements |
| CE marking | The legally binding mark affixed to a conforming system, extending existing EU product compliance practice to AI |
| Article 71 database | The EU's centralized, publicly accessible registry of high-risk AI systems |
| Post-market monitoring | The ongoing obligation to track a deployed system's performance and report serious incidents |

## Practice questions

1. Why is Annex IV's technical documentation described as a pre-market
   gate rather than a living document, in contrast to ISO 42001's
   Statement of Applicability?
2. Who decides whether a high-risk system uses internal control or
   notified body assessment — the provider, or the Act itself?
3. Why does internal control raise the stakes of getting technical
   documentation right, even though it's procedurally less burdensome
   than notified body assessment?
4. What makes CE marking a meaningfully different kind of legal
   declaration than a typical compliance checklist sign-off?
5. How does the EU database's public accessibility differ from the
   evidence model used in ISO 42001 and NIST AI RMF?
6. Why is EU AI Act compliance effort for high-risk systems described as
   front-loaded, compared to the more evenly distributed effort in an
   ISO 42001 implementation?

## How to explain it in an interview

> "Conformity assessment for high-risk systems is a six-step, mostly
> pre-market process. It starts with building Annex IV technical
> documentation — which has to exist in complete form before assessment
> even begins, unlike an SoA that matures over time. Then the system's
> classification determines whether it goes through internal
> self-assessment or requires an independent notified body — the
> provider doesn't get to choose. Once conformity is confirmed, the
> provider issues a formal declaration and applies CE marking, which is
> a legally binding claim, not a badge. Then it has to be registered in
> a public EU database before it can launch — which is a real difference
> from ISO 42001 and NIST AI RMF, where the evidence stays internal or
> goes only to a certification body. Only after all of that does
> post-market monitoring kick in, which is the one piece that actually
> resembles ISO 42001's continuous operating model. The practical
> takeaway for scoping client work: almost all the heavy lifting happens
> before launch, which is the opposite of how effort distributes across
> an ISO 42001 engagement."

---

*Previous: [Module 3 — Limited-Risk Transparency Obligations and General-Purpose AI](module-03-transparency-gpai.md)*
*Next: Module 5 — Governance Bodies, Enforcement, and Penalties*
