#!/usr/bin/node
let list = process.argv;
list = list.slice(2, list.length);
if (list.length > 1) {
  const sortedList = list.sort((a, b) => a > b ? -1 : 1);
  console.log(sortedList[1]);
} else {
  console.log(0);
}
