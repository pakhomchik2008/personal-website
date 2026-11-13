import SectionLabel from '@/components/SectionLabel'

const ITEMS = [
  {
    title: 'Course Representative — Computer Systems Engineering',
    org: 'University of Warwick',
    date: 'Oct 2026 — Present',
    desc: 'Represent ~120 students; work with ~50 academics to raise satisfaction and attendance and resolve issues.',
  },
  {
    title: "Children's Karate Coach & Mentor",
    org: 'Coventry, UK',
    date: '2025 — Present',
    desc: 'Coach a weekly group of ~20 children, giving individual feedback every session. Brought 10 athletes to international level.',
  },
  {
    title: 'IB Maths Tutor',
    org: 'Private tutoring',
    date: '2025 — Present',
    desc: 'Private tutor for IB students in Mathematics.',
  },
  {
    title: 'National Team Karate Captain',
    org: '2024 European Karate Championships',
    date: '2024',
    desc: 'Team captain; the team finished 2nd in the overall medal table.',
  },
  {
    title: 'Math Olympiads',
    org: '2nd Place, Mathcounts (national) · 1st Place, German District Olympiad',
    date: '2019',
    desc: '',
  },
]

export default function Experience() {
  return (
    <section id="experience" className="mb-24 scroll-mt-20">
      <SectionLabel>Experience</SectionLabel>
      <div className="divide-y divide-border">
        {ITEMS.map(({ title, org, date, desc }) => (
          <div key={title} className="py-5">
            <div className="flex justify-between items-baseline gap-3 flex-wrap">
              <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">{title}</span>
              <span className="font-mono text-[0.75rem] text-[#64748b]">{date}</span>
            </div>
            <p className="text-[0.825rem] text-accent mt-0.5">{org}</p>
            {desc && <p className="text-[0.83rem] text-[#64748b] mt-1.5 leading-relaxed">{desc}</p>}
          </div>
        ))}
      </div>
    </section>
  )
}
