# Decisions

**Status:** Living Document

**Last Updated:** 2026-08-01

**Audience:** Developers, AI Assistants

**Related Documents:**
- architecture.md
- current-state.md
- design-principles.md

---

# About This Document

This document records significant architectural and product decisions.

Each entry should answer:

- What changed?
- Why?
- What alternatives were considered?
- Why was this approach selected?

Only record decisions that are expected to influence future development.

---

# Decision Template

## YYYY-MM-DD

### Decision

...

### Reason

...

### Alternatives Considered

...

### Impact

...

---

# 2026-07-XX

## Project Scope

### Decision

LevLake will be developed specifically for one family.

### Reason

General-purpose software introduces unnecessary complexity.

Optimizing for one family allows simpler workflows and better user experience.

### Alternatives Considered

- Multi-family platform
- Vacation rental software
- Generic reservation system

### Impact

Future features should optimize for this family's workflow rather than general flexibility.

---

# 2026-07-XX

## Server Rendered Application

### Decision

Use FastAPI with server-rendered templates.

### Reason

Simpler architecture.

Less JavaScript.

Faster development.

Easy for AI assistants to understand.

### Alternatives Considered

React

Vue

Next.js

SPA architecture

### Impact

Client-side JavaScript should remain an enhancement layer rather than becoming the primary application.

---

# 2026-07-XX

## Prose First Interface

### Decision

The landing page communicates primarily through narrative summaries.

### Reason

Users understand situations faster through concise summaries than by interpreting multiple independent widgets.

### Alternatives Considered

Dashboard-style interface

Widget-first design

### Impact

Future features should summarize information before presenting detailed data.

Cards support the narrative rather than replace it.

---

# 2026-07-XX

## Landing Page Focus

### Decision

The landing page should answer:

"What do I need to know about the lake today?"

### Reason

Users should understand the current state within a few seconds.

### Alternatives Considered

Feature navigation

Dashboard homepage

Menu-driven interface

### Impact

New landing page components should directly support situational awareness.

---

# 2026-07-XX

## Family Specific Terminology

### Decision

Use family terminology throughout the application.

Examples include:

- Pop-Pop
- Mimi
- Lake Brief

### Reason

The application is intentionally personal.

Generic terminology makes the experience feel less natural.

### Alternatives Considered

Generic labels

Commercial terminology

### Impact

Future features should continue using family language where appropriate.

---

# 2026-08-01

## Documentation First

### Decision

Project documentation is maintained alongside the codebase.

### Reason

Documentation becomes the permanent memory of the project.

Future AI assistants should understand previous decisions without relying on chat history.

### Alternatives Considered

Rely on repository history.

Rely on chat history.

### Impact

Architectural decisions should be documented before they are forgotten.