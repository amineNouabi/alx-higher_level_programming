#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

const usersCompleted = {};

request(url, (error, response, body) => {
  if (error) {
    console.log('Error: ');
    console.error(error);
    return;
  }
  if (!response || response.statusCode > 399) {
    console.log('HTTP Error: ', response && response.statusCode);
    return;
  }
  const todos = JSON.parse(body);

  todos.forEach(todo => {
    const userId = parseInt(todo.userId, 10);
    if (todo.completed) {
      if (!(userId in usersCompleted)) { usersCompleted[userId] = 1; } else { usersCompleted[userId]++; }
    }
  });

  console.log(usersCompleted);
});
