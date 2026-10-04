'use client'
import { useEffect, useRef } from 'react'

export default function Spotlight() {
  const ref = useRef<HTMLDivElement>(null)
  useEffect(() => {
    const move = (e: MouseEvent) => {
      if (ref.current)
        ref.current.style.background = `radial-gradient(600px at ${e.clientX}px ${e.clientY}px, rgba(99,102,241,0.07), transparent 80%)`
    }
    window.addEventListener('mousemove', move)
    return () => window.removeEventListener('mousemove', move)
  }, [])
  return <div ref={ref} className="pointer-events-none fixed inset-0 z-10" />
}
