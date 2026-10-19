# Module 6 — Governance Controls
## Policies · Processes · Controls · Evidence · Monitoring

> **Framework:** NIST AI Risk Management Framework (AI RMF 1.0)
> **Module:** 6 of 10
> **Status:** ✅ Complete

---

## The foundational concept — what a control actually is

A **control** is a specific action, process, or mechanism that reduces the
likelihood or severity of a risk. It is not a policy statement. It is not an
aspiration. It is something that actually happens — on a defined schedule,
by a named person, with documented evidence.

**Not a control:**
> "We take bias seriously and test our models regularly."

**A control:**
> "The data science team conducts a demographic performance analysis of the
> loan approval model every quarter. Results are reviewed by the AI Risk Owner
> and presented to the AI Review Board. Findings are documented in the bias
> audit report filed in the GRC system. If the demographic performance gap
> exceeds 5%, an immediate model review is triggered."

The second version is auditable. The first is not.

---

## The four types of controls

| Type | Definition | AI Example |
|---|---|---|
| **Preventive** | Stops a risk from materializing before it happens | AI Review Board approval required before any system deploys |
| **Detective** | Identifies when a risk has materialized | Monitoring dashboard flags when model accuracy drops below threshold |
| **Corrective** | Fixes a problem after it is detected | Incident response plan defining how to remediate a bias finding |
| **Compensating** | Alternative when primary control cannot be implemented | Enhanced human review when explainability cannot be added to a model |

---

## The governance chain

```
Policy → Control → Monitoring → Evidence → Reporting
(what must   (how it    (is it      (proof it   (leadership
 happen)      happens)   working?)   worked)      sees it)
```

---

## The twelve governance control domains

### Domain 1 — Data Governance

**Why it is the foundation:** Every AI risk traces back to data. Biased data
produces biased models. Poor quality data produces unreliable models.

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| DG-001 | Data lineage documentation | Per data change | Data engineer | Lineage diagram, data dictionary |
| DG-002 | Training data quality assessment | Pre-training | Data scientist | Quality report, demographic coverage |
| DG-003 | Training data access control | Quarterly review | CISO / IT | Access logs, quarterly review records |
| DG-004 | Data retention and disposal | Annual review | Privacy officer | Retention schedule, disposal certificates |

**DG-001 — Data lineage documentation**
Complete record of where every piece of training and operational data came from,
how it was transformed, and how it was used. Without lineage, you cannot answer
the auditor's most basic question: "where did this data come from?"

**DG-002 — Training data quality assessment**
Formal review of completeness, accuracy, consistency, and demographic
representativeness before training begins. Covers: missing value rates, outlier
analysis, class balance, demographic coverage, and data recency.

**DG-003 — Training data access control**
Restricted access with role-based controls. All access events logged. Access
rights reviewed quarterly and revoked when no longer needed.

**DG-004 — Data retention and disposal**
Defined retention periods for training data, model outputs, and records.
Secure disposal at end of retention with documented certificate of destruction.

---

### Domain 2 — Bias & Fairness

**Why it requires its own domain:** Bias is the most frequently found and most
consequential AI risk. It requires controls across the entire AI lifecycle.

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| BF-001 | Pre-deployment fairness testing | Pre-deployment | GRC engineer | Fairness test report, demographic breakdown |
| BF-002 | Quarterly bias audit | Quarterly | GRC engineer | Audit report, trend analysis, board minutes |
| BF-003 | Proxy variable review | Pre-deployment + annual | Legal + data science | Feature analysis, legal sign-off |
| BF-004 | Bias incident log | Ongoing | GRC engineer | Incident log, root cause analysis |

**BF-001 — Pre-deployment fairness testing**
Structured test comparing model outputs across all protected demographic groups.
If disparity exceeds threshold (typically 4/5ths rule or 20% relative difference),
the model cannot deploy until remediated.

**BF-002 — Quarterly bias audit**
Recurring audit of production outputs by demographic group. Catches drift
that was not present at deployment. Results presented to AI Review Board.

**BF-003 — Proxy variable review**
Formal review of every model input feature for correlation with protected
characteristics. ZIP code, university name, and employment gaps are common
proxy variables that must be reviewed and legally justified.

