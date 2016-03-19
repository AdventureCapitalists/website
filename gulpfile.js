var os = require('os');
var gulp = require('gulp');
var sass = require('gulp-uglify');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var livereload = require('gulp-livereload');
var open = require('gulp-open');

var exec;
exec = require('child_process').exec;

/* Watch Files For Changes */
gulp.task('watch', function() {
  livereload.listen();
  gulp.watch('**/js/**').on('change', livereload.changed);
  gulp.watch('**/css/**').on('change', livereload.changed);
  gulp.watch('**/templates/**').on('change', livereload.changed);

});

var browser = os.platform() === 'linux' ? 'google-chrome' : (
  os.platform() === 'darwin' ? 'google chrome' : (
  os.platform() === 'win32' ? 'chrome' : 'firefox'));

gulp.task('open', function(){
  var options = {
    uri: 'http://localhost:8000',
    app: browser 
  };
  gulp.src(__filename)
  .pipe(open(options));
});

gulp.task('django', function() {
  var proc;
  proc = exec('python adcap_website/manage.py runserver');
  proc.stderr.on('data', function(data) {
    return process.stdout.write(data);
  });
  return proc.stdout.on('data', function(data) {
    return process.stdout.write(data);
  });
});

gulp.task('default', ['django', 'watch', 'open']);
