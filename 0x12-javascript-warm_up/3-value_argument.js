#!/usr/bin/node
// a script that prints the first argument passed to it
const arr = process.argv;
console.log(arr[2] ? arr[2] : 'No argument');
