# React
React is a javascript library for building user interfaces. It's possible to insert react components in an html page as **React** was made to be gradually adopted.

### The motivation


### HTML implementation
You will need to create an **DOM Container** in your `html`, that consists of a html element with a specific id like:

```html
<!-- ... existing HTML ... -->

<div id="like_button_container"></div>

<!-- ... existing HTML ... -->
```

The component can be empty as **React** will populate it with other child elements. You will need to also the library and a javascript script to write your `React` code. For that you can use some `<script>` html tags as follows:

```html
<!-- Load React. -->
<!-- Note: when deploying, replace "development.js" with "production.min.js". -->
<script src="https://unpkg.com/react@17/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js" crossorigin></script>

<!-- Load our React component. -->
<script src="like_button.js"></script>

</body>
```
Then, we have our library loaded before our script, so it will be available, even if you don't have `npm` installed or `node`. The dependencies will be downloaded in the client machine.

### JavaScript implementation
Now that we have our `docking point` in the web page, we can write our component. Like the one ahead:

```javascript
'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);
```

And that's it. The final function will render the component in the specified `html` component. You can reuse this component too, in other elements in the page.

Interestingly enough, when you create a `React app` there will be an file called `Index.js` that will have something like this:

```javascript
import React from 'react'
import ReactDOM from 'react-dom'
import App from './containers/App.js'
import './index.css'

ReactDOM.render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>,
  document.getElementById('root')
)
```
With is just the same function saw before, but here it encapsulate all page creating what is known as a `React app`. The element where `React` renders itself is on the pages `root` component. So the frame work occupies the complete page.

Is worth mentioning that the `App` component is imported too from other `javascript` code. It's another react component in a structure known as `component composition`.
