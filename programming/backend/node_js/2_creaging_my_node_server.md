# Creating the damn server
Now we will see how to create the server with node. The first thing we must do is indicate to nodemon our `server.js` file. That is done by editin the file `package.json` with the following line: `"start":"nodemon server.js"`.

You can populate the file with:

```Javascript

// Server development file
const http = require('http');

const server = http.createServer((request, response)=>{


  console.log('headers', request.headers);
  console.log('method', request.method);
  console.log('url', request.url);

  response.setHeader('Content-Type', 'text/html');
  response.end('<h1> Hello </h1>');

})

console.log("i hear you!. thanks for the request.");

server.listen(3000);

```

There we can se the importance of the `http` module. It is used for creating the `server` object that inputs a function that is called every time that there is interaction with the specified port (`server.listen(3000)`). The arguments of this function can be `request` and `response`. With request we can take information about the requesting client, like url, method, headers, with:

```Javascript 

console.log('headers', request.headers);
console.log('method', request.method);
console.log('url', request.url);

```
So with any request we can see all this information about the system making the request. Those are informations that came with the http request.

The `response` input can be used to program the response to the request. For example, `response.setHeader('Content-Type', 'text/html')` determines the type of the request and `response.end('<h1> Hello </h1>')` determine the response. Is interesting that for every reload on the page in an chrome browser, there is two requests, the one for the content to show on the screen and one for the favicon. I mean, here is the output for each "refresh" command with the server configured as above:

```
i hear you!. thanks for the request.
headers {
  host: '127.0.0.1:3000',
  connection: 'keep-alive',
  'cache-control': 'max-age=0',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36',
  accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-gpc': '1',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
  cookie: 'io=8x7bbBbJec_0bNOVAAAA'
}
method GET
url /
headers {
  host: '127.0.0.1:3000',
  connection: 'keep-alive',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36',
  accept: 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
  'sec-gpc': '1',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-dest': 'image',
  referer: 'http://127.0.0.1:3000/',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
  cookie: 'io=8x7bbBbJec_0bNOVAAAA'
}
method GET
url /favicon.ico
```

So the request for the favicon is made in the address `/favicon.ico` and is made autonomously for each refresh.

## Creating a node API
So now we can do all sort of things. One of those is that we don't need to response an `html`. We can answer http calls with jason, as an API. For that we must change the type of the response of course and the response, as we can see ahead.

```Javascript

// Server development file
const http = require('http');

const server = http.createServer((request, response)=>{


  console.log('url', request.url);

  const user = {
    name: 'João',
    dinheiro: '2000,00'
  }

  response.setHeader('Content-Type', 'application/json');
  response.end(JSON.stringify(user));

})

server.listen(3000);

```

And the `http` call will respond with an `json` with useful information. Thing is, you can read the `url` information and depending of the type of the request you can send different kinds of things. Such flexibility is awesome. In the following example, depending on the `url` of the `http` call all sorts of information are passed, and when only the `localhost` **ip** is called a html page is the response.

Here is an example of implementation:

```Javascript

// Server development file
const http = require('http');

const data_base = {
  Felipe:"200,00",
  Emília:"2300,00",
  Antônio:"3940,00",
  Yuri:"3903,00",
  Flávio:"2030,00",
}

const server = http.createServer((request, response)=>{


  console.log('headers', request.headers);
  console.log('method', request.method);
  console.log('url', request.url);

  if (request.url === '/'){
    response.setHeader('Content-Type', 'text/html; charset=utf-8');
    response.end('<h1> Bem vindo a essa API </h1> <p> Va em <a href=\"http://127.0.0.1:3000/help\">http://127.0.0.1:3000/help</a> para ver o que se pode conseguir com essa API.</p>');
  } else if(request.url === '/help') {

    response.setHeader('Content-Type', 'text/html; charset=utf-8');
    response.write('<h1>Dados disponíveis aqui</h1>')
    response.write('<p>Esta é uma api de teste para vermos as possibilidades de utilisação de um servidor node para atender requests http.</p>')
    response.write('<p>Os dados presentes aqui são os seguintes:</p>')
    response.write('<h3>Trabalhador e salário:</h3>')
    i = 0
    for (const element in data_base) {
      response.write('<p>' + i.toString() + ' - ' + element + ' : ' + data_base[element] + '</p>')
      i++
    }
    response.write('<h1>Os comandos disponíveis são:</h1>')
    response.write('<p><a href=\"http://127.0.0.1:3000\">http://127.0.0.1:3000</a>             ===> Responde com página http de boas vindas.</p>')
    response.write('<p><a href=\"http://127.0.0.1:3000/help\">http://127.0.0.1:3000/help</a>   ===> Responde com página http com instruções de uso.</p>')
    response.write('<p><a href=\"http://127.0.0.1:3000/todos\">http://127.0.0.1:3000/todos</a> ===> Responde com json de todos os dados disponíveis.</p>')
    response.write('<p><a href=\"http://127.0.0.1:3000/Felipe\">http://127.0.0.1:3000/nome</a> ===> Responde com json com salário desse trabalhador.</p>')

    response.end('<div></div>')
  } else if(request.url === '/todos') {

    response.setHeader('Content-Type', 'application/json');
    response.end(JSON.stringify(data_base));
  } else if(request.url === '/fofinha') {
    response.setHeader('Content-Type', 'text/html; charset=utf-8');
    response.write('<h1>Te amo meu amor S2</h1>')
    response.end('<div></div>')
  } else {

    response.setHeader('Content-Type', 'application/json');
    response.end(JSON.stringify(data_base[request.url.split("/")[1]]));
  }

})

console.log("i hear you!. thanks for the request.");

server.listen(3000);

```
This is an API with some html help pages. Neat stuff!
