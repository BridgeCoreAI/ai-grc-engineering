#!/bin/bash
# =============================================================================
# AI GRC Engineering — GitHub Repository Setup Script
# =============================================================================
# Run this script once to initialize your local Git repository and make your
# first commit. Then push to GitHub using the instructions at the bottom.
#
# Usage:
#   chmod +x setup-repo.sh
#   ./setup-repo.sh
# =============================================================================

set -e

echo ""
echo "=================================================="
echo "  AI GRC Engineering — Repository Setup"
echo "=================================================="
echo ""

# Initialize Git
git init
echo "✅ Git repository initialized"

# Configure Git identity (edit these before running)
# git config user.name "Your Name"
# git config user.email "your.email@example.com"

# Create .gitignore
cat > .gitignore << 'EOF'
# OS files
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
*.pyo
.env
venv/
.venv/

# Node
node_modules/
npm-debug.log

# Output files (generated — not tracked)
outputs/
*.tmp

# Sensitive files — never commit these
*.key
*.pem
secrets.json
.env.local
credentials.json

# IDE
.vscode/
.idea/
*.swp
EOF
echo "✅ .gitignore created"

# Stage all files
git add .
echo "✅ All files staged"

# First commit
git commit -m "feat: initial commit — AI GRC Engineering portfolio

Modules completed through Module 4 (NIST AI RMF):
- Module 1: Framework overview, purpose, and stakeholders
- Module 2: Four core functions (GOVERN, MAP, MEASURE, MANAGE)
- Module 3: Key concepts (trustworthy AI, lifecycle, risk types, impact)
- Module 4: Real-world application and industry use cases

Reference cards added:
- Seven properties of trustworthy AI
- AI lifecycle stages with GRC touchpoints
- AI risk types with examples and identification questions
- Human oversight levels decision guide

Templates added:
- AI intake workflow (six stages with approval gates)
- AI risk assessment template (Sections A–D)
- AI control library (25 controls across 9 domains)"

echo ""
echo "✅ First commit created"
echo ""
echo "=================================================="
echo "  Next steps — push to GitHub"
echo "=================================================="
echo ""
echo "1. Create a new repository on GitHub:"
echo "   https://github.com/new"
echo "   Name suggestion: ai-grc-engineering"
echo "   Visibility: Public (for portfolio) or Private"
echo "   Do NOT initialize with README (you already have one)"
echo ""
echo "2. Add the remote and push:"
echo ""
echo "   git remote add origin https://github.com/YOUR-USERNAME/ai-grc-engineering.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. After each module, commit your new notes:"
echo ""
echo "   git add ."
echo "   git commit -m 'feat: complete Module 5 — AI risk assessment deep dive'"
echo "   git push"
echo ""
echo "=================================================="
echo "  Commit message conventions for this project"
echo "=================================================="
echo ""
echo "  feat:     New module notes or templates"
echo "  docs:     Updates to existing documentation"
echo "  refactor: Reorganizing content or structure"
echo "  scripts:  Adding Python automation scripts"
echo "  ci:       GitHub Actions workflow changes"
echo ""
echo "  Examples:"
echo "  git commit -m 'feat: add Module 5 risk assessment deep dive'"
echo "  git commit -m 'docs: update trustworthy AI reference card'"
echo "  git commit -m 'scripts: add risk register generator script'"
echo "  git commit -m 'feat: add ISO 42001 framework overview'"
echo ""
