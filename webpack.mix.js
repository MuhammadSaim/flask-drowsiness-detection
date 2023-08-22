const mix = require('laravel-mix');


mix.options({
  fileLoaderDirs: {
    fonts: "assets/fonts",
    images: "assets/images",
  },
});



mix.js("src/js/app.js", "app/assets/js")
  .sass('./src/scss/app.scss', 'app/assets/css', {}, [
        require('tailwindcss')
    ]);