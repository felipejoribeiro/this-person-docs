const express = require('express');

const app = express();

app.use(express.urlencoded({extended: false}));
app.use(express.json());

// Middle ware
app.use((req,res,next) => {
	next();
})

app.get('/', (req, res) => {
	res.send('<h1> hello </h1>');
})

app.get('/profile/:id', (req,res) => {

  console.log(req.query);
	console.log(req.body);
  console.log(req.params);
  console.log(req.headers);

	res.send('success');
})

app.listen(2033);
