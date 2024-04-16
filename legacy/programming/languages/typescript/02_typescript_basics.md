## Basics of typescript
Here we will see the basics of the typescript language.

### Declaring variables:
For declaring variables, there are two recommended e:

- `const`: Creates a constant variable, that is, it's value never changes.
- `let`: Creates a variable that can be assigned to new values over time.

These two are recommended because they are kept in the scope where they are declared safer than the `var` way.

### Usual types:
Variables in typescript can have the following types:

```typescript
let foo: string
let bar: boolean
let baz: number
let qux: string[]
let qix: [number, string]            //tuple
let qax: { [key: number]: string }
let qox: Set<number>

foo = 'hello'
bar = true
baz = 23
qux = ['i', 'o', '1']
qix = [3, 'oi']
qax = { 123: "hello", 345: "hy" }
qox = new Set([1, 2, 3])
```

We have strings, boolean, number, an array of strings, a tuple with a number and a string. A dictionary with number keys and values as strings and there is a set which is a type of number.

**obs:** These two lines do the same thing:

```typescript
console.log(a['c'])
console.log(a.c)
```

But this don't work if the key is a number. In this case only the first notation will work as expected.

**obs:** The tuple isn't supported in JavaScript and, instead, works like an array. In typescript it is forced as an tuple, that is, the types and size are explicitly determined when the variable is declared. 
**obs:** The set is similar to an array but it don't admits duplicated values.

### Classes:
They are templates that can be used when creating custom objects.
Here goes a simple example:

```typescript
class Cat {
  name: string

  constructor (name: string) {
    this.name = name
  }

  walk(steps: number): void {
    console.log(this.name + ' the cat is walking ' + steps + ' steps.')
  }
}

const Cat = new Cat("felina")
Cat.walk()
```
The constructor is called when the object is created. In it you can add computations and declarations to modify the state of the object which is represented by the constants inside it.

**obs:** You can extend classes as well with the proper syntax. What it will do is have everything defined in the based class plus what you create in this derived one.
check the example bellow extending the class we created in the example before:
```typescript
class myCat extends Cat { 
  ownerName: string

  constructor (name: string, ownerName: string) {
    super(name)
    this.ownerName = ownerName
  }

  getOwnerName ():void {
    console.log(this.ownerName)
  }
}
```
**obs**: Super calls the mother class constructor, its necessary for derived classes. You can use `super.name` for example to refer to something declared in the mother class (a function, for example, in the derived class).

### Interfaces:
Interfaces can ensure that a given class follows or conform to specific rules that you can determine.

```typescript
interface IAnimal {
  name: string
  age: number

  feed(food: string, amount: number): void
}
```

To a class be checked against the interface you must indicate with the following syntax:
```typescript
class Cat implements IAnimal {
  name: string
  .
  .
  .
}
```
**obs:** The class can have its own custom methods not determined in the interface, but it must have everything in there.

### Abstract classes
Are a mixture of interfaces with derived classes. You can create a class with optional methods and properties, but also indicate which methods and properties must be implemented in the derived class.
That can be done with the following code:

```typescript
abstract class Animal {
  abstract name: string
  age: number

  constructor(age: number) {
    this.age = age
  }

  feed(food: string, amount: number): void {
    console.log('feeding ' + name + ' ' + food + ' by ' + amount)
  }

  abstract walk(steps: number, how: string, isFast: boolean)
}
```
**obs:** In this case `name` must be defined in the derived class. Putting `abstract` before a method will have the same result but the body (implementation must be created in the derived class).

### Access modifiers
All classes support access modifiers which deal with allowing 'external to the class' methods to access some class functionalities or variables.
By default everything inside a class is public. if you declare something as `private` it will only be readable inside the class context.
```typescript
abstract class Animal {
  public abstract name: string
  private age: number

  constructor(age: number) {
    this.age = age
  }

  protected feed(food: string, amount: number): void {
    console.log('feeding ' + name + ' ' + food + ' by ' + amount)
  }
}
```
One important thing to notice is that when compiled to JavaScript it will not have the private keyword as it is just enforced in the typescript part. If you want to force the behavior in the JavaScript as well initiate the variable name with `#` to do it and don't need to use the keyword `private` anymore.
If you want your variable to be accessible in subclasses as well use the `protected` access modifier.

### Static members
The members are everything defined in the class, so methods, constructor and properties (variables). By establishing static members you set a variable to be shared by all class instances (they will all point to the same thing in memory). 

```typescript
abstract class Animal {
  static private name: string
  private age: number
}
```
So if a class has only static members it doesn't even make sense creating various instances of it as they will all refer to the same thing. this is a way of create singletons as well without to much focefuu.

### imports and exports in ES6
It's common to separate your code in various files. So importing is how you fetch the code from a different file.
To have access to a module or variable from another file you must first `export` it from it's implementation script. That can be done as follows:

```typescript
export default abstract class Animal {
  static private name: string
  private age: number
}
```
In this case you will be able to import the class using `import Animal from '../path';` Without the default you would need to do something like `import { Animal } from '../path';`.
In the compiler options it's important to use `"module": "CommonJS",` as node isn't capable of reading this syntax, only the old one with`require`.
