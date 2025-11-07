const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello World</title>
  <meta name="description" content="A simple hello world page">
</head>
<body>
  <h1>Hello World!</h1>
  <p>Welcome to our test CI application.</p>
</body>
</html>`);
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
