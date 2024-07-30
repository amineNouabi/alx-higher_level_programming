#!/usr/bin/node

const request = require('request');

const apiBaseUrl = 'https://swapi-api.alx-tools.com/api';
const filmId = process.argv[2];

function filmCallback (error, response, body) {
  if (error) {
    console.log('Error: ');
    console.error(error);
    return;
  }
  if (!response || response.statusCode > 399) {
    console.log('HTTP Error: ', response && response.statusCode);
    return;
  }
  const film = JSON.parse(body);
  film.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.log('Error: ');
        console.error(error);
        return;
      }
      if (!response || response.statusCode > 399) {
        console.log('HTTP Error: ', response && response.statusCode);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
}

request(`${apiBaseUrl}/films/${filmId}`, filmCallback);
