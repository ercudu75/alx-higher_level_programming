#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let curr = 0;
  for (i of list) {
    if (i === searchElement) {
      curr++;
    }
  }
  return curr;
}
