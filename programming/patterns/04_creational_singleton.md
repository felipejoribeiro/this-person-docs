# Singleton Pattern
Some times you need am object in an application where there is only one instance.

So you don't want many versions of this object going around the run time of the application. It could be a database connection or the life bar of you game character. So this type of implementation allows for the creation of many instances of a class but they all must point to the same place in memory.

So this is the Singleton's definition a class that can be instantiated many times but all these instances point to the same implementation in memory. It can be accessed globally but it's not a global  variable. It can be instantiated many times, but with exception of the first they will always reference the first created.

![uml](./data/05.svg)

```typescript
// Singleton Concept Sample Code

export class Singleton {
    // The Singleton Class
    static instance: Singleton
    id: number

    constructor(id: number) {
        this.id = id
        if (Singleton.instance) {
            return Singleton.instance
        }
        Singleton.instance = this
    }
}

// The Client
// All uses of the singleton point to the same original object

const OBJECT1 = new Singleton(1) // setting its id property to 1
const OBJECT2 = new Singleton(2) // setting its id property to 2

console.log(OBJECT1 === OBJECT2) // = true
console.log(OBJECT1.id) // returns 1
console.log(OBJECT2.id) // returns 1
```
obs: Notice the `static` being used to force the reference. So it's not the same thing as using all `static` properties and functions as if a class inherits another there could be some problems.

So: 
- There must be only one copy of the singleton that can be instantiated throughout the code.
- You want the atributes of the singleton to be globally accessible without the need for global variables.
- You want controlled access to a sole instance.
