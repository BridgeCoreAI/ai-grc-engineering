# Module 6 — ISO/IEC 42001:2023 Operational Controls and Clause 8
## Where risk decisions become day-to-day practice across the AI system lifecycle

> **Framework:** ISO/IEC 42001:2023 — AI Management System (AIMS)
> **Module:** 6 of 10
> **Status:** ✅ Complete

---

## Why Clause 8 is where most GRC engineering time is spent

If Clause 6 is where an organization decides what to do about AI risk,
Clause 8 — Operation — is where that decision actually gets executed across
the lifetime of every AI system in scope. It is the longest and most
operationally dense clause in the standard. Where Clauses 4 through 6 are
largely about planning and documentation, Clause 8 is about what actually
happens day to day: systems being designed, deployed, monitored, changed,
and eventually retired, with controls checked at each step rather than
audited once at the end.

For a GRC engineer, Clause 8 is where the bulk of ongoing work lives. Once
the initial certification is achieved, Clauses 4 through 7 mostly stay
static between major changes. Clause 8 activity never stops, because new
AI systems keep entering the pipeline and existing ones keep changing.

## The AI system inventory: the load-bearing artifact

Before any of the individual lifecycle controls make sense, the
organization needs a single source of truth: an inventory of every AI
system in scope. For each system, the inventory records what the system
does, what data it uses, who owns it, what risk tier it carries from the
Clause 6 risk assessment, and which Annex A controls apply to it.

This inventory is what every other part of Clause 8 hangs off of. A
deployment gate, a monitoring requirement, a change management trigger —
all of these only function if the system in question is actually in the
inventory to begin with. The most basic question a Clause 8 audit opens
with is: how many AI systems does this organization actually have, and how
confident are you that this list is complete?

A common gap auditors specifically probe for is shadow AI — tools adopted
by individual teams or business units without going through the formal
AIMS process. A marketing team quietly using a generative AI tool for
customer-facing copy, or an engineering team fine-tuning an open-source
model for internal use, can both exist entirely outside the inventory if
the organization has no mechanism for surfacing new AI adoption. The
inventory is only as good as the discovery process that feeds it, and a
mature AIMS includes a defined way for new AI systems to be identified and
registered, not just a static spreadsheet that gets updated when someone
remembers to.

## The lifecycle stages and their gates

Clause 8 structures operational control around the AI system lifecycle,
and each stage has a gate — a requirement that must be satisfied before
the system can move to the next stage.

**Design and development.** Before building or acquiring an AI system, the
organization documents its intended purpose, the AI objectives it serves,
and a preliminary risk assessment. This is also where the build-versus-buy
decision gets made and recorded: develop in-house, procure from a vendor,
or fine-tune an existing foundation model. The gate: no system enters
development without a documented intended-use statement and a preliminary
risk screen.

**Data management.** Controls covering data quality, provenance, and
suitability for the system's intended purpose, including verifying
training data lineage, checking for known bias sources, and confirming a
lawful basis where personal data is involved. The gate: data quality and
provenance documentation must exist before a system trained on that data
can proceed to deployment.

**Deployment.** Before an AI system goes live, the organization verifies
the Clause 6 risk assessment is current (not stale from an earlier design
phase), that required Annex A controls are actually implemented — not
merely planned — and that a rollback or human-override mechanism exists
for higher-risk systems. The gate: deployment is blocked until risk
sign-off is current and controls are verified as operating, not just
scheduled for implementation.

**Monitoring and incident response.** Once live, systems are monitored for
performance drift, unexpected outputs, and incidents, with a defined
incident response process specific to AI failure modes. The gate: an
AI-specific incident response procedure must exist before a deployed
system is considered operationally controlled, regardless of whether it
is technically functioning in production.

**Change management and retirement.** Any material change to a deployed
system — retraining, a new data source, an expanded use case, a swapped
base model — triggers a re-assessment rather than just a changelog entry.
Retirement requires documented decommissioning, data handling, and
inventory removal, with the same formality as the original deployment.
The gate: a changed system reverts to needing fresh risk sign-off; a
retired system needs documented decommissioning, not just deletion from
production.

## Why AI incident response can't borrow from IT incident response

A common and understandable instinct is to fold AI incident handling into
an organization's existing IT incident response playbook. This is usually
a mistake worth flagging explicitly to clients, because the failure modes
are structurally different.

A server outage has an obvious trigger and a clear resolution state:
something broke, an alert fired, the team responds, the system comes back
up. An AI system that has been gradually drifting toward biased or
degraded outputs over several weeks has no equivalent alarm. There is no
single trigger event — the "incident" is a slow accumulation that someone
eventually notices, often well after the harm has already occurred and
diffused across many decisions.

