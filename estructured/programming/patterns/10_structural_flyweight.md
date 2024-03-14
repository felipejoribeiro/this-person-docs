# Flyweight Pattern
Fly in the term Flyweight means  light/not heavy.

Instead of creating thousands of objects that share common attributes, and result in a situation where a large amount of memory or other resources are used, you can modify your classes to share multiple instances simultaneously by using some kind or reference to the shared object instead.

The best example to describe this is a document containing many words and sentences and made up of many letters. Rather than storing a new object for each individual letter describing its font, position, color, padding and many other potential things. You can store just a lookup id of a character in a collection of some sort and then dynamically create the object with its proper formatting etc., only as you need to.

This approach saves a lot of memory at the expense of using some extra CPU instead to create the object at presentation time.

The Flyweight pattern, describe how you can share objects rather than creating thousands of almost repeated objects unnecessarily.

When describing flyweights, its useful to describe in terms of:
- Intrinsic: (in or include) are the attributes of a flyweight that are internal and unique from the other flyweights. An example is each letter of the alphabet.
- Extrinsic: (outside or external) are the attributes that are used to present the flyweight in terms of the context where it will be used. One example would be the fact that the letters must be aligned, so the positions where they should go.

Terminology:
- Flyweight Interface: An interface where a flyweight receives its extrinsic attributes.
- Concrete Flyweight: The flyweight object that stores the intrinsic attributes and implement the interface to apply extrinsic attributes.
- Unshared Flyweights: Not all flyweights will be shared, the flyweight enables sharing, not enforcing it. It also possible that flyweights can share other flyweights but still not yet be used in any contexts anywhere.
- Flyweight Factory: Creates and manages flyweights at runtime. It reuses flyweights in memory, or creates a new one in demand.
- Client: The client application that uses and creates the Flyweight.

![uml](11.svg)

```typescript
// The Flyweight Concept

interface IFlyweight {
    code: number
}

class Flyweight implements IFlyweight {
    // The Concrete Flyweight
    code: number
    constructor(code: number) {
        this.code = code
    }
}

class FlyweightFactory {
    // Creating the FlyweightFactory as a static class

    static flyweights: { [id: number]: Flyweight } = {}

    static getFlyweight(code: number): Flyweight {
        // A static method to get a flyweight based on a code
        if (!(code in FlyweightFactory.flyweights)) {
            FlyweightFactory.flyweights[code] = new Flyweight(code)
        }
        return FlyweightFactory.flyweights[code]
    }

    static getCount(): number {
        // Return the number of flyweights in the cache
        return Object.keys(FlyweightFactory.flyweights).length
    }
}

class AppContext {
    // An example context that holds references to the flyweights in a
    // particular order and converts the code to an ascii letter
    private codes: number[] = []

    constructor(codes: string) {
        for (let i = 0; i < codes.length; i++) {
            this.codes.push(codes.charCodeAt(i))
        }
    }

    output() {
        // The context specific output that uses flyweights
        let ret = ''
        this.codes.forEach((c) => {
            ret =
                ret +
                String.fromCharCode(FlyweightFactory.getFlyweight(c).code)
        })

        return ret
    }
}

// The Client
const APP_CONTEXT = new AppContext('abracadabra')

// use flyweights in a context
console.log(APP_CONTEXT.output())

console.log(`abracadabra has ${'abracadabra'.length} letters`)
console.log(
    `FlyweightFactory has ${FlyweightFactory.getCount()} flyweights`
)
```

So: 
- Clients should access Flyweight objects only the through a `flyweightfactory` object to ensure that they are shared.
- Intrinsic values are stored internally in the Flyweight.
- Extrinsic values are passed to the Flyweight and customise it depending on the context.
- Implementing the flyweight is a balance between storing all objects in memory, versus storing small unique parts in memory, and potentially calculating extrinsic values in the context objects.
- Use the flyweight to save memory when it is beneficial. The offset is that extra CPU may be required during calculating and passing extrinsic values to the flyweights.
- The flyweight reduces memory footprint because it shares objects and allows the possibility of dynamically creating extrinsic attributes.
- The contexts will generally calculate the extrinsic values used by the flyweights, but it is not necessary. Values can be stored or referenced from other objects if necessary.
- When architecting the flyweight, start with considering which parts of a common object may be able to be split and applied using extrinsic attributes.
