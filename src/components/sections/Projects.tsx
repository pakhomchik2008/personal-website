import Link from 'next/link'
import SectionLabel from '@/components/SectionLabel'
import Tag from '@/components/Tag'

const PROJECTS = [
  {
    title: 'Examik',
    href: '/projects/examik',
    summary: 'Problem: exam material existed, but nothing clearly explained why an answer was wrong. Solution: an AI exam-prep platform with live subscriptions.',
    desc: 'Solo-founded, live product covering 5+ core syllabuses (A levels, GCSE, SAT and more). Built end-to-end with AI-assisted development (Claude Code, Cursor), ~977 automated tests. Supabase backend on Vercel, Stripe and RevenueCat subscriptions, iOS build via Capacitor.',
    tags: ['AI', 'Supabase', 'Vercel', 'Stripe', 'RevenueCat', 'Capacitor'],
    liveHref: 'https://examik.net',
  },
  {
    title: 'Internet Divide in the UK, 2015–2025',
    href: '/projects/digital-divide',
    summary: 'Problem: does the UK digital divide still exist? Solution: independent data analysis across urban/rural areas and the 4 UK nations.',
    desc: 'Independent research on digital inequality. Python for data processing and Matplotlib for the trends; distinction awarded and findings presented to ~500 peers and teachers.',
    tags: ['Python', 'Matplotlib', 'Data Analysis', 'Research'],
    showDetail: true,
  },
  {
    title: 'Flat-Matcher',
    href: '/projects/flatmate-matcher',
    summary: 'Problem: finding compatible flatmates at university. Solution: a weighted 10-question quiz that scores lifestyle compatibility from 0 to 100.',
    desc: 'Full-stack web app that pairs UK university students with compatible flatmates. Helped ~100 UK students find their flatmates. Features real-time messaging, profile management, and a guest demo mode.',
    tags: ['TypeScript', 'Full-Stack', 'Matching Algorithm'],
    githubHref: 'https://github.com/pakhomchik2008/flatmate-matcher',
    liveHref: 'https://www.flat-matcher.com',
  },
  {
    title: "Whispers at Victor's Manor",
    href: '/projects/narrative-game',
    summary: 'Problem: build a branching mystery game from scratch. Solution: heap-based clue engine, stack-driven undo, and a 40-scene narrative in Python.',
    desc: 'University course group project (team of 4): built as team lead and core developer, covering ~30 Python topics. High distinction; second best project in the group. Implements custom data structures, OOP architecture, and a tkinter GUI with a live evidence panel.',
    tags: ['Python', 'tkinter', 'Data Structures', 'Team Lead'],
    codeHref: '/whispers-at-victors-manor.py',
    codeLabel: 'Source (.py)',
    githubHref: 'https://github.com/1wuzhengjiang1/group-project',
    showDetail: true,
  },
  {
    title: 'AI Exam Coach',
    href: '/projects/ai-exam-coach',
    summary: 'AI-driven exam prep coach that builds a personalised revision plan and adapts it as you study.',
    desc: 'Generates day-by-day exam prep schedules based on topic difficulty and daily time, with an AI tutor layer for guidance. Tracks streaks, progress, and auto-reschedules when you fall behind. Built with Next.js, Supabase, and Claude.',
    tags: ['TypeScript', 'Next.js', 'Supabase', 'AI', 'In Development'],
    liveHref: 'https://ai-exam-coach-v2.vercel.app',
    inProgress: true,
  },
  {
    title: 'LnkRise',
    href: '/projects/lnkrise',
    summary: 'AI-powered LinkedIn growth coach — turns raw post performance into a concrete content strategy.',
    desc: 'SaaS that analyses your LinkedIn analytics and coaches you on what to post next, with a confirm-then-post publishing flow (no auto-posting). Built with Next.js, Postgres/Prisma, and Claude.',
    tags: ['TypeScript', 'Next.js', 'Postgres', 'AI', 'In Development'],
    inProgress: true,
  },
]

export default function Projects() {
  return (
    <section id="projects" className="mb-24 scroll-mt-20">
      <SectionLabel>Projects</SectionLabel>
      <div className="space-y-4">
        {PROJECTS.map(({ title, href, summary, desc, tags, codeHref, codeLabel, githubHref, liveHref, inProgress, showDetail }) => (
          <div key={href}
            className="bg-surface border border-border rounded-lg overflow-hidden
              hover:border-accent/30 transition-colors duration-200">
            <div className="p-5">
              <p className="text-[0.7rem] font-mono text-accent mb-2 leading-relaxed">{summary}</p>
              <div className="flex items-center gap-2 mt-1 mb-1">
                <p className="font-bold text-[1.05rem] text-white">{title}</p>
                {inProgress && (
                  <span className="px-2 py-0.5 rounded-full text-[0.65rem] font-semibold
                    bg-yellow-500/15 text-yellow-400 border border-yellow-500/30">
                    In Development
                  </span>
                )}
              </div>
              <p className="text-[0.83rem] text-[#64748b] mt-1.5 leading-relaxed">{desc}</p>
              <div className="flex flex-wrap gap-1.5 mt-3">
                {tags.map((t) => <Tag key={t}>{t}</Tag>)}
              </div>
              <div className="flex gap-2 mt-4">
                {showDetail && (
                  <Link href={href}
                    className="px-3.5 py-1.5 rounded-md text-[0.75rem] font-semibold
                      bg-accent text-white hover:bg-accent/80 transition-colors duration-200">
                    View Project
                  </Link>
                )}
                {liveHref && (
                  <a href={liveHref} target="_blank" rel="noopener noreferrer"
                    className="px-3.5 py-1.5 rounded-md text-[0.75rem] font-semibold
                      bg-accent text-white hover:bg-accent/80 transition-colors duration-200">
                    Live Site ↗
                  </a>
                )}
                {githubHref && (
                  <a href={githubHref} target="_blank" rel="noopener noreferrer"
                    className="px-3.5 py-1.5 rounded-md text-[0.75rem] font-semibold
                      border border-border text-[#94a3b8] hover:text-[#e2e8f0] hover:border-[#e2e8f0]/20
                      transition-colors duration-200">
                    GitHub ↗
                  </a>
                )}
                {codeHref && (
                  <a href={codeHref} download
                    className="px-3.5 py-1.5 rounded-md text-[0.75rem] font-semibold
                      border border-border text-[#94a3b8] hover:text-[#e2e8f0] hover:border-[#e2e8f0]/20
                      transition-colors duration-200">
                    {codeLabel}
                  </a>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}
