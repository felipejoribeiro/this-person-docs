const express = require('express');

const app = express();
const port = 2033;
app.use(express.urlencoded({extended: false}));
app.use(express.json());

const database = {
	users: [
		{
			id: '123',
			name: 'John',
			email: 'john@gmail.com',
			password: 'cookies',
			entries: 0,
			joined: new Date()
		},
		{
			id: '124',
			name: 'Kele',
			email: 'Keile@gmail.com',
			password: 'bananas',
			entries: 0,
			joined: new Date()
		}
	]
}

app.get('/', (req, res) => {
	res.send(database.users);
})

app.post('/signin', (req, res) => {
	if (req.body.email === database.users[0].email && req.body.password === database.users[0].password) {
		res.json('success');
	}else{
		res.status(404).json('Error logging in :\(');
	}
})

app.post('/register', (req, res) => {
	const{email, name, password} = req.body;
	database.users.push({
		id: '125',
		name: name,
		email: email,
		password: password,
		entries: 0,
		joined: new Date()
	})
	res.json(database.users[database.users.length - 1]);
})

app.get('/profile/:id', (req, res) => {
	const {id} = req.params;
	let found = false;

	database.users.forEach(user => {
		if (user.id === id) {
			res.json(user);
			found = true;
		}
	});

	if (!found) {
		res.status(400).json("Não achei o meliante");
	}
})

app.put('/image', (req, res) => {
	const {id} = req.body;
	let found = false;

	database.users.forEach(user => {
		if (user.id === id) {
			found = true;
			user.entries++;
			return res.json(user.entries);
		}
	});
	if (!found) {
		res.status(400).json("Não achei o meliante");
	}
})

app.listen(port, () => {
	console.log('App is running on port ' + port.toString());
})
