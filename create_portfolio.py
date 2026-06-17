#!/usr/bin/env python3
"""
Hlib Pakhomov Portfolio — full Next.js scaffolder.
Run:  python3 create_portfolio.py
Then: cd hlib-portfolio && npm run dev
"""
import pathlib, subprocess, sys, webbrowser, threading, time, urllib.request

ROOT = pathlib.Path(__file__).parent / "hlib-portfolio"

def w(rel: str, text: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.lstrip("\n"), encoding="utf-8")
    print(f"  ✓  {rel}")

print("Scaffolding hlib-portfolio/\n")

# ── Config ──────────────────────────────────────────────────────────

w("package.json", """
{
  "name": "hlib-portfolio",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "14.2.5",
    "react": "^18",
    "react-dom": "^18"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "autoprefixer": "^10",
    "postcss": "^8",
    "tailwindcss": "^3",
    "typescript": "^5"
  }
}
""")

w("tsconfig.json", """
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
""")

w("tailwind.config.ts", """
import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./src/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {
      colors: {
        bg:      '#0d0d0d',
        surface: '#141414',
        border:  '#222222',
        accent: {
          DEFAULT: '#6366f1',
          low:  'rgba(99,102,241,0.08)',
          mid:  'rgba(99,102,241,0.25)',
        },
      },
      fontFamily: {
        sans: ['var(--font-inter)', 'sans-serif'],
        mono: ['var(--font-mono)', 'monospace'],
      },
    },
  },
  plugins: [],
}

export default config
""")

w("postcss.config.js", """
module.exports = { plugins: { tailwindcss: {}, autoprefixer: {} } }
""")

w("next.config.mjs", """
/** @type {import('next').NextConfig} */
const nextConfig = {}
export default nextConfig
""")

w(".gitignore", """
node_modules/
.next/
out/
.env
.env.local
.DS_Store
npm-debug.log*
""")

# ── Global CSS ───────────────────────────────────────────────────────

w("src/app/globals.css", """
@tailwind base;
@tailwind components;
@tailwind utilities;

html { scroll-behavior: smooth; }

body {
  background: #0d0d0d;
  color: #e2e8f0;
  -webkit-font-smoothing: antialiased;
}

::selection {
  background: rgba(99, 102, 241, 0.2);
  color: #a5b4fc;
}

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0d0d0d; }
::-webkit-scrollbar-thumb { background: #222; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #333; }
""")

# ── Root layout ──────────────────────────────────────────────────────

w("src/app/layout.tsx", """
import type { Metadata } from 'next'
import { Inter, JetBrains_Mono } from 'next/font/google'
import './globals.css'
import Spotlight from '@/components/Spotlight'

const inter = Inter({ subsets: ['latin'], variable: '--font-inter', display: 'swap' })
const mono  = JetBrains_Mono({ subsets: ['latin'], variable: '--font-mono', display: 'swap' })

export const metadata: Metadata = {
  title: 'Hlib Pakhomov',
  description:
    'CS student at University of Warwick. Aspiring software developer. Former Ukraine national team karate athlete.',
  openGraph: {
    title: 'Hlib Pakhomov',
    description: 'CS Student at Warwick. Building things with Python.',
    type: 'website',
  },
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} ${mono.variable}`}>
      <body className="font-sans bg-bg text-[#e2e8f0]">
        <Spotlight />
        {children}
      </body>
    </html>
  )
}
""")

# ── Components ───────────────────────────────────────────────────────

w("src/components/Spotlight.tsx", """
'use client'
import { useEffect, useRef } from 'react'

export default function Spotlight() {
  const ref = useRef<HTMLDivElement>(null)
  useEffect(() => {
    const move = (e: MouseEvent) => {
      if (ref.current)
        ref.current.style.background = `radial-gradient(600px at ${e.clientX}px ${e.clientY}px, rgba(99,102,241,0.07), transparent 80%)`
    }
    window.addEventListener('mousemove', move)
    return () => window.removeEventListener('mousemove', move)
  }, [])
  return <div ref={ref} className="pointer-events-none fixed inset-0 z-10" />
}
""")

