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
        ga('send', 'event', 'SoundCloud', 'Play', sound.title, {page: window.location.pathname});

        window['optimizely'] = window['optimizely'] || [];
        window.optimizely.push(["trackEvent", "songPlay"]);
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
    ga('send', 'event', 'SoundCloud', 'Finish', window.current_song, {page: window.location.pathname}); 
    window['optimizely'] = window['optimizely'] || [];
    window.optimizely.push(["trackEvent", "songFinish"]);
  }
}

function handlePauseEvent(event) {
  return function(event) {
    ga('send', 'event', 'SoundCloud', 'Pause', window.current_song, {'dimension1': window.current_progress_bucket}); 
    window['optimizely'] = window['optimizely'] || [];
    window.optimizely.push(["trackEvent", "songPause"]);
  }
}

function handleSeekEvent(event) {
  return function(event) {
    ga('send', 'event', 'SoundCloud', 'Seek', window.current_song, {'dimension1': window.current_progress_bucket}); 
    window['optimizely'] = window['optimizely'] || [];
    window.optimizely.push(["trackEvent", "songSeek"]);
  }
}

function handleDownloadEvent(event) {
  return function(event) {
    ga('send', 'event', 'SoundCloud', 'Download', window.current_song, {'dimension1': window.current_progress_bucket}); 
    window['optimizely'] = window['optimizely'] || [];
    window.optimizely.push(["trackEvent", "songDownload"]);
  }
}

function handleBuyEvent(event) {
  return function(event) {
    ga('send', 'event', 'SoundCloud', 'Buy', window.current_song, {'dimension1': window.current_progress_bucket}); 
    window['optimizely'] = window['optimizely'] || [];
    window.optimizely.push(["trackEvent", "songBuy"]);
  }
}

function handleShareEvent(event) {
  return function(event) {
    ga('send', 'event', 'SoundCloud', 'Share', window.current_song, {'dimension1': window.current_progress_bucket}); 
    window['optimizely'] = window['optimizely'] || [];
    window.optimizely.push(["trackEvent", "songShare"]);
  }
}

function handleErrorEvent(event) {
  return function(event) {
    ga('send', 'event', 'SoundCloud', 'Error', window.location.pathname); 
  }
}

$(document).ready( function() {
  var widget_iframe = document.getElementById("soundcloud_widget");
  if (widget_iframe != null) {
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
  }
});
