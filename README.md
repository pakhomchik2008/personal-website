# Personal Website

Personal portfolio — Next.js (App Router) + TypeScript + Tailwind CSS.

Live: https://personal-website-ten-alpha-61.vercel.app

## Sections

- About, Education, Certifications, Writing, Contact — homepage sections (`src/components/sections/`)
- Project write-ups: digital divide research, cryptocurrency/blockchain essay, narrative game (`src/app/projects/`)
- Karate — standalone page with competition photos (`src/app/karate/`)

## Stack

Next.js · TypeScript · Tailwind CSS · deployed on Vercel

## Running locally

```bash
npm install
npm run dev
```

Open http://localhost:3000.

## Structure

```
src/
  app/
    page.tsx              landing page
    karate/                karate page
    projects/               per-project write-ups
  components/
    sections/               homepage sections (About, Education, Certifications, ...)
    Nav.tsx, Socials.tsx, Spotlight.tsx, Tag.tsx, BackButton.tsx, SectionLabel.tsx
public/                    resume, certificates, project assets
```
