#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const targetCharacterID = 18;

function filmsCallback (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (!response || response.statusCode > 399) {
    console.log('Error: ', response && response.statusCode);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach(film => {
    for (let i = 0; i < film.characters.length; i++) {
      const characterID = film.characters[i].slice(0, -1).split('/').pop();
      if (parseInt(characterID, 10) === targetCharacterID) { count++; break; }
    }
  });
  console.log(count);
}

request(`${apiUrl}?`, filmsCallback);
