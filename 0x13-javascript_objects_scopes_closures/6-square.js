#!/usr/bin/node

const SquareOld = require('./5-square');

class Square extends SquareOld {
  charPrint (c) {
    let char = 'X';
    if (c) {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
