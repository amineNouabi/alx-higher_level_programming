#!/usr/bin/node

const request = require('request');

const apiBaseUrl = 'https://swapi-api.alx-tools.com/api';
const filmId = process.argv[2];

function fetchCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.log('Error: ');
        console.error(error);
        return reject(error);
      }
      if (!response || response.statusCode > 399) {
        console.log('HTTP Error: ', response && response.statusCode);
        return reject(new Error('HTTP Error'));
      }
      resolve(JSON.parse(body).name);
    });
  });
}

async function filmCallback (error, response, body) {
  if (error) {
    console.log('Error: ');
    console.error(error);
    return;
  }
  if (!response || response.statusCode > 399) {
    console.log('HTTP Error: ', response && response.statusCode);
    return;
  }
  const charactersUrls = JSON.parse(body).characters;
  try {
    const charactersNames = await Promise.all(charactersUrls.map(fetchCharacterName));
    charactersNames.forEach(characterName => {
      console.log(characterName);
    });
  } catch (err) {
    console.error(err);
  }
}

request(`${apiBaseUrl}/films/${filmId}`, filmCallback);
