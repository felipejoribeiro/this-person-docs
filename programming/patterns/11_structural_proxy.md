# Proxy Pattern
The Proxy design pattern is a class functioning as an interface to another class or object.

A proxy could be for anything, such as a network connection, an object in memory, a file, or anything else you need to provide an abstraction between.

Types of proxies:

- Virtual Proxy: An object that can cache parts of the real object, and then complete loading the full object when necessary.
- Remote Proxy: Can relay messages to a real object that exists in a different address space.
- Protection Proxy: Apply an authentication layer in front of the real object.
- Smart Reference: An object whose internal attributes can be overridden or replaced.

Additional functionality can be provided at the proxy abstraction if required. E. g., caching, authorizing, validation, lazy initialization, logging.

The proxy should implement the subject interface as much as possible so that the proxy and subject appear identical to the client.

Terminology:
- Proxy: An object with an interface identical to the real subject. Can act as a placeholder until the  real subject is loaded or as gatekeeper applying extra functionality.
- Subject interface: An interface implemented by both the proxy and real subject.
- Real subject: The actual real object that the proxy is representing.
- Client: The client application that uses and creates the proxy.


![uml](./data/12.svg)

```typescript
// A Proxy Concept Example

interface ISubject {
    // An interface implemented by both the Proxy and Real Subject
    request(): void
    // A method to implement
}

class RealSubject implements ISubject {
    // The actual real object that the proxy is representing

    enormousData: number[]

    constructor() {
        // hypothetically enormous amounts of data
        this.enormousData = [1, 2, 3]
    }

    request() {
        return this.enormousData
    }
}

class ProxySubject implements ISubject {
    // In this case the proxy will act as a cache for
    // `enormous_data` and only populate the enormous_data when it
    // is actually necessary

    enormousData: number[]
    realSubject: RealSubject

    constructor() {
        this.enormousData = []
        this.realSubject = new RealSubject()
    }
    request() {
        // Using the proxy as a cache, and loading data into it only if
        // it is needed
        if (this.enormousData.length === 0) {
            console.log('pulling data from RealSubject')
            this.enormousData = this.realSubject.request()
            return this.enormousData
        }
        console.log('pulling data from Proxy cache')
        return this.enormousData
    }
}

// The Client
const PROXY_SUBJECT = new ProxySubject()
// Use the Subject. First time it will load the enormous amounts of data
console.log(PROXY_SUBJECT.request())
// Use the Subject again, but this time it retrieves it from the local cache
console.log(PROXY_SUBJECT.request())
```
So:
- Proxy forwards requests onto the Real Subject when applicable, depending on the kind of proxy;
- A virtual proxy can cache elements of a real subject before loading the full object into memory;
- A protection proxy can provide an authentication layer. For example, an NGINX proxy can add Basic authentication restriction to a http request.
- A proxy can perform multiple tasks if necessary.
- A proxy is different than an Adapter. The adapter will try to adapt two existing interfaces together. The proxy will use the same interface as the subject.
- It is also very similar to the Facade, except you can add extra responsibilities, just like the decorator. The decorator however can be used recursively.
- The intent of the proxy is to provide a stand in for when it is inconvenient to access a real subject directly.
- The proxy design pattern may also be called the surrogate design pattern.
