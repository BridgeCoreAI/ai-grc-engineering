# Module 7 — EU AI Act Data Governance and Human Oversight Requirements
## Article 10 and Article 14, unpacked from Module 4's checklist

> **Framework:** EU AI Act — Regulation (EU) 2024/1689
> **Module:** 7 of 10 (estimated)
> **Status:** ✅ Complete

---

## Why these two articles share a module

Module 4's substantive requirements checklist for conformity assessment
listed data governance and human oversight as line items among several
others. Module 6 went deep on Article 9's risk management requirement.
This module unpacks the other two substantive requirements that Article
9's risk thinking actually has to produce concretely: Article 10's data
governance standards, and Article 14's human oversight requirements.

## Article 10: data governance for training, validation, and testing data

High-risk AI systems are only as defensible as the data they're built
and tested on, and Article 10 sets specific standards for that data.

**Relevance, representativeness, and freedom from error.** Training,
validation, and testing data must be relevant to the system's intended
purpose, sufficiently representative of the population and context the
system will actually be deployed in, and as free of errors as reasonably
possible given that purpose. Notably, this standard does not come with a
fixed numerical bar. Unlike the systemic-risk compute threshold covered
in Module 3, which the Act defines as a hard number, "sufficiently
representative" is judged relative to a system's specific intended
purpose and deployment context — a deliberate design choice, not an
oversight. A facial recognition system intended for nationwide deployment
needs a different standard of demographic representativeness than a
narrow internal tool used by a single employer for a single function.
This means data governance compliance work is inherently context-specific:
there is no universal checklist item specifying a fixed representation
threshold. The actual legal standard requires a justified, documented
argument that the dataset is adequate for this system's specific purpose.

**Examination for bias.** Datasets must be examined for possible biases
likely to affect people's health, safety, or lead to discrimination, with
appropriate mitigation measures applied where bias is identified. This
connects directly to Article 9's mitigation requirement covered in
Module 6 — identifying bias in a dataset isn't sufficient on its own; the
provider has to actually address it.

**Accounting for the deployment context.** Datasets must account for the
specific geographical, contextual, behavioral, or functional setting the
system is intended to operate within, rather than relying on data that
happens to be available without examining whether it actually reflects
the real conditions the system will face.

**The special category data exception.** This is one of the more
distinctive provisions in Article 10, and it creates a genuinely unusual
legal carve-out worth understanding precisely. Under GDPR, processing
special category personal data — race, ethnicity, health status, and
similar sensitive categories — is heavily restricted by default. Article
10 of the EU AI Act creates a narrow, safeguarded exception specifically
permitting high-risk system providers to process this kind of data for
the limited purpose of detecting and correcting bias in their training,
validation, and testing datasets. This is a meaningful intersection
between two pieces of EU law that initially appear to pull in opposite
directions: GDPR generally restricts processing this sensitive data, and
the EU AI Act permits it in this narrow circumstance, precisely because
failing to check for bias creates its own distinct harm. The exception is
narrow and safeguarded, not a blanket permission to process sensitive
data freely — it applies specifically to bias detection and correction
purposes, under appropriate technical and organizational safeguards.

## Article 14: human oversight requires genuine capability, not symbolic presence

A common and understandable assumption is that "human oversight" means
having a person somewhere in the process — a human technically present
when the AI system operates. Article 14 sets a substantially higher bar
than mere presence.

**Understanding and monitoring.** Overseers must be able to properly
understand the system's capabilities and limitations, and to monitor its
operation for signs of anomalies, dysfunction, or unexpected performance.
A person who doesn't understand what the system is actually doing or
capable of cannot meaningfully oversee it, regardless of their formal
role.

**Resisting automation bias.** Overseers must be able to correctly
interpret the system's output and remain aware of the well-documented
human tendency to automatically over-rely on a system's output simply
because the system produced it — known as automation bias. This is
explicitly named in Article 14 because it's a recognized human factors
problem, not a hypothetical one: a person nominally "overseeing" a system
who reflexively defers to its output without genuinely engaging with
whether it makes sense has not exercised meaningful oversight, even
though a human was technically present and clicked approve.

