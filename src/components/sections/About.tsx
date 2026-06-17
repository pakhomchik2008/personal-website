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
            className="text-accent underline underline-offset-2 decoration-accent/40
              hover:decoration-accent transition-colors duration-200 inline-flex items-baseline gap-0.5">
            former Ukraine national team karate athlete
            <span className="text-[0.7rem] leading-none">↗</span>
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
