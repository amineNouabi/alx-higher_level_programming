$(document).ready(function () {
  function fetchTranslation () {
    const lang = $('input#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
      success: function (data) {
        $('div#hello').html(data.hello);
      }
    });
  }

  $('input#btn_translate').click(fetchTranslation);
  $('input#language_code').keypress(function (e) {
    if (e.which === 13) { fetchTranslation(); }
  });
});
