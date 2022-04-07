#!/usr/bin/node
const data = require('./100-data').list;
console.log(data);
const newData = [];
data.map(function (val, index) {
  newData[index] = val * index;
  return newData;
});
console.log(newData);