w("src/components/Nav.tsx", """
'use client'
import { useEffect, useState } from 'react'

const SECTIONS = [
  { id: 'about',     label: 'About' },
  { id: 'education', label: 'Education' },
  { id: 'projects',  label: 'Projects' },
  { id: 'contact',   label: 'Contact' },
]

export default function Nav() {
  const [active, setActive] = useState('about')

  useEffect(() => {
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => { if (e.isIntersecting) setActive(e.target.id) }),
      { rootMargin: '-25% 0px -65% 0px' },
    )
    SECTIONS.forEach(({ id }) => { const el = document.getElementById(id); if (el) io.observe(el) })
    return () => io.disconnect()
  }, [])

  const scrollTo = (id: string) =>
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })

  return (
    <nav className="mt-11 flex flex-col gap-0.5">
      {SECTIONS.map(({ id, label }) => {
        const on = active === id
        return (
          <button key={id} onClick={() => scrollTo(id)}
            className="flex items-center gap-3.5 py-1.5 w-fit group cursor-pointer">
            <span className={`h-px transition-all duration-200 ${on
              ? 'w-12 bg-[#e2e8f0]'
              : 'w-6 bg-[#64748b] group-hover:w-12 group-hover:bg-[#e2e8f0]'}`} />
            <span className={`text-[0.7rem] font-semibold tracking-[0.15em] uppercase transition-colors duration-200 ${on
              ? 'text-[#e2e8f0]'
              : 'text-[#64748b] group-hover:text-[#e2e8f0]'}`}>
              {label}
            </span>
          </button>
        )
      })}
    </nav>
  )
}
""")

w("src/components/Socials.tsx", """
import Link from 'next/link'

const LINKS = [
  {
    label: 'GitHub',
    href: 'https://github.com/pakhomchik2008',
    d: 'M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z',
  },
  {
    label: 'LinkedIn',
    href: 'https://linkedin.com/in/hlibpakhomov',
    d: 'M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z',
  },
  {
    label: 'Email',
    href: 'mailto:hlib.pakhomov@warwick.ac.uk',
    d: 'M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z',
  },
]

export default function Socials() {
  return (
    <div className="flex gap-4 items-center">
      {LINKS.map(({ label, href, d }) => (
        <Link key={label} href={href}
          target={href.startsWith('http') ? '_blank' : undefined}
          rel={href.startsWith('http') ? 'noopener noreferrer' : undefined}
          aria-label={label}
          className="text-[#64748b] hover:text-[#e2e8f0] hover:-translate-y-0.5 transition-all duration-200 flex">
          <svg viewBox="0 0 24 24" className="w-[18px] h-[18px] fill-current">
            <path d={d} />
          </svg>
        </Link>
      ))}
    </div>
  )
}
""")

w("src/components/Tag.tsx", """
export default function Tag({ children }: { children: React.ReactNode }) {
  return (
    <span className="font-mono text-[0.68rem] px-2.5 py-1 rounded-full
      bg-accent-low text-accent border border-accent-mid">
      {children}
    </span>
  )
}
""")

w("src/components/SectionLabel.tsx", """
export default function SectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex items-center gap-3 mb-7">
      <span className="text-[0.7rem] font-semibold tracking-[0.16em] uppercase text-[#64748b]">
        {children}
      </span>
      <span className="flex-1 h-px bg-border max-w-[160px]" />
    </div>
  )
}
""")

w("src/components/BackButton.tsx", """
'use client'
import { useRouter } from 'next/navigation'

export default function BackButton() {
  const router = useRouter()
  return (
    <button onClick={() => router.back()}
      className="inline-flex items-center gap-2 text-[0.72rem] font-semibold
        tracking-[0.12em] uppercase text-[#64748b] hover:text-accent
        hover:-translate-x-1 transition-all duration-200 mb-14">
      ← Back
    </button>
  )
}
""")

# ── Sections ─────────────────────────────────────────────────────────

w("src/components/sections/About.tsx", """
import Link from 'next/link'
import Tag from '@/components/Tag'
import SectionLabel from '@/components/SectionLabel'

const SKILLS = [
  'Python','Git & GitHub','Data Structures','OOP',
  'API Integration','Data Analysis','Algorithms','Matplotlib',
]

export default function About() {
  return (
    <section id="about" className="mb-24 scroll-mt-20">
      <SectionLabel>About</SectionLabel>
      <div className="space-y-3.5 text-[0.9rem] text-[#94a3b8] leading-relaxed max-w-[580px]">
        <p>
          I&apos;m an incoming Computer Science student at the{' '}
          <span className="text-accent">University of Warwick</span>, combining strong
          academic performance with a sports scholarship. Ambitious, driven, and
          focused on building a career in tech.
        </p>
        <p>
          Outside of code I&apos;m a{' '}
          <Link href="/karate"
            className="text-accent border-b border-accent-mid hover:border-accent transition-colors duration-200">
            former Ukraine national team karate athlete
          </Link>{' '}
          — which taught me discipline, pressure management, and how to lead. I also
          coached 20+ children as a martial arts instructor in Kyiv.
        </p>
        <p>
          Currently looking for a{' '}
          <span className="text-[#e2e8f0]">part-time role or summer internship</span> to
          gain hands-on experience and contribute to real projects.
        </p>
      </div>
      <div className="flex flex-wrap gap-2 mt-9">
        {SKILLS.map((s) => <Tag key={s}>{s}</Tag>)}
      </div>
    </section>
  )
}
""")

