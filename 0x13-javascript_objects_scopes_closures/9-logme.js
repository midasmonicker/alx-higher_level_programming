#!/usr/bin/node
/**
 * Prints the number of arguments already printed
 * and new argument value
 */
let counter = 0;

exports.logMe = function (item) {
  console.log(`${counter} : ${item}`);
  counter += 1;
};
