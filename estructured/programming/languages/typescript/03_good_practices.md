## Good practices with typescript
When writing typescript code, it's better to follow good practices to avoid problems down the line with unreadable and unmaintainable code. Here we will present a set of guidelines to deal with typescript:
- Strict type checking;
- Linters;
- Interfaces and type Aliases;
- About using tuples;
- The `any`, `Unknown` and `never` types;
- Using the `keyof` operator;

### 🚧 - Strict type checking
In typescript it's possible to configure the compiler to not use strict type checking. To ensure that your code is being checked for types, make sure to properly configure your `tsconfig.json`. Namely, make sure that you have the following configuration set: `"strict": true,`. Having this line in said file will ensure that your types are the expected ones.

### 🚧 - Linters
When dealing with code, it's useful not to meet errors only in the compiling or testing stages of your codebase. Linters do exactly that. They scan your code wile you write it, checking for errors and wrong types when dealing with typescript.

Some good linters are:
- **TSLint**: A typescript specific linter that is great for handling **codeActions**, it is a series of actions that can be triggered by the developer when an error is identified or at arbitrary times. Some examples are: **ApplyFix**, **renameFile**, **renameSymbol**, etc... Check the docs of your IDE to know how to install and configure it to your need.
- **ESLint**: The most used Linter for general **Javascript**. It can be used for typescript though as well. But make sure to properly configure your `.eslintrc.js` to allow for typescript checks. That can be accomplished with the following configuration:
```javascript
module.exports = {
  root: true,
  extends: '@react-native-community',
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  overrides: [
    {
      files: ['.ts', '.tsx'],
      rules: {
        '@typescript-eslint/no-shadow': ['error'],
        'no-shadow': 'off',
        'no-undef': 'off',
      },
    },
  ],
};
```
- **eslint_d**: Makes the **eslint** the fastest linter on the planet. It runs an ESLint server on the background bringing the lint time from `700 miliseconds` to `160`. Sometimes can cause issues when you change libs or eslint configurations, but all cab be resolved by running the `eslint_d restart` command which restarts the server and reset cached values.
- **Prettier**: A great plugging to ensure code formatting. It doesn't check for errors but how your code is formatted. Like, if there is space between your object elements and the brackets: `{ jonny: hello }`. And it comes with code actions to apply formatting rules. These are great to apply developing patterns and make your codebase consistent. Which improve greatly readability. The configuration can be set to comply to popular templates.

### 🚧 - Using Interfaces and Type aliases
Interfaces and Type aliases are great options to avoid in-line type declarations, that are fine for simple symbols but can get pretty clunky pretty quickly for complex objects. You can create separated files to determine types and import these types to use them in your objects. This make the code as easy to read as **javascript**, but with all the benefits of strict type checking. You can even use interfaces inside interfaces which is great for very complex objects. Aliases can be used as well and they are great as they allow for merging and other interesting operations. As a rule of thumb, here's a list for when to use each type definition:
- **Primitive types**: Something like `type Name = string` can only be done by alias;
- **Arrays**: Representations like `type Names = string[]` is better when done with alias, for more consise syntax;
- **tuples**: Interfaces can't represent tuples, so alias it is: `type Point = [number, number]`;
- **functions**: The alias syntax, once more, is much better to read: `type log = (message: string) => void`; 
- **Unions type**: Alias allows for union of types as well, so here is a tip: `type Status = "pending" | " working" | "complete"`;
- **Objects**: Here the interface seems better, but type aliases allow for composition with unions which is pretty useful, here is an example:
```typescript
type StringActions =
  | { type: "loading" }
  | { type: "loaded"; data: string[] };
type NumberActions =
  | { type: "loading" }
  | { type: "loaded"; data: number[] };
type Actions = StringActions & NumberActions;
```

So, in summary, it's better to use type aliases in most cases. Interfaces can be used for classes though.

### 🚧 - About using tuples
Great way of representing fixed sized arrays of elements with different types and specific order. Here is an example of a 3D vector tuple: `let point: [number, number, number] = [ 1, 1, 1 ]`. You can even create the type to make it easy to read:

```typescript
type CoordinateX = number;
type CoordinateY = number;
type CoordinateZ = number;
type Vector3D = [CoordinateX, CoordinateY, CoordinateZ] | undefined;
type ApplyMovement = (inputA: Vector3D, inputB: Vector3D) => Vector3D;

let position: Vector3D = [0, 0, 1];
let movement: Vector3D = [1, 3, 1];

const updatePosition: ApplyMovement = (currentPosition, moveTo) => {
  let nextPosition: Vector3D = currentPosition;
  if (currentPosition && moveTo) {
    const [x, y, z] = currentPosition;
    const [dx, dy, dz] = moveTo;
    nextPosition = [x + dx, y + dy, z + dz];
  }
  return nextPosition;
};

updatePosition(position, movement);
```
Remember that tuples can't be directly added, so it's a good practice to create handlers for it. The best way to deal with these values is with classes, that can define these types and declare the handlers to deal with then.

### 🚧 - The `any`, `Unknown` and `never` types
Using the `any` type allows for the developer not to declare the types. But as a powerful tool it must be used with extreme caution. It makes typescript behave like typescript. It can be used in moments where the types are really unknown, like when dealing with libraries that doesn't offer type declarations, or with dynamically created objects like:
```typescript
function log(data: any) {
  console.log(data);
}
```
But always you must try to provide the most specific types to avoid problems.

The `unknown` type is an example. Its more specific than the `any` type. Typescript will always ask you to check the type before any operation when using `unknown`, assuring type safety in your code:

```typescript
function print(input: unknown) {
 if (typeof input === "string") {
   console.log(input);
 } else {
   console.log("Not a string");
 }
}
```
Finally, the `never` type is used to indicate that a value should never exist. So for example, you can assure that a function will never return a value this way. Here is an example: 

```typescript
function division(numerator: number, denominator: number): number | never {
  if (denominator === 0) {
    throw new Error("Division by zero ocurred!")
  }
  return numerator / denominator;
}
```
Then you indicate that the function, sometimes, will not return a value, but only throw an error.

### 🚧 - Using the keyof operator
The keyof operator is incredible to retrieve the types of the keys of a given symbol. It's useful for type compliance that aim at object keys. It returns a union of all types of the keys of the input object.
Here is a usage example:
```typescript
interface User {
  name: string;
  age: number;
}
function getKeyValue<Object, Key extends keyof Object>(obj: Object, key: Key) {
  return obj[key];
}
let user: User = { name: 'John', age: 30 };
console.log(getKeyValue(user, 'name'));
```

# Source of information:
- [21 best typescript practices](https://itnext.io/mastering-typescript-21-best-practices-for-improved-code-quality-2f7615e1fdc3#97cf)
- [when to use type vs interfaces](https://www.carlrippon.com/when-to-use-type-aliases-v-interfaces/)
