#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
fs.readFile(args[2], function (err, data) {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(args[4], data, function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
fs.readFile(args[3], function (err, data) {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(args[4], '\n' + data,
    {
      encoding: 'utf8',
      flag: 'a',
      mode: 0o666
    },
    function (err) {
      if (err) {
        return console.error(err);
      }
    });
});
