var gulp = require('gulp');
var sass = require('gulp-uglify');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var livereload = require('gulp-livereload');

/* Watch Files For Changes */
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('**/static/js/*.js').on('change', livereload.changed);
    gulp.watch('**/static/css/*.css').on('change', livereload.changed);
    gulp.watch('**/templates/**').on('change', livereload.changed);

});

gulp.task('default', ['watch']);
