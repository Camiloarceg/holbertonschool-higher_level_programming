#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  let wedgeAntilles = 0;
  JSON.parse(body).results.forEach(movie => {
    movie.characters.forEach(character => {
      if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
        wedgeAntilles += 1;
      }
    });
  });
  console.log(wedgeAntilles);
});
