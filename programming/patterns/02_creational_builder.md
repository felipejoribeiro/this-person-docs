# Builder Pattern
This is a creational pattern just like the factory one. Which provides a way of separating the construction of a complex object from its representation, so that you can use the same construction process to build different representations.

Problems the builder tries to solve:
- How a class create different representations of a complex object?
- How can a class that includes creating a complex object be simplifies?

So, as you can see this and the factory pattern are very similar but the differ by the fact that it is direct to an object. So, instead a class returning directly an object, it calls the builder which returns it.

Terminology:
- Product: The product being built.
- Builder interface: The interface that the concrete builder should implement.
- Builder: Provides methods to build and retrieve the concrete product. Implements the **Builder Interface**.
- Director: Has a `construct()`method that when called creates a customized product using the methods of the **Builder**.
- Fluent interface: is the chaining of methods to describe the object created.

![uml](./data/03.svg)

```typescript
// Builder Concept Sample Code
class Product {
    parts: string[] = []
}

interface IBuilder {
    buildPartA(): this
    buildPartB(): this
    buildPartC(): this
    getResult(): Product
}

class Builder implements IBuilder {
    // The Concrete Builder
    product: Product

    constructor() {
        this.product = new Product()
    }

    buildPartA() {
        this.product.parts.push('a')
        return this
    }

    buildPartB() {
        this.product.parts.push('b')
        return this
    }

    buildPartC() {
        this.product.parts.push('c')
        return this
    }

    getResult() {
        return this.product
    }
}

class Director {
    // The Director, building a complex representation

    static construct() {
        'Constructs and returns the final product'
        return new Builder()
            .buildPartA()
            .buildPartB()
            .buildPartC()
            .getResult()
    }
}

// The Client
const PRODUCT1 = Director.construct()
console.log(PRODUCT1.parts)
```
As you can se, the complexity is only related to building this complex object and all the code is dedicated to creating the final object.
So the factory pattern deals with abstractions related to instantiating wile the builder patter deals with abstractions related to construction. Its lower level in this sense.

So:
- The builder patter is used to create more complex objects.
- The builder pattern should be able to construct complex object in any order and include/exclude whichever available components it likes.
- You can use an **Abstract Factory** to add an abstraction between the client and Director.
