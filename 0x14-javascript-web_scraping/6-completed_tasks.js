#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const users = {};

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  JSON.parse(body).forEach(entry => {
    if (entry.completed === true) {
      users[entry.userId] = users[entry.userId] + 1 || 1;
    }
  });
  console.log(users);
});
