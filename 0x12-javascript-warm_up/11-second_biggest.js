#!/usr/bin/node
const badList = process.argv;
if (!badList[2] || !badList[3]) {
  console.log(0);
} else {
  const goodList = badList.slice(2, badList.length);
  const sortedList = goodList.sort((a, b) => a > b ? -1 : 1);
  console.log(sortedList[1]);
}