w("src/components/sections/Education.tsx", """
import SectionLabel from '@/components/SectionLabel'
import Tag from '@/components/Tag'

export default function Education() {
  return (
    <section id="education" className="mb-24 scroll-mt-20">
      <SectionLabel>Education</SectionLabel>
      <div className="divide-y divide-border">
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">University of Warwick</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">2025 — 2026</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">
            International Foundation Programme · Computer Science
          </p>
          <p className="text-[0.8rem] text-[#64748b] mt-1.5 leading-relaxed">
            Pure Maths 80% · Stats &amp; Further Maths 86% · Computer Science 72%
          </p>
        </div>
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">IT Step School Kyiv</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">Secondary</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">Computer Science &amp; Mathematics</p>
          <p className="text-[0.8rem] text-[#64748b] mt-1.5">
            Overall 10.8 / 12 · Mathematics 10 / 12 · Physics 10 / 12
          </p>
        </div>
        <div className="py-5">
          <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">Certifications</span>
          <div className="flex flex-wrap gap-2 mt-2.5">
            <Tag>Claude Code in Action — Anthropic</Tag>
            <Tag>AI Fluency — Anthropic</Tag>
          </div>
        </div>
      </div>
    </section>
  )
}
""")

w("src/components/sections/Projects.tsx", """
import Link from 'next/link'
import SectionLabel from '@/components/SectionLabel'
import Tag from '@/components/Tag'

const PROJECTS = [
  {
    title: 'Digital Divide Research — UK',
    href: '/projects/digital-divide',
    desc: 'Independent analysis of UK broadband inequality 2015–2025. Revealed the divide shifted from an access gap to a performance gap — rural areas are connecting, but to slower infrastructure.',
    tags: ['Python','Matplotlib','Linear Regression','Ofcom Data','Statistics'],
  },
  {
    title: 'Narrative Game — The Emma Chen Case',
    href: '/projects/narrative-game',
    desc: 'Interactive detective story built as team leader and core developer. Designed the heap-based clue-priority system, stack-driven undo mechanic, and dependency graph for clue sequencing.',
    tags: ['Python','OOP','Data Structures','Heap','Stack','Team Lead'],
  },
]

export default function Projects() {
  return (
    <section id="projects" className="mb-24 scroll-mt-20">
      <SectionLabel>Projects</SectionLabel>
      <div className="space-y-1">
        {PROJECTS.map(({ title, href, desc, tags }) => (
          <Link key={href} href={href}
            className="group block p-5 rounded-lg border border-transparent
              hover:bg-surface hover:border-border hover:translate-x-1
              transition-all duration-200 relative overflow-hidden">
            <span className="absolute left-0 top-0 bottom-0 w-0.5 bg-accent
              scale-y-0 group-hover:scale-y-100 transition-transform duration-200 origin-bottom" />
            <div className="flex items-center gap-2 font-semibold text-[0.9rem]
              text-[#e2e8f0] group-hover:text-accent transition-colors duration-200">
              {title}
              <span className="text-sm opacity-0 -translate-x-1
                group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-200">
                ↗
              </span>
            </div>
            <p className="text-[0.83rem] text-[#64748b] mt-2 leading-relaxed">{desc}</p>
            <div className="flex flex-wrap gap-1.5 mt-3">
              {tags.map((t) => <Tag key={t}>{t}</Tag>)}
            </div>
          </Link>
        ))}
      </div>
    </section>
  )
}
""")