**Deciding not to use, or overriding the system.** Overseers must be
able to decide, in a given situation, not to use the system at all, or to
disregard, override, or reverse its output. This requires both the
practical capability and the organizational authority to actually make
that call — an overseer technically permitted to override a system but
practically discouraged or unable to do so within the organization's
actual workflow does not satisfy this requirement.

**A genuine stop capability.** Overseers must be able to intervene in the
system's operation or stop it entirely through a clearly identifiable
mechanism. This has to be a real, accessible function available to the
person in the actual moment they might need it — not a stop capability
that exists in the system's design documentation but is impractical or
inaccessible to use in a live operational situation.

**The competence requirement.** Oversight responsibility has to be
assigned to people with the necessary competence, training, and
authority to exercise it meaningfully — not simply whoever happens to
have system access or sits nearest the relevant dashboard. Assigning
oversight without genuinely training the person on what they're looking
for, or without empowering them to act on what they find, doesn't satisfy
Article 14 even if an organizational chart formally names a human
overseer for the system.

## How these two articles connect back to the risk management cycle

Both Article 10 and Article 14 are concrete instantiations of what
Article 9's risk management system, covered in Module 6, has to actually
produce. A bias risk identified during Article 9's risk identification
stage gets addressed through Article 10's data governance examination and
mitigation requirements. A risk that some harm could go undetected once
the system is deployed gets addressed through Article 14's human
oversight mechanisms — the people positioned to catch what automated
monitoring alone might miss. Neither article exists in isolation; both
are the practical, substantive expression of the risk thinking Article 9
requires.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Article 10 | The provision setting data governance standards for training, validation, and testing data |
| Sufficiently representative | A context-dependent standard for whether training data adequately reflects a system's intended deployment, with no fixed numerical bar |
| Special category data exception | The narrow Article 10 carve-out permitting processing of sensitive personal data specifically to detect and correct bias |
| Article 14 | The provision establishing human oversight requirements for high-risk AI systems |
| Automation bias | The human tendency to over-rely on a system's output simply because the system produced it |
| Stop capability | A genuine, accessible mechanism allowing a human overseer to intervene in or halt a system's operation |

## Practice questions

1. Why is "sufficiently representative" under Article 10 not defined
   with a fixed numerical threshold?
2. What is the special category data exception under Article 10, and why
   does it represent a notable intersection with GDPR?
3. Why does having a human technically present during a system's
   operation not, by itself, satisfy Article 14?
4. What is automation bias, and why does Article 14 specifically name it
   as something overseers must resist?
5. What two things does an overseer need, beyond technical capability,
   to genuinely be able to override a system's output?
6. How do Article 10 and Article 14 connect back to Article 9's risk
   management cycle from Module 6?

## How to explain it in an interview

> "Article 10 and Article 14 are where Article 9's risk management
> requirement actually gets made concrete. Article 10 sets data
> governance standards — relevance, representativeness, bias
> examination — and the representativeness standard is deliberately
> context-dependent rather than a fixed number, because what counts as
> adequate depends entirely on the system's actual intended purpose.
> There's also a genuinely interesting carve-out where the Act actually
> permits processing sensitive personal data, which GDPR otherwise
> restricts, specifically to detect and correct bias — a narrow exception
> recognizing that not checking for bias creates its own harm. Article
> 14 is human oversight, and the bar there is much higher than just
> having a person in the loop. Overseers have to genuinely understand the
> system, resist automation bias — the tendency to just trust the
> output because the system produced it — and have a real, accessible
> way to override or stop the system, not a theoretical one. And the
> people doing that oversight actually need the training and authority
> to act, not just system access."

---

*Previous: [Module 6 — Risk Management Systems Under Article 9](module-06-risk-management-article9.md)*
*Next: Module 8 — National Implementation and the AI Pact*
