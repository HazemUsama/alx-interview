#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, { json: true }, async (err, res) => {
  if (!err) {
    const characters = res.body.characters;
    for (const characterUrl of characters) {
      await printCharacter(characterUrl)
    }
  }
});

async function printCharacter (characterUrl) {
  const res = await new Promise((resolve, reject) => {
    request(characterUrl, { json: true } ,(error, res) => {
      if (error) {
        reject(error);
      } else {
        resolve(res.body.name);
      }
    });
  });
  console.log(res);
}
