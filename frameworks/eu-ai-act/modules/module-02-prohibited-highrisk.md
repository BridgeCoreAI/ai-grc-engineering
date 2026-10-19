# Module 2 — EU AI Act Prohibited Practices and the High-Risk Classification System
## Article 5's banned list and Annex III's high-risk categories, in depth

> **Framework:** EU AI Act — Regulation (EU) 2024/1689
> **Module:** 2 of 10 (estimated)
> **Status:** ✅ Complete

---

## Why this module matters

Module 1 introduced the four-tier risk structure. This module goes deep
on the two tiers that carry the most legal and practical weight:
unacceptable risk, governed by Article 5's prohibited practices list, and
high-risk, governed by Annex III's enumerated use case categories.
Together, these two articles determine whether an AI system can be built
at all, and if it can, whether it triggers the Act's most extensive
compliance obligations.

## Article 5: prohibited practices are a fixed, enumerated list

It's tempting to think of "unacceptable risk" as a flexible category
filled in case by case based on how harmful a system seems. It isn't.
Article 5 specifies a fixed list of prohibited practices, which makes
classification work here closer to legal interpretation of defined terms
than open-ended risk judgment — a genuinely different skill from the
qualitative risk scoring covered in ISO 42001's Clause 6 risk
assessment.

The prohibited practices include:

- **Subliminal or manipulative techniques** that materially distort a
  person's behavior in a way likely to cause significant harm, where the
  person cannot reasonably perceive the technique or its effect
- **Exploitation of vulnerabilities** tied to age, disability, or a
  specific social or economic situation, in a way that materially
  distorts behavior and causes harm
- **Social scoring** by public authorities — evaluating or classifying
  people based on their social behavior or predicted characteristics in
  ways that lead to detrimental or unfavorable treatment unrelated to the
  original context the data was generated in
- **Real-time remote biometric identification** in publicly accessible
  spaces for law enforcement purposes, with narrow, specifically defined
  exceptions — such as searching for a victim of a specific crime like
  abduction, or preventing a specific, substantial, and imminent threat
  to life
- **Emotion recognition** in workplaces and educational institutions,
  except for narrow medical or safety-related purposes
- **Untargeted scraping of facial images** from the internet or CCTV
  footage to build or expand facial recognition databases
- **Biometric categorization systems** that infer sensitive
  characteristics like race, political opinions, trade union membership,
  religious beliefs, or sexual orientation, with limited exceptions

Because this is an enumerated list rather than a general principle,
there is no risk treatment option available for a system that genuinely
matches one of these definitions. This is unlike the four treatment
choices — modify, avoid, share, retain — covered in Module 5 of the ISO
42001 curriculum. Here, "modify" and "share" don't exist as options. The
only available outcomes are: the system doesn't actually match the
prohibited definition (in which case proceed to high-risk classification),
or it does, in which case it cannot be built or deployed at all.

## Annex III: the high-risk category is a specific, living list

The high-risk tier is similarly defined by an enumerated list rather than
a general principle, found in Annex III of the Act. The categories
include:

- Biometric identification and categorization of natural persons
- Management and operation of critical infrastructure
- Education and vocational training (including access and assessment)
- Employment, worker management, and access to self-employment
  (including recruitment, decisions affecting promotion or termination)
- Access to essential private and public services, including credit
  scoring and insurance risk assessment
- Law enforcement (specific use cases, e.g., risk assessment tools)
- Migration, asylum, and border control management
- Administration of justice and democratic processes

A crucial detail: Annex III is not static. The European Commission has
the authority to update and expand this list over time as new AI use
cases and risks emerge. This means high-risk classification is not a
one-time determination an organization completes and then forgets — a
system that wasn't classified as high-risk when it was first assessed
could become high-risk later if Annex III is amended to include its use
case. Ongoing classification monitoring is itself a compliance
obligation, not just an initial step.

## The Article 6 carve-out: not everything in an Annex III category is automatically high-risk

A meaningful nuance sits inside Article 6. Even if an AI system touches
one of the domains listed in Annex III, it may not be classified as
high-risk if it performs one of a narrow set of limited functions:

- A narrow procedural task
- Improving the result of a previously completed human activity
- Detecting decision-making patterns or deviations from prior patterns,
  without replacing or influencing the human assessment already performed
