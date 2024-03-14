---
id: 99_js_examples
aliases: []
tags: []
---

# Examples of javascript application:

## About objects

```javascript
let object = {
  name: "hy, there",
  date: "october, 10th",
  nationality: "brasilian",
};

console.log({ ...object });

let var_name = "hello";

object = {
  ...object,
  [var_name]: "caio",
};

console.log(object);

let objeto = {
  casa: "hello",
  horario: "hy",
  visto: "brasilian",
};

let { casa, visto } = objeto; //pass copy

let objeto_2 = objeto; //pass reference

let objeto_2 = { ...objeto }; //pass copy

console.log(visto);

console.log(Object.values(objeto)); //return stored values as list

console.log(Object.keys(objeto)); // return the names of values

console.log(Object.entries(objeto)); // turn the object into a list

let oi_object = Object.fromEntries(oi); //convert to object
```

## About arrays

```javascript
let hello = [1, 2, 3, 4, 5, 6];

hello.forEach((i) => {
  console.log(i);
});

let hello_plus_one = hello.map((i) => {
  return i + 1;
});

let hello_filtered = hello.filter((i) => i > 3);

let hello_reduced = hello.reduce((a, b) => a + (a > b), 0); // sum all elements
let hello_reduced = hello.reduce((a, b) => a + (4 > b), 0); // counts elements <4

let hello_2 = hello; //passed reference. Alterations in hello_2 will reflect in hello

hello_2.push(3);

let hello_2 = [].concat(hello); //copy

let hello_3 = hello.flat(i); // concatenate elements if they are arrays in i levels
```

## About logic operations

```javascript
while (i<10) {
  console.log(i)
  i++
}

do {console.log(i)} while (i<10)

false ? console.log("true") : console.log("false")

switch (var) {
  case "oi":
    console.log("oi")
  case "la":
    console.log("la")
  default:
    console.log("?")
}

For (item of array) {console.log(item)}
for (item in object) {console.log(item)} // return keys
for (item in object) {console.log(object.item)} // return keys
for (item in objeto) {console.log(objeto[item])} // return values
```

## Others

```javascript
"hello".include("o"); // check if there is "o" in the string, can be used with strings.

"hello".padEnd(10); // add spaces
"hello".padStart(10); // add spaces
"hello".trimStart(); // take off spaces
"hello".trimEnd(); // take off spaces
```
