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
