import type { Metadata } from 'next'
import Image from 'next/image'
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
  { src: '/karate/img_1456.jpg', caption: 'Competition' },
  { src: '/karate/img_1778.jpg', caption: 'Training session' },
  { src: '/karate/img_2431.jpg', caption: 'Coaching kids' },
  { src: '/karate/img_3764.jpg', caption: 'National team' },
  { src: '/karate/img_4866.jpg', caption: 'Medal ceremony' },
  { src: '/karate/img_7452.jpg', caption: 'Team photo' },
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
      <div className="grid grid-cols-2 md:grid-cols-3 gap-2.5">
        {GALLERY.map(({ src, caption }) => (
          <div key={src} className="group relative aspect-[4/3] overflow-hidden rounded-lg bg-surface">
            <Image
              src={src}
              alt={caption}
              fill
              className="object-cover transition-transform duration-300 group-hover:scale-105"
              sizes="(max-width: 768px) 50vw, 33vw"
            />
            <div className="absolute inset-0 bg-black/0 group-hover:bg-black/30 transition-colors duration-300" />
            <span className="absolute bottom-2 left-2.5 text-[0.7rem] font-medium text-white
              opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              {caption}
            </span>
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
