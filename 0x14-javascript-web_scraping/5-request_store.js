#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log('Error: ');
    console.error(error);
    return;
  }
  if (!response || response.statusCode > 399) {
    console.log('HTTP Error: ', response && response.statusCode);
    return;
  }

  fs.writeFile(fileName, body, (err) => {
    if (err) { console.log(err); }
  });
});
