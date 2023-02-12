# Adapter Pattern
Some times a class is written and you don't have the option of modifying their interface to suit your needs. This happens if the method you are calling is on a different system across a network, a library that you  may import or generally something that is not viable to modify directly for your particular needs.

The Adapter solve:
- How can a class be reused that does not have an interface that a client requires?
- How can classes that have incompatible interfaces work together?
- How can an alternative interface be provided for a class?

It is similar to a decorator in a sense that it wraps an object and is also used in runtime. But it's not designed to be used recursively.

Its an alternative interface over an existing interface. It can also implement new functionalities.

Terminology:
- Target: The domain specific interface or class that needs to be adapted.
- Adapter Interface: The interface of the target that the adapter will need to implement.
- Adapter: The concrete adapter class containing the adaption process.
- Client: The client application that will use the Adapter.

![uml](./data/07.svg)

```typescript
// Adapter Concept Sample Code

interface IA {
    methodA(): void
}

class ClassA implements IA {
    methodA() {
        console.log('method A')
    }
}

interface IB {
    methodB(): void
}

class ClassB implements IB {
    methodB() {
        console.log('method B')
    }
}

class ClassBAdapter implements IA {
    // ClassB does not have a methodA, so we can create an adapter

    #classB: ClassB

    constructor() {
        this.#classB = new ClassB()
    }

    methodA() {
        'calls the class b method_b instead'
        this.#classB.methodB()
    }
}

// The Client
// Before the adapter I need to test the objects class to know which
// method to call.
const ITEMS = [new ClassA(), new ClassB()]
ITEMS.forEach((item) => {
    if (item instanceof ClassB) {
        item.methodB()
    } else {
        item.methodA()
    }
})

// After creating an adapter for ClassB I can reuse the same method
// signature as ClassA (preferred)
const ADAPTED = [new ClassA(), new ClassBAdapter()]
ADAPTED.forEach((item) => {
    item.methodA()
})
```

So:
- It Adapts the object with a compatible set of properties and methods which can be used by a factory or client.
- You can do this when the parent class can't be modified to accommodate your codebase needs.
- They will most commonly just adapt existing functionalities of existing classes, but they can also implement new functionalities as well.
- It is similar to the Decorator patter except that it changes the interface to the object whereas the decorator adds responsibilities without changing the existing interface.
- It's similar to the Bridge pattern and may look identical after the implementation, but the intent is different. The Bridge is a result of refactoring existing interfaces, whereas the Adapter is about adapting over existing interfaces that are not viable to modify due to many existing constraints. 
