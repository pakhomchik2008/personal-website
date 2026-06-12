import type { Metadata } from 'next'
import BackButton from '@/components/BackButton'
import Tag from '@/components/Tag'

export const metadata: Metadata = {
  title: 'Digital Divide Research | Hlib Pakhomov',
  description: 'How has internet connectivity changed in the UK from 2015 to 2025?',
}

function Finding({ stat, children }: { stat: string; children: React.ReactNode }) {
  return (
    <div className="bg-surface border border-border rounded-lg p-5 my-6 border-l-2"
      style={{ borderLeftColor: '#6366f1' }}>
      <p className="font-mono text-[0.8rem] text-accent mb-2">{stat}</p>
      <p className="text-[0.875rem] text-[#94a3b8] leading-relaxed">{children}</p>
    </div>
  )
}

function ChartWrap({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="bg-surface border border-border rounded-lg p-5 my-6">
      <p className="text-[0.72rem] font-semibold tracking-widest uppercase text-[#64748b] mb-4">
        {title}
      </p>
      {children}
    </div>
  )
}

const LP = { fill: 'none', strokeWidth: 2.2, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const }
const GRID = { stroke: '#222', strokeWidth: 0.5, strokeDasharray: '4,4' }
const AXIS = { stroke: '#333', strokeWidth: 1 }
const YRS  = ['2015','2017','2019','2021','2023','2025']

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
        <p>Internet access has become central to work, education and public services in
        the UK since 2015. Government policy framed the &ldquo;digital divide&rdquo; as
        a coverage problem. This research asks a harder question: has the divide actually
        closed, or has it simply changed shape?</p>
        <p>Using public datasets from Ofcom Connected Nations Reports (2015&ndash;2025)
        and the House of Commons Library, the analysis revealed a counterintuitive paradox:{' '}
        <strong className="text-[#e2e8f0]">as rural coverage improved dramatically, the
        performance gap widened to its largest ever level.</strong></p>
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Finding 1 — Urban–Rural Speed Gap</h2>
      <Finding stat="r(9) = .881, p = .015 — statistically significant (H₀ rejected)">
        Strong positive correlation between year and urban–rural median download speed gap.
        Gap widened from 22 Mbit/s in 2015 to 190 Mbit/s in 2025, even as rural FTTP coverage
        rose from under 5% to over 60%.
      </Finding>
      <ChartWrap title="Urban vs Rural median download speed (Mbit/s)">
        <svg viewBox="0 0 560 230" style={{ width: '100%', overflow: 'visible' }}>
          <defs>
            <linearGradient id="ug" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#6366f1" stopOpacity="0.12" />
              <stop offset="100%" stopColor="#6366f1" stopOpacity="0" />
            </linearGradient>
          </defs>
          <style>{`.cl{font-family:var(--font-mono,monospace);font-size:9px;fill:#64748b}`}</style>
          <line x1="60" y1="200" x2="540" y2="200" {...AXIS} />
          <line x1="60" y1="20"  x2="60"  y2="200" {...AXIS} />
          {[140,80,20].map(y => <line key={y} x1="60" y1={y} x2="540" y2={y} {...GRID} />)}
          <text className="cl" x="52" y="204" textAnchor="end">0</text>
          <text className="cl" x="52" y="143" textAnchor="end">100</text>
          <text className="cl" x="52" y="83"  textAnchor="end">200</text>
          <text className="cl" x="52" y="23"  textAnchor="end">300</text>
          {YRS.map((yr,i) => <text key={yr} className="cl" x={60+i*96} y="216" textAnchor="middle">{yr}</text>)}
          <polygon fill="url(#ug)" points="60,179 108,174.8 156,168.8 204,162.8 252,156.8 300,153.2 348,155 396,137 444,104 492,62 540,23 540,200 60,200" />
          <polyline {...LP} stroke="#6366f1" points="60,179 108,174.8 156,168.8 204,162.8 252,156.8 300,153.2 348,155 396,137 444,104 492,62 540,23" />
          <polyline {...LP} stroke="#94a3b8" strokeDasharray="6,3" points="60,192.2 108,190.4 156,189.2 204,188 252,186.8 300,185.6 348,186.8 396,182 444,167 492,149 540,137" />
          <circle cx="60"  cy="179"   r="3" fill="#6366f1" /><circle cx="540" cy="23"  r="4" fill="#6366f1" />
          <circle cx="60"  cy="192.2" r="3" fill="#94a3b8" /><circle cx="540" cy="137" r="3" fill="#94a3b8" />
          <text className="cl" x="68"  y="176" fill="#6366f1">35</text>
          <text className="cl" x="510" y="19"  fill="#6366f1">295</text>
          <text className="cl" x="510" y="134" fill="#94a3b8">105</text>
        </svg>
        <div className="flex flex-wrap gap-4 mt-3">
          {[['#6366f1','Urban median speed'],['#94a3b8','Rural median speed']].map(([c,l]) => (
            <div key={l} className="flex items-center gap-1.5 text-[0.72rem] text-[#64748b]">
              <span className="w-2.5 h-2.5 rounded-full inline-block" style={{ background: c }} />{l}
            </div>
          ))}
        </div>
      </ChartWrap>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Finding 2 — Full-Fibre Rollout by UK Nation</h2>
      <Finding stat="r(9) = .548, p = .081 — not significant (H₀ accepted)">
        No statistically significant change in between-nation FTTP variation overall, but
        trajectories diverged sharply from 2020: Northern Ireland reached 95% by 2025 while
        Scotland lagged at 71%.
      </Finding>
      <ChartWrap title="Full-fibre (FTTP) availability by UK nation (% of premises)">
        <svg viewBox="0 0 560 230" style={{ width: '100%', overflow: 'visible' }}>
          <style>{`.cl{font-family:var(--font-mono,monospace);font-size:9px;fill:#64748b}`}</style>
          <line x1="60" y1="200" x2="540" y2="200" {...AXIS} />
          <line x1="60" y1="20"  x2="60"  y2="200" {...AXIS} />
          {[146,92,38].map(y => <line key={y} x1="60" y1={y} x2="540" y2={y} {...GRID} />)}
          <text className="cl" x="52" y="204" textAnchor="end">0%</text>
          <text className="cl" x="52" y="149" textAnchor="end">30%</text>
          <text className="cl" x="52" y="95"  textAnchor="end">60%</text>
          <text className="cl" x="52" y="41"  textAnchor="end">90%</text>
          {YRS.map((yr,i) => <text key={yr} className="cl" x={60+i*96} y="216" textAnchor="middle">{yr}</text>)}
          <polyline {...LP} stroke="#6366f1" points="60,199.6 108,199.1 156,198.2 204,196.4 252,191 300,182 348,173 396,146 444,101 492,77.6 540,63.2" />
          <polyline {...LP} stroke="#34d399" points="60,199.8 108,199.6 156,199.1 204,198.2 252,194.6 300,185.6 348,164 396,119 444,74 492,47 540,29" />
          <polyline {...LP} stroke="#f59e0b" strokeDasharray="5,3" points="60,199.8 108,199.5 156,198.6 204,197.3 252,194.6 300,187.4 348,178.4 396,160.4 444,128 492,95.6 540,72.2" />
          <polyline {...LP} stroke="#94a3b8" strokeDasharray="3,3" points="60,199.8 108,199.6 156,199.1 204,198.2 252,195.5 300,191 348,183.8 396,167.6 444,137 492,106.4 540,79.4" />
          <circle cx="540" cy="29"   r="4" fill="#34d399" />
          <circle cx="540" cy="63.2" r="3" fill="#6366f1" />
          <circle cx="540" cy="72.2" r="3" fill="#f59e0b" />
          <circle cx="540" cy="79.4" r="3" fill="#94a3b8" />
          <text className="cl" x="492" y="24" fill="#34d399">95%</text>
        </svg>
        <div className="flex flex-wrap gap-4 mt-3">
          {[['#6366f1','England (76%)'],['#34d399','N. Ireland (95%)'],['#f59e0b','Scotland (71%)'],['#94a3b8','Wales (67%)']].map(([c,l]) => (
            <div key={l} className="flex items-center gap-1.5 text-[0.72rem] text-[#64748b]">
              <span className="w-2.5 h-2.5 rounded-full inline-block" style={{ background: c }} />{l}
            </div>
          ))}
        </div>
      </ChartWrap>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Finding 3 — UK Average Download Speed</h2>
      <Finding stat="28.9 Mbit/s (2015) → 285 Mbit/s (2025) — S-curve growth">
        Consistent upward trend matching Oughton et al. (2021)&apos;s S-curve prediction. A slight
        dip in 2020–21 due to COVID-19, then sharp acceleration after 2022 as FTTP rollout expanded.
      </Finding>
      <ChartWrap title="UK average fixed-line download speed (Mbit/s)">
        <svg viewBox="0 0 560 230" style={{ width: '100%', overflow: 'visible' }}>
          <defs>
            <linearGradient id="sg" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#6366f1" stopOpacity="0.18" />
              <stop offset="100%" stopColor="#6366f1" stopOpacity="0" />
            </linearGradient>
          </defs>
          <style>{`.cl{font-family:var(--font-mono,monospace);font-size:9px;fill:#64748b}`}</style>
          <polygon fill="url(#sg)" points="60,182.7 108,178.4 156,172.4 204,167.6 252,161.6 300,159.2 348,161 396,146 444,107 492,68 540,29 540,200 60,200" />
          <line x1="60" y1="200" x2="540" y2="200" {...AXIS} />
          <line x1="60" y1="20"  x2="60"  y2="200" {...AXIS} />
          {[140,80,20].map(y => <line key={y} x1="60" y1={y} x2="540" y2={y} {...GRID} />)}
          <text className="cl" x="52" y="204" textAnchor="end">0</text>
          <text className="cl" x="52" y="143" textAnchor="end">100</text>
          <text className="cl" x="52" y="83"  textAnchor="end">200</text>
          <text className="cl" x="52" y="23"  textAnchor="end">300</text>
          {YRS.map((yr,i) => <text key={yr} className="cl" x={60+i*96} y="216" textAnchor="middle">{yr}</text>)}
          <polyline {...LP} stroke="#6366f1" strokeWidth={2.5} points="60,182.7 108,178.4 156,172.4 204,167.6 252,161.6 300,159.2 348,161 396,146 444,107 492,68 540,29" />
          <circle cx="60"  cy="182.7" r="3.5" fill="#6366f1" />
          <circle cx="540" cy="29"    r="4"   fill="#6366f1" />
          <text className="cl" x="68"  y="179" fill="#6366f1">28.9</text>
          <text className="cl" x="510" y="25"  fill="#6366f1">285</text>
        </svg>
      </ChartWrap>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Conclusion</h2>
      <div className="space-y-3.5 text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        <p>The UK digital divide has{' '}
        <strong className="text-[#e2e8f0]">not closed</strong> — it has shifted from an access
        gap to a performance and regional quality gap. Rural premises are increasingly connected,
        but to lower-tier services, widening the speed gap.</p>
        <p>Policy should pivot from coverage targets to{' '}
        <strong className="text-[#e2e8f0]">speed-parity and regional equity</strong>. Future
        research should incorporate affordability and digital skills data, which nation-level
        Ofcom reporting cannot capture.</p>
      </div>
    </div>
  )
}
