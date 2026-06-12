'use client'
import { useEffect, useState } from 'react'

const SECTIONS = [
  { id: 'about',     label: 'About' },
  { id: 'education', label: 'Education' },
  { id: 'projects',  label: 'Projects' },
  { id: 'contact',   label: 'Contact' },
]

export default function Nav() {
  const [active, setActive] = useState('about')

  useEffect(() => {
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => { if (e.isIntersecting) setActive(e.target.id) }),
      { rootMargin: '-25% 0px -65% 0px' },
    )
    SECTIONS.forEach(({ id }) => { const el = document.getElementById(id); if (el) io.observe(el) })
    return () => io.disconnect()
  }, [])

  const scrollTo = (id: string) =>
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })

  return (
    <nav className="mt-11 flex flex-col gap-0.5">
      {SECTIONS.map(({ id, label }) => {
        const on = active === id
        return (
          <button key={id} onClick={() => scrollTo(id)}
            className="flex items-center gap-3.5 py-1.5 w-fit group cursor-pointer">
            <span className={`h-px transition-all duration-200 ${on
              ? 'w-12 bg-[#e2e8f0]'
              : 'w-6 bg-[#64748b] group-hover:w-12 group-hover:bg-[#e2e8f0]'}`} />
            <span className={`text-[0.7rem] font-semibold tracking-[0.15em] uppercase transition-colors duration-200 ${on
              ? 'text-[#e2e8f0]'
              : 'text-[#64748b] group-hover:text-[#e2e8f0]'}`}>
              {label}
            </span>
          </button>
        )
      })}
    </nav>
  )
}
