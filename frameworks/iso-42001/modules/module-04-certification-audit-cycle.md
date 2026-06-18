# Module 4 — ISO/IEC 42001:2023 Certification Process and Audit Cycle
## How an organization actually earns — and keeps — a certificate

> **Framework:** ISO/IEC 42001:2023 — AI Management System (AIMS)
> **Module:** 4 of 10
> **Status:** ✅ Complete

---

## Why certification is a process, not a single event

Module 1 introduced the distinction between being conformant with ISO 42001
and being certified against it. This module is about the second half of
that distinction: the actual mechanics of how a certificate gets issued,
what keeps it valid, and what eventually causes it to expire if nobody
renews it. None of this is a single audit. It is a recurring cycle that
runs for as long as an organization wants to keep the certificate,
structured so a certification body never has to take an organization's
word for it twice in a row without checking.

This matters for anyone doing GRC engineering work, because clients rarely
ask "can you help us get ISO 42001 certified" as a one-time question. They
are really asking for help building and operating a system that can survive
an audit cycle that repeats indefinitely, on a clock that does not pause
for product launches, layoffs, or a busy quarter.

## Accreditation: who is actually allowed to certify you

Not just anyone can issue a valid ISO 42001 certificate. A certification
body has to be accredited — formally authorized — by a national
accreditation body before its certificates carry real weight. In the
United States that is typically ANAB (the ANSI National Accreditation
Board); in the United Kingdom, UKAS; most countries have an equivalent.
These national accreditation bodies are themselves coordinated
internationally through the IAF, the International Accreditation Forum,
which is what allows an ISO 42001 certificate issued in one country to be
recognized by a buyer or regulator in another.

This layered structure exists because the entire value of certification
rests on independence. If certification bodies could self-declare their own
legitimacy, "certified" would mean nothing more than "we paid someone to
say so." Accreditation is the check that keeps the credential meaningful —
and it is also the first thing a GRC engineer should verify when a client
says they are working with a certification body: is this organization
actually accredited for ISO 42001 specifically, not just for ISO 27001 or
some adjacent standard with a similar-sounding name.

Because ISO 42001 is so new, accredited certification bodies with genuine
AI-specific audit experience are still a smaller pool than the
well-established ISO 27001 ecosystem. Part of selecting a certification
body well is asking how many ISO 42001 audits a given body has actually
completed, not just whether it is accredited in principle.

## The audit cycle, stage by stage

The certification lifecycle runs across six stages, and the first three
happen once, while the last three repeat on a three-year clock.

**Stage 1 audit — documentation review.** The certification body reviews
the organization's core AIMS documentation: the AI policy, scope statement,
risk assessment methodology, and Statement of Applicability. The question
being answered is whether the management system has been designed on
paper, not yet whether it operates day to day. The outcome is a stage 1
report listing any major documentation gaps; if readiness looks solid,
stage 2 gets scheduled, usually a few weeks out.

**Stage 2 audit — implementation review.** Auditors test whether the AIMS
documented in stage 1 is actually operating: interviewing staff, sampling
evidence like risk assessments and training records, and walking through
clauses 4 through 10 plus the specific Annex A controls listed in the
Statement of Applicability. The outcome is a certification recommendation,
with any nonconformities logged as major or minor.

**Certification decision.** An independent technical reviewer inside the
certification body — someone other than the auditor who conducted stage
2 — reviews the stage 2 findings. Minor nonconformities need a corrective
action plan but do not block certification. Major nonconformities must be
resolved and verified, sometimes through a dedicated follow-up visit,
before a certificate is issued. The outcome is a certificate valid for
three years, subject to ongoing surveillance.

**Surveillance audit, year 1 and year 2.** A lighter-touch audit sampling
part of the AIMS rather than re-auditing everything. Common focus areas
include any prior nonconformities, changes to scope or AI systems, and a
rotating subset of Annex A controls — usually a different subset in year 2
than year 1, so that between both visits most of the system has been
touched before recertification. The outcome each year is confirmation that
the certificate remains valid, or new nonconformities to fix.

**Recertification audit, year 3.** Effectively a full stage 2-level audit
again, covering the entire AIMS rather than a sample, to confirm the system
has operated effectively across the whole three-year cycle. The outcome is
a fresh three-year certificate, and the cycle restarts at year 1
surveillance.

The one structural detail worth calling out explicitly: the reviewer who
decides whether to issue the certificate is required to be someone other
than the auditor who did the stage 2 fieldwork. That separation of duties
exists for the same reason it matters in financial controls — the person
who gathered the evidence should not also be the person who grades it.

