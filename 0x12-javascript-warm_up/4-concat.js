#!/usr/bin/node
const argv = process.argv;
const c = argv[2] !== undefined ? argv[2] : 'undefined';
const fun = argv[3] !== undefined ? argv[3] : 'undefined' ;
console.log('${c} is ${fun}');