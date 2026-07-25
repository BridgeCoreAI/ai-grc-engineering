<div align="center">

### BridgeCore AI LLC — AI Governance Practice
*Engineering responsible AI governance for federal agencies and enterprises*

*"Governance is not what is defined. It is what is enforced at execution."*

---

</div>

# AI GRC Engineering Portfolio

> A practical, engineering-first approach to AI Governance, Risk, and Compliance —
> translating frameworks into working systems, templates, automation scripts, and audit-ready evidence.

See [`AIGRC_Executive_Summary.md`](./AIGRC_Executive_Summary.md) for a one-page overview of this project.

---

## What this repository is

This repository documents the translation of AI GRC practice into AI GRC **engineering**. It covers the major AI governance frameworks, translates them into operational controls and workflows, and engineers those into repeatable, measurable, and auditable systems.

It is both a completed learning record and a professional portfolio. Every framework is documented from first principles. Every template is production-ready. Every script automates a real GRC task.

A private companion repository extends this work with client-facing tooling, evidence-generation systems, and applied consulting artifacts not published here.

---

## Frameworks covered

| Framework | Status | Folder |
|---|---|---|
| NIST AI Risk Management Framework (AI RMF 1.0) | ✅ Complete | `frameworks/nist-ai-rmf/` |
| ISO/IEC 42001:2023 | ✅ Complete | `frameworks/iso-42001/` |
| EU AI Act | ✅ Complete | `frameworks/eu-ai-act/` |

Each framework folder follows the same structure: a `README.md` overview, a `modules/` set of module-by-module breakdowns, and an `assets/` folder with supporting diagrams. NIST AI RMF additionally includes a `references/` folder of quick-lookup cards.

---

## Repository structure

```
ai-grc-engineering/
│
├── README.md                          ← You are here
├── AIGRC_Executive_Summary.md         ← One-page project overview
├── LICENSE
├── setup-repo.sh                      ← Repo bootstrap script
│
├── frameworks/
│   ├── nist-ai-rmf/
│   │   ├── README.md
│   │   ├── modules/                   ← 9 modules, overview through practical templates
│   │   ├── references/                ← 4 quick-reference cards
│   │   └── assets/                    ← 4 diagrams
│   │
│   ├── iso-42001/
│   │   ├── modules/                   ← 9 modules, overview through Annex B impact assessments
│   │   └── assets/                    ← PDCA cycle diagram
│   │
│   └── eu-ai-act/
│       ├── modules/                   ← 9 modules, overview through cross-framework comparison
│       └── assets/                    ← Risk-tiers diagram
│
├── templates/
│   └── intake/
│       └── ai-intake-workflow.md      ← AI system intake and triage workflow
│
├── scripts/                           ← GRC automation (Python)
│   ├── README.md
│   ├── risk_rating.py
│   ├── risk_tier_classifier.py
│   ├── generate_risk_register.py
│   ├── check_evidence_staleness.py
│   └── package_evidence.py
│
└── assets/
    └── three-pillars-ai-governance-comparison.png
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
5. **Make it measurable** (e.g. risk score, staleness check)
6. **Make it auditable** (e.g. version-controlled record, packaged evidence bundle)

---

## How to use this repository

**If you are learning AI GRC:** Read the module notes in order under each framework's `modules/` folder. Each module builds on the last. Reference documents under `frameworks/nist-ai-rmf/references/` are quick-lookup cards you will use repeatedly.

**If you are a hiring manager or client:** `templates/intake/ai-intake-workflow.md` is production-ready and adaptable for immediate use. The scripts under `scripts/` demonstrate applied automation of GRC tasks — risk rating, risk register generation, evidence staleness checks, and evidence packaging.

**If you are an auditor or reviewer:** Every document is version-controlled with commit history. `scripts/README.md` documents what each automation script does and how it maps to control requirements.

---

## Scripts

| Script | Purpose |
|---|---|
| `risk_rating.py` | Scores an AI system's risk based on defined inputs |
| `risk_tier_classifier.py` | Assigns a risk tier consistent with framework risk categories |
| `generate_risk_register.py` | Builds a structured risk register from intake data |
| `check_evidence_staleness.py` | Flags governance evidence that has aged past a defined threshold |
| `package_evidence.py` | Bundles evidence artifacts into an audit-ready package |

See `scripts/README.md` for usage details.

---

## Technologies used

- **Documentation:** Markdown
- **Templates:** Markdown
- **Scripting:** Python
- **Version control:** Git / GitHub

---

## About this project

Built as a structured AI GRC engineering portfolio covering:
NIST AI RMF · ISO/IEC 42001:2023 · EU AI Act ·
AI risk assessment · GRC engineering automation · audit readiness · evidence generation

---

*Last updated: All three frameworks (NIST AI RMF, ISO 42001, EU AI Act) complete, alongside intake workflow templates and GRC automation scripts.*
