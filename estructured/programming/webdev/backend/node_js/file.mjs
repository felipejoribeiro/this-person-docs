// File 1
import {largeNumber} from './file_2.mjs'
import path from 'path'


const __dirname = path.resolve(path.dirname(''));
const a = 4;
const b = 5;

setTimeout(() =>{
	console.log(a+b);
}, 1000)

console.log(__dirname);
console.log(largeNumber);
