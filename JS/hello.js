
var x,y,z

function sum(x,y) {
    return x + y 
}

sum(1,2) // doest show a damn thing
//console.log(sum(1,2))
//console.log("Hello World.")

var h = 10;
{
    let h = 2;
    console.log(h) // This will be 2
}

console.log(h) // This will be 10


var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World!');
}).listen(8080); 

//This will print Hello World in your browser. (Local though. Go to localhost:8080 to see it!)

