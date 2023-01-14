var express = require('express');
var app = express();

app.get('/book/', function (req, res) {
   res.send({
    title :"Domain Driven Design", 
    IBAN: "AL35202111090000000001234567",
    pages: 426
   });
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})