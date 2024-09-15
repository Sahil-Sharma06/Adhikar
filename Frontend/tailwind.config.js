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
      },
    },
  },
  plugins: [],
}

