# Introduction to Redux
The `Redux` tool is a state manager that help the developer to manage what is saved in memory. So, before this tool all state was implemented in components. So there was states that were implemented in componentes down the hierarch and up, and all this information had to interact well throughalt the app. In big apps this logical jungle becomes very difficult to sustain. So for that the `Redux` library creates a general state and all components interacts with it.

It got inspiration from database design. So it concentrates information and makes easily available throughalt the entire app. So this solution is ideal for big apps with lots and lots of containers and components. Bear in mind that without this, if a component down in the hierarch wants to alter a state that is saved up the hierarch it has to comunicate with all nodes between. So, not very good.

### Motivation
Most of `React` apps are implemented with `redux`, that is important because React is mainly a graphical tool, but memory management is comblestome. Sharing memory between containers is difficult as they often aren't directly related, causing the developer to create a route for this data through the app. To solve this `Redux` is implemented with three principles in mind:

- Single source of truth: Only one database with data.
- State is read only: So we don't modify it, a new state is created always.
- Changes using pure functions: A pure function receives a input and returns an output.

The process which defines `redux` is the following:

	Action ==> Reducer ==> Store ==> Make changes

- Action: Is an event, like the click of a buton, or a drop down menu.
- Reducer: Is a pure function, that receives the action and creates the new state.
- Store: Store is the created new state.
- Make changes: React notices the change in state an redraw.

This appears more complicated than something like `jquery`, but things are more controllable and organized. For instance, here is a flow chart of what `jquery` does:

	Action ==> Make changes
	Action ==> Make changes
	Action ==> Make changes
	Action ==> Make changes
	Action ==> Make changes

In the mean time, here is what `Redux` do:

	Action  -.
	Action   |
	Action    > Reducer ==> Store ==> Make changes 
	Action   |
	Action  -' 

So whe can now understand relationship between actions and the present state extremely more easily, avoiding the constant state checking and repetitive rules that become necessaire when each action is an independent entity.

### The Flux Pattern
Architecture in software is used as a way to make sure that we are able to solve problems in a logical sense and in a organized fashion.
In this flux pattern there is the idea the you have an action, and you have a dispatcher, that handle the action and send information to a storage and then to the view. Like follows:

	Action ==> Dispatcher ==> Store ==> View

Before this, we hade `MVC`, that is "Model view controll", that is something like this:


                         .-> Model <----<.-----------------> View
                        /                 \
                       .  .> Model <-------\----------.<---> View
                       | /                  \        /
	Action ==> Controller + -> Model <---------`<-----/------> View
                       | \                         /
                       '  .> Model <-----<.------<'--------> View
                        \                  \   
                         '-> Model <--------`<-------------> View

So the controller listen to what events, and depending on then he activates models. These models then update the view. The problem here is that the models are independent and don't know about each other and must look at the view or some kind of chared memory to know what is happening.

One thing that is interesting is that both methods can coexist, so depending on the application, you can still use then together.






