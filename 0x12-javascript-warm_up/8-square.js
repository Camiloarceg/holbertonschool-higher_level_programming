#!/usr/bin/node
const size = parseInt(process.argv[2]);
let string = '';
if (!size) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  string = '';
  for (let j = 0; j < size; j++) {
    string += 'X';
  }
  console.log(string);
}
