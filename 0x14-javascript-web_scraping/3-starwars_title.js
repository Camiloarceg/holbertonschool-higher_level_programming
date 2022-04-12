#!/usr/bin/node
const args = process.argv;
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
