#!/usr/bin/node
/**
 * Defines a square & inherits from Square class
 * in 5-square.js
 */
const prevSquare = require('./5-square');

class Square extends prevSquare {
  charPrint (c) {
	const myChar = c === undefined ? 'X' : c;
	for (let i = 0; i < this.height; i++) {
	  let myVar = '';
	  let y = 0;
	  while (y < this.width) {
		myVar += myChar;
		y++;
	  }

	  console.log(myVar);
	}
  }
}

module.exports = Square;
