$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      for (const film of data.results) {
        $('UL#list_movies').append($('<li></li>').text(film.title));
      }
    }
  });
});
