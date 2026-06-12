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
