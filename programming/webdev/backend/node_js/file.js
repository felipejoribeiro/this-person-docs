// File 1
const file_2 = require('./file_2.js')

const a = 4;
const b = 5;

setTimeout(() =>{
	console.log(a+b);
}, 1000)

console.log(__dirname);
console.log(file_2.largeNumber);
