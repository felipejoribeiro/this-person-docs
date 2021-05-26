# The fs module is very importante
`fs` is relative to "file system". So we can import this module that comes pre-installed in node with `const fs = require('fs')`. It gives the ability to access the computer file system. Lets see an example:

Era uma vez um lugarzinho no meio do nada com cheiro de terra e sabor de vez aluguel aminésia. 

```javascript
fs.readFile('./hello.txt', (err, data) => {
  if (err) {
    console.log("there is an error");
  } 
    console.log(data.toString());
})

console file = fs.readFileSync('./hello.txt');

```

This code will read the file `hello.txt` in the directory where the `server.js` is located. The data is converted to strings and logged in the console. Note that the `readFile` command is asynchronous. And the `readFileSync` is synchronous. For a server is very important to use async commands to not block the execution of the program.

If you try to read a file that doesn't exist it will result in an error.

## The append command
You can, beside reading information, write too. For doing that you will use the `appendFile()` command as shown bellow:

```javascript

fs.appendFile('./hello.txt', 'this text will be written', err => {
  if (err) {
    console.log(err);
  }
})

```
If the file doesn't existe it will be created.

## The write command
There is also the `writeFile` command, that will write on the chose file.

```javascript

fs.writeFile('./hello.txt', 'this text will be written', err => {
  if (err) {
    console.log(err);
  }
})

```

## The delete command
You can delete files too with the `unlink` command.
```javascript

fs.unlink('./hello.txt', err => {
  if (err) {
    console.log(err);
  }
  console.log("deleted")
})
```

With those commands we can save information in the server. We can read an excel file with the right library. Send emails and do all sorts of things. A server is a programmable robot that you can configure as you will.
