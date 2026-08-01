# LevLake

The Levenson Family Lake House Portal

## Goals

- Reservation Calendar
- Booking Approval
- Email Notifications
- House Guide
- Shopping List
- Cleaning Requests
- Closing Checklist

## Stack

- FastAPI
- SQLite
- SQLAlchemy
- Jinja2
- Docker
- Caddy
- GitHub
- TrueNAS

## Development

```bash
uv run uvicorn app.main:app --reload
```

# Levenson Lake (LevLake)

> *A private family coordination platform for Levenson Lake.*

LevLake is a lightweight web application designed specifically for our family's lake house. It replaces scattered text messages, emails, and phone calls with a single place to coordinate reservations, weekend planning, house status, meals, boating, weather, and family communication.

This is intentionally **not** a vacation rental platform, social network, or home automation dashboard. Its purpose is to make family planning effortless while remaining elegant, simple, and enjoyable to use.

---

# Project Goals

LevLake exists to answer one question:

> **"What do I need to know before going to the lake?"**

Everything in the application should reduce uncertainty, unnecessary communication, or planning effort.

Primary goals:

- Family-first experience
- Mobile-first design
- Information density without clutter
- Calm, elegant interface
- Fast performance
- Minimal maintenance
- AI-friendly architecture
- Easy for future family members to understand and extend

---

# Current Technology

| Component | Purpose | Why We Chose It |
|-----------|----------|----------------|
| Python | Backend language | Readable, mature, AI-friendly |
| FastAPI | Web framework | Simple, typed, minimal boilerplate |
| Jinja2 | HTML templating | Keeps presentation straightforward without unnecessary frontend complexity |
| HTML/CSS | User Interface | Full control over the experience |
| Git + GitHub | Version Control | Simple collaboration and history |
| Cloudflare | Deployment & Security | Excellent edge performance and secure remote access |

Technology choices are documented in more detail in **docs/architecture.md**.

---

# Repository Structure

```
LevLake/
│
├── app/
│   ├── main.py
│   ├── static/
│   └── templates/
│
├── docs/
│
├── tests/
│
├── README.md
└── pyproject.toml
```

---

# Quick Start

Clone the repository

```bash
git clone <repository>
cd LevLake
```

Install dependencies

```bash
uv sync
```

Run the application

```bash
uv run uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# Documentation

Every contributor (human or AI) should read these documents before making significant changes.

| Document | Purpose |
|-----------|----------|
| docs/vision.md | Long-term vision |
| docs/project-philosophy.md | Design philosophy |
| docs/design-principles.md | UX and interaction principles |
| docs/architecture.md | Technical decisions |
| docs/ui-guidelines.md | Visual language |
| docs/reference.md | Lake-specific information |
| docs/current-state.md | Current development focus |
| docs/decisions.md | Architecture Decision Record (ADR) |
| docs/session-log.md | Development journal |
| docs/anti-goals.md | Things LevLake intentionally is not |
| docs/ai-context.md | Instructions for AI coding assistants |

---

# Development Workflow

Before beginning work:

1. Pull the latest changes.
2. Read `docs/current-state.md`.
3. Read any relevant design or architecture documents.
4. Make focused, incremental changes.
5. Update documentation if the design or architecture changes.

Before committing:

- Verify the application runs.
- Remove unused code.
- Keep changes small and understandable.
- Update documentation when needed.

---

# Design Philosophy

LevLake values:

- Simplicity over cleverness
- Information over decoration
- Calm over flashy
- Family utility over feature count
- Readability over abstraction
- Long-term maintainability over short-term convenience

Every feature should answer:

> **Does this reduce friction for the family?**

If not, it probably doesn't belong.

---

# AI Contributors

AI assistants are expected to understand the project before modifying it.

They should:

- Read documentation first.
- Preserve existing design language.
- Prefer small incremental improvements.
- Avoid unnecessary frameworks or dependencies.
- Explain architectural changes before implementing them.
- Document significant decisions.

LevLake is intended to be understandable by both humans and future AI assistants.

---

# Current Status

The project is currently focused on building a polished MVP for internal family use.

Current priorities include:

- Landing page refinement
- Reservation workflow
- Calendar experience
- Lake Brief
- Family planning tools

See `docs/current-state.md` for the latest priorities.


---

# License

Private repository.

Copyright © Levenson Family.

Not intended for public distribution.