#!/usr/bin/node

const request = require('request');

const apiBaseUrl = 'https://swapi-api.alx-tools.com/api';
const filmID = process.argv[2];

const options = {
  url: `${apiBaseUrl}/films/${filmID}`
};

function callback (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (body) {
    console.log(JSON.parse(body).title);
  }
}

request(options, callback);
