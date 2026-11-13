import type { Metadata } from 'next'
import { Inter, JetBrains_Mono } from 'next/font/google'
import './globals.css'
import Spotlight from '@/components/Spotlight'

const inter = Inter({ subsets: ['latin'], variable: '--font-inter', display: 'swap' })
const mono  = JetBrains_Mono({ subsets: ['latin'], variable: '--font-mono', display: 'swap' })

export const metadata: Metadata = {
  title: 'Hlib Pakhomov',
  description:
    'Computer Systems Engineering student at the University of Warwick. Founder of Examik. Former Ukraine national team karate athlete.',
  openGraph: {
    title: 'Hlib Pakhomov',
    description: 'Computer Systems Engineering student at Warwick. Founder of Examik.',
    type: 'website',
  },
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} ${mono.variable}`}>
      <body className="font-sans bg-bg text-[#e2e8f0]">
        <Spotlight />
        {children}
      </body>
    </html>
  )
}
