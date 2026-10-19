# Module 7 — ISO/IEC 42001:2023 Performance Evaluation Under Clause 9
## The check function: confirming the AIMS actually works, not just exists

> **Framework:** ISO/IEC 42001:2023 — AI Management System (AIMS)
> **Module:** 7 of 10
> **Status:** ✅ Complete

---

## Why Clause 9 matters

Clause 9, Performance Evaluation, is the standard's check function. Clauses
6 and 8, covered in Modules 5 and 6, are about deciding what to do about AI
risk and executing those decisions across the AI system lifecycle. Clause 9
is about confirming that any of it actually works — that the controls
implemented in Clause 8 are functioning as intended, that the risk
treatment decisions from Clause 6 remain appropriate, and that the AIMS as
a whole is operating rather than merely existing as a folder of policy
documents.

This is the clause that turns documentation into evidence. An organization
can have an excellent risk assessment methodology and a thorough Statement
of Applicability and still fail an audit if it cannot demonstrate it is
actually checking whether any of that is working in practice. Clause 9 is
where that demonstration happens, structured into three connected
sub-clauses operating at different cadences.

## 9.1 — Monitoring and measurement: continuous

The first sub-clause requires ongoing tracking of whether AI systems and
AIMS controls are performing as intended. This is broader than watching
model performance metrics. Clause 9.1 covers two distinct things:

**Monitoring AI systems themselves** — drift metrics, incident logs,
output anomaly indicators, and the kind of operational data introduced in
Module 6's discussion of the monitoring lifecycle stage.

**Monitoring the management system itself** — are policies actually being
followed, is the AI system inventory staying current as new systems enter
scope, are risk assessments getting refreshed when changes trigger a
re-assessment under Clause 8's change management requirement, are training
records for AI literacy (Clause 7) actually up to date.

The standard requires the organization to define, in writing, what gets
measured, how often, by what method, and who is responsible for reviewing
the results. A vague intention to "monitor AI systems" without this
specificity is a common documentation gap — auditors look for a defined
monitoring plan, not just evidence that monitoring happens informally.

## 9.2 — Internal audit: periodic and independent

At planned intervals, the organization audits its own AIMS against the
standard's clause requirements and the controls it has claimed to
implement in its Statement of Applicability. This is functionally a
rehearsal for the external certification or surveillance audit covered in
Module 4, conducted by the organization on itself.

The independence requirement here mirrors the independence requirement
that governs the certification decision externally: the person conducting
an internal audit of a given area cannot be the same person who manages
that area day to day. For a small organization, this often means
cross-training someone from a different department to conduct internal
audits, or engaging an external party for this specific function — but the
auditor must be structurally separate from what they're auditing.

Internal audit findings are classified using the same major and minor
framework introduced in Module 4 for external audits, and they are tracked
through to closure with the same rigor. An internal audit program that
produces findings nobody follows up on does not satisfy Clause 9.2, even
if the audits themselves are conducted on schedule.

## 9.3 — Management review: where findings become decisions

At defined intervals, top leadership formally reviews the AIMS. This is
not a status update meeting. The standard specifies mandatory inputs that
must be considered:

- The status of actions arising from previous management reviews
- Changes in external and internal context relevant to the AIMS
- Performance data from 9.1 monitoring and measurement
- Audit results from 9.2 internal audits (and any external audit findings)
- Feedback from interested parties, including customer complaints
- The status of nonconformities and corrective actions
- Opportunities for continual improvement

The output cannot be passive acknowledgment. Management review has to
produce actual decisions — resourcing changes, policy revisions, scope
adjustments to the AIMS — and those decisions become direct inputs to
Clause 10's continual improvement process. A management review meeting
that confirms "things look fine" without substantively engaging the data
fed in from 9.1 and 9.2 does not satisfy the clause's intent, even if it
happens on the scheduled cadence.

## The feed chain: why these three sub-clauses aren't independent

