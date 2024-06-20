#!/usr/bin/node

let array = require('./100-data').list;
console.log(array);

array = array.map((value, index) => {
  return value * index;
});

console.log(array);