w("src/components/sections/Contact.tsx", """
import Link from 'next/link'
import SectionLabel from '@/components/SectionLabel'

const LINKS = [
  { label: 'hlib.pakhomov@warwick.ac.uk', href: 'mailto:hlib.pakhomov@warwick.ac.uk',
    d: 'M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z' },
  { label: 'linkedin.com/in/hlibpakhomov', href: 'https://linkedin.com/in/hlibpakhomov',
    d: 'M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z' },
  { label: 'github.com/pakhomchik2008', href: 'https://github.com/pakhomchik2008',
    d: 'M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z' },
]

export default function Contact() {
  return (
    <section id="contact" className="mb-24 scroll-mt-20">
      <SectionLabel>Contact</SectionLabel>
      <p className="text-[0.875rem] text-[#94a3b8] max-w-[500px] mb-8 leading-relaxed">
        I&apos;m looking for{' '}
        <span className="text-[#e2e8f0]">part-time roles and summer internships</span>.
        If you&apos;re working on interesting problems and think I&apos;d be a good fit,
        I&apos;d love to hear from you.
      </p>
      <div className="flex flex-col gap-3.5">
        {LINKS.map(({ label, href, d }) => (
          <Link key={label} href={href}
            target={href.startsWith('http') ? '_blank' : undefined}
            rel={href.startsWith('http') ? 'noopener noreferrer' : undefined}
            className="inline-flex items-center gap-3 text-[0.875rem] text-[#64748b]
              hover:text-accent hover:translate-x-1 transition-all duration-200 w-fit">
            <svg viewBox="0 0 24 24" className="w-3.5 h-3.5 fill-current flex-shrink-0">
              <path d={d} />
            </svg>
            {label}
          </Link>
        ))}
      </div>
    </section>
  )
}
""")

# ── Main page ────────────────────────────────────────────────────────

w("src/app/page.tsx", """
import Nav from '@/components/Nav'
import Socials from '@/components/Socials'
import About from '@/components/sections/About'
import Education from '@/components/sections/Education'
import Projects from '@/components/sections/Projects'
import Contact from '@/components/sections/Contact'

export default function Home() {
  return (
    <div className="max-w-[1180px] mx-auto lg:grid lg:grid-cols-[350px_1fr] min-h-screen">
      <aside className="lg:sticky lg:top-0 lg:h-screen flex flex-col justify-between
        py-16 px-8 lg:px-10">
        <div>
          <h1 className="text-[2.1rem] font-bold tracking-tight leading-tight text-white">
            Hlib<br />Pakhomov
          </h1>
          <p className="text-[0.875rem] font-medium text-accent mt-2 tracking-wide">
            CS Student · Warwick
          </p>
          <p className="text-[0.825rem] text-[#64748b] mt-3.5 leading-relaxed max-w-[210px]">
            Building software and solving real problems. Former national team athlete.
          </p>
          <Nav />
        </div>
        <Socials />
      </aside>
      <main className="py-16 px-8 lg:px-0 lg:pr-14 pb-32">
        <About />
        <Education />
        <Projects />
        <Contact />
      </main>
    </div>
  )
}
""")

# ── Research page ────────────────────────────────────────────────────

