# UI Guidelines

**Status:** Living Document

**Last Updated:** 2026-08-01

**Audience:** Developers, Designers, AI Assistants

**Related Documents:**
- design-principles.md
- reference.md
- decisions.md

---

# Purpose

This document defines the visual language of LevLake.

It should guide design decisions without prescribing implementation.

---

# Design Goals

The interface should feel:

- Calm
- Premium
- Understated
- Comfortable
- Familiar

The application should resemble a thoughtfully designed family notebook rather than business software.

---

# Information Hierarchy

Users should understand the current state of the lake within a few seconds.

Display information in this order:

1. What matters today
2. Upcoming reservations
3. Supporting information
4. Navigation

The most important information should require the least effort to find.

---

# Landing Page

The landing page should answer:

"What do I need to know before going to the lake?"

It should not attempt to expose every feature.

---

# Lake Brief

Lake Brief is the primary communication mechanism.

It should:

- summarize
- prioritize
- explain

It should not simply list data.

Example

GOOD

"Eight family members are expected this weekend. Saturday morning offers the best boating weather. Dinner is nearly planned, but someone still needs to bring ice."

BAD

Weather

Boat

Meals

Ice

Reservations

The prose provides understanding.

The cards provide supporting detail.

---

# Cards

Cards exist to support the summary.

Cards should:

- contain one idea
- remain visually consistent
- avoid unnecessary text

Cards should never compete with the Lake Brief.

---

# Calendar

Purpose

Situational awareness.

Not scheduling.

The calendar should quickly communicate:

- occupied dates
- upcoming trips
- availability

It is not intended to become a scheduling application.

---

# Reservations

Reservation information should emphasize:

Arrival

Departure

Duration

Availability

Users should immediately understand:

Who

When

For how long

---

# Typography

Typography should communicate hierarchy before decoration.

Use:

- spacing
- size
- weight

before introducing color.

---

# Color

Color communicates meaning.

It should not exist solely for decoration.

Primary uses:

- reservation ownership
- status
- emphasis

Avoid decorative color usage.

---

# White Space

White space is intentional.

Do not fill empty areas simply because space exists.

---

# Motion

Animation should communicate state changes.

Avoid animation that exists only for visual interest.

---

# Mobile

Mobile is the primary experience.

Desktop should expand the layout rather than introduce new interactions.

---

# Components

Components should remain:

- reusable
- predictable
- consistent

Avoid creating one-off components.

---

# AI Guidance

When modifying the interface:

Prefer

- fewer elements
- better hierarchy
- stronger typography
- clearer summaries

Avoid

- dashboard widgets
- visual noise
- unnecessary controls
- decorative effects

When uncertain, remove complexity rather than add it.