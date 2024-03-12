#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