Clause 8 requires monitoring and incident response calibrated to these
AI-specific failure modes: drift detection over time rather than
point-in-time alerting, output anomaly monitoring that can catch
qualitative degradation rather than just downtime, and escalation paths
designed for harms that don't present as a conventional security incident.
An organization that simply routes "AI issues" into its existing ticketing
system with no AI-specific triage process has not actually satisfied this
part of Clause 8, even if the tickets technically get resolved eventually.

## Change management resets the risk clock — deliberately

One of the more common compliance gaps in practice is treating a model
update as a routine deployment event rather than recognizing that it
reopens the Clause 6 risk assessment obligation. The risk profile of
"model X used for purpose A" does not automatically transfer to "model X,
retrained on new data, now also used for purpose B." A change that looks
incremental from an engineering perspective — a routine retrain, a minor
fine-tune — can materially shift the risk profile from a governance
perspective, particularly around bias, data provenance, or scope creep
into higher-stakes use cases than the system was originally assessed for.

This is why Clause 8's change management requirement is structured as a
trigger back into Clause 6, not a standalone change log. Documenting that
a change happened is necessary but not sufficient; the organization also
has to re-run the risk thinking that produced the original treatment
decision, because the original decision may no longer hold.

## Retirement is not just turning a system off

Decommissioning an AI system carries its own documentation burden, often
overlooked because it feels like the end of the process rather than a
governed step in its own right. Retirement requires removing the system
from the active inventory (with a record of why and when), addressing what
happens to any data the system processed or was trained on, and confirming
that dependent systems or workflows that relied on the retired system have
been accounted for. A retired system that simply disappears from
production without this trail leaves a gap an auditor can find — either in
the inventory (a system that should have an exit record but doesn't) or in
data handling (training or inference data with no documented disposition).

## How this connects to the rest of the standard

Clause 8 is where Clauses 6 and 7 actually get tested. The risk
methodology and treatment decisions from Clause 6 only matter if Clause 8's
gates enforce them at design, deployment, and change points. The
competence and awareness requirements from Clause 7 (covered in Module 2)
show up here as the people actually running monitoring, triaging
incidents, and reviewing changes. And the outputs of Clause 8 — inventory
records, deployment sign-offs, incident logs, change re-assessments — are
the evidence base that Clause 9's internal audits and management reviews
draw on, and that an external stage 2 auditor samples directly.

---

## Key terms

| Term | Plain meaning |
|---|---|
| AI system inventory | The central register of every AI system in scope, including risk tier, owner, and applicable controls |
| Shadow AI | AI tools adopted outside the formal AIMS process, missing from the inventory |
| Lifecycle gate | A checkpoint that blocks an AI system from progressing to the next stage until a requirement is satisfied |
| Intended-use statement | Documentation of an AI system's purpose and objectives, required before development begins |
| Drift | Gradual performance or behavior degradation in a deployed AI system, often without a clear trigger event |
| AI-specific incident response | A monitoring and escalation process tailored to AI failure modes, distinct from generic IT incident response |
| Change re-assessment | The requirement that a material change to a deployed AI system triggers a fresh Clause 6 risk assessment |
| Decommissioning | The formal retirement process for an AI system, including inventory removal and data disposition |

## Practice questions

1. Why is the AI system inventory described as the load-bearing artifact
   of Clause 8?
2. What is shadow AI, and why does it represent a specific audit risk?
3. Name the gate requirement for each of the five lifecycle stages covered
   in this module.
4. Why can't AI incident response simply be folded into an existing IT
   incident response process?
5. If a deployed model is retrained on new data for the same use case,
   what does Clause 8 require before that change goes live?
6. What documentation gap can occur when an AI system is retired without
   a formal decommissioning process?

## How to explain it in an interview

> "Clause 8 is operations — it's where Clause 6's risk decisions actually
> get enforced day to day across the AI system lifecycle. Everything hangs
> off a central AI system inventory: no system is governed if it's not in
> that inventory, and shadow AI — tools adopted outside the formal process
> — is one of the most common gaps auditors find. Each lifecycle stage,
> from design through deployment to retirement, has a gate that blocks
> progress until a requirement is met, not just a checklist reviewed
> afterward. The two parts people most often get wrong: AI incident
> response can't just be bolted onto an existing IT process, because AI
> failure modes like drift don't have an obvious trigger event the way an
> outage does. And any material change to a deployed system — a retrain, a
> new data source — has to trigger a fresh Clause 6 risk assessment, not
> just get logged as a routine deployment."

---

*Previous: [Module 5 — AI Risk Assessment and Treatment Under Clause 6](module-05-risk-assessment-treatment.md)*
*Next: Module 7 — Performance Evaluation Under Clause 9*
