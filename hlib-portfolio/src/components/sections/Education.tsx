import SectionLabel from '@/components/SectionLabel'

export default function Education() {
  return (
    <section id="education" className="mb-24 scroll-mt-20">
      <SectionLabel>Education</SectionLabel>
      <div className="divide-y divide-border">
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">University of Warwick</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">2026 — 2029</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">
            Bachelor of Science · Computer Science
          </p>
        </div>
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">University of Warwick</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">2025 — 2026</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">
            International Foundation Programme · Computer Science
          </p>
        </div>
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">IT Step School Kyiv</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">2014 — 2025</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">Computer Science &amp; Mathematics</p>
        </div>
      </div>
    </section>
  )
}
