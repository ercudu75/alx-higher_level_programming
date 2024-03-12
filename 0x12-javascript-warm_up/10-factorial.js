#!/usr/bin/node

function fact (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * fact(n - 1);
}

const m = parseInt(process.argv[2]);

console.log(fact(m));
