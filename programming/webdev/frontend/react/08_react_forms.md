# Forms in React
With forms we can get data from users and send it to the backend. Pretty nice and necessary stuff in this day and age. It's farely tricky to deal with `forms` in React. You must understand `state` really well. The documentation for this follows ahead:

https://reactjs.org/docs/forms.html

## Implementation
In vanilla `JavaScript` you must create the form in `HTML` and submit it through `http` protocol. With all the information nice and gathered. It's different from the `React` way, in which you store the information in the component's state:

```javascript
class App extends Component {
    constructor() {
        super()
        this.state = {
            firstName: "",
            lastName: ""
        }
        this.handleChange = this.handleChange.bind(this)
    }
    
    handleChange(event) {
        const {name, value} = event.target
        this.setState({
            [name]: value
        })
    }
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input 
                    type="text" 
                    value={this.state.firstName} 
                    name="firstName" 
                    placeholder="First Name" 
                    onChange={this.handleChange} 
                />
                <br />
                <input 
                    type="text" 
                    value={this.state.lastName} 
                    name="lastName" 
                    placeholder="Last Name" 
                    onChange={this.handleChange} 
                />
                <h1>{this.state.firstName} {this.state.lastName}</h1>
                <button>Submit</button>
            </form>
        )
    }
}
```

Here we have some interesting things to analyse. The input fields have it's `values` determined by `state`. That is important to assure that what is in the box is the present state and avoid bugs. Other thing that worth mention is the `handler` of change that receives the event with information about what is happening. The `name` propertie is important too, as it is used to identify what `form` is being changed and is passed to the `onChange` handler with the change content. The `placeHolder` text don't go to state too. It's just a visual thing that appears when the `form` is empty, so it indicates that the state is empty.

One thing that is very important as well is the `handleChange` method. Notice that it creates a copy of the state before changin it. That's advised as it avoid bugs. So the following code is bad practice and must be avoided:

```javascript
handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }
```

Because the `setState` is reading state as well, which isn't good. A last observation is that the name of the state value is being determined by a variable. This can be done by wraping the variable in square brackets.

The submit button will trigger the `handleSubmit` method that can send `json` to an `API` or something.

## Textarea
The `textarea` form element is very similar to the `input` element (which is different from the pure `HTML` way). Here goes an example:

```javascript
<textarea value={"Some default value"}/>
```

And in pure `HTML` we have:

```html
<textarea 
    name="about" 
    cols="30" 
    rows="10"
    onChange={this.handleChange}> 
        The initial text...
</textarea>
```

## Checkbox
Check box are done as follows in React:

```javascript
<input 
  type="checkbox"
  name="isSomething"
  checked={this.state.isSomething}
  onChange={this.handleChange}
  />
```

Observe that it doesn't have a `value` property. The value is stored in the `checked` property that is a `bollean`. 

## Radio
The radio uses the `value` and `checked` properties. As follows:

```javascript
<label>
    <input 
        type="radio" 
        name="gender"
        value="male"
        checked={this.state.gender === "male"}
        onChange={this.handleChange}
    /> Male
</label>
<br />
<label>
    <input 
        type="radio" 
        name="gender"
        value="female"
        checked={this.state.gender === "female"}
        onChange={this.handleChange}
    /> Female
</label>
```

But the `checked` isn't a `boolean` anymore.

## Select
The Select has child components, as follows:

```javascript
<select 
    value={this.state.favColor}
    onChange={this.handleChange}
    name="favColor">

    <option value="blue">Blue</option>
    <option value="green">Green</option>
    <option value="red">Red</option>
    <option value="orange">Orange</option>
    <option value="yellow">Yellow</option>

</select>
```

The value will be setted as the chosen option.