w("src/app/projects/digital-divide/page.tsx", """
import type { Metadata } from 'next'
import BackButton from '@/components/BackButton'
import Tag from '@/components/Tag'

export const metadata: Metadata = {
  title: 'Digital Divide Research | Hlib Pakhomov',
  description: 'How has internet connectivity changed in the UK from 2015 to 2025?',
}

function Finding({ stat, children }: { stat: string; children: React.ReactNode }) {
  return (
    <div className="bg-surface border border-border rounded-lg p-5 my-6 border-l-2"
      style={{ borderLeftColor: '#6366f1' }}>
      <p className="font-mono text-[0.8rem] text-accent mb-2">{stat}</p>
      <p className="text-[0.875rem] text-[#94a3b8] leading-relaxed">{children}</p>
    </div>
  )
}

function ChartWrap({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="bg-surface border border-border rounded-lg p-5 my-6">
      <p className="text-[0.72rem] font-semibold tracking-widest uppercase text-[#64748b] mb-4">
        {title}
      </p>
      {children}
    </div>
  )
}

const LP = { fill: 'none', strokeWidth: 2.2, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const }
const GRID = { stroke: '#222', strokeWidth: 0.5, strokeDasharray: '4,4' }
const AXIS = { stroke: '#333', strokeWidth: 1 }
const YRS  = ['2015','2017','2019','2021','2023','2025']

export default function DigitalDivide() {
  return (
    <div className="max-w-[780px] mx-auto px-6 md:px-10 py-14 pb-32">
      <BackButton />
      <h1 className="text-[2.2rem] font-bold tracking-tight leading-tight text-white">
        How has internet connectivity changed in the UK from 2015 to 2025?
      </h1>
      <p className="text-[0.9rem] text-accent font-medium mt-2.5">
        Digital Divide Research · University of Warwick, 2025
      </p>
      <div className="flex flex-wrap gap-2 mt-4">
        {['Python','Matplotlib','Ofcom Data','Linear Regression','Pearson r'].map((t) => <Tag key={t}>{t}</Tag>)}
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Overview</h2>
      <div className="space-y-3.5 text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        <p>Internet access has become central to work, education and public services in
        the UK since 2015. Government policy framed the &ldquo;digital divide&rdquo; as
        a coverage problem. This research asks a harder question: has the divide actually
        closed, or has it simply changed shape?</p>
        <p>Using public datasets from Ofcom Connected Nations Reports (2015&ndash;2025)
        and the House of Commons Library, the analysis revealed a counterintuitive paradox:{' '}
        <strong className="text-[#e2e8f0]">as rural coverage improved dramatically, the
        performance gap widened to its largest ever level.</strong></p>
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Finding 1 — Urban–Rural Speed Gap</h2>
      <Finding stat="r(9) = .881, p = .015 — statistically significant (H₀ rejected)">
        Strong positive correlation between year and urban–rural median download speed gap.
        Gap widened from 22 Mbit/s in 2015 to 190 Mbit/s in 2025, even as rural FTTP coverage
        rose from under 5% to over 60%.
      </Finding>
      <ChartWrap title="Urban vs Rural median download speed (Mbit/s)">
        <svg viewBox="0 0 560 230" style={{ width: '100%', overflow: 'visible' }}>
          <defs>
            <linearGradient id="ug" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#6366f1" stopOpacity="0.12" />
              <stop offset="100%" stopColor="#6366f1" stopOpacity="0" />
            </linearGradient>
          </defs>
          <style>{`.cl{font-family:var(--font-mono,monospace);font-size:9px;fill:#64748b}`}</style>
          <line x1="60" y1="200" x2="540" y2="200" {...AXIS} />
          <line x1="60" y1="20"  x2="60"  y2="200" {...AXIS} />
          {[140,80,20].map(y => <line key={y} x1="60" y1={y} x2="540" y2={y} {...GRID} />)}
          <text className="cl" x="52" y="204" textAnchor="end">0</text>
          <text className="cl" x="52" y="143" textAnchor="end">100</text>
          <text className="cl" x="52" y="83"  textAnchor="end">200</text>
          <text className="cl" x="52" y="23"  textAnchor="end">300</text>
          {YRS.map((yr,i) => <text key={yr} className="cl" x={60+i*96} y="216" textAnchor="middle">{yr}</text>)}
          <polygon fill="url(#ug)" points="60,179 108,174.8 156,168.8 204,162.8 252,156.8 300,153.2 348,155 396,137 444,104 492,62 540,23 540,200 60,200" />
          <polyline {...LP} stroke="#6366f1" points="60,179 108,174.8 156,168.8 204,162.8 252,156.8 300,153.2 348,155 396,137 444,104 492,62 540,23" />
          <polyline {...LP} stroke="#94a3b8" strokeDasharray="6,3" points="60,192.2 108,190.4 156,189.2 204,188 252,186.8 300,185.6 348,186.8 396,182 444,167 492,149 540,137" />
          <circle cx="60"  cy="179"   r="3" fill="#6366f1" /><circle cx="540" cy="23"  r="4" fill="#6366f1" />
          <circle cx="60"  cy="192.2" r="3" fill="#94a3b8" /><circle cx="540" cy="137" r="3" fill="#94a3b8" />
          <text className="cl" x="68"  y="176" fill="#6366f1">35</text>
          <text className="cl" x="510" y="19"  fill="#6366f1">295</text>
          <text className="cl" x="510" y="134" fill="#94a3b8">105</text>
        </svg>
        <div className="flex flex-wrap gap-4 mt-3">
          {[['#6366f1','Urban median speed'],['#94a3b8','Rural median speed']].map(([c,l]) => (
            <div key={l} className="flex items-center gap-1.5 text-[0.72rem] text-[#64748b]">
              <span className="w-2.5 h-2.5 rounded-full inline-block" style={{ background: c }} />{l}
            </div>
          ))}
        </div>
      </ChartWrap>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Finding 2 — Full-Fibre Rollout by UK Nation</h2>
      <Finding stat="r(9) = .548, p = .081 — not significant (H₀ accepted)">
        No statistically significant change in between-nation FTTP variation overall, but
        trajectories diverged sharply from 2020: Northern Ireland reached 95% by 2025 while
        Scotland lagged at 71%.
      </Finding>
      <ChartWrap title="Full-fibre (FTTP) availability by UK nation (% of premises)">
        <svg viewBox="0 0 560 230" style={{ width: '100%', overflow: 'visible' }}>
          <style>{`.cl{font-family:var(--font-mono,monospace);font-size:9px;fill:#64748b}`}</style>
          <line x1="60" y1="200" x2="540" y2="200" {...AXIS} />
          <line x1="60" y1="20"  x2="60"  y2="200" {...AXIS} />
          {[146,92,38].map(y => <line key={y} x1="60" y1={y} x2="540" y2={y} {...GRID} />)}
          <text className="cl" x="52" y="204" textAnchor="end">0%</text>
          <text className="cl" x="52" y="149" textAnchor="end">30%</text>
          <text className="cl" x="52" y="95"  textAnchor="end">60%</text>
          <text className="cl" x="52" y="41"  textAnchor="end">90%</text>
          {YRS.map((yr,i) => <text key={yr} className="cl" x={60+i*96} y="216" textAnchor="middle">{yr}</text>)}
          <polyline {...LP} stroke="#6366f1" points="60,199.6 108,199.1 156,198.2 204,196.4 252,191 300,182 348,173 396,146 444,101 492,77.6 540,63.2" />
          <polyline {...LP} stroke="#34d399" points="60,199.8 108,199.6 156,199.1 204,198.2 252,194.6 300,185.6 348,164 396,119 444,74 492,47 540,29" />
          <polyline {...LP} stroke="#f59e0b" strokeDasharray="5,3" points="60,199.8 108,199.5 156,198.6 204,197.3 252,194.6 300,187.4 348,178.4 396,160.4 444,128 492,95.6 540,72.2" />
          <polyline {...LP} stroke="#94a3b8" strokeDasharray="3,3" points="60,199.8 108,199.6 156,199.1 204,198.2 252,195.5 300,191 348,183.8 396,167.6 444,137 492,106.4 540,79.4" />
          <circle cx="540" cy="29"   r="4" fill="#34d399" />
          <circle cx="540" cy="63.2" r="3" fill="#6366f1" />
          <circle cx="540" cy="72.2" r="3" fill="#f59e0b" />
          <circle cx="540" cy="79.4" r="3" fill="#94a3b8" />
          <text className="cl" x="492" y="24" fill="#34d399">95%</text>
        </svg>
        <div className="flex flex-wrap gap-4 mt-3">
          {[['#6366f1','England (76%)'],['#34d399','N. Ireland (95%)'],['#f59e0b','Scotland (71%)'],['#94a3b8','Wales (67%)']].map(([c,l]) => (
            <div key={l} className="flex items-center gap-1.5 text-[0.72rem] text-[#64748b]">
              <span className="w-2.5 h-2.5 rounded-full inline-block" style={{ background: c }} />{l}
            </div>
          ))}
        </div>
      </ChartWrap>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Finding 3 — UK Average Download Speed</h2>
      <Finding stat="28.9 Mbit/s (2015) → 285 Mbit/s (2025) — S-curve growth">
        Consistent upward trend matching Oughton et al. (2021)&apos;s S-curve prediction. A slight
        dip in 2020–21 due to COVID-19, then sharp acceleration after 2022 as FTTP rollout expanded.
      </Finding>
      <ChartWrap title="UK average fixed-line download speed (Mbit/s)">
        <svg viewBox="0 0 560 230" style={{ width: '100%', overflow: 'visible' }}>
          <defs>
            <linearGradient id="sg" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#6366f1" stopOpacity="0.18" />
              <stop offset="100%" stopColor="#6366f1" stopOpacity="0" />
            </linearGradient>
          </defs>
          <style>{`.cl{font-family:var(--font-mono,monospace);font-size:9px;fill:#64748b}`}</style>
          <polygon fill="url(#sg)" points="60,182.7 108,178.4 156,172.4 204,167.6 252,161.6 300,159.2 348,161 396,146 444,107 492,68 540,29 540,200 60,200" />
          <line x1="60" y1="200" x2="540" y2="200" {...AXIS} />
          <line x1="60" y1="20"  x2="60"  y2="200" {...AXIS} />
          {[140,80,20].map(y => <line key={y} x1="60" y1={y} x2="540" y2={y} {...GRID} />)}
          <text className="cl" x="52" y="204" textAnchor="end">0</text>
          <text className="cl" x="52" y="143" textAnchor="end">100</text>
          <text className="cl" x="52" y="83"  textAnchor="end">200</text>
          <text className="cl" x="52" y="23"  textAnchor="end">300</text>
          {YRS.map((yr,i) => <text key={yr} className="cl" x={60+i*96} y="216" textAnchor="middle">{yr}</text>)}
          <polyline {...LP} stroke="#6366f1" strokeWidth={2.5} points="60,182.7 108,178.4 156,172.4 204,167.6 252,161.6 300,159.2 348,161 396,146 444,107 492,68 540,29" />
          <circle cx="60"  cy="182.7" r="3.5" fill="#6366f1" />
          <circle cx="540" cy="29"    r="4"   fill="#6366f1" />
          <text className="cl" x="68"  y="179" fill="#6366f1">28.9</text>
          <text className="cl" x="510" y="25"  fill="#6366f1">285</text>
        </svg>
      </ChartWrap>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Conclusion</h2>
      <div className="space-y-3.5 text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        <p>The UK digital divide has{' '}
        <strong className="text-[#e2e8f0]">not closed</strong> — it has shifted from an access
        gap to a performance and regional quality gap. Rural premises are increasingly connected,
        but to lower-tier services, widening the speed gap.</p>
        <p>Policy should pivot from coverage targets to{' '}
        <strong className="text-[#e2e8f0]">speed-parity and regional equity</strong>. Future
        research should incorporate affordability and digital skills data, which nation-level
        Ofcom reporting cannot capture.</p>
      </div>
    </div>
  )
}
""")