---

### Domain 3 — Transparency

**Two levels:**
- **System-level:** Does the organization disclose that AI is being used?
- **Decision-level:** Can the AI explain why it made a specific decision?

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| TR-001 | Model card publication | Per system + updates | AI system owner | Published model card, version history |
| TR-002 | AI disclosure to affected individuals | At point of decision | Product + legal | Disclosure language, delivery confirmation |
| TR-003 | Explainability output requirement | Per high-risk decision | AI system owner | Sample outputs, accuracy validation |

**Model card must include:**
- Model name and version
- Purpose and intended use cases
- Out-of-scope uses
- Training data description and demographic coverage
- Performance metrics by demographic group
- Known limitations and failure modes
- Human oversight requirements
- Contact information and last updated date

---

### Domain 4 — Privacy

**AI-specific privacy risks:**
- Model memorization of training data
- Sensitive inferences from predictions
- Re-identification from model outputs
- Large-scale profiling without consent

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| PR-001 | Privacy impact assessment | Pre-deployment + annual | Privacy officer | Completed PIA, sign-off, data flow diagram |
| PR-002 | Data minimization review | Pre-deployment | Privacy officer | Minimization checklist, justification log |
| PR-003 | Individual rights process | Ongoing | Privacy officer | Request log, response records, SLA report |

---

### Domain 5 — Cybersecurity

**AI-specific security threats:**

| Threat | What it means |
|---|---|
| Model poisoning | Attacker corrupts training data to cause specific failures |
| Adversarial attacks | Crafted inputs designed to fool the model |
| Model extraction | Repeated queries to reverse-engineer model behavior |
| Model inversion | Queries designed to extract training data |

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| SC-001 | AI system security assessment | Pre-deployment + annual | CISO | Security report, pen test results, remediation log |
| SC-002 | Adversarial robustness testing | Pre-deployment + major updates | Security engineer | Adversarial test report, findings, remediation |
| SC-003 | Model access and authentication | Continuous | CISO | Access policy, authentication config, access logs |

---

### Domain 6 — Human Oversight

**GRC engineer's view:** Human oversight is not a philosophy — it is a set of
specific, auditable controls that must be designed, implemented, and monitored.

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| HO-001 | Human override capability | Continuous | AI system owner | Override mechanism docs, override log |
| HO-002 | Override rate monitoring | Monthly | GRC engineer | Monthly rate report, trend analysis |
| HO-003 | Human oversight training | Annual + system changes | AI system owner | Training completion records, competency results |

**Override rate interpretation:**
- Very high (>30%): AI not trustworthy — model review needed
- Very low (<1%) in high-stakes system: humans may be rubber-stamping — investigation needed
- Sudden change: something has changed in model or reviewer behavior — investigate

---

### Domain 7 — Model Validation

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| MV-001 | Pre-deployment validation | Pre-deployment | Independent validator | Validation report, sign-off |
| MV-002 | Ongoing model validation | Annual + after material change | Data scientist + GRC | Re-validation report |
| MV-003 | Model change management | Per change | AI system owner | Change request, impact assessment, approval record |

**Key rule:** For Tier 1 systems, pre-deployment validation must be conducted
by someone independent of the team that built the model.

---

### Domain 8 — Vendor Risk

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| VR-001 | AI vendor due diligence | Pre-contract + annual | GRC + procurement | Due diligence questionnaire, assessment report |
| VR-002 | AI vendor contract requirements | Per contract | Legal + GRC | Signed contract with required clauses |
| VR-003 | Ongoing vendor monitoring | Annual | GRC engineer | Reassessment report, change notifications |

**Required contract clauses:**
- Audit rights
- Model change notification (minimum 30 days)
- Data handling terms
- Liability clauses
- AI governance obligations

Contracts without these provisions are a governance gap.

---

### Domain 9 — Monitoring and Reporting

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| MN-001 | AI performance monitoring dashboard | Daily review | AI system manager | Dashboard screenshots, alert records |
| MN-002 | Model drift detection | Monthly | Data scientist | Drift detection reports, model review records |
| MN-003 | Executive reporting | Monthly + quarterly | GRC engineer | Board reports, executive summaries |

