import type { Metadata } from 'next'
import BackButton from '@/components/BackButton'
import Tag from '@/components/Tag'

export const metadata: Metadata = {
  title: 'Cryptocurrency & Blockchain Essay | Hlib Pakhomov',
  description: 'Academic essay on the ethical and legal issues of cryptocurrency and blockchain technologies.',
}

export default function CryptocurrencyEssay() {
  return (
    <div className="max-w-[780px] mx-auto px-6 md:px-10 py-14 pb-32">
      <BackButton />
      <h1 className="text-[2.2rem] font-bold tracking-tight leading-tight text-white">
        Ethical and Legal Issues of Cryptocurrency and Blockchain
      </h1>
      <p className="text-[0.9rem] text-accent font-medium mt-2.5">
        Academic Essay · FP023 EAP for Maths and Computer Science · University of Warwick, 2025
      </p>
      <div className="flex flex-wrap gap-2 mt-4">
        {['Blockchain', 'Cryptocurrency', 'Ethics', 'Law', 'Computer Science', 'Academic Writing'].map(
          (t) => <Tag key={t}>{t}</Tag>
        )}
      </div>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-3.5">Overview</h2>
      <p className="text-[0.875rem] text-[#94a3b8] leading-[1.85] max-w-[660px]">
        This essay examines how cryptocurrency and blockchain — technologies built on pseudonymity,
        decentralisation, and immutability — create a structural regulatory paradox: the very features
        that make them valuable for financial inclusion and privacy are the same ones that enable money
        laundering, illicit trade, and the evasion of institutional oversight. Drawing on empirical data,
        case studies of China and El Salvador, and scholarly literature, it argues that the ethical
        challenges of these technologies are not accidental but are embedded in their architectural
        design — and that computer scientists bear a direct responsibility for the social consequences
        of the systems they build.
      </p>

      <hr className="border-border my-11" />

      <h2 className="text-base font-semibold text-[#e2e8f0] mb-4">Download</h2>
      <a href="/cryptocurrency-blockchain-essay.pdf" download
        className="flex items-start gap-4 p-4 bg-surface border border-border rounded-lg
          hover:border-accent-mid transition-colors duration-200 group w-fit min-w-[320px]">
        <div className="w-10 h-10 rounded-md bg-accent-low flex items-center justify-center
          text-accent font-mono text-[0.62rem] font-bold flex-shrink-0
          group-hover:bg-accent/15 transition-colors duration-200">
          PDF
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-[0.875rem] font-semibold text-[#e2e8f0]">Full Essay</p>
          <p className="text-[0.83rem] text-[#64748b] mt-1">
            16 pages · Harvard referencing · FP023 module submission
          </p>
        </div>
        <span className="text-[#64748b] group-hover:text-[#e2e8f0] transition-colors duration-200 mt-0.5 text-sm flex-shrink-0">↓</span>
      </a>
    </div>
  )
}
