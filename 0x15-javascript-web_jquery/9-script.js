$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('div#hello').text(data.hello);
    }
  });
});
