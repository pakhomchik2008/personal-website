import Image from 'next/image'
import Link from 'next/link'
import Tag from '@/components/Tag'
import SectionLabel from '@/components/SectionLabel'

const SKILLS = [
  'Python','Git & GitHub','Data Structures',
  'API Integration','Data Analysis','Matplotlib',
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
      <div className="mt-8 w-[200px]">
        <div className="rounded-lg overflow-hidden border border-border" style={{ aspectRatio: '210 / 297' }}>
          <Image src="/photo-1.jpg" alt="Hlib in the mountains" width={3024} height={4032}
            className="w-full h-full object-cover object-center" />
        </div>
      </div>
      <div className="flex flex-wrap gap-2 mt-7">
        {SKILLS.map((s) => <Tag key={s}>{s}</Tag>)}
      </div>
      <a href="/resume.pdf" download
        className="mt-6 inline-flex items-center gap-2
          px-5 py-2.5 rounded-lg
          text-[0.8rem] font-semibold text-[#fca5a5]
          border border-[#7f1d1d]/60 bg-[#7f1d1d]/20
          hover:bg-[#7f1d1d]/40 hover:border-[#ef4444]/50
          transition-all duration-200">
        <svg viewBox="0 0 24 24" className="w-3.5 h-3.5 fill-current flex-shrink-0">
          <path d="M12 16l-6-6h4V4h4v6h4l-6 6zm-6 2h12v2H6v-2z"/>
        </svg>
        Download Résumé
      </a>
    </section>
  )
}
