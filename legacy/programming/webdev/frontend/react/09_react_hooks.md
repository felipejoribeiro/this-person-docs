# Introduction to react Hooks
From the React `16.8` we have this concept of React Hooks. In the way things where done before, it's really hard to reuse statefull logic. When we want to reuse logical functions this becomes a real challenge. Besides that, when components grow in size and complexity they can become really hard to understand. Things like `componentDidUpdate`, `componentDidMount` or `componentDidUnmount` can be a challenge to comprehend. But the bigest motivation, is that classes are confusing. Like `super props`. Hooks allows us to not use classes. Other major reason is that React wants to do ahead of the time compilation. The best way of learning is to convert an app that is done in vanilla react to a hooks aided one.

The changes will be registered here. Maybe, even without the context of all the app that will be converted, the information can be condensed and only details that are important will be covered. 

So, the central idea behind `hooks` is that you can use it in a function to "Hook into" the `React` app state and life cycle, making the use of classes obsolete. They can't even be used inside classes.

Before hooks, we only created function components without state, that is, they only return rendered component given the input values. if a component must have state, then we would have to make it a class.

The first thing is to import some libraries in the class script. You don't need to install anything, as it is implemented in React. Like follows:

```javascript
import React, {useState, useEffect} from 'react'
```

This will be used in the Hooks creation inside the function. So now we will convert a react class into a function with the use of these React Hooks:

```javascript
class App extends Component {
  constructor (props) {
    super(props)
    this.state = {
      robots: [],
      searchfield: ''
    }
  }

  componentDidMount () {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json())
      .then(users => { this.setState({ robots: users }) })
  }

  onSearchChange = (event) => {
    this.setState({ searchfield: event.target.value })
  }

  render () {
    const { robots, searchfield } = this.state
    const filteredRobots = robots.filter(robot => {
      return robot.name.toLowerCase().includes(searchfield.toLowerCase())
    })
    return()
  }
}

export default App
```
And the version after the implementation of hooks:

``` javascript
function App () {

	const [robots, setRobots] = useState([])
	const [searchfield, setSearchfield] = useState('')

	useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json())
      .then(users => { setRobots(users) });
	},[])

  const onSearchChange = (event) => {
    setSearchfield(event.target.value)
  }
  
	const filteredRobots = robots.filter(robot => {
		return robot.name.toLowerCase().includes(searchfield.toLowerCase())
	})
  return()
}

export default App
```

Observe that the `useState()` function returns an `Array` which the first element is the variable that references the state, and the second is the function to change the state.
If your state has various elements. For each one you must call the `useState()` function.

So the `useState()` is used to create the state and determine a variable to receive the state element and a function to alter it. And the `useEffect()` determine side effects from a function component. That is, logical operations that occurs from environment events like mount and umount.

Functions for life cycle like `componentDidMount`, `componentDidUpdate` and `componentWillUnmount` can be used with `hooks` too. With:

```javascript
useEffect(() => {
  //Logic
}, [variable, to, watch, change]);
```

If you don't declare the list, the effect will run with any change to the component, having the same effect as `componentDidUpdate`. And if you declare a empty list `[]`, it will have the same effect as `componentDidMount`.

To use `componentWillUnmount` we have to do something like this:

```javascript
useEffect(() => {
  //Logic
  return () => {
    // Logic to run when the component is umount
  }
}, []);
```

So, the returned function of the effect will be run when the component unmount.

That is not a reason to dump all classes from your code. These tools can be used together without problems. So you can use then with strategy.
And there is a bunch of legacy code that will stay implemented as classes. So be aware of both and know how to work with both.

Other thing is that Hooks are React specific, so they don't exist in general javascript.

You can build your own Hooks too ir you need more complex applications involving state.


