#!/usr/bin/node

let i = 0;
exports.logMe = function (item) {
  if (item !== 'undefined') {
    console.log(i + ': ' + item);
    i++;
  }
};
