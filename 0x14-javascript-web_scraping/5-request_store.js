#!/usr/bin/node
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
