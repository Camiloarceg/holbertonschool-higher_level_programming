#!/usr/bin/node
const oldDict = require('./101-data').dict;
const newDict = {};
for (const value of Object.values(oldDict)) {
  newDict[value] = [];
}
for (const [key, value] of Object.entries(oldDict)) {
  newDict[value].push(key);
}
console.log(newDict);
