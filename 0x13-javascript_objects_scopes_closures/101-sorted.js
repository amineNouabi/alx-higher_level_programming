#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

Object.values(dict).forEach(value => {
  if (!Object.keys(newDict).includes(value)) {
    newDict[value] = [];
  }
});

Object.keys(dict).forEach(key => {
  newDict[dict[key]].push(key);
});

console.log(newDict);
