/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './app/views/**/*.jinja2',
      './src/js/**/*.js',
      './app/forms/**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('@tailwindcss/typography'),
      require('daisyui'),
  ],
}