# ── Narrative game page ──────────────────────────────────────────────

w("src/app/projects/narrative-game/page.tsx", """
import type { Metadata } from 'next'
import BackButton from '@/components/BackButton'
import Tag from '@/components/Tag'

export const metadata: Metadata = {
  title: 'Narrative Game | Hlib Pakhomov',
  description: 'Interactive detective story — The Emma Chen Case.',
}

function Card({ icon, title, desc }: { icon: string; title: string; desc: string }) {
  return (
    <div className="flex gap-4 p-4 bg-surface border border-border rounded-lg">
      <div className="w-9 h-9 rounded-md bg-accent-low flex items-center justify-center text-base flex-shrink-0">
        {icon}
      </div>
      <div>
        <p className="text-[0.875rem] font-semibold text-[#e2e8f0]">{title}</p>
        <p className="text-[0.8rem] text-[#64748b] mt-1 leading-relaxed">{desc}</p>
      </div>
    </div>
  )
}

export default function NarrativeGame() {
  return (
    <div className="max-w-[780px] mx-auto px-6 md:px-10 py-14 pb-32">
      <BackButton />
      <h1 className="text-[2.2rem] font-bold tracking-tight leading-tight text-white">
        The Emma Chen Case
      </h1>
      <p className="text-[0.9rem] text-accent font-medium mt-2.5">
        Interactive Narrative Game · Group Project · Python
      </p>
      <div className="flex flex-wrap gap-2 mt-4">
        {['Python','OOP','Data Structures','Heap','Stack','Graph','Team Lead'].map((t) => <Tag key={t}>{t}</Tag>)}
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Overview</h2>
      <div className="space-y-3.5 text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        <p>An interactive story where the player — journalist{' '}
        <strong className="text-[#e2e8f0]">Emma Chen</strong> — investigates the suspicious
        death of Victor Harlan. Built as a group project where I served as core developer
        and team leader.</p>
        <p>The focus:{' '}
        <strong className="text-[#e2e8f0]">gameplay logic, structural design, and clean
        maintainable code</strong>. Every mechanic is backed by a real data structure
        chosen for the right algorithmic reason.</p>
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-4">Technical Architecture</h2>
      <div className="space-y-2.5">
        <Card icon="△" title="Heap-based clue priority system"
          desc="A min-heap surfaces the most relevant clue at any moment. Priority adapts dynamically as new evidence is uncovered — O(log n) insertion and extraction." />
        <Card icon="↩" title="Stack-driven undo / rewind mechanic"
          desc="Every player action is pushed to a stack. Rewinding pops it, restoring exact prior state. Clean O(1) undo without copying the full game tree." />
        <Card icon="⬡" title="Dependency graph for clue sequencing"
          desc="A directed graph ensures clues unlock in the correct narrative order. Topological sort prevents the player accessing later evidence before prerequisites are met." />
        <Card icon="▭" title="Pop-up window system"
          desc="Designed and built the windowed UI layer: evidence panels, clue inspection pop-ups, and in-game notification dialogs." />
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">My Role</h2>
      <p className="text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        As team leader I coordinated the group&apos;s work, reviewed all code before merging,
        and set the structural conventions the team followed. As core developer I owned the
        data structure layer end-to-end.
      </p>
    </div>
  )
}
""")

