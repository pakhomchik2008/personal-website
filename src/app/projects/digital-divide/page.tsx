import type { Metadata } from 'next'
import Image from 'next/image'
import BackButton from '@/components/BackButton'
import Tag from '@/components/Tag'

export const metadata: Metadata = {
  title: 'Digital Divide Research | Hlib Pakhomov',
  description: 'How has internet connectivity changed in the UK from 2015 to 2025?',
}

export default function DigitalDivide() {
  return (
    <div className="max-w-[780px] mx-auto px-6 md:px-10 py-14 pb-32">
      <BackButton />
      <h1 className="text-[2.2rem] font-bold tracking-tight leading-tight text-white">
        How has internet connectivity changed in the UK from 2015 to 2025?
      </h1>
      <p className="text-[0.9rem] text-accent font-medium mt-2.5">
        Digital Divide Research · University of Warwick, 2025
      </p>
      <div className="flex flex-wrap gap-2 mt-4">
        {['Python','Matplotlib','Ofcom Data','Linear Regression','Pearson r'].map((t) => <Tag key={t}>{t}</Tag>)}
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Overview</h2>
      <div className="space-y-3.5 text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        <p>
          Internet access has become central to work, education, and public services in the UK
          since 2015. Government policy framed the &ldquo;digital divide&rdquo; as a coverage
          problem — build infrastructure, close the gap. This research asks a harder question:
          has the divide actually closed, or has it simply changed shape?
        </p>
        <p>
          Using public datasets from Ofcom Connected Nations Reports (2015&ndash;2025) and the
          House of Commons Library, the analysis uncovered a counterintuitive paradox:{' '}
          <strong className="text-[#e2e8f0]">as rural coverage improved dramatically, the
          performance gap widened to its largest recorded level.</strong>
        </p>
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-5">Key Findings</h2>
      <div className="space-y-3">
        {[
          {
            stat: 'r = .881, p = .015',
            label: 'Urban–Rural Speed Gap',
            desc: 'Strong significant correlation between year and the urban–rural median download speed gap. The gap widened from 22 Mbit/s in 2015 to 190 Mbit/s in 2025 — even as rural FTTP coverage rose from under 5% to over 60%.',
          },
          {
            stat: 'r = .548, p = .081',
            label: 'Full-Fibre by UK Nation',
            desc: 'No significant change in between-nation variation overall, but trajectories diverged sharply from 2020. Northern Ireland reached 95% FTTP by 2025; Scotland lagged at 71%.',
          },
          {
            stat: '28.9 → 285 Mbit/s',
            label: 'UK Average Download Speed',
            desc: 'Consistent S-curve growth across the decade. A brief dip in 2020–21 during COVID-19 was followed by sharp acceleration after 2022 as large-scale FTTP deployment expanded.',
          },
        ].map(({ stat, label, desc }) => (
          <div key={label}
            className="bg-surface border border-border border-l-2 rounded-lg p-5"
            style={{ borderLeftColor: '#6366f1' }}>
            <div className="flex items-baseline gap-3 mb-1.5">
              <span className="font-mono text-[0.75rem] text-accent">{stat}</span>
              <span className="text-[0.8rem] font-medium text-[#e2e8f0]">{label}</span>
            </div>
            <p className="text-[0.84rem] text-[#64748b] leading-relaxed">{desc}</p>
          </div>
        ))}
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3">Research Poster</h2>
      <p className="text-[0.83rem] text-[#64748b] mb-4 leading-relaxed">
        Full visual summary — methodology, charts, and key findings condensed onto one page.
        Click to download the PDF.
      </p>
      <a href="/digital-divide-poster.pdf" download
        className="group block relative w-full rounded-lg overflow-hidden
          border border-border hover:border-accent-mid transition-colors duration-200">
        <Image
          src="/digital-divide-poster.jpg"
          alt="Digital Divide research poster"
          width={1200}
          height={1697}
          className="w-full h-auto"
        />
        <div className="absolute inset-0 bg-black/0 group-hover:bg-black/50
          transition-colors duration-200 flex items-center justify-center">
          <span className="opacity-0 group-hover:opacity-100 transition-opacity duration-200
            text-white text-[0.85rem] font-medium bg-black/70 px-4 py-2 rounded-md">
            Download PDF
          </span>
        </div>
      </a>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-5">Learning Outcomes</h2>
      <div className="space-y-3">
        {[
          {
            title: 'Working with real-world data',
            body: 'Cleaned and reconciled Ofcom datasets spanning a decade — handling inconsistent column names, missing years, and methodology changes between report editions.',
          },
          {
            title: 'Statistical reasoning under uncertainty',
            body: 'Applied Pearson correlation and hypothesis testing to draw defensible conclusions. Learned to distinguish statistical significance from practical significance when interpreting p-values close to the threshold.',
          },
          {
            title: 'Visualisation as an argument',
            body: 'Designed charts in Matplotlib to make the speed-gap paradox immediately visible. Each visual choice — axis scale, colour, annotation — was made to support the central claim rather than just display data.',
          },
          {
            title: 'Nuance in policy analysis',
            body: 'Realised that surface-level metrics (coverage percentages) can mask underlying inequality. Framing the conclusion around speed parity rather than access parity required moving beyond the data to interpret what it actually meant.',
          },
        ].map(({ title, body }) => (
          <div key={title} className="flex gap-4">
            <div className="mt-1.5 w-1.5 h-1.5 rounded-full bg-accent shrink-0" />
            <div>
              <p className="text-[0.875rem] font-medium text-[#e2e8f0] mb-1">{title}</p>
              <p className="text-[0.84rem] text-[#64748b] leading-relaxed">{body}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
