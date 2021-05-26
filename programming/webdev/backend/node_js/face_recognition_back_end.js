const express = require('express');
const bcrypt = require('bcrypt-nodejs');
const cors = require('cors');

const app = express();
const port = 2033;
app.use(express.urlencoded({extended: false}));
app.use(express.json());

app.use(cors())

const database = {
	users: [
		{
			id: '123',
			name: 'John',
			email: 'John@gmail.com',
			password: '$2a$10$dEWC7TgviNTissZ.lDlod.FxUWHzwTQ37NzeR3Pjj0QTn83uXJA/O',//cookies
			entries: 0,
			joined: new Date()
		},
		{
			id: '124',
			name: 'Kele',
			email: 'Kele@gmail.com',
			password: '$2a$10$Z29wiyOM9uYVYSwQQs9rKuoimgXnIof4i/TZgtETVrn3RfviSthpO',//bananas
			entries: 0,
			joined: new Date()
		}
	],
	login: [
		{
			id: '987',
			hash: '',
			email: 'john@gmail.com'
		}
	]
}


app.get('/', (_, res) => {
	res.send(database.users);
})

app.get('/exit', () => {
	process.exit();
})

function check_pass(request){
	for(i = 0; i < database.users.length; i++){
		if (request.body.email === database.users[i].email){
			return [true, i];
		}
	};
	return [false, 0];
}

app.post('/signin', (req, res) => {
	[email_present, i] = check_pass(req)
	if (email_present){
		bcrypt.compare(req.body.password, database.users[i].password, function(_, res_comp) {
			if (res_comp){
				res.json({
					id : database.users[i].id,
					name : database.users[i].name,
					email : database.users[i].email,
					entries : database.users[i].entries,
					joined : database.users[i].joined
				});
			} else {
				res.status(400).json("Email or password incorrect")
			}
		});
	} else {
		res.status(400).json("Email or password incorrect");
	}
})

app.post('/register', (req, res) => {
	const{email, name, password} = req.body;
	bcrypt.hash(password, null, null, function(_, hash) {
		database.users.push({
			id: '125',
			name: name,
			email: email,
			password: hash,
			entries: 0,
			joined: new Date()
		});
		res.json({
			id : database.users[database.users.length - 1].id,
			name : database.users[database.users.length - 1].name,
			email : database.users[database.users.length - 1].email,
			entries : database.users[database.users.length - 1].entries,
			joined : database.users[database.users.length - 1].joined
		});
	});
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
		res.status(404).json("Não achei o meliante");
	}
})

app.put('/image', (req, res) => {
	console.log(req.body);
	const {id} = req.body;
	let found = false;
	console.log(id);
	database.users.forEach(user => {
		console.log(user.id);
		if (user.id === id) {
			console.log("achei");
			found = true;
			user.entries++;
			return res.json(user.entries);
		}
	});
	if (!found) {
		res.status(400).json("Não achei o meliante");
	}
})


// // Load hash from your password DB.
// bcrypt.compare("bacon", hash, function(err, res) {
//     // res == true
// });
// bcrypt.compare("veggies", hash, function(err, res) {
//     // res = false
// });

app.listen(port, () => {
	console.log('App is running on port ' + port.toString());
})
