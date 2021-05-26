# The connection of back and front end
Here we will see how to connect a react app front end to a node back end. This is done with `http` calls from the front in the back end address. First thing to test our Backend API is to check the response of a fetch command, as follows:

```javascript

  componentDidMount() {
    fetch('http://localhost:3000/')
      .then(response => response.json())
      .then(console.log) // this is the same as data => console.log(data)
  }
```

This can be done in the `App` class and it will send a `GET` request in the chosen link.

For this to work you will need a `cors` package, you can install it with `npm install cors`. This have to be done in the back end side. And in the back end code this must be done:

```javascript
const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors())
```

This middlewere activates the Cross-origin resource sharing. This http-header based protocol is important to enable the client to take resources from more than one server and we need him to take information from the react app server and the restfull api. The mechanism also checks if the chosen addres outside the page server is functional.

Then, after enabling this kind of interaction `fetch` commands become possible. For executing that on the client side here goes an example:

```javascript
fetch('http://localhost:2033/signin', {
  method: 'post',
  headers: {'Content-Type':'application/json'},
  body: JSON.stringify({
    email: "output_email",
    password: "output_password"
  })
}).then(response => response.json())
  .then(input => {
    if (input === "ok"){
      doSomeThing();
    }
  })
```

Here we send an email and a password for the back end and we take the response probably passing it to an autentication process of some sort. Here we specify the addres, the `http` protocol, the headers and what goes into de body. In this case some `JSON` data. Note that this is an `Async` function therefore we need to couple the following proceedings with the `then` statement.

In conclusion, now we can have two servers runing, they can be in the same machine or even in different servers. And bouth front and back end can comunicate with ease.
