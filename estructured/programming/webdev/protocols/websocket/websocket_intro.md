# Introduction to WebSocket
It is a protocol that allows the creation of a tunnel with bidirectional comunication between a client and a server. The protocol is part of the `html5` specification and is supported on the lattest version of the browsers.

## Comparing with HTTP
In the `http` protocol the communication is done by requests. So the client sends a request to the server that answer with a response and that is it. For each response there must be a request and the communication is unidirectional, so the server can't make a request to the client.

This is a problem to real time applications. As there is a delay for creating this connection each time. Even with `AJAX` things aren't as fast because under the rood the application is using `http`.

Now, using the `websocket`, the connection is continuous. So a new connection don't need to be created, it stays online wile the application is running in the client.

## How it works
It is based in events. So the browser and the server will emit events to each other. A good example is a chat application. In the conventional way, with `http` wile i'm typing a message, both browser are making requests continuously to see if there is another new message. So The client only will receive the message when the Server gives a message response to the request. The message isn't given automatically, but only over a request. With websocket, a persistent connection is made between each browser and the server. Then, the Server is able to send information to the client.
