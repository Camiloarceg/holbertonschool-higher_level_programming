#!/usr/bin/node
let x = parseInt(process.argv[2]);
if (!x) {
  console.log('Missing number of occurrences');
}
while (x > 0) {
  console.log('C is fun');
  x -= 1;
}
