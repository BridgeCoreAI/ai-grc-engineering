# AI GRC Engineering Portfolio

> A practical, engineering-first approach to AI Governance, Risk, and Compliance —
> translating frameworks into working systems, templates, automation scripts, and audit-ready evidence.

---

## What this repository is

This repository documents my journey from AI GRC practitioner to AI GRC **engineer**. It covers the major AI governance frameworks, translates them into operational controls and workflows, and engineers those into repeatable, measurable, and auditable systems.

It is both a learning record and a professional portfolio. Every framework is documented from first principles. Every template is production-ready. Every script automates a real GRC task.

---

## Frameworks covered

| Framework | Status | Folder |
|---|---|---|
| NIST AI Risk Management Framework (AI RMF 1.0) | ✅ In progress | `frameworks/nist-ai-rmf/` |
| ISO/IEC 42001:2023 | 🔜 Coming soon | `frameworks/iso-42001/` |
| EU AI Act | 🔜 Coming soon | `frameworks/eu-ai-act/` |
| OECD AI Principles | 🔜 Coming soon | `frameworks/oecd-ai-principles/` |

---

## Repository structure

```
ai-grc-engineering/
│
├── README.md                          ← You are here
│
├── frameworks/
│   └── nist-ai-rmf/
│       ├── README.md                  ← Framework overview
│       ├── modules/                   ← Module-by-module learning notes
│       │   ├── module-01-overview.md
│       │   ├── module-02-four-functions.md
│       │   └── module-03-key-concepts.md
│       ├── references/                ← Quick-reference documents
│       │   ├── trustworthy-ai-properties.md
│       │   ├── ai-lifecycle-stages.md
│       │   ├── risk-types.md
│       │   └── human-oversight-levels.md
│       └── templates/                 ← Framework-specific templates
│
├── templates/                         ← Operational GRC templates
│   ├── intake/
│   │   └── ai-intake-workflow.md
│   ├── risk-assessment/
│   │   └── ai-risk-assessment-template.md
│   └── control-library/
│       └── ai-control-library.md
│
├── scripts/                           ← Automation scripts (coming after Module 8)
│
├── case-studies/                      ← Applied case studies by industry
│   ├── healthcare/
│   ├── banking/
│   ├── hr/
│   ├── government/
│   └── cybersecurity/
│
├── control-mappings/                  ← Cross-framework control mappings
│
├── dashboards/                        ← GRC dashboard apps (coming after Module 10)
│
└── .github/workflows/                 ← CI automation (coming after Module 9)
```

---

## GRC engineering philosophy

> Policy → Control → Workflow → Evidence → Dashboard → Executive Report

A GRC engineer does not just understand frameworks — they translate them into
systems that organizations can actually operate. Every artifact in this repository
follows that chain:

1. **Start with the framework requirement** (e.g. NIST AI RMF GOVERN function)
2. **Translate it into a policy or control** (e.g. AI Governance Policy, AI risk ownership)
3. **Engineer it into a workflow** (e.g. AI intake process, approval gate)
4. **Define the evidence** (e.g. signed approval record, risk register entry)
5. **Make it measurable** (e.g. dashboard metric, monitoring alert)
6. **Make it auditable** (e.g. version-controlled record, change log)

---

## How to use this repository

**If you are learning AI GRC:** Read the module notes in order under `frameworks/nist-ai-rmf/modules/`. Each module builds on the last. The reference documents are quick-lookup cards you will use repeatedly.

**If you are a hiring manager or client:** The templates under `templates/` are production-ready and can be adapted for immediate use. The case studies show applied thinking across industries. Scripts (coming) demonstrate engineering capability.

**If you are an auditor or reviewer:** Every document is version-controlled with commit history. The control library maps controls to framework requirements. The evidence checklist shows what documentation is maintained.

---

## Modules completed

| Module | Topic | Status |
|---|---|---|
| Module 1 | What NIST AI RMF is, why it was created, who uses it | ✅ Complete |
| Module 2 | The four core functions: GOVERN, MAP, MEASURE, MANAGE | ✅ Complete |
| Module 3 | Key concepts: Trustworthy AI, AI lifecycle, risk types, impact | ✅ Complete |
| Module 4 | Real-world application and industry use cases | ✅ Complete |
| Module 5 | AI risk assessment — deep dive | ✅ Complete |
| Module 6 | Governance controls | 🔜 Coming |
| Module 7 | Audit readiness and evidence | 🔜 Coming |
| Module 8 | GRC engineering and automation | 🔜 Coming |
| Module 9 | Practical templates | 🔜 Coming |
| Module 10 | Career, interview prep, and capstone | 🔜 Coming |

---

## Technologies used

- **Documentation:** Markdown
- **Templates:** Markdown, Excel (coming), Word (coming)
- **Scripting:** Python (coming — after Module 8)
- **Automation:** GitHub Actions (coming — after Module 9)
- **Dashboard:** Streamlit (coming — after Module 10)

---

## About this project

Built as part of a structured AI GRC engineering curriculum covering:
NIST AI RMF · ISO/IEC 42001:2023 · EU AI Act · OECD AI Principles ·
AI risk assessment · GRC engineering · audit readiness · control automation

---

*Last updated: Module 4 complete*
