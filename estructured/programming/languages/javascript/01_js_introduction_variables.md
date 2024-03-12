# Introduction to JavaScript
The language was created on 1995 in the **NetScape** browser. It was a way of adding logic to the page. Other browser created their versions and then they came to agree in a standard which was the creation of the language. And fast forward to today, we have frameworks, like `React`, `Node` and others, that are built over the raw language. Today it as much important as `html` and `css`.

The types that are supported are the following:
- Numbers: With all mathematical operations, like sum (+), subtraction (-), multiplication (*), power (**), mod(%) and division (/).
- Text: We can concatenate text by sum (+). If a number is summed to a text it is transformed in text.
- Boolean: We have the logical operators (=== , !==, !=, <=, <, >, >=, || and &&). Ao se somar booleans, eles são convertidos para números. Null conta como false.

For printing information to the screen, you can use the `console.log("text")`. For acquiring information from the user, one method is to use the `prompt()` function but it's only available in the browser. For node applications you can do something like this:

```javascript
const readline = require('readline').createInterface({
  input : process.stdin,
  output : process.stdout
})

let oi = 0

readline.question('hello', i => {
  console.log(i)
  oi = oi + i
  readline.close()
})

console.log(oi)
```

You can transforme a variable from one type in other with `number()` and `string()`. These are converter functions.

To define variables one can use `var variable = 9`, for example. There are objects that come declared. Like `console`, in the browser, or `process` in node applications.

## Adding javascript to your html page
Remember that `html` loads things linearly. So, when you put your `<script>` tag in your page, make sure that 





