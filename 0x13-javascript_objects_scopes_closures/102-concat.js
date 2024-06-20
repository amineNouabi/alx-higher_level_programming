#!/usr/bin/node

const fs = require('fs');

const readPaths = process.argv.slice(2, 4);

let content = '';

readPaths.forEach(path => {
  content += fs.readFileSync(path).toString();
});

fs.writeFileSync(process.argv[4], content);
