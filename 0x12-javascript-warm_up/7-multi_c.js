#!/usr/bin/node
// a script that prints x times “C is fun”
const x = Math.floor(Number(process.argv[2]));
if (Number.isInteger(x)) {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
