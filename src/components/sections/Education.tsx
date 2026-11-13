import SectionLabel from '@/components/SectionLabel'

export default function Education() {
  return (
    <section id="education" className="mb-24 scroll-mt-20">
      <SectionLabel>Education</SectionLabel>
      <div className="divide-y divide-border">
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">University of Warwick</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">Sep 2026 — Jun 2029</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">
            BEng · Computer Systems Engineering
          </p>
          <p className="text-[0.78rem] text-[#64748b] mt-1">
            Academic Scholar and Sports Scholar · Modules: Introduction to Java, Web Development,
            Functional Programming, Computer Architecture
          </p>
        </div>
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">University of Warwick</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">Sep 2025 — Jul 2026</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">
            International Foundation Programme · 83% overall in first year
          </p>
        </div>
        <div className="py-5">
          <div className="flex justify-between items-baseline gap-3 flex-wrap">
            <span className="font-semibold text-[0.9rem] text-[#e2e8f0]">IT STEP School</span>
            <span className="font-mono text-[0.75rem] text-[#64748b]">2014 — Apr 2025</span>
          </div>
          <p className="text-[0.825rem] text-accent mt-0.5">Secondary education · Honor Roll</p>
        </div>
      </div>
    </section>
  )
}
