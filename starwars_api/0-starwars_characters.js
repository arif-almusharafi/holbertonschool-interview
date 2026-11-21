#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

function getJson (link) {
  return new Promise((resolve, reject) => {
    request(link, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function main () {
  const film = await getJson(url);
  for (const link of film.characters) {
    const person = await getJson(link);
    console.log(person.name);
  }
}

main().catch((error) => console.log(error));
