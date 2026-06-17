import Nav from '@/components/Nav'
import Socials from '@/components/Socials'
import About from '@/components/sections/About'
import Education from '@/components/sections/Education'
import Projects from '@/components/sections/Projects'
import Writing from '@/components/sections/Writing'
import Contact from '@/components/sections/Contact'

export default function Home() {
  return (
    <div className="max-w-[1180px] mx-auto lg:grid lg:grid-cols-[350px_1fr] min-h-screen">
      <aside className="lg:sticky lg:top-0 lg:h-screen flex flex-col justify-between
        py-16 px-8 lg:px-10">
        <div>
          <h1
            className="text-[3rem] font-bold tracking-tight leading-[1.05] select-none"
            style={{
              background: 'linear-gradient(135deg, #ffffff 0%, #c7d2fe 60%, #a5b4fc 100%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
            }}
          >
            Hlib<br />Pakhomov
          </h1>

          <div className="mt-4 flex flex-wrap items-center gap-x-2 gap-y-1 max-w-[240px]">
            {['Computer Science (BSc)', 'University of Warwick', 'CS Student & Developer', 'Karate Athlete'].map((item, i, arr) => (
              <span key={item} className="flex items-center gap-x-2">
                <span className="text-[0.75rem] text-[#94a3b8] font-medium">{item}</span>
                {i < arr.length - 1 && (
                  <span className="text-[#2a2a2a] text-[0.65rem] select-none">|</span>
                )}
              </span>
            ))}
          </div>
          <Nav />
        </div>
        <Socials />
      </aside>
      <main className="py-16 px-8 lg:px-0 lg:pr-14 pb-32">
        <About />
        <Education />
        <Projects />
        <Writing />
        <Contact />
      </main>
    </div>
  )
}