- A preparatory task to an assessment relevant to one of the Annex III
  use cases

This carve-out means classification cannot stop at "does this system
operate in employment, yes or no." It requires assessing the system's
actual function within that domain. A tool that flags resumes for a
recruiter's review, where the recruiter retains full decision-making
authority, may fall under this carve-out. A tool that autonomously
screens out candidates without meaningful human review does not — it
performs the actual high-stakes function the carve-out is designed to
exclude. Getting this distinction right requires understanding not just
what domain a system touches, but exactly what decision-making role it
plays within that domain.

## The temporal structure of high-risk obligations: front-loaded, not continuous

One of the more important practical differences from ISO 42001's
operating model: high-risk AI systems must complete a conformity
assessment and be registered in an EU-wide database before they can be
placed on the market at all. This is closer in structure to a pre-market
regulatory approval process — similar in spirit to medical device
regulation — than to a continuously operating management system like
ISO 42001's AIMS, where evidence accumulates progressively across the
system's operational lifecycle.

This means a significant share of the heaviest compliance work for a
high-risk AI system has to be completed before launch, not built up
gradually afterward. A later module in this curriculum will cover
conformity assessment in detail, but the structural point is worth
establishing now: under the EU AI Act, "we'll build out our compliance
documentation as we go" is not a viable strategy for a high-risk system
the way ongoing monitoring and improvement is the expected pattern under
ISO 42001's Clause 8 and Clause 9.

## Why this distinction matters for classification work in practice

The combination of Article 5's fixed prohibited list, Annex III's
enumerated high-risk categories (with the Article 6 carve-out), and the
fact that Annex III itself can change over time means classification
work under the EU AI Act requires a different posture than risk
assessment under ISO 42001. It is less about scoring likelihood and
impact on a continuous scale, and more about correctly applying specific,
sometimes narrowly worded legal definitions to a given AI system's actual
function — then revisiting that classification periodically as both the
system and the regulation itself can change.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Article 5 | The section of the Act listing prohibited AI practices, with no available compliance pathway |
| Annex III | The list of high-risk AI use case categories, which the European Commission can amend over time |
| Article 6 | The provision allowing certain narrow-function AI systems to avoid high-risk classification even within an Annex III domain |
| Conformity assessment | The mandatory pre-market evaluation process required for high-risk systems |
| Social scoring | A prohibited practice involving public authorities evaluating people's trustworthiness based on behavior, leading to unjustified detrimental treatment |

## Practice questions

1. Why is Article 5's prohibited practices list described as fixed and
   enumerated rather than open-ended?
2. Name three practices banned outright under Article 5.
3. Why is Annex III described as a "living list," and what practical
   consequence does that have for ongoing compliance work?
4. Under what conditions might an AI system touching an Annex III domain
   still avoid high-risk classification?
5. How does the temporal structure of high-risk compliance obligations
   differ from the ongoing operating model of ISO 42001's AIMS?
6. Why does classification under the EU AI Act require more than just
   identifying which domain an AI system operates in?

## How to explain it in an interview

> "Article 5 and Annex III are the two provisions that do the heaviest
> lifting in the EU AI Act's classification system, and they work
> differently than people sometimes assume. Article 5's prohibited
> practices — things like social scoring, manipulative AI, and
> unrestricted real-time biometric surveillance — are a fixed,
> enumerated list, not a flexible harm judgment, so there's no compliance
> pathway if a system genuinely matches one of those definitions.
> Annex III's high-risk categories are also a specific list — employment,
> credit scoring, critical infrastructure, and so on — but it's a living
> list the European Commission can expand over time, which means
> classification isn't a one-time exercise. And there's a carve-out in
> Article 6: even inside an Annex III domain, a system performing a
> narrow procedural task or just flagging something for human review
> might not actually count as high-risk. So classification really comes
> down to understanding a system's specific function, not just which
> domain it touches. And once something is classified high-risk, most of
> the compliance work — conformity assessment, registration — has to
> happen before the system ever launches, which is a very different
> rhythm than ISO 42001's continuous improvement model."

---

*Previous: [Module 1 — Overview](module-01-overview.md)*
*Next: Module 3 — Limited-Risk Transparency Obligations and General-Purpose AI*
