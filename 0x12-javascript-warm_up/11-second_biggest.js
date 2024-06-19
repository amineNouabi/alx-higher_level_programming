#!/usr/bin/node

let biggest = 0;
let secondBiggest = 0;

for (let i = 0; i < process.argv.length; i++) {
  const current = parseInt(process.argv[i], 10);
  if (!isNaN(current) && current > biggest) {
    secondBiggest = biggest;
    biggest = current;
  }
}

console.log(secondBiggest);
