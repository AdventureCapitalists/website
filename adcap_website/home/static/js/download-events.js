$(document).ready( function() {
  var download_link_divs = document.getElementsByClassName("download");
  
  for (var i = 0; i < download_link_divs.length; i++ ) {
    download_link_divs[i].onclick = function(download_link_div) {
      var format = this.innerHTML;
      var record = this.href.split("_").pop().split(".")[0];
      console.log(record, format);
      ga('send', 'event', 'Download', record, format);
    }
  }
});
