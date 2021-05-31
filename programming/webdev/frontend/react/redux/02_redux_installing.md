# Installation of redux
Here we will see how to install the `Redux` library. This can be done in `npm`, with the `npm install redux` command.
With it installed, the first thing worth mention is that 90% of the code will stay the same. Redux will add some functionalities to the table.
Then you must install the interface package with the `npm install react-redux` command. It will connect only the containers with the central client state data-base. They will comunicate using this library.

It's important to talk about Redux Toolkit too. This tool can assist you with redux development simplifying things. But here we will work with plain `Redux` so that we can understand it's functionalities.

Now we can import this tool with:

```
import { Provider, connect } from 'react-redux'
```

### Creating the Store
Then we must create a `Store` that is the only source of truth. That is a big object that describes the state of our app.




