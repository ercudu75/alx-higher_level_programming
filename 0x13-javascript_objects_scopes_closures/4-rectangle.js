#!/usr/bin/node

class Rectangle {
  width;
  height;
  tmp;

  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (printC = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(`${printC}`.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    this.tmp = this.height;
    this.height = this.width;
    this.width = this.tmp;
  }
}

module.exports = Rectangle;
