export default function SectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex items-center gap-3 mb-7">
      <span className="text-[0.7rem] font-semibold tracking-[0.16em] uppercase text-[#64748b]">
        {children}
      </span>
      <span className="flex-1 h-px bg-border max-w-[160px]" />
    </div>
  )
}
