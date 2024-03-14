# The five most important design patterns
---

On this document, we will discuss the five most important design patterns that are implemented on a daily basis in software engineering. The principles will be listed bellow and they are the basis of how to write good code.

## The Singleton principle
Almost every application implements these singletons in one or more areas of their inner functions. 
It states: Classes that are singletons just are "constructed" one time, That is, a object is created from the class in run time and all other calls refers to this same instance. So it is a limitation to just one construction per runtime for the class.

```csharp
public class SingletonDemo {
   private static SingletonDemo instance = null;
   
   private SingletonDemo() {
   }
   
   public static SingletonDemo getInstance() {
      if(instance == null) {
         instance = new SingletonDemo();
      }
      return instance;
   }
}
```

The method `getInstance()` makes sure that only one instance of the object is created. The construct is private and can only be assessed throw the function. There are lots scenarios where we only want one instance of a class opened.
The problem with this design pattern is that the function `getInstance()` is not thread-safe. So it's possible to exist more than one instance simultaneously.

## The Factory Pattern principle
Such principle is important as it frees a client routine of creating objects. This is nice because it separates a high level code from low level tasks as object creation. This is important too because it allows one to add new functionalities without breaking the Open-Close principle. This Design pattern is important as it enhance polymorphism in our code. With this method it's possible to not determine a type on the code in an concrete manner. As an alternative we can call a constructor that knows what to use. By doing that one can avoid creating cross dependency between a parent and a child class.

For example:

```csharp
public interface ICar
{
    void SetModel(string model);
}

public ICar GetCar(string brand)
{
    switch(brand)
    {
        case "bmw":
            return new BMW();
        case "audi":
            return new Audi();
        default:
            return null;
    }
}

class Audi : ICar
{
    private string _model;

    public void SetModel(string model)
    {
        _model = model;
    }
}

class BMW : ICar
{
    private string _model;

    public void SetModel(string model)
    {
        _model = model;
    }
}
```

This is bad. The class GetCar is a part of the client code. There are some problems:
- If the agency needs to add a new brand in the code, the client code would need to be modified. This breaks the open close principle.
- The code isn't very extensible. If the company needed different brands to appear in different client applications, each client would need to create it's own car brand query, and changes on these car brands would result in changes that wound have to be applied in each client code.



