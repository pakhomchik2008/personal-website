import type { Metadata } from 'next'
import BackButton from '@/components/BackButton'

export const metadata: Metadata = {
  title: 'Karate | Hlib Pakhomov',
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
