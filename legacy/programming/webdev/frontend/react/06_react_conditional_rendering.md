# Conditional rendering
This is important to enable rendering dependence on logic. Such ability is important in various use cases. For instance, if you have a call to a API and things will load for a bit, it is advised to sinilize that the app is loading something to the user. For that you can use a state variable `isLoading`, for example, to tell if something is loading.

```javascript

componentDidMount() {
        setTimeout(() => {
            this.setState({
                isLoading: false
            })
        }, 1500)
    }

```
Here is an example of something that can be slow to execute.

And the implementation is simple. You can have more than one `return()` statement that conditionally is triggered based in logic, for example. A way that this is done very commonly is by `ternary` operators as in the following example:

```javascript
function Conditional(props) {
    return (
        <div>
            <h1>Navbar</h1>
            
            {
              props.isLoading 
                ? <h1>Loading...</h1>
                : <h1>Some cool stuff about conditional rendering</h1>
            }
            
            <h1>Footer</h1>
        </div>
    )
}
```

It's important to make the state in witch the loading is determined be located in the same component that will display the loading screen, so that we avoid updating components that don't need to update. You can use `&&` too other than the `ternary`:

```javascript
{
  props.isLoading && <h1>Loading...</h1>
}
```

But in this case the component just checks wether o not something must be rendered.




