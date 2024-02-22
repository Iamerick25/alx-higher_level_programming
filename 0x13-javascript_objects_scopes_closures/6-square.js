#!/usr/bin/node
// a class Square that defines a square and inherits from Rectangle class of
// 4-rectangle.js
module.exports = class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
