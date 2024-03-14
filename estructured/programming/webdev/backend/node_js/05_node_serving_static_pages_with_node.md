# Creating static pages with node
You can serve static pages with node pretty easily. You only need to create a `/public` folder along side the `server.js` file and point to there with the code:

```javascript

const express = require('express');

const app = express();

app.use(express.static(__dirname + "/public"));

app.listen(2033);
```
Than you can create a `index.html` file for example in that folder it will be seeded as expected. You can add javascript and css as normal too.

