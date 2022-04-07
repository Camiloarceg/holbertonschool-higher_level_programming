#!/usr/bin/node
exports.esrever = function (list) {
  const rlist = [];
  let j = 0;
  const len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    rlist[j] = list[i];
    j++;
  }
  return rlist;
};
