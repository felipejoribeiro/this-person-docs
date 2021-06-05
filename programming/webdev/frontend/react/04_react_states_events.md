# React States and events
State is information a component stores in itself. Props don't really apply as they can't be changed inside the component. And events are triggers that are activated with page interaction.


### State
States can only exist in `class` based components. The syntax goes as follows:

```javascript
class App extends React.Component {
    constructor() {
        super()
        this.state = {
            answer: "Yes"
        }
    }
    
    render() {
        return (
            <div>
                <h1>Is state important to know? {this.state.answer}</h1>
                <ChildComponent answer={this.state.answer}/>
            </div>
        )
    }
}

export default App
```

The `super()` method is important to the class to inherits things from the super class `React.Component`. Then you can determine the property `state` of the class. It can be accessed from anywhere in the class with `this.state`. In the `constructor()`, the initial values are determined, but they can be changed during the life cycle of the component.

The interesting thing is that changing the state aromatically changes what is rendered in the screen. And `React` goes in the components that receive the changed state and update then as well.

### Events
Events are very similar to vanilla `HTML`, like `onclick="myFunction()"`. The only difference is the reference method and the CamelCase. So in the case of `jsx` it would be `onClick={function(){}}`. And the function will be called when the `jsx` element is clicked in the page. Here goes an example:

```javascript
function App() {
    return (
        <div>
            <img onMouseOver={() => console.log("Hovered!")} src="./image"/>
        </div>
    )
}
export default App
```

We can use loads of events in `React`:

- Clipboard Events
- Composition Events
- Keyboard Events
- Focus Events
- Form Events
- Generic Events
- Mouse Events
- Pointer Events
- Selection Events
- Touch Events
- UI Events
- Wheel Events
- Media Events
- Image Events
- Animation Events
- Transition Events
- Other Events

Each one of these will check for some trigger in the page to call a function.

### Changing the state
Now that we can react to events would be nice to change the state of our component. To do that we can use special methods created just for that that came from `React.Component` through the `super()` method. One of these is the `this.setState()` that is used for changing state. You can't just modify the state directly like `this.state.value = "hello"`, you must use this new method for that as it does some other important things besides changing the state object. Here goes the examplo:

```javascript
class App extends React.Component {
    constructor() {
        super()
        this.state = {
            count: 0
        }
        this.handleClick = this.handleClick.bind(this)
    }
    
    handleClick() {
        this.setState({ count: 1 })
    }
    
    handleClick2() {
        this.setState(prevState => {
            return {
                count: prevState.count + 1
            }
        })
    }

    render() {
        return (
            <div>
                <h1>{this.state.count}</h1>
                <button onClick={this.handleClick}>Change!</button>
                <button onClick={this.handleClick2}>Yo!</button>
            </div>
        )
    }
}
```
The binding is necessary for allowing us to use `setState()`. But you can avoid it using arrow functions in the definition of the method:


```javascript
class App extends React.Component {
    constructor() {
        super()
        this.state = {
            count: 0
        }
    }
    
    handleClick = () => {
        this.setState(prevState => {
            return {
                count: prevState.count + 1
            }
        })
    }

    render() {
        return (
            <div>
                <h1>{this.state.count}</h1>
                <button onClick={this.handleClick}>Change!</button>
            </div>
        )
    }
}
```

In this way the binding isn't necessary.



