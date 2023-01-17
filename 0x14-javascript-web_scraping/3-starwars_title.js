#!/usr/bin/node
const request = require('request');
let t_url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(t_url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
