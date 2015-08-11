function calculate_bucket(_t) {
    if (_t <= 0 || _t > 100) return;
    var bucket = (_t > 10 ? 1 : 0) * (
        Math.floor((_t - 1) / 10) * 10 + 1
    );
    bucket = String(bucket) + '-' +
        String(Math.ceil(_t / 10) * 10);
    return bucket;
}

function handlePlayEvent(event) {
  return function(event) {
    setTimeout(function() {
      window.soundcloud_widget.getCurrentSound(function(sound) {
        window.current_song = sound.title;
        ga('send', 'SoundCloud', 'Play', sound.title, {page: window.location.pathname});
      });
    }, 1);
  }
}

function handlePlayProgressEvent(event) {
  return function(event) {
    window.current_progress_bucket = calculate_bucket(Math.floor(event.relativePosition * 100));  
  }
}

function handleFinishEvent(event) {
  return function(event) {
    ga('send', 'SoundCloud', 'Finish', window.current_song, {page: window.location.pathname}); 
  }
}

function handlePauseEvent(event) {
  return function(event) {
    ga('send', 'SoundCloud', 'Pause', window.current_song, window.current_progress_bucket); 
  }
}

function handleSeekEvent(event) {
  return function(event) {
    ga('send', 'SoundCloud', 'Seek', window.current_song, window.current_progress_bucket); 
  }
}

function handleDownloadEvent(event) {
  return function(event) {
    ga('send', 'SoundCloud', 'Download', window.current_song, window.current_progress_bucket); 
    console.log("Download.");
  }
}

function handleBuyEvent(event) {
  return function(event) {
    ga('send', 'SoundCloud', 'Buy', window.current_song, window.current_progress_bucket); 
    console.log("Buy");
  }
}

function handleShareEvent(event) {
  return function(event) {
    ga('send', 'SoundCloud', 'Share', window.current_song, window.current_progress_bucket); 
    console.log("Share.");
  }
}

function handleErrorEvent(event) {
  return function(event) {
    ga('send', 'SoundCloud', 'Error', window.location.pathname); 
  }
}

$(document).ready( function() {
  var widget_iframe = document.getElementById("soundcloud_widget");
  window.soundcloud_widget = SC.Widget(widget_iframe);

  window.current_song = "";
  window.current_progress_bucket = 0;

  soundcloud_widget.bind(SC.Widget.Events.READY, function() {
    soundcloud_widget.bind(SC.Widget.Events.PLAY, handlePlayEvent(event));
    soundcloud_widget.bind(SC.Widget.Events.PLAY_PROGRESS, handlePlayProgressEvent(event));
    soundcloud_widget.bind(SC.Widget.Events.FINISH, handleFinishEvent(event));
    soundcloud_widget.bind(SC.Widget.Events.PAUSE, handlePauseEvent(event));
    soundcloud_widget.bind(SC.Widget.Events.SEEK, handleSeekEvent(event));
    soundcloud_widget.bind(SC.Widget.Events.CLICK_DOWNLOAD, handleDownloadEvent(event));
    soundcloud_widget.bind(SC.Widget.Events.CLICK_BUY, handleBuyEvent(event));
    soundcloud_widget.bind(SC.Widget.Events.OPEN_SHARE_PANEL, handleShareEvent(event));
    soundcloud_widget.bind(SC.Widget.Events.ERROR, handleErrorEvent(event));
  });
});
