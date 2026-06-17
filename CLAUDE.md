# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm run dev       # start dev server at localhost:3000
npm run build     # production build
npm run start     # serve production build
```

No linter or test suite is configured.

To preview changes locally, run `python check.py` from this repo — it starts the dev server and opens the browser (expects the project at `~/Downloads/hlib-portfolio`).

## Architecture

Next.js 14 App Router, TypeScript, Tailwind CSS.

**Layout:** `src/app/layout.tsx` wraps everything with two Google Fonts (Inter as `font-sans`, JetBrains Mono as `font-mono`) and a full-screen `Spotlight` component that renders a mouse-tracking radial gradient overlay (indigo, `z-10`, `pointer-events-none`).

**Home page (`/`):** Two-column layout — sticky left sidebar (name, `Nav`, `Socials`) + scrollable right content (`About`, `Education`, `Projects`, `Contact` sections). On mobile it collapses to single column.

**Project detail pages:** `/projects/digital-divide` and `/projects/narrative-game` are standalone pages using `BackButton` to return home.

**`/karate`** is an additional standalone page.

**Component locations:**
- `src/components/` — shared UI primitives (`Nav`, `Socials`, `BackButton`, `SectionLabel`, `Tag`, `Spotlight`)
- `src/components/sections/` — homepage section blocks (`About`, `Education`, `Projects`, `Contact`)

**Adding a new project:** Add an entry to the `PROJECTS` array in `src/components/sections/Projects.tsx`, then create `src/app/projects/<slug>/page.tsx`.

## Design tokens (tailwind.config.ts)

| Token | Value |
|---|---|
| `bg-bg` | `#0d0d0d` |
| `bg-surface` | `#141414` |
| `border-border` | `#222222` |
| `text-accent` / `bg-accent` | `#6366f1` (indigo) |
| `accent-low` | `rgba(99,102,241,0.08)` |
| `accent-mid` | `rgba(99,102,241,0.25)` |

## GitHub Actions

`.github/workflows/claude.yml` runs Claude Code in CI when issues or PR comments mention `@claude`. It expects `npm run setup` and `npm run dev:daemon` scripts (not currently in `package.json` — add them if enabling this workflow).
