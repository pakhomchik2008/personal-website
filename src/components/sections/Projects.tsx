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
