# Module 3 — Annex A Controls Catalog
## The control set you actually select from

> **Framework:** ISO/IEC 42001:2023 — AI Management System (AIMS)
> **Module:** 3 of 10
> **Status:** ✅ Complete

---

## What Annex A actually is, structurally

Annex A is a **normative annex** — a required part of the standard, not
optional supplementary reading. It lists AI-related controls organized into
families, and an organization must consider every control and document,
for each one, either that it's implemented or a justified reason for
exclusion. This "consider everything, justify exclusions" structure is
identical to ISO 27001's Annex A for information security controls.

This produces a required document called the **Statement of Applicability
(SoA)** — a list of every Annex A control with columns showing whether it's
applicable, whether it's implemented, and justification either way. The SoA
is typically one of the first documents a certification auditor requests,
because it's the master index connecting risk assessment to control
implementation.

---

## The control families

### A.2 — Policies related to AI
Requires documented AI policies covering responsible AI development and
use, beyond the single top-level policy required under Clause 5.2 — more
granular coverage, such as specific policies addressing particular AI risk
categories identified in the Clause 6 risk assessment.

### A.3 — Internal organization
Requires defined roles and responsibilities specific to AI governance,
distinct from general organizational roles — clarity on who's accountable
for AI risk decisions, who can approve deployment, how responsibilities are
communicated and reviewed.

### A.4 — Resources for AI systems
Requires identifying and documenting computational, human, and financial
resources needed for responsible AI development and operation, and
ensuring they're actually available, not just planned. Connects to Clause
7.1's general resourcing requirement, applied specifically to AI needs.

### A.5 — Assessing impacts of AI systems
Operationalizes the AI system impact assessment concept from Clauses 6.1.4
and 8.2 — specifying what an impact assessment must examine (impacts on
individuals, groups, society) and requiring it at defined lifecycle points,
not just once at the beginning.

### A.6 — AI system life cycle
One of the largest, most operationally significant families. Covers
requirements and design, verification and validation before deployment,
deployment, operation and monitoring, and decommissioning. Structurally
similar to a secure software development lifecycle (SSDLC) framework, but
applied to AI-specific concerns like model drift, retraining triggers, and
performance degradation. Includes controls for what happens when an AI
system is retired — handling training data and model artifacts
appropriately, ensuring dependent systems aren't left broken.

### A.7 — Data for AI systems
Requires documented processes for data acquisition, quality assessment,
preparation and labeling, and ongoing data provenance tracking — tracing
exactly where training data came from and how it was transformed. Goes
considerably further than NIST AI RMF's general data governance language,
giving specific, auditable activities to point to.

### A.8 — Information for interested parties
Requires providing appropriate information to people affected by AI
systems — connecting to the transparency concept from NIST AI RMF, framed
as a management system requirement with documented processes for what
information is provided, to whom, and when.

### A.9 — Use of AI systems
Addresses how the organization itself uses AI systems — internally built or
vendor-sourced — including a documented process for evaluating whether a
system is fit for its intended use before relying on it operationally.

### A.10 — Third-party and customer relationships
Requires controls around supplier relationships specifically for AI —
assessing supplier AI governance maturity, contractual requirements, and
ongoing monitoring of third-party AI components. Maps closely to NIST AI
RMF Module 6's vendor risk controls (VR-001 through VR-003), with more
formal, audit-ready documentation expectations.

---

## Annex A controls vs. NIST AI RMF's control library

NIST AI RMF's twelve-domain control library (Module 6) is organized around
**risk types** — bias controls, privacy controls, security controls.
Annex A is organized around **management areas** — policy, resourcing,
lifecycle stage, third-party relationships. They cut across the same
underlying universe of AI safeguards from different angles, like organizing
a bookshelf by author versus by genre.

A single implemented control — say, a quarterly fairness audit — gets
documented once but referenced from two schemes: in the NIST AI RMF
library it sits under "Bias & Fairness" (BF-002); in ISO 42001 it would be
referenced under A.6 (AI system lifecycle, monitoring/operation stage) and
possibly A.5 (impact assessment, since fairness audits are a form of
ongoing impact monitoring). Same control, same evidence, two filing
systems — the practical mechanism behind the Module 9 control mapping
matrix's cross-framework efficiency argument.

---

## What a GRC engineer actually does with Annex A

After completing the Clause 6 risk assessment, go through every Annex A
control family and, for each control, determine applicability to the
identified risks. Where applicable, document implementation and supporting
evidence. Where not applicable, write a justification — for example, "A.10
third-party controls are not applicable; this organization develops all AI
systems internally with no third-party AI components" is legitimate,
provided it's actually true and stays true.

This produces the Statement of Applicability — the connective document
between the risk assessment (Clause 6), actual operational controls
(A.2 through A.10), and audit evidence (organized the way learned in NIST
AI RMF Module 7, relabeled to ISO terminology).

---

## Key terms

| Term | Plain meaning |
|---|---|
| Normative annex | A required part of the standard, not optional supplementary content |
| Statement of Applicability (SoA) | The master document listing every Annex A control, applicability, implementation status, and justification |
| Control family | A grouping of related Annex A controls addressing one management area |
| AI system lifecycle | The full span from requirements and design through decommissioning, covered by A.6 |
| Data provenance | The ability to trace where a piece of data came from and how it was transformed |
| Exclusion justification | The documented reason a particular Annex A control doesn't apply to an organization's scope |

---

## Practice questions

1. What's the difference between how NIST AI RMF organizes its control library and how ISO 42001's Annex A organizes its controls?
2. What is a Statement of Applicability, and why is it usually one of the first documents an auditor requests?
3. Can an organization simply skip a control family in Annex A without documentation? Why or why not?
4. Give an example of one control that could be filed under both a NIST AI RMF domain and an ISO 42001 Annex A family — what is it filed as in each?
5. Why does A.6 (AI system lifecycle) include decommissioning controls, and what specifically should those address?

---

## How to explain it in an interview

> "Annex A is ISO 42001's normative controls catalog, organized into
> families like organizational controls, AI system lifecycle, data for AI
> systems, and third-party relationships. Unlike a voluntary control
> library, every Annex A control must be addressed in a Statement of
> Applicability — you either implement it and show evidence, or formally
> justify why it doesn't apply. What's interesting from a GRC engineering
> perspective is that Annex A organizes the same underlying universe of AI
> safeguards differently than NIST AI RMF does — by management area rather
> than risk type — so a single control like a quarterly bias audit gets
> implemented once but can be referenced from both a NIST risk domain and
> an ISO Annex A family. That's the practical foundation for cross-framework
> efficiency when an organization needs to satisfy multiple standards at
> once."

---

*Previous: [Module 2 — The Seven Core Clauses in Depth](module-02-seven-clauses.md)*
*Next: Module 4 — Certification Process and Audit Cycle*