# ── Karate page ──────────────────────────────────────────────────────

w("src/app/karate/page.tsx", """
import type { Metadata } from 'next'
import BackButton from '@/components/BackButton'

export const metadata: Metadata = {
  title: 'Karate | Glib Pakhomov',
  description: 'Former Ukraine national team karate athlete.',
}

function Achievement({ icon, title, desc }: { icon: string; title: string; desc: string }) {
  return (
    <div className="flex gap-4 p-4 bg-surface border border-border rounded-lg">
      <div className="w-9 h-9 rounded-md bg-accent-low flex items-center justify-center text-base flex-shrink-0">
        {icon}
      </div>
      <div>
        <p className="text-[0.875rem] font-semibold text-[#e2e8f0]">{title}</p>
        <p className="text-[0.8rem] text-[#64748b] mt-1 leading-relaxed">{desc}</p>
      </div>
    </div>
  )
}

const GALLERY = [
  'Competition','National team','Medal ceremony',
  'Training session','Coaching kids','Team photo',
]

export default function Karate() {
  return (
    <div className="max-w-[780px] mx-auto px-6 md:px-10 py-14 pb-32">
      <BackButton />
      <h1 className="text-[2.2rem] font-bold tracking-tight leading-tight text-white">
        Karate
      </h1>
      <p className="text-[0.9rem] text-accent font-medium mt-2.5">
        Former Ukraine National Team Athlete
      </p>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">My Story</h2>
      <div className="space-y-3.5 text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        <p>I started karate as a child and eventually competed at national level for Ukraine.
        Sport at that level demands discipline, focus under pressure, and relentless iterative
        improvement — the same qualities I now apply directly to software.</p>
        <p>When a routine fails in competition you don&apos;t have time to panic. You adapt,
        execute the next move, and reflect afterwards. That feedback loop is identical to
        software engineering: write, run, debug, improve.</p>
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Gallery</h2>
      <p className="text-[0.78rem] text-[#64748b] mb-4">
        Add your photos here — competitions, training, team shots, coaching sessions.
      </p>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-2.5">
        {GALLERY.map((caption) => (
          <div key={caption}
            className="aspect-[4/3] bg-surface border border-dashed border-border rounded-lg
              flex flex-col items-center justify-center gap-2 text-[#2d3748]
              text-[0.72rem] text-center p-3 cursor-pointer
              hover:border-accent-mid hover:text-[#64748b] transition-all duration-200">
            <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current opacity-30">
              <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z" />
            </svg>
            {caption}
          </div>
        ))}
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-4">Achievements</h2>
      <div className="space-y-2.5">
        <Achievement icon="🇺🇦" title="Ukraine National Team"
          desc="Selected to represent Ukraine at national level in competitive karate" />
        <Achievement icon="🥋" title="Martial Arts Instructor — Kyiv"
          desc="Coached 20+ children aged 6–12, planning and leading structured weekly training sessions" />
        <Achievement icon="🏆" title="Sports Scholarship — University of Warwick"
          desc="Awarded a sports scholarship alongside academic admission to Warwick's CS programme" />
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">What It Taught Me</h2>
      <div className="space-y-3.5 text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        <p>Elite sport teaches you to{' '}
        <strong className="text-[#e2e8f0]">fail fast and iterate</strong>. You lose a match,
        you analyse what went wrong, and you fix it before the next one. That&apos;s the same
        loop as debugging software.</p>
        <p>Coaching children added something different: the ability to{' '}
        <strong className="text-[#e2e8f0]">explain complex ideas simply</strong>, stay patient
        under pressure, and lead a group toward a shared goal — skills that transfer directly to
        team projects and technical communication.</p>
      </div>
    </div>
  )
}
""")

