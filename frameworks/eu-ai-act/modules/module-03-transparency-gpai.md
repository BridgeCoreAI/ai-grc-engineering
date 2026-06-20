# Module 3 — EU AI Act Limited-Risk Transparency Obligations and General-Purpose AI
## Two different governance logics that sit next to each other in the Act

> **Framework:** EU AI Act — Regulation (EU) 2024/1689
> **Module:** 3 of 10 (estimated)
> **Status:** ✅ Complete

---

## Why these two topics share a module

Limited-risk transparency obligations (Article 50) and General-Purpose AI
obligations operate on fundamentally different logic, even though they
often get studied together because neither fits the high-risk
conformity-assessment model covered in Module 2. Article 50 is about
disclosure to the people interacting with an AI system. GPAI obligations
are about the provider of a foundation model, independent of who ends up
using anything built on top of it downstream. Keeping the distinction
clear matters, because the two sets of obligations attach to different
parties and are triggered by different things.

## Article 50: transparency obligations are broad, and the disclosure requirement varies by context

The "limited risk" tier introduced in Module 1 is governed primarily by
Article 50, which requires informing people when they're interacting with
or being shown content from an AI system. The obligation sounds simple,
but its reach is broad across consumer-facing AI products.

**Chatbots and conversational AI.** People must be informed they are
interacting with an AI system — unless it is already obvious from the
context to a reasonably well-informed person. This built-in exception
means a chatbot explicitly branded and presented as an AI assistant may
not need an additional disclaimer, but a system designed to convincingly
mimic human conversation does need one.

**Synthetic content and deepfakes.** AI-generated or AI-manipulated
image, audio, or video content that resembles real people, objects,
places, or events must be labeled as artificially generated or
manipulated. Unlike the chatbot obligation, there is no "it's obvious"
exception built into this requirement — the labeling obligation applies
regardless of how apparent the synthetic nature might seem to a viewer.
This is a substantially broader requirement than it first appears,
because it covers the enormous and growing volume of ordinary generative
AI image, audio, and video content, not just clearly deceptive material
like fabricated political videos.

**Emotion recognition and biometric categorization systems.** When
deployed outside the prohibited contexts covered in Module 2 (workplaces
and educational institutions), people subject to these systems must be
informed that the system is operating on them.

**AI-generated text on matters of public interest.** Text published to
inform the public on matters of public interest must be disclosed as
AI-generated, unless the content underwent human review or editorial
control — a provision aimed at AI-generated news and informational
content specifically.

This is the obligation flagged in Module 1 as easy to underestimate. The
individual requirement — tell people, label the content — sounds minor.
But because it applies across nearly the entire landscape of
consumer-facing generative AI products, it has one of the broadest
practical footprints of any obligation in the Act, even though it carries
none of the heavy pre-market conformity assessment machinery that
high-risk systems require.

## Why General-Purpose AI doesn't fit the risk-tier system at all

The four-tier classification system from Module 1, and the prohibited
and high-risk categories detailed in Module 2, all classify AI systems
based on what they do — their function, their use case, their domain.
That classification logic breaks down for General-Purpose AI models,
because a foundation model has no fixed function. A large language model
can power a customer service chatbot (limited risk), a hiring screening
tool (high-risk), or a spam filter (minimal risk), depending entirely on
how a downstream developer chooses to deploy it.

Rather than force GPAI into the existing tier system, the Act creates a
separate, parallel track of obligations attached to the GPAI model
provider specifically — the organization that develops and releases the
foundation model — independent of the risk tier any particular downstream
application might eventually fall into.

## Baseline GPAI obligations: applicable to every provider

Every provider of a General-Purpose AI model, regardless of the model's
size or capability, carries baseline obligations:

- **Technical documentation** of the model's capabilities, limitations,
  and architecture
- **Information sufficient for downstream integration** — enough detail
  for developers building on top of the model to understand its behavior
  and limitations well enough to comply with their own obligations
- **A policy to comply with EU copyright law**, including respecting
  rights reservations on training data — a notably specific inclusion
  for what is otherwise an AI safety and risk regulation, reflecting how
  closely GPAI regulation intersects with ongoing copyright disputes
  around training data
- **A published summary of training content**, providing transparency
  into what data the model was trained on

