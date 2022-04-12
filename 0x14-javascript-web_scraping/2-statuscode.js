#!/usr/bin/node
const args = process.argv;
const request = require('request');
request(args[2], function (err, response) {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
