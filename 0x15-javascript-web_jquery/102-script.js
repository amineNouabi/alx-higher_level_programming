$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
      success: function (data) {
        $('div#hello').html(data.hello);
      }
    });
  });
});
