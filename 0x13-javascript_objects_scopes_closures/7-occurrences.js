#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let curr = 0;
  for (const i of list) {
    if (i === searchElement) {
      curr++;
    }
  }
  return curr;
};
