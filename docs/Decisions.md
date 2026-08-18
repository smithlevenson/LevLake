# Decisions

**Status:** Living Document

**Last Updated:** 2026-08-17

**Audience:** Developers, AI Assistants

**Related Documents:**
- Architecture.md
- Roadmap.md

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

---

# 2026-08-17

## Dedicated Lake Edge Computer

### Decision

Use the Dynabook Portégé X40-K as the dedicated always-on lake computer named `LEVLAKE-EDGE`.

The machine has an Intel Core i7-1260P, 12 cores / 16 logical processors, 16 GB RAM, Windows 11 Pro, integrated Intel graphics, and an internal laptop battery.

### Reason

The initial edge workload is light, but the lake needs a reliable local bridge for future MQTT, webhooks, camera integration, local APIs, house-state collection, and remote access.

The Dynabook provides substantial unused compute headroom for future workloads while remaining power-efficient enough for always-on operation.

Its laptop battery is also useful because utility power at the lake fails frequently.

### Alternatives Considered

- HP Core 3 100U / 12 GB laptop
- Core i3-1005G1 / 8 GB laptop
- Dedicated mini PC
- No local compute node

The smaller laptops are sufficient for the current edge workload, but they leave much less headroom for virtualization and future local compute.

### Impact

`LEVLAKE-EDGE` becomes part of the lake infrastructure architecture and should be treated as a persistent node rather than a personal workstation.

It should remain lightly loaded during normal operation and reserve compute capacity for future services.

---

# 2026-08-17

## Edge Power and Network Placement

### Decision

Keep `LEVLAKE-EDGE` in the Lake Office on wired Ethernet rather than moving it to a generator-powered location.

Use the laptop battery plus a small UPS as ride-through power.

### Reason

The Lake Office is hardwired by CAT5 to the lake networking equipment. The networking equipment and Starlink connection are generator-backed even though the office outlet is not.

The laptop therefore remains connected to a powered network during many utility outages while its UPS and internal battery keep the computer operating.

### Alternatives Considered

- Move the laptop to a generator-backed room
- Rewire the Lake Office immediately
- Rely only on the laptop battery

### Impact

The laptop can potentially report utility-power loss while retaining network and Internet access.

Power-state telemetry should eventually be incorporated into Edge monitoring, but laptop AC/battery state alone should not be treated as an authoritative whole-house power sensor.

---

# 2026-08-17

## Starlink Connectivity Strategy

### Decision

Design lake remote access and cloud-to-local communication around outbound connections, authenticated HTTPS/webhooks, MQTT, and Tailscale rather than public inbound ports.

### Reason

Starlink connectivity is well suited to outbound application traffic and overlay networking but should not be treated as a traditional public-IP connection for inbound service exposure.

The lake architecture should remain secure and tolerant of changing Internet conditions.

### Alternatives Considered

- Public port forwarding
- Directly exposing local APIs
- Cloud-only architecture with no local Edge node

### Impact

Local automation should continue functioning during Internet outages where possible, buffer relevant state, and reconcile with cloud services after connectivity returns.

---

# 2026-08-17

## Future Lake Arcade on Edge Hardware

### Decision

Preserve enough compute headroom on `LEVLAKE-EDGE` to support a future lightweight Lake Arcade workload.

The Lake Arcade should be curated rather than copied wholesale from the primary home ArcadeVM.

### Reason

The i7-1260P and 16 GB RAM provide enough CPU capacity for an occasional arcade workload while edge services remain lightweight.

A lake-specific library does not need modern high-end emulation. Classic systems through at least Nintendo 64 are considered appropriate targets.

### Alternatives Considered

- Dedicated arcade computer at the lake
- Use one of the lower-spec laptops as Edge and retain the Dynabook elsewhere
- Duplicate the full primary ArcadeVM

### Impact

The eventual implementation may use a lightweight VM if graphics acceleration is adequate, or run natively on Windows if integrated-GPU virtualization is unnecessarily limiting.

The arcade workload should normally be stopped when not in use.

---

# 2026-08-17

## Separate Website and Automation Responsibilities

### Decision

Keep LevLake as the family-facing website/application and plan for a separate lake automation codebase when low-level device orchestration becomes substantial.

LevLake may display live house state and issue high-level requests, but it should not absorb device-specific automation logic.

### Reason

The existing LevLake roadmap explicitly says the application is not intended to become a smart-home controller.

The website and the physical-house integration layer have different lifecycles, failure modes, security concerns, and responsibilities.

Separating them keeps both systems easier to understand and maintain.

### Alternatives Considered

- Put all Edge and automation code directly in the LevLake repository
- Build all automation functionality as internal LevLake services
- Keep the systems completely disconnected

### Impact

A future `LakeAutomation` or similarly named repository should own MQTT, cameras, device APIs, local automation, power/network monitoring, and Edge runtime services.

LevLake and the automation system should integrate through explicit contracts such as authenticated APIs, webhooks, and MQTT.