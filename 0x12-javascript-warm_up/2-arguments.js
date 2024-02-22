#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed
const arg = process.argv.length;
console.log(arg === 2 ? 'No argument' : arg === 3 ? 'Argument found' : 'Arguments found');
