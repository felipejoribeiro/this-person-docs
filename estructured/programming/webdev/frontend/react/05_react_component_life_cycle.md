# React components life cycle
Every component that we create goes through series of events as they are rendered, loaded and updated. So we will see the most important ones. In React `16.3` this changed a log.

- The `render` method is an example. His job is too determine what and how the component will be rendered in the screen. Everytime the state changes, react will call this function again, to update what is on the screen.

- The `componentDidMount` is other method that is called when the component is mounted in the screen. In the first time the component shows up on the screen. But the method just runs once. Re-renders do not remount the component. But when new components are loaded. The thing that usually is used in this method is to retrieve data that is necessary for a component from an `API`.

- The `componentWillReceiveProps` this method is called everytime `props` are passed to a component. A common usecase is to run some logical operations in the props to check something in the props and change some states or something like that. It receives the `nextProps` input that is the new props that are arriving. But this was deprecated starting in `16.3`. Until the `17.0` version they renamed the component to `UNSAFE_componentWillReceiveProps` so you can still use it, but after the new release it will be completely disabled.

- The `shouldComponentUpdate` Every time `React` asks itself if a component needs to update, it will update. And that is not the best approach in some circunstancies, in large applications, as it can be expensive computationally-wise. This method stipulates rules to weather or not the app needs to update. It will receive the incoming `props` and the income `state`, and in the body you need to return `true` or `false`, to sinilize weather the component needs to be re-rendered.

- The `componentWillUnmount`. This method is called when the component will be discarted. And it can performe some cleaning and changes to the state. One good use case is to remove some event listenner associated to that component, for example.

- The `componentDidUpdate(prevProps, prevState)`. This method is called everytime when the component is updated. So when you change the state of a component It will render again and then will call this method. So it is called as last thing after an update. Then you must avoid completely change state in this component as it will create a infinity loop, because it will change the state that will trigger a new update.

Here are some references about the life cycle methods that wil change:

All life cycle methods before the change:
https://engineering.musefind.com/react-lifecycle-methods-how-and-when-to-use-them-2111a1b692b1

The change:
https://reactjs.org/blog/2018/03/29/react-v-16-3.html#component-lifecycle-changes

Summarizing, the three `life cycle` methods that will cease to existe are:

- componentWillMount()
- componentWillReceiveProps()
- componentWillUpdate()

The reason react deprecated those was that they caused problems frequently and were source of confusion in the development comunity. They where substituted by two new life cycle components:

- `getDerivedStateFromProps(props, state) {return newState}`
- `getSnapshotBeforeUpdate()`






