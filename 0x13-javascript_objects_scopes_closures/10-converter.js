#!/usr/bin/node

exports.converter = function (base) {
/**
 * Converts a number from base 10 to another base
 * passed as argument.
 */
  function newConverter (n) {
    return n.toString(base);
  }

  return newConverter;
};
