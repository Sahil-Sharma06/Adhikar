/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        'custom-dark-blue': '#11163B',
        'custom-pink': '#F23E79',
        'custom-black': '#0f0f0f',
        'custom-signup-border': '#1C1C1C',
        'custom-button': '#F7F7F7',
        'custom-green': '#064942',
      },
    },
  },
  plugins: [],
}

