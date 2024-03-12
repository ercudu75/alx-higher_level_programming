#!/usr/bin/node

let first_arg = parseInt(process.argv[2]);
if (Number.isInteger(first_arg)){
	console.log('My number: ' + first_arg);
}
else {
	console.log('Not a number');
}
