'use client'
import { useRouter } from 'next/navigation'

export default function BackButton() {
  const router = useRouter()
  return (
    <button onClick={() => router.back()}
      className="inline-flex items-center gap-2 text-[0.72rem] font-semibold
        tracking-[0.12em] uppercase text-[#64748b] hover:text-accent
        hover:-translate-x-1 transition-all duration-200 mb-14">
      ← Back
    </button>
  )
}
