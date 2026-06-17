import SectionLabel from '@/components/SectionLabel'

const CERTS = [
  {
    title: 'Claude Code in Action',
    issuer: 'Anthropic',
    href: '/certificate-claude-code-in-action.pdf',
  },
  {
    title: 'Claude Code 101',
    issuer: 'Anthropic',
    href: '/certificate-claude-code-101.pdf',
  },
]

export default function Certifications() {
  return (
    <section id="certifications" className="mb-24 scroll-mt-20">
      <SectionLabel>Certifications</SectionLabel>
      <div className="space-y-1">
        {CERTS.map(({ title, issuer, href }) => (
          <a key={title} href={href} download
            className="group flex items-center justify-between p-5 rounded-lg border border-transparent
              hover:bg-surface hover:border-border hover:translate-x-1
              transition-all duration-200 relative overflow-hidden">
            <span className="absolute left-0 top-0 bottom-0 w-0.5 bg-accent
              scale-y-0 group-hover:scale-y-100 transition-transform duration-200 origin-bottom" />
            <div>
              <p className="text-[0.875rem] font-semibold text-[#e2e8f0] group-hover:text-accent transition-colors duration-200">
                {title}
              </p>
              <p className="text-[0.78rem] text-[#64748b] mt-0.5">{issuer}</p>
            </div>
            <span className="text-[#64748b] group-hover:text-[#e2e8f0] transition-colors duration-200 text-sm flex-shrink-0 ml-4">
              ↓
            </span>
          </a>
        ))}
      </div>
    </section>
  )
}