## The systemic-risk threshold: one of the Act's few quantitative triggers

Nearly every other classification decision covered so far in this
curriculum — prohibited practices under Article 5, high-risk
classification under Annex III and the Article 6 carve-out — requires
interpreting what an AI system does. The systemic-risk threshold for
GPAI models is different: it is a quantitative, compute-based trigger.

A GPAI model trained using more than 10^25 floating-point operations
(FLOPs) of compute is presumed to carry systemic risk. This is a
deliberately legible, numerically defined line, in contrast to the
qualitative judgment calls that dominate the rest of the Act's
classification logic — even though precisely measuring training compute
in practice carries its own engineering and verification challenges.

Models that cross this threshold face additional obligations beyond the
baseline:

- **Model evaluation and adversarial testing**, including red-teaming to
  identify dangerous capabilities
- **Systemic risk assessment and mitigation**, requiring providers to
  identify and address risks the model could pose at scale
- **Incident tracking and reporting**, requiring providers to monitor and
  report serious incidents involving the model
- **Adequate cybersecurity protections**, given the elevated stakes of a
  highly capable model being compromised, leaked, or misused

## Who actually carries these obligations

A detail worth being precise about: GPAI obligations attach to the model
provider — the organization that trains and releases the foundation
model — not to every company that fine-tunes it, builds a product on top
of it, or deploys it in a downstream application. This is a narrower set
of actors than the broad provider/deployer distinction introduced in
Module 1 for the risk-tier system generally.

In practice, this means a startup building a chatbot on top of a major
foundation model operates under Article 50's transparency rules (because
it's building a conversational AI product) and whatever risk tier its
specific application falls under from Modules 1 and 2 — but it does not
carry the GPAI provider obligations itself. Those obligations sit with
the company that actually trained and released the underlying model.
Scoping any EU AI Act compliance engagement correctly requires being
clear about which role — provider of the foundation model, or downstream
deployer building on top of it — the client actually occupies.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Article 50 | The provision establishing transparency obligations for AI systems interacting with people or generating synthetic content |
| Synthetic content labeling | The requirement to mark AI-generated or manipulated media resembling real people, places, or events |
| General-Purpose AI (GPAI) | A foundation model with broad downstream applicability, governed by a separate set of provider obligations |
| Systemic risk | A GPAI risk classification triggered by a quantitative compute threshold (10^25 FLOPs), carrying additional obligations |
| GPAI provider | The organization that trains and releases a foundation model, distinct from downstream developers building on top of it |

## Practice questions

1. Why does the chatbot disclosure obligation include an "it's already
   obvious" exception, while the synthetic content labeling obligation
   does not?
2. Why can't General-Purpose AI models be classified using the same
   risk-tier logic applied to other AI systems?
3. What are the four baseline obligations that apply to every GPAI
   provider, regardless of model size?
4. What makes the systemic-risk threshold different from most other
   classification triggers in the Act?
5. If a startup fine-tunes a major foundation model to build a hiring
   tool, which obligations does it carry, and which does it not carry?
6. Why is a copyright compliance policy included among a GPAI provider's
   obligations under an AI safety regulation?

## How to explain it in an interview

> "Article 50 and the GPAI obligations are easy to study together but
> they're actually solving different problems. Article 50 is
> transparency — tell people when they're talking to AI, label
> AI-generated content, and it applies really broadly across consumer
> products, more broadly than people expect, because the synthetic
> content labeling requirement doesn't have an 'it's obvious' exception
> the way the chatbot disclosure does. GPAI obligations exist because a
> foundation model doesn't have one fixed function, so it can't be
> classified the way the rest of the Act classifies systems — instead,
> obligations attach to the model provider directly. Every GPAI provider
> has baseline obligations around documentation and copyright compliance,
> and then there's a systemic-risk tier triggered by a hard
> compute threshold, ten-to-the-twenty-fifth FLOPs, which is one of the
> only purely quantitative triggers in the whole Act. The thing worth
> getting right when scoping client work is that GPAI obligations sit
> with whoever actually trained the model, not with everyone building
> products on top of it."

---

*Previous: [Module 2 — Prohibited Practices and the High-Risk Classification System](module-02-prohibited-highrisk.md)*
*Next: Module 4 — Conformity Assessment for High-Risk AI Systems (coming soon)*
