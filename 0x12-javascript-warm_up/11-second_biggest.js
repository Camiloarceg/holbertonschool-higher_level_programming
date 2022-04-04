#!/usr/bin/node
let list = process.argv;
const array = [];
list = list.slice(2, list.length);
if (list.length > 1) {
  for (let i = 0; i < list.length; i++) {
    array.push(parseInt(list[i]));
  }
  const sortedList = array.sort((a, b) => a > b ? -1 : 1);
  console.log(sortedList[1]);
} else {
  console.log(0);
}
