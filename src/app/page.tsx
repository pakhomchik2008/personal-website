import Nav from '@/components/Nav'
import Socials from '@/components/Socials'
import About from '@/components/sections/About'
import Education from '@/components/sections/Education'
import Projects from '@/components/sections/Projects'
import Contact from '@/components/sections/Contact'

export default function Home() {
  return (
    <div className="max-w-[1180px] mx-auto lg:grid lg:grid-cols-[350px_1fr] min-h-screen">
      <aside className="lg:sticky lg:top-0 lg:h-screen flex flex-col justify-between
        py-16 px-8 lg:px-10">
        <div>
          <h1 className="text-[2.1rem] font-bold tracking-tight leading-tight text-white">
            Hlib<br />Pakhomov
          </h1>
          <p className="text-[0.875rem] font-medium text-accent mt-2 tracking-wide">
            CS Student · Warwick
          </p>
          <p className="text-[0.825rem] text-[#64748b] mt-3.5 leading-relaxed max-w-[210px]">
            Building software and solving real problems. Former national team athlete.
          </p>
          <Nav />
        </div>
        <Socials />
      </aside>
      <main className="py-16 px-8 lg:px-0 lg:pr-14 pb-32">
        <About />
        <Education />
        <Projects />
        <Contact />
      </main>
    </div>
  )
}
