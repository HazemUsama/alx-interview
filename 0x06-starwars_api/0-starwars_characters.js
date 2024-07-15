#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, { json: true }, (err, res) => {
  if (err) {
    return console.error('Request failed:', err);
  }

  const characters = res.body.characters;
  for (const characterUrl of characters) {
    request(characterUrl, { json: true }, (err, res) => {
      if (err) {
        return console.error('Request failed:', err);
      }
      const character = res.body.name;
      console.log(character);
    });
  }
});