The most important structural point in Clause 9 is that monitoring,
internal audit, and management review are not three parallel activities —
they form a feed chain.

Monitoring data from 9.1 is the raw material that internal audit checks
against in 9.2: an auditor reviewing whether a control is "working"
ultimately has to look at the monitoring evidence to know. Internal audit
findings from 9.2 are a mandatory input to management review in 9.3 — they
cannot be quietly resolved without ever reaching leadership's attention.
And management review decisions from 9.3 flow into Clause 10's corrective
action process, which can in turn redefine what gets monitored under 9.1,
closing the loop.

This is the same closed-loop structure as the PDCA cycle introduced in
Module 1, operating specifically at the Check phase. An auditor examining
Clause 9 evidence across an organization is effectively asking one
question through all three sub-clauses: does this organization actually
use what it measures, or does it just measure?

## What a stage 2 auditor looks for in Clause 9 evidence

In practice, Clause 9 readiness comes down to a handful of artifacts an
auditor will ask to see:

- A documented monitoring plan specifying what is measured, how often,
  and by whom — not just raw monitoring data, but the plan that justifies it
- Evidence of internal audits actually being conducted on the defined
  schedule, with findings recorded and classified
- A closed-loop trail showing internal audit findings were tracked to
  resolution, not just logged and forgotten
- Management review meeting minutes that show the mandatory inputs were
  actually discussed, and that decisions resulted — not just attendance
- A visible connection between management review decisions and subsequent
  changes to the AIMS, demonstrating the loop is real and not theoretical

An organization that can produce all five of these has effectively
demonstrated Clause 9 conformance regardless of how the evidence happens
to be formatted or stored.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Monitoring and measurement (9.1) | Continuous tracking of AI system performance and AIMS control effectiveness |
| Internal audit (9.2) | Periodic, independent self-audit of the AIMS against standard requirements and the SoA |
| Management review (9.3) | A formal, defined-interval leadership review of AIMS performance with mandatory inputs and required outputs |
| Audit independence | The requirement that an internal auditor be structurally separate from the area they are auditing |
| Mandatory inputs | The specific categories of information management review must consider, defined by the standard |
| Feed chain | The dependency relationship where 9.1 data feeds 9.2 audits, which feed 9.3 review, which feeds Clause 10 |

## Practice questions

1. What is the difference between what 9.1 requires an organization to
   monitor regarding AI systems versus the management system itself?
2. Why must an internal auditor be independent from the area they audit,
   and how might a small organization satisfy this requirement?
3. Name three of the mandatory inputs management review must consider
   under Clause 9.3.
4. Why is a management review meeting that simply confirms "things look
   fine" insufficient, even if held on schedule?
5. Describe the feed chain connecting 9.1, 9.2, and 9.3, and explain how
   it connects to Clause 10.
6. What five artifacts would an auditor look for to confirm Clause 9
   conformance in practice?

## How to explain it in an interview

> "Clause 9 is the check function in the PDCA cycle — it's how an
> organization proves its AIMS actually works rather than just exists on
> paper. It's three connected pieces: continuous monitoring under 9.1,
> which covers both AI system performance and whether the management
> system itself is being followed; periodic, independent internal audits
> under 9.2 that mirror what an external certification audit will do;
> and management review under 9.3, where leadership has to engage with
> specific mandatory inputs — monitoring data, audit findings, prior
> action status — and produce real decisions, not just attendance. The
> key thing is that these three aren't parallel activities, they're a
> feed chain: monitoring data feeds the audit, audit findings feed
> management review, and management review decisions feed back into
> Clause 10's improvement process and back into what gets monitored
> next. An auditor looking at Clause 9 is really asking whether the
> organization uses what it measures."

---

*Previous: [Module 6 — Operational Controls and Clause 8](module-06-operational-controls-clause8.md)*
*Next: Module 8 — Continual Improvement Under Clause 10*
