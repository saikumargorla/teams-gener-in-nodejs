
const fs = require('fs');
let rawdata = fs.readFileSync('student.json'); 

var parsed = JSON.parse(rawdata);
var arr = [];
for(var x in parsed.students){
arr.push(parsed.students[x].Name);

}
var shuffle = require('shuffle-array');
shuffle(arr);
console.log(arr);

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('how many teams ', (n) => {
  console.log(`the number of teams: ${n}`);

  rl.close();

var i;
var b = []
var k = 1;
var bigin = 0
while(arr.length > n){
var slice = require('array-slice');

 b = arr.slice(bigin,n);
console.log(`${k} team`);
k++;
console.log(b);
arr.splice(bigin,n);

}
console.log(`the ${k} team`);
console.log(arr);

});







