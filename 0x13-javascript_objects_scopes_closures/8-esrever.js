#!/usr/bin/node

exports.esrever = function (list) {
  const copy = list.slice();
  const n = Math.floor(copy.length / 2);

  for (let i = 0; i < n; i++) {
    const temp = copy[i];
    copy[i] = copy[copy.length - i - 1];
    copy[copy.length - i - 1] = temp;
  }
  return copy;
};
