import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./src/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {
      colors: {
        bg:      '#0d0d0d',
        surface: '#141414',
        border:  '#222222',
        accent: {
          DEFAULT: '#6366f1',
          low:  'rgba(99,102,241,0.08)',
          mid:  'rgba(99,102,241,0.25)',
        },
      },
      fontFamily: {
        sans: ['var(--font-inter)', 'sans-serif'],
        mono: ['var(--font-mono)', 'monospace'],
      },
    },
  },
  plugins: [],
}

export default config
