# Installing Node Js
On this archive we will see how to install node in a fresh installed machine.

### Debian
If you have a Debian based server, than all you need to do to have the node LTS edition is the following commands:

```bash
sudo apt update
sudo apt install nodejs npm
```

### Arch 
If you have a Arch based system install with pacman the required package:

- nodejs-lts-fermium - For 14.X version
- nodejs-lts-erbium - For 12.X version
- nodejs-lts-dubnium - For 10.X version

```
sudo pacman -S nodejs-lts-dubnium
```

## To check your node installation
To se if node is installed and it's version, you can run the following command:

```
node -v
```
If this command results in a version on the prompt, you can now run node, just like python and you will see it's terminal on the screen where you can performe mathematical opperations proving that javascript is indeed runing in your box.

## JavaScript on the terminal
It's interesting, for example, that, different from the brownser javascript, here, we don't have some objects that we took for granted there. Like the window object. Those are not defined here. But we have others that are essential in the server side. 

One example is the `global` object. It has a bunch of things we can use. We wont be able to execute 'global.fetch' and 'document' too, for example. Because, once more, these are objects declared in the brownser execution of javascript only.

More one object that we have here is the `process` object, that comes with information about the javascript process. One important command that resides in `process` is the `process.exit()` that terminate the node instance and get you back to your bash session.

## Executing JavaScript scripts with node
Now that we have a JavaScript interpreter we can execute scripts just like python (again). For example, executing the following code with the command `node file.js` results in `9` and `<path>` in the console:

```javascript
const a = 4;
const b = 5;

setTimeout(() =>{
	console.log(a+b);
}, 3000)

console.log(__dirname);
```

Something interesting is that, if you call the command `globalThis` in the javascript that is running in your brownser, the value returned will be the `window` object. If you run this command in the desktop, in node, you will receive the `global` object. So, the thing is, despite having different names, with different elements, `globalThis` is the same thing in both instances, so we can have a unified codebase.

## Loading local modules in node
Something really important in node is de ability to import other codes as libraries. There are some methods for that to work. The first one is using vanilla node, and is the legacy solution. You just use this code to import object from file_2 to file:

```javascript
// File 1
const file_2 = require('./file_2.js')

const a = 4;
const b = 5;

setTimeout(() =>{
	console.log(a+b);
}, 1000)

console.log(__dirname);
console.log(file_2.largeNumber);
```

```javascript
//file_2
const largeNumber = 356;

module.exports = {
	largeNumber: largeNumber
};
```

But there is a way of using ES6 expressions from node version 12 and beyond, what is better as the syntax is more palatable. The functions turn into `import {largeNumber} from './file_2.mjs'` and `export const largeNumber = 356`. This can be done in two ways:
- The first way is by changing the extension name to `file.mjs` as hinted before. This is important to tell to the node interpreter to use ES6 syntax.

- The other way is to run `npm init -y` to create a `package.json` file in the project folder. There you can instruct node to consider modules in a ES6 way by defining `"type":"module"` inside the `package.jason` file.

## The three types of modules in node
There are three kind of modules in node. First there is the ones you create like the ones we studied above. 

There is also the build in modules, that are modules that come pre installed in node. Like the `const c = require('fs')` module that comes with all sorts of utilities for reading the file system. Like read through a text file and extract how many time the word "hello" appears with `const c = require('fs').readFile`. Other module very important is the `const c = require('http')` that is used for web server.

The third and last type is the **npm** packages. To install node packages, first you must run `npm init -y` and then some thing like `npm install nodemon --save-dev` to install the nodemon package. The "--save-dev" flag is for packages that are only used in development. In this case the package create a live update instance that will keep looking your source files and keep executing your code when there is a change. This is interesting as automate the `node file.js` work flow. That is possible adding the line `"start":"nodemon",` in the scripts part of the `package.json` file. Then you can call `npm start` to start running code.

