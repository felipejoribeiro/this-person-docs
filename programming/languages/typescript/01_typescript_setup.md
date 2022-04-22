# Initial steps with Typescript
The first thing one must do to start playing with typescript is to install node in one's machine. After that you must use **NPM** to install the **typescript compiler**, that can be done with teh following command:

```
sudo npm install -g tsc
```

This is a compiler. That's due to the fact that **typescript** is compiled to **javascript** which than can be run with node or in the browser.

To use the compiler you can issue the following command:

```
tsc ./src/test.ts --outDir ./dist
```

In this example we take the file `test.ts` and we compile it to javascript inside the `./dist` directory.

Here is an example of compilation:

```typescript
\\ test.ts
function foo(bar: string) {
	return 'Hello, ' + bar
}

let baz = 'ABC'

console.log(foo(baz))
```
The code above is compiled on the code bellow:

```javascript
\\ test.js
function foo(bar) {
	return 'Hello, ' + bar;
}
let baz = 'ABC';
console.log(foo(baz));
```

So the compiled code is safe from a type point of view, that means that it expects that `bar` is always a string.
