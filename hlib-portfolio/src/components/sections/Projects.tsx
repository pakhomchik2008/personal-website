import Link from 'next/link'
import SectionLabel from '@/components/SectionLabel'
import Tag from '@/components/Tag'

const PROJECTS = [
  {
    title: "Whispers at Victor's Manor",
    href: '/projects/narrative-game',
    summary: 'Problem: build a branching mystery game from scratch. Solution: heap-based clue engine, stack-driven undo, and a 40-scene narrative in Python.',
    desc: 'Desktop mystery game built as team lead and core developer. Implements custom data structures, OOP architecture, and a tkinter GUI with a live evidence panel.',
    tags: ['Python', 'tkinter', 'Data Structures', 'Team Lead'],
    codeHref: '/whispers-at-victors-manor.py',
    codeLabel: 'Source (.py)',
  },
]

export default function Projects() {
  return (
    <section id="projects" className="mb-24 scroll-mt-20">
      <SectionLabel>Projects</SectionLabel>
      <div className="space-y-4">
        {PROJECTS.map(({ title, href, summary, desc, tags, codeHref, codeLabel }) => (
          <div key={href}
            className="bg-surface border border-border rounded-lg overflow-hidden
              hover:border-accent/30 transition-colors duration-200">
            <div className="p-5">
              <p className="text-[0.7rem] font-mono text-accent mb-2 leading-relaxed">{summary}</p>
              <Link href={href}
                className="group inline-flex items-center gap-1.5 font-semibold text-[0.9rem]
                  text-[#e2e8f0] hover:text-accent transition-colors duration-200">
                {title}
                <span className="opacity-0 -translate-x-1 group-hover:opacity-100 group-hover:translate-x-0
                  transition-all duration-200 text-sm">↗</span>
              </Link>
              <p className="text-[0.83rem] text-[#64748b] mt-1.5 leading-relaxed">{desc}</p>
              <div className="flex flex-wrap gap-1.5 mt-3">
                {tags.map((t) => <Tag key={t}>{t}</Tag>)}
              </div>
              <div className="flex gap-2 mt-4">
                <Link href={href}
                  className="px-3.5 py-1.5 rounded-md text-[0.75rem] font-semibold
                    bg-accent text-white hover:bg-accent/80 transition-colors duration-200">
                  View Project
                </Link>
                <a href={codeHref} download
                  className="px-3.5 py-1.5 rounded-md text-[0.75rem] font-semibold
                    border border-border text-[#94a3b8] hover:text-[#e2e8f0] hover:border-[#e2e8f0]/20
                    transition-colors duration-200">
                  {codeLabel}
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}
