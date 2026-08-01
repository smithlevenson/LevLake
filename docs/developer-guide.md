# developer-guide.md

# Developer Guide

**Status:** Living Document

**Last Updated:** 2026-08-01

**Audience:** Developers, AI Assistants

**Related Documents:**
- README.md
- architecture.md
- current-state.md
- work-queue.md

---

# Purpose

This document describes how LevLake is developed.

It documents workflow rather than architecture.

---

# Development Philosophy

Development should optimize for:

- Readability
- Maintainability
- Clear documentation
- Reproducible development

---

# Starting Development Session

1. Pull the latest changes.
2. Read:
   - README.md
   - ai-context.md
   - current-state.md
   - work-queue.md
4. Begin work.

---


# Commits

Commits should represent one logical change.

Examples:

✓ Improve reservation card layout

✓ Refactor calendar component

Avoid:

✗ Misc fixes

✗ Updates

---

# Documentation

Update documentation when:

- Architecture changes
- Design direction changes
- Workflow changes
- User behavior changes

Documentation should explain *why*.

---

# AI Contributors

AI should:

- Read documentation first
- Stay within the current sprint
- Avoid unrelated improvements
- Explain architectural changes
- Update documentation when appropriate

---

# Repository Organization

Keep related files together.

Avoid duplicate implementations.

Remove obsolete code after replacement.

---

# General Rule

The code should be easier to understand after every commit.