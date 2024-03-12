#!/usr/bin/node

const firstarg = parseInt(process.argv[2]);
if (Number.isInteger(firstarg)) {
  console.log('My number: ' + firstarg);
} else {
  console.log('Not a number');
}
