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

The input arguments of the function is called `props`, and they are passed through the `jsx` element sintax as shown. Note that every time that you must insert javascript elements inside the `HTML` sections you must wrap the code in brackets.

Other than `Props` the children are passed as well. It is recommended to always start a component name with Capital letters as `React` treats components starting with lowercase letters as `DOM` tags, like `<div>`.

It's recommended to give names to `Props` that refers to the components point of view and not the applications's perspective.

A final observation that worth mention is that all `Props` must be pure functions, that is, they must not modify the content of it's props. They are `read only`.

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

