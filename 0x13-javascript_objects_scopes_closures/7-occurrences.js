#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (val) {
    if (val === searchElement) {
      count += 1;
    }
  });
  return count;
};
