# Express, the back end go to library
When we are in the Front End we can use React to enhance our lives as developers. The frame work can simplify things and really help in the development process. We have something similar for the back end. The **Express** library is a `Javascript` frame work for better development of back ends. It automates boring tasks and do a bunch of stuff for us.

## Installing Express on a project
The first thing that needs to be done is installing the library:

```
npm install express
```

Than we can create a basic server with the following code present in `server_2.js`:

```javascript
const express = require('express');

const app = express();

app.get('/', (req, res) => {
	const user = {
		name: 'sally',
		hobby: 'soccer'
	}
	res.send(user);
})

app.listen(2033);
```

Or, for a html page:

```javascript
const express = require('express');

const app = express();

app.get('/', (req, res) => {
	res.send('<h1> hello </h1>');
})

app.listen(2033);
```
Note that we don't need to specify the type of the response. That is pretty handy already.

## Middleware


