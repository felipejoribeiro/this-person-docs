# Prototype Pattern
The prototype pattern is good for creating objects that you don't have all the resources to make. A file you downloaded from the server may be large, but since it is already in memory, you could just clone it, and work on the new copy independentty of the original.

In the prototype interface you create  `clone` method that should be implemented by all classes that use the interface. How the clone method is implemented in the concrete class is up to you. You will need to decide whether a shallow or deep copy is required.
- A shallow copy, copies and creates new references one level deep,
- A deep copy, copies and creates new references for all levels.

In JavaScript you have mutable objects such as Arrays, Dictionaries, Sets and any custom Object you may have created. A shallow copy will create new copies of the object with new references in memory, but the underlying data, e.g., the actual element in an array, will point to the same memory location as the original array/object being copied. You must test this behaviour to be certain it carries these properties as shallow copies are much more easy to precess and store.

Terminology:
- Prototype Interface: The interface that describes the `clone()` method.
- Prototype: The Object/Product that implements the Prototype interface.
- Client: The client application that uses and creates the Proto Type.

![uml](04.svg)

```typescript
interface IProtoType {
    // interface with clone method
    clone(): this
    // The clone is deep or shallow.
    // It is up to you how you want to implement
    // the details in your concrete class
}

class MyClass implements IProtoType {
    // A Concrete Class
    field: number[]

    constructor(field: number[]) {
        this.field = field // any value of any type
    }

    clone() {
        return Object.assign({}, this) // shallow copy
        // return JSON.parse(JSON.stringify(this)); //deep copy
    }
}

// The Client
// Create an object containing an array
const OBJECT1 = new MyClass([1, 2, 3, 4])
console.log(`OBJECT1: ${JSON.stringify(OBJECT1)}`)

const OBJECT2 = OBJECT1.clone() // Clone
console.log(`OBJECT2: ${JSON.stringify(OBJECT2)}`)
// Change the value of one of the array elements in OBJECT2
// Depending on your clone method, either a shallow or deep copy
// was performed
OBJECT2.field[1] = 101

// Comparing OBJECT1 and OBJECT2
console.log(`OBJECT2: ${JSON.stringify(OBJECT2)}`)
console.log(`OBJECT1: ${JSON.stringify(OBJECT1)}`)
```
obs: This copied just the properties and not the methods so you couldn't call `const OBJECT3 = OBJECT2.clone()` for example as it doesn't have the methods implemented. How much information should be copied is specific to each implementation. You could make the `clone()` method accept an argument to determine if it returns a shallow or deep copy, for example, or any kind of copy.

So:
- It is used to create an object in run time.
- Methods aren't copied as well. If you want those than you should instantiate a new class member and not copy an existing one. This pattern is used to create a representation of the properties of an object.
- Having these clones means that you don't need to create many classes for specific combinations of objects. You can instantiate it once and clone it as you like.
- It can be used as a snapshot tool as well, so if you want a certain state in an object, you don't need to instantiate it and call all the methods to configure it, you can clone the one that has the desired atributes.
