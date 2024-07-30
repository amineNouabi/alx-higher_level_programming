#!/usr/bin/node

const fs = require('fs');

const file_name = process.argv[2];
const file_content = process.argv[3];
fs.writeFile(file_name, file_content, (err) => {
  if (err) { console.log(err); }
});
