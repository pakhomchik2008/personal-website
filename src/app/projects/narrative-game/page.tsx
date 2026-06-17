import type { Metadata } from 'next'
import BackButton from '@/components/BackButton'
import Tag from '@/components/Tag'

export const metadata: Metadata = {
  title: "Whispers at Victor's Manor | Hlib Pakhomov",
  description: 'A branching narrative mystery game built in Python — FP016 CS group project.',
}

export default function NarrativeGame() {
  return (
    <div className="max-w-[780px] mx-auto px-6 md:px-10 py-14 pb-32">
      <BackButton />
      <h1 className="text-[2.2rem] font-bold tracking-tight leading-tight text-white">
        Whispers at Victor&apos;s Manor
      </h1>
      <p className="text-[0.9rem] text-accent font-medium mt-2.5">
        Branching Narrative Mystery Game · FP016 Computer Science · Group Project · Python
      </p>
      <div className="flex flex-wrap gap-2 mt-4">
        {['Python', 'tkinter', 'OOP', 'Data Structures', 'Graph Algorithms', 'Agile', 'Team Lead'].map(
          (t) => <Tag key={t}>{t}</Tag>
        )}
      </div>

      {/* ── Overview ──────────────────────────────────── */}
      <hr className="border-border my-11" />
      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Overview</h2>
      <div className="space-y-3 text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        <p>
          A desktop mystery game built in Python where the player investigates a suspicious death
          at Victor&apos;s Manor. Choices branch the narrative across 40+ scenes and lead to{' '}
          <strong className="text-[#e2e8f0]">four distinct endings</strong>. Built as a group
          project for FP016 Computer Science, where I served as{' '}
          <strong className="text-[#e2e8f0]">team lead and core systems developer</strong>.
        </p>
        <p>
          The game features a full tkinter GUI with a dark theme, per-scene background images,
          a live evidence panel, and an algorithm analysis dashboard that exposes the underlying
          data structures to the player.
        </p>
      </div>

      {/* ── Technologies & Concepts ───────────────────── */}
      <hr className="border-border my-11" />
      <h2 className="text-base font-semibold text-[#e2e8f0] mb-4">What We Implemented</h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
        {[
          { label: 'Object-Oriented Programming', sub: 'typed classes & inheritance' },
          { label: 'Custom Data Structures', sub: 'Stack · Priority Heap' },
          { label: 'Graph Algorithms', sub: 'DFS · BFS · Topological Sort' },
          { label: 'Branching Narrative Engine', sub: '40+ story nodes · 4 endings' },
          { label: 'tkinter GUI', sub: 'dark theme · tab views · popups' },
          { label: 'Agile Development', sub: 'Scrum-based · 4-person team' },
        ].map(({ label, sub }) => (
          <div key={label} className="bg-surface border border-border rounded-lg px-4 py-3">
            <p className="text-[0.82rem] font-medium text-[#e2e8f0]">{label}</p>
            <p className="text-[0.72rem] text-[#64748b] mt-0.5">{sub}</p>
          </div>
        ))}
      </div>

      {/* ── Team ──────────────────────────────────────── */}
      <hr className="border-border my-11" />
      <h2 className="text-base font-semibold text-[#e2e8f0] mb-4">Team &amp; Responsibilities</h2>
      <div className="space-y-2">
        {[
          {
            name: 'Hlib (me)',
            role: 'Team Lead · Core Systems',
            detail: 'Data structures, rewind system, clue manager, analysis dashboard, evidence panel, team coordination.',
            highlight: true,
          },
          {
            name: 'Wu (ZhengJiang)',
            role: 'Algorithms · Game Engine',
            detail: 'DFS, BFS, insertion sort, topological sort, and the engine driving all game state.',
            highlight: false,
          },
          {
            name: 'Melih',
            role: 'Story Graph',
            detail: 'All 40+ scenes, branching dialogue, clue placements, and four endings.',
            highlight: false,
          },
          {
            name: 'Sylvie',
            role: 'Main GUI · Functions',
            detail: 'Main menu, toolbar, status bar, and supporting utility functions.',
            highlight: false,
          },
        ].map(({ name, role, detail, highlight }) => (
          <div key={name}
            className={`flex gap-4 p-4 rounded-lg border ${highlight ? 'bg-surface border-accent/30' : 'bg-surface border-border'}`}>
            <div className="w-1 rounded-full flex-shrink-0 self-stretch"
              style={{ background: highlight ? '#6366f1' : '#2a2a2a' }} />
            <div>
              <div className="flex items-baseline gap-2 flex-wrap">
                <span className={`text-[0.875rem] font-semibold ${highlight ? 'text-accent' : 'text-[#e2e8f0]'}`}>{name}</span>
                <span className="font-mono text-[0.7rem] text-[#64748b]">{role}</span>
              </div>
              <p className="text-[0.83rem] text-[#64748b] mt-1 leading-relaxed">{detail}</p>
            </div>
          </div>
        ))}
      </div>

      {/* ── What I Built ──────────────────────────────── */}
      <hr className="border-border my-11" />
      <h2 className="text-base font-semibold text-[#e2e8f0] mb-4">What I Built</h2>
      <div className="space-y-3">
        {[
          {
            label: 'Story System',
            desc: 'Designed the object-oriented architecture used to represent and manage 40+ branching story scenes — each scene a typed class guaranteeing consistent structure across the codebase.',
          },
          {
            label: 'Data Structures',
            desc: 'Implemented a custom Stack powering the rewind mechanic (LIFO, O(1) undo) and a Priority Heap for clue management, ensuring the most important evidence always surfaces first.',
          },
          {
            label: 'Analysis Dashboard',
            desc: 'Built an interactive four-tab dashboard visualising DFS reachability, BFS shortest paths to each ending, evidence timelines, and topological clue ordering.',
          },
        ].map(({ label, desc }) => (
          <div key={label}
            className="bg-surface border border-border border-l-2 rounded-lg p-5"
            style={{ borderLeftColor: '#6366f1' }}>
            <p className="text-[0.875rem] font-semibold text-[#e2e8f0] mb-1.5">{label}</p>
            <p className="text-[0.84rem] text-[#64748b] leading-relaxed">{desc}</p>
          </div>
        ))}
      </div>

      {/* ── What I Learned ────────────────────────────── */}
      <hr className="border-border my-11" />
      <h2 className="text-base font-semibold text-[#e2e8f0] mb-4">What I Learned</h2>
      <ul className="space-y-2.5">
        {[
          'Choosing the right data structure can dramatically simplify a problem.',
          'Building and testing components independently improves overall reliability.',
          'Real projects often require learning beyond course material.',
          'Team coordination is as important as technical implementation.',
        ].map((item) => (
          <li key={item} className="flex gap-3 text-[0.875rem] text-[#94a3b8] leading-relaxed">
            <span className="text-accent mt-0.5 flex-shrink-0">—</span>
            {item}
          </li>
        ))}
      </ul>

      {/* ── Downloads ─────────────────────────────────── */}
      <hr className="border-border my-11" />
      <h2 className="text-base font-semibold text-[#e2e8f0] mb-4">Downloads</h2>
      <div className="space-y-3">
        {[
          {
            href: '/narrative-game-report.pdf',
            ext: 'PDF',
            label: 'Technical Report',
            desc: 'Design decisions, implementation details, and testing evidence for the components I built.',
          },
          {
            href: '/whispers-at-victors-manor.py',
            ext: '.PY',
            label: 'Source Code',
            desc: 'Full Python source (~1800 lines). My contributions are Sections 1 and 5, clearly marked in comments. Requires Python 3.12+ and Pillow.',
          },
        ].map(({ href, ext, label, desc }) => (
          <a key={label} href={href} download
            className="flex items-start gap-4 p-4 bg-surface border border-border rounded-lg
              hover:border-accent-mid transition-colors duration-200 group">
            <div className="w-10 h-10 rounded-md bg-accent-low flex items-center justify-center
              text-accent font-mono text-[0.62rem] font-bold flex-shrink-0
              group-hover:bg-accent/15 transition-colors duration-200">
              {ext}
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-[0.875rem] font-semibold text-[#e2e8f0]">{label}</p>
              <p className="text-[0.83rem] text-[#64748b] mt-1 leading-relaxed">{desc}</p>
            </div>
            <span className="text-[#64748b] group-hover:text-[#e2e8f0] transition-colors duration-200 mt-0.5 text-sm flex-shrink-0">↓</span>
          </a>
        ))}
      </div>
    </div>
  )
}
