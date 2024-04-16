# Decorator Pattern
It's a structural pattern, that allows you to attach additional responsibilities to an object at runtime. It can even add responsibilities recursively over and over again.

It can be used in both Object oriented and function oriented paradigms. It adds extensibility without the need to modify the original object.

You can nest decorators recursively.

Terminology:
- Component Interface: An interface for objects.
- Component: The object that may be decorated.
- Decorator: The class that applies the extra responsibilities to the component being decorated. It also implements the same component interface.

![uml](06.svg)

```typescript
// Decorator Concept Sample Code

interface IComponent {
    method(): string
}

class Component implements IComponent {
    method(): string {
        return 'Component Method'
    }
}

class Decorator implements IComponent {
    #object: IComponent

    constructor(object: IComponent) {
        this.#object = object
    }

    method(): string {
        return `Decorator Method(${this.#object.method()})`
    }
}

// The Client
const COMPONENT = new Component()
console.log(COMPONENT.method())

// The component can be decorated
const Decorated = new Decorator(COMPONENT)
console.log(Decorated.method())

// The decorated component can be decorated again
const Decorated2 = new Decorator(Decorated)
console.log(Decorated2.method())
```
Obs: Notice the private `#object` property.

So:
- Use this pattern to add responsibilities to objects dynamically without affecting the inner object.
- Its best to have an option to remove the decorator from an object in case you no longer need it.
- Comparing to extending the decorator is mor flexible as you can easily add/remove the decorators at runtime.
- A decorator shouldn't modify the internal objects data or references. This allows the original object to stay intact if the decorator is later removed.
