import SectionLabel from '@/components/SectionLabel'
import Tag from '@/components/Tag'

export default function Education() {
  return (
    <section id="education" className="mb-24 scroll-mt-20">
      <SectionLabel>Education</SectionLabel>
      <div className="divide-y divide-border">
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">University of Warwick</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">2025 — 2026</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">
            International Foundation Programme · Computer Science
          </p>
          <p className="text-[0.8rem] text-[#64748b] mt-1.5 leading-relaxed">
            Pure Maths 80% · Stats &amp; Further Maths 86% · Computer Science 72%
          </p>
        </div>
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">IT Step School Kyiv</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">Secondary</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">Computer Science &amp; Mathematics</p>
          <p className="text-[0.8rem] text-[#64748b] mt-1.5">
            Overall 10.8 / 12 · Mathematics 10 / 12 · Physics 10 / 12
          </p>
        </div>
        <div className="py-5">
          <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">Certifications</span>
          <div className="flex flex-wrap gap-2 mt-2.5">
            <Tag>Claude Code in Action — Anthropic</Tag>
            <Tag>AI Fluency — Anthropic</Tag>
          </div>
        </div>
      </div>
    </section>
  )
}
