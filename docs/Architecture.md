# Architecture

**Status:** Living Document

**Last Updated:** 2026-08-01

**Audience:** Developers, AI Assistants

**Related Documents:**
- README.md
- ai-context.md
- decisions.md

Levenson Lake is a mobile-first Progressive Web App hosted on Cloudflare Workers.

The application is organized around weekends, not reservations.

Every major feature supports one of three phases:

- Before the Trip
- During the Stay
- Heading Home

---

# Design Goals

The application should...

- reduce friction
- encourage family time
- disappear into the background
- reward planning
- communicate naturally
- feel handcrafted


# Navigation

Home

Calendar

House

Boat

More

---

# Home

Purpose

Answer the five most common questions immediately.

Who's there?

When is the next trip?

Is the house ready?

Should we take the boat out?

Anything I should know?

---

# Calendar

Purpose

Coordinate family weekends.

The calendar is a visualization of reservations.

---

# Weekend

Purpose

Everything specific to one trip.

Planning

Meals

Shopping

Activities

Notes

Heading Home

Summary

---

# House

Purpose

Permanent information.

House Status

Projects

Wi-Fi

Cleaning

House Guide

Maintenance

---

# Boat

Purpose

Current lake conditions.

Boat Status

Fuel

Weather

Water Temperature

Best Boating Window

Seasonal Advisor

---

# More

Purpose

Everything else.

Weather

Journal

Family

Settings

About



---

# Current Architecture

```
Browser
    │
    ▼
FastAPI
    │
Jinja Templates
    │
HTML / CSS / JavaScript
```

The application intentionally renders HTML on the server.

Client-side JavaScript should enhance the experience rather than become the application.

---

# Why FastAPI

## Why We Chose It

FastAPI provides an excellent balance between simplicity and capability.

It offers:

- Excellent readability
- Strong typing
- Minimal boilerplate
- First-class Python support
- Excellent AI comprehension
- Easy API expansion if mobile applications are added later

For LevLake, FastAPI disappears into the background and allows us to focus on solving family problems rather than framework problems.

---

## What It Optimizes

✓ Readability

✓ Simplicity

✓ AI generated code quality

✓ Maintainability

---

## What Would Justify Replacing It

FastAPI should only be replaced if there is a measurable benefit.

Examples include:

- Performance limitations become significant.
- A future mobile architecture requires something fundamentally different.
- Maintenance becomes impractical.

Curiosity or popularity alone are not valid reasons.

---

# Why Server Rendered HTML

LevLake is intentionally built around server-rendered pages.

Reasons:

- Faster development.
- Easier debugging.
- Better AI understanding.
- Less frontend complexity.
- Excellent performance for a small family application.

Single Page Applications are not a goal.

Interactive JavaScript should be added only where it genuinely improves the user experience.

---

# Why Jinja Templates

Templates keep presentation separate from application logic while remaining extremely easy to understand.

Advantages:

- Clean HTML.
- Minimal abstraction.
- Easy reuse.
- Excellent AI compatibility.

---

# Why Plain HTML and CSS

The user interface is intentionally handcrafted.

Reasons:

- Complete design control.
- Long-term stability.
- Easier debugging.
- Easier customization.

Frameworks should reduce complexity rather than introduce it.

---

# CSS Philosophy

CSS should remain organized around reusable components rather than individual pages.

The visual language should remain:

- calm
- elegant
- restrained
- readable

Avoid unnecessary animations or effects.

---

# JavaScript Philosophy

JavaScript is an enhancement layer.

It should never become the primary application.

Good uses include:

- Calendar interaction
- Small interface improvements
- Progressive enhancement

Avoid large client-side frameworks unless they provide overwhelming value.

---

# Data Philosophy

LevLake stores information that helps families make decisions.

It is not intended to become a general-purpose database.

Data should always support a user-facing decision or answer a real question.

---

# AI Philosophy

The codebase is intentionally written to be AI-friendly.

That means:

- descriptive names
- small functions
- explicit behavior
- clear comments where necessary
- limited abstraction
- minimal magic

Future AI assistants should be able to understand the project after reading only a few files.

---

# Dependency Philosophy

Every dependency introduces long-term maintenance.

Before adding a dependency ask:

1. Does Python already solve this?

2. Can we write this ourselves in a few lines?

3. Does this reduce overall complexity?

Only if the answer is yes should a dependency be added.

---

# Repository Philosophy

The repository is intended to become the permanent memory of the project.

Important decisions belong in documentation rather than chat history.

Documentation should explain:

- why
- not just what

Future contributors should understand the reasoning behind every major architectural decision.

---

# Future Evolution

LevLake should evolve slowly.

Small improvements are preferred over major rewrites.

The architecture should remain understandable to someone reading the code five years from now.

New technology should be adopted only when it clearly improves the experience for both users and developers.

Stability is a feature.