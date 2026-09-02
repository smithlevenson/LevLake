# deployment.md

# Deployment

**Status:** Living Document

**Last Updated:** 2026-09-02

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

Public hosting: Cloudflare Worker `levlake`, serving static files from `public/`.

Development application: FastAPI under `app/`.

See the verified deployment notes below.

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


## Verified public deployment — 2026-09-02

The Cloudflare Worker overview confirms the existing `levlake` Worker serves
static assets, has custom domain `levlake.us`, and was manually deployed with
Wrangler. It also lists `levlake.levlake.workers.dev`. No Git-based continuous
deployment was shown. The domain overview's “No Workers connected” card was
inconsistent with this Worker-specific custom-domain configuration.

`wrangler.jsonc` deploys `public/`. The FastAPI application under `app/` is a
separate development implementation and is not deployed by this static-assets
configuration. Earlier notes describing the public site as obsolete are not
evidence that it was removed.

### LevAssistant information pages

The following static pages support LevAssistant's Google OAuth branding:

- Homepage: https://levlake.us/levassistant/
- Privacy: https://levlake.us/levassistant/privacy/
- Terms: https://levlake.us/levassistant/terms/

Their source is `public/levassistant/`, with a stylesheet scoped to those pages.
The pages contain public app information only. Google tokens and household
calendar events stay out of this site. The local LevAssistant appliance is not
exposed through this Worker.

These additions are prepared in source; deployment and public URL verification
are pending. Do not enter URLs in OAuth branding until all three load publicly.

From the existing Windows LevLake checkout, review `git status --short --branch`
and pull `main` with `git pull --ff-only`. Preserve local work if the pull cannot
proceed. Review changes before deployment: Wrangler publishes the entire
`public/` directory, not just the new pages.

Deploy using the existing configuration:

```powershell
npx wrangler deploy
```

If authentication is required, use Wrangler's browser login with the Cloudflare
account that owns the existing Worker. Never paste credentials into chat or
commit them. After deployment, verify the existing root page and all three
LevAssistant URLs. Record the resulting Worker version and acceptance here.

In Google OAuth Branding, use `levlake.us` as the authorized domain and the three
verified HTTPS URLs above. Complete any domain ownership verification Google
requests. Do not enter the local appliance hostname as a public domain.

The privacy policy describes the currently implemented read-only integration.
Review it before enabling additional calendars, persistent event storage, AI
processing, account features, or new data sharing.
