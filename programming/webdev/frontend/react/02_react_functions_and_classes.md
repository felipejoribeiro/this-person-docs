# React functions and classes
The react components are functions or classes. If they are functions they must `return` the elements that will be rendered, as follows:

```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Carla" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

```

In this case we have only functions composing the react app. All of then returns `DOM` elements which are javascript constructs created to simplify the understanding. Remember, this isn't `HTML` or `PHP`, it's plain `JavaScript` but we have access to these `html` like structures when we import the `React` library. This **JavaScript** with flavors of **HTML** is known as `.jsx`.

### Props

The input arguments of the function is called `props`, and they are passed through the `jsx` element sintax as shown. Note that every time that you must insert javascript elements inside the `HTML` sections you must wrap the code in brackets, otherwise it will interpret it as plain text.

Other than `Props` the children are passed as well. It is recommended to always start a component name with Capital letters as `React` treats components starting with lowercase letters as `DOM` tags, like `<div>`.

It's recommended to give names to `Props` that refers to the components point of view and not the applications's perspective.

A final observation that worth mention is that all `Props` must be pure functions, that is, they must not modify the content of it's props. They are `read only`.

If the props aren't served then they will be `null` in the component. And will not be rendered. But this don't break the component. If the props are used as text in the component they will not be displayed. But this may cause issues if more complex logic operations aremade withe these. This is important as you can create styles that react logically to these situations creating components that are more reusable.

A way of using these `components` with `Props` is with ` array_b = array.map(function)`, that is a higher order array method. It takes a function as parameter and parses the array with it. Other methods that worth mention are `filter`, `reduce` and others. It will return an array of thing. It can be an array of components, and in this case this cab simply be placed directly in the `jsx` and things will render as expected.

### Child
If your react component has child components, a developer can access then with a `this.props.children` statement. It returns a array, containing the references to the child React node instances. Here goes an example:

```javascript
var Parent2 = React.createClass({
  componentDidMount: function() {
	//access to <span>child2text</span>, if only one child no array used
	console.log(this.props.children);
	//would log child2text, because I am grabbing the child of the <span>
	console.log(this.props.children.props.children);
  },

  render: function() {return <div />;}
});

var Parent = React.createClass({
  componentDidMount: function() {
	//access to array, containing <div>test</div><div>test</div>
	console.log(this.props.children);
	//would log childtext, because I am grabbing the child of the first <div> in the array
	console.log(this.props.children[1].props.children);
  },

  render: function() {return <Parent2><span>child2text</span></Parent2>;}
});

ReactDOM.render(
  <Parent><div>child</div><div>childtext</div></Parent>,
  document.getElementById('app')
);
```
Check out this `crazy` sintax. There are numerous ways of doing things. Here we can se the component acessing it's children.

There are some good methods to take note:
-`React.Children.map(this.props.children, function(){})`: Invoke every immediate child contained and passa function. Returns an array.
-`React.Children.forEach(this.props.children, function(){})`: Like the above but doesn't return array.
-`React.Children.count(this.props.children)`: Returns the number of times that a callback passed to map or forEach would be invoked, that is, the number of child components.
-`React.Children.only(this.props.children)`: Return the only child, and if there is more than one throws.
-`React.Children.toArray(this.props.children)`: Returns a simple array of children elements.

### React Functions
One of the ways in witch we can create components is with functions. The convention is to create components with Capital first letter and CammelCase. Then you must return the `jsx` that the component must render. Like follows:

```javascript
import React from "react"
import ReactDOM from "react-dom"

function MyApp() {
  return (
    <div>
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
    </ul>
    <ol>
    </ol>
    </div>
  )
}

ReactDOM.render(
  <MyApp />,
  document.getElementById("root")
)
```
The element then can be referenced in `jsx` like a `HTML` tag. But you could implement this function in a different file and import it. In that case you would need to export it there, but we will see that in a moment.

It is important to notice that you can only return one element, not two. In the latter case you must wrap everything in a `<div></div>` tag.

Other convention to naming, When dealing with `React` components is to give the same name of the component to the file where it is stored, like, if we were to move the `<MyApp/>` component definition to a different file it would be placed in `MyApp.js`.

So the app above can be translated as follows: 


```javascript
import React from "react"

function MyApp() {
  return (
    <div>
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
    </ul>
    <ol>
    </ol>
    </div>
  )
}
export default MyInfo
```

```javascript
import React from "react"
import ReactDOM from "react-dom"
import MyApp from "./MyApp"

ReactDOM.render(
  <MyApp />,
  document.getElementById("root")
)
```
Notice that when we import an `jsx` file the extencions is optional. And we need to import `React` always to have access to the `jsx` tags. These tags are called `Elements` and they represent vanilla `HTML` elements in our `DOM`.

### React Classes
Class based components are interesting. They can store state and deal with events. As we can define functions in there and let then handle events. they too must return some rendered components. Here goes the minimal example of `class` component:

```javascript
class App extends React.Component {
  yourMethodHere() {
    console.log("hy")
  }

  render() {
    yourMethodHere()
    return (
      <div>
        <h1>Code goes here</h1>
      </div>
    )
  }
}

export default App
```

The  render method returns What must be rendered, but it can execute logic as well. Which will occur when the class is rendered. That is usefull for conditional styling and other things. and the class can accept `Props` too. That can be accomplished with `this.props.value`.


