export default function Tag({ children }: { children: React.ReactNode }) {
  return (
    <span className="font-mono text-[0.68rem] px-2.5 py-1 rounded-full
      bg-accent-low text-accent border border-accent-mid">
      {children}
    </span>
  )
}
