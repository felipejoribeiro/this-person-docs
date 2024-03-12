# Facade Pattern
Some times you have a system that becomes quite complex over time as more features are added or modified. It may be useful to provide a simplified API over it.

Essentially it is an interface that simplifies or reduces existing interfaces abstracting its complexity.

It can also be considered as a high level interface that shields the consumer from the unnecessary low-level complications of integrating into many subsystems.

![uml](./data/08)

```typescript
// The Facade pattern concept

class SubSystemClassA {
    // A hypothetically complicated class
    method(): string {
        return 'A'
    }
}

class SubSystemClassB {
    // A hypothetically complicated class
    method(value: string): string {
        return value
    }
}

class SubSystemClassC {
    // A hypothetically complicated class
    method(value: { C: number[] }): { C: number[] } {
        return value
    }
}

class Facade {
    // A simplified facade offering the services of subsystems
    subSystemClassA(): string {
        // Uses the subsystems method
        return new SubSystemClassA().method()
    }

    subSystemClassB(value: string): string {
        // Uses the subsystems method
        return new SubSystemClassB().method(value)
    }

    subSystemClassC(value: { C: number[] }): { C: number[] } {
        // Uses the subsystems method
        return new SubSystemClassC().method(value)
    }
}

// The Client
// Calling potentially complicated subsystems directly
console.log(new SubSystemClassA().method())
console.log(new SubSystemClassB().method('B'))
console.log(new SubSystemClassC().method({ C: [1, 2, 3] }))

// or using the simplified facade instead
const FACADE = new Facade()
console.log(FACADE.subSystemClassA())
console.log(FACADE.subSystemClassB('B'))
console.log(FACADE.subSystemClassC({ C: [1, 2, 3] }))
```

So:
- Use when you want to provide a simple interface to a complex subsystem.
- You want to layer your subsystem into an abstraction which is easier to understand.
- Abstract Factor and Facade can be considered very similar. An abstract Factory is about creating an interface over several creational classes of similar objects, whereas the facade is more like an API layer over many creational, structural and/or behavioral patterns.
- The Mediator is similar to the Facade in the way that it abstracts existing classes. The Facade is not intended to modify, load balance or apply any extra logic. A subsystem does not need to consider that existence of the facade, it would still work without it.
- A Facade is a minimal interface that could also be implemented as a Singleton.
- A Facade is an optional layer that does not alter the subsystem. The subsystem does not need to know about the Facade, and could even be used by many other facades created for different audiences.