---

### Domain 10 — Incident Response

| Control ID | Control name | Frequency | Owner | Evidence |
|---|---|---|---|---|
| IR-001 | AI incident response plan | Annual review + per incident | GRC engineer | IR plan, tabletop exercise records |
| IR-002 | Incident log | Ongoing | GRC engineer | Incident log, root cause analysis |
| IR-003 | Post-incident review | Per significant incident | GRC engineer | Review report, control improvement actions |

---

### Domains 11 & 12 — Reporting and Accountability

**Reporting controls:**
- Monthly AI governance report to AI Review Board
- Quarterly executive summary to leadership
- Annual board-level AI risk report
- Regulatory submissions as required

**Accountability controls:**
- RACI matrix for every AI system
- Named AI Risk Owner for every system
- Governance committee charter and meeting minutes
- Escalation path documented and tested
- Audit trail for all material decisions about AI systems

---

## The four things an auditor needs to see for every control

| What auditors check | What it means | Evidence |
|---|---|---|
| The control **exists** | Documented in control library with owner, frequency, description | Control library entry |
| The control **operates** | Evidence it actually runs on schedule | Operating records, logs, reports |
| The control is **effective** | Evidence it is achieving its purpose | Test results, metrics, trend analysis |
| **Exceptions** are managed | Documented exceptions with compensating controls or risk acceptance | Exception log, risk acceptance forms |

---

## Worked example — BridgeCore AI LLC federal engagement

**Client:** Federal agency — AI benefits screening system
**Risk:** Bias risk — training data may underrepresent certain demographics

**Controls selected:**

| Control | Owner | Frequency | Evidence |
|---|---|---|---|
| BF-001: Pre-deployment fairness testing | GRC engineer | Pre-deployment | Fairness test report |
| BF-002: Quarterly bias audit | GRC engineer | Quarterly | Bias audit report |
| BF-003: Proxy variable review | Legal + data science | Pre-deployment | Feature analysis, legal sign-off |
| DG-002: Training data quality assessment | Data scientist | Pre-training | Data quality report |
| HO-001: Human override capability | System owner | Continuous | Override docs, override log |
| HO-002: Override rate monitoring | GRC engineer | Monthly | Override rate report |

**What this proves:** Six specific controls manage the bias risk, operate on
defined schedules, and maintain evidence of effectiveness.

---

## Key terms

| Term | Plain meaning |
|---|---|
| Control | Specific action that reduces likelihood or severity of a risk |
| Preventive control | Stops a risk from happening |
| Detective control | Identifies when a risk has materialized |
| Corrective control | Fixes a problem after detection |
| Compensating control | Alternative when primary control cannot be implemented |
| Control owner | Named person accountable for operating a specific control |
| Control effectiveness | Whether the control is actually achieving its purpose |
| Evidence | Documentation proving a control operated as designed |
| Exception | Documented situation where a control could not be performed |
| Model card | Standardized document describing an AI model's purpose, data, performance, and limits |
| Override rate | How often human reviewers change AI outputs |

---

## Practice questions

1. What is the difference between a policy and a control?
2. Name the four types of controls with an AI example of each
3. What are the four things an auditor needs for every control?
4. What does a very high override rate signal? A very low rate?
5. What must a model card include?
6. Name three AI-specific cybersecurity threats
7. Why is data minimization a control, not just a principle?
8. What is a proxy variable and why does it need its own control?

---

## How to explain it in an interview

> "Governance controls are the operational heart of an AI governance program.
> A GRC engineer translates risk findings into specific controls — each with a
> named owner, defined frequency, and documented evidence requirement. I organize
> controls across twelve domains: data governance, bias and fairness, transparency,
> privacy, cybersecurity, human oversight, model validation, vendor risk, monitoring,
> incident response, reporting, and accountability. For each control, I ensure four
> things: it is documented, it operates on schedule, there is evidence it is working,
> and exceptions are formally managed. That transforms a governance framework from
> a document into a living system that auditors can verify and leadership can trust."

---

*Previous: [Module 5 — AI Risk Assessment](module-05-risk-assessment.md)*
*Next: Module 7 — Audit Readiness and Evidence*
