# deployment.md

# Deployment

**Status:** Living Document

**Last Updated:** 2026-08-01

**Audience:** Developers

**Related Documents:**
- architecture.md
- developer-guide.md

---

# Purpose

Document how LevLake is developed, deployed, and maintained.

---

# Development Environment

Current

- Windows
- VS Code
- Python
- uv
- FastAPI

Start application

uv run uvicorn app.main:app --reload

---

# Source Control

GitHub

Main branch

main

GitHub Desktop is the preferred Git client.

---

# Current Deployment

Current hosting

Cloudflare

Current application

FastAPI

(Current deployment details to be expanded.)

---

# Future Deployment

Possible future options

- Docker
- Windows Development VM
- Cloud Development VM

Future deployment decisions belong in decisions.md.

---

# Environment Variables

Document here as they are added.

Current

(None)

---

# DNS

Primary domain

levlake.us

Additional DNS entries should be documented here.

---

# Certificates

Document certificate requirements as they are introduced.

---

# Backups

Repository

GitHub

Application data

(TBD)

---

# Deployment Checklist

Before deployment

- Pull latest code
- Verify application starts
- Verify documentation
- Verify responsive layout
- Verify no debug code remains

