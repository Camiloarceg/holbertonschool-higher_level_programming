#!/usr/bin/node
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  JSON.parse(body).characters.forEach(characterUrl => {
    request(characterUrl, function (err, response, body) {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
