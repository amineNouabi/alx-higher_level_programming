#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];
const fileContent = process.argv[3];
fs.writeFile(fileName, fileContent, (err) => {
  if (err) { console.log(err); }
});
