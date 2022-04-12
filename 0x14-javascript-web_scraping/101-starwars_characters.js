#!/usr/bin/node
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');

function getNames (characters) {
  const characterUrl = characters.shift();
  if (!characterUrl) {
    return;
  }
  request(characterUrl, function (err, response, body) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(JSON.parse(body).name);
    getNames(characters);
  });
}

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  getNames(JSON.parse(body).characters);
});