# ── public/.gitkeep ──────────────────────────────────────────────────
w("public/.gitkeep", "")

# ── npm install ──────────────────────────────────────────────────────
print()
print("Running npm install (≈30s)...")
try:
    r = subprocess.run(["npm", "install"], cwd=ROOT, capture_output=True, text=True, timeout=180)
    if r.returncode == 0:
        print("  ✓  npm install done")
    else:
        print("  ✗  npm install failed — run it manually inside hlib-portfolio/")
        if r.stderr:
            print(r.stderr[:500])
        sys.exit(1)
except FileNotFoundError:
    print("  ✗  npm not found — install Node.js first, then run: cd hlib-portfolio && npm install")
    sys.exit(1)
except Exception as e:
    print(f"  ✗  {e}")
    sys.exit(1)

print()
print("=" * 52)
print(f"  Project:  {ROOT}")
print()
print("Starting dev server at http://localhost:3000 ...")
print("  (press Ctrl+C to stop)")
print("=" * 52)

def _open_when_ready():
    for _ in range(60):
        time.sleep(1)
        try:
            urllib.request.urlopen("http://localhost:3000", timeout=1)
            webbrowser.open("http://localhost:3000")
            return
        except Exception:
            pass

threading.Thread(target=_open_when_ready, daemon=True).start()
subprocess.run(["npm", "run", "dev"], cwd=ROOT)