## Nonconformities: the vocabulary that actually decides outcomes

Every audit produces findings, and findings get classified as either major
or minor, because that classification is what determines whether
certification gets blocked.

A **major nonconformity** means something is either missing entirely or so
broken that it calls the whole management system's effectiveness into
question — for example, no risk assessment was ever performed for a
deployed AI system, or the Statement of Applicability claims a control is
implemented but no evidence of it exists anywhere. A major nonconformity
has to be corrected and the correction verified before a certificate can be
issued.

A **minor nonconformity** is an isolated lapse that does not undermine the
system as a whole — a training record missing for one employee, a policy
document that has not been reviewed on the schedule it specifies. Minor
nonconformities require a corrective action plan with a deadline, but they
do not block certification outright; the certification body simply checks
that the plan was carried out at the next opportunity, usually the
following surveillance audit.

The practical implication for a GRC engineer: readiness work ahead of an
actual audit is essentially trying to predict which gaps an auditor would
call major versus minor, and prioritizing the major-shaped ones first.

## Selecting a certification body, and the line a consultancy should not cross

When BridgeCore — or any GRC consultancy — helps a client get audit-ready,
there is a hard boundary worth understanding early: the consultancy that
helps build and prepare the management system generally should not also be
the certification body that audits it. That is the same independence
requirement that keeps an external financial auditor from also doing a
company's bookkeeping. A consultancy can run a pre-audit gap assessment,
help draft the Statement of Applicability, and coach the team through mock
interviews — but the actual certification decision has to come from an
accredited, independent third party with no stake in the outcome.

This is a useful distinction to keep ready in client conversations: the
service a consultancy sells is readiness, not the certificate itself. Being
explicit about that boundary builds trust rather than undermining it,
because clients who understand the independence requirement will trust a
consultancy that respects it more than one that quietly implies it can
shortcut the process.

## How this compares to NIST AI RMF

NIST AI RMF has no equivalent to any of this. There is no accreditation
body, no stage 1 or stage 2, no nonconformity classification, no
surveillance cycle, because NIST AI RMF was never designed to be audited by
a third party in the first place — it is voluntary guidance, not a
certifiable management system standard. An organization can be deeply,
rigorously aligned with NIST AI RMF and there is still no certificate
anyone can issue for it. That is the practical heart of the distinction
Module 1 introduced, and the audit cycle in this module is what that
distinction actually looks like in operation.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Accreditation body | A national authority (like ANAB or UKAS) that authorizes certification bodies to issue valid ISO certificates |
| IAF | International Accreditation Forum — coordinates accreditation bodies globally so certificates are recognized across borders |
| Stage 1 audit | A documentation review confirming the AIMS has been designed before checking whether it operates |
| Stage 2 audit | An implementation audit testing whether the documented AIMS is actually being followed |
| Major nonconformity | A finding serious enough to block certification until it is corrected and the correction verified |
| Minor nonconformity | An isolated finding that requires a corrective action plan but does not block certification |
| Surveillance audit | A lighter-touch annual audit during the three-year certification cycle, sampling part of the system rather than re-auditing all of it |
| Recertification audit | A full audit at the end of the three-year cycle that issues a fresh certificate and restarts the cycle |

## Practice questions

1. Why does a certification body need to be accredited, and who accredits the accreditation bodies?
2. What is the difference in purpose between a stage 1 audit and a stage 2 audit?
3. Why does the certification decision have to be made by someone other than the stage 2 auditor?
4. Give an example of a finding that would likely be classified as major versus one that would likely be classified as minor.
5. Why shouldn't the same consultancy that helped build a client's AIMS also serve as their certification body?
6. What happens at the end of the three-year certification cycle?

## How to explain it in an interview

> "ISO 42001 certification isn't a one-time event, it's a recurring cycle.
> You go through a stage 1 documentation review and a stage 2
> implementation audit to get certified initially, an independent reviewer
> inside the certification body — not the field auditor — makes the actual
> certification decision, and once you're certified you're on a three-year
> clock with lighter surveillance audits in years one and two and a full
> recertification audit in year three that starts the cycle over. Findings
> get classified as major or minor, and that classification is what
> determines whether they block certification outright or just need a
> corrective action plan. It's a genuinely different muscle than NIST AI
> RMF, which has no certification mechanism at all — there's no
> accreditation body, no stage 1 or 2, because it was built as voluntary
> guidance, not an auditable management system standard."

---

*Previous: [Module 3 — Annex A Controls Catalog](module-03-annex-a-controls.md)*
*Next: Module 5 — AI Risk Assessment and Treatment Under Clause 6 (coming soon)*
