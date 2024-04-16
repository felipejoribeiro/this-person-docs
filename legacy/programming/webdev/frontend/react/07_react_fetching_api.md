# Fetching data fro an API
On this section we will see how to fetch data fro an `API`.

## The componentDidMount life cycle method
For fetching information from an `API`, the method that is most used is the life cycle method. This will run something in the moment a component is loaded to the screen. And it isn't called with re-renders.

## Promisses
We will use promisses in this sections as the `fetch` command is async. If you need to refresh this subject in your mind here goes a good article about the topic:
https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-promise-27fc71e77261

## Implementation
So, to fetch some data from an `API` we use the following structure in the code:

```javascript
componentDidMount() {
        this.setState({loading: true})
        fetch("https://swapi.dev/api/people/1/")
            .then(response => response.json())
            .then(data => {
                this.setState({
                    loading: false,
                    character: data
                })
            })
    }
```
Observe how beautiful and `declarative` is the syntax. If you were to use `jquery` to create this application things would get pretty `imperative` and nasty pretty quickly with constant `queries` by id.



