# React styling with css.
Here we shall learn how to style our web app. We will do that with `CSS` language. There are several ways of doing that.

### With Class declaration

First here goes the most familiar and common way, with `CSS` classes and `CSS` classes definitions:

```javascript
import React from "react"

function App() {
    return (
        <header className="navbar">This is the header</header>
    )
}

export default App
```

Notice that we use `className` other than `class` that is used in vanilla `HTML`. The reason for that is that `jsx` uses javascript `DOM` manipulation under the rood. So if we remember how to add a class to a `HTML` element using pure javascript, that is done as follows:

```javascript
document.getElementById("something").className += " new-class-name"
```

Other than that, everything will remain the same as dealling with `CSS` in a pure `HTML` page so, `SASS` can be applyied normally to generate the `CSS` as well as other tools you may have found by working with legacy code.

Other important thing is that the only thing you can apply `className` definitions are elements (pure `jsx`) and not your components.

Finally, at last, when you use `FlexBox` for example, do not mention your component names there as they will not end up in your `DOM`. Refere to the main element inside it instead.

### With inline Styling
Direct style determination, via inline styling, isn't recommended as it contradicts the separation of concerns principle. But may suit debuging needs, or prototyping endeavour.
For that you cant just define the style property as done in vanilla `HTML` (`<h1 style='font-size:12px'>oi</h1>`), as it will result in a error.
So, to do that we need to meet the `jsx` way of doing inline style. That is done as follows:

```javascript
<h1 style={{color: "#4d4d4d", backgroundColor: "#474747", fontSize: "200px"}}>Title</h1>
```

Notice first that we have two pairs of brackets. The first one is necessary to reference javascript code and the second one is to reference a javascript object. So the style property accepts only a javascript objects as input in contrast to the string that vanilla `HTML` accepts. A consequence is that we can't use `background-color` as in vanilla `html`, we need to use CamelCase notation. Sudo selectors such as column and rover are impossible to use. In those cases you must use `CSS` classes determination. There are libraries that can be usefull to address these limitations too.
Using inline styling is interesting too because it enables the dev to make logical determinations too, as you can alter the style javascript object in your code with conditional statements.

