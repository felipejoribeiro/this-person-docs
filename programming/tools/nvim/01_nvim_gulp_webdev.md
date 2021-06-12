# Webdev in NeoVim
Here we will see how to make a web development environment in `Neovim`.

## Serving simple js, html, css pages
for serving simple html pages we can install `browser-sync` with `node`. This is a terminal utility to serve simple html pages really quickly.

You should install `gulp` too, as it enables the dev to run various tasks with only one command. This is important because there are other utilities that must be considered like `sass` for example.

For that, install `gulp` globally with `npm install -g gulp-cli`.

Then install `gulp` locally with:

```bash
npm install gulp browser-sync --save-dev
```

And lastelly, create the `gulpfile.js` in the root of your project with:

```javascript
var gulp = require('gulp');
var browserSync = require('browser-sync').create();

gulp.task('default', function(){
    browserSync.init(
    {
        watch: true,
        ui: false,
        server: "./",
        files: ["css/*.css", "*.html", "js/*.js"]
    });
});
```

And that is it. You can add more things too to the default task and create new tasks as well besides the `default` one.
