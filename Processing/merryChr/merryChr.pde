PImage present;
PImage tree;

int buttonOpenAndCloseX = 0;
int buttonOpenAndCloseY = 0;
int buttonOpenAndCloseW = 0;
int buttonOpenAndCloseH = 0;
boolean set = false;

int topEllipseX = 350;
int topEllipseY = 50;
int topEllipseW = 50;
int topEllipseH = 50;

int downEllipseX = 550;
int downEllipseY = 650;
int downEllipseW = 50;
int downEllipseH = 50;

void setup() {
  size(600, 700);
  background(255);
  present = loadImage("present.png");
  tree = loadImage("tree.png");
}

void draw() {  
  //Basic Settings
  stroke(0);
  strokeWeight(10);
  fill(255);
  rect(0, 0, 600, 700);

  if (set == true) {
    line(width/2, 0, width/2, 700);
    text("CLOSE", 10, 50);
    buttonOpenAndCloseX = 50;
    buttonOpenAndCloseY = 20;

    fill(0);
    textSize(20);
    text("Christmas is the time to", 10, 150);
    textSize(20);
    text("touch every heart with", 10, 180);
    textSize(20);
    text("love and care.", 10, 210);
    textSize(20);
    text("Christmas is the time to", 10, 240);
    textSize(20);
    text("receive and send blessings.", 10, 270);
    textSize(20);
    text("It is the time to breathe the", 10, 300);
    textSize(20);
    text("magic in the air. Wishing you", 10, 330);
    textSize(20);
    text("a very Merry Christmas.", 10, 360);
    strokeWeight(10);

    if (topEllipseY <= 640 && topEllipseX == 350) {
      topEllipseY += 10;
      fill(#1753E5);
    }

    if (downEllipseY >= 60 && downEllipseX == 550) {
      downEllipseY -= 10;
      fill(#F50A0A);
    }

    if (topEllipseY == 650) {
      topEllipseX += 10;
      if (topEllipseX >= 550) {
        topEllipseX = 550;
      }
    }

    if (downEllipseY == 50) {
      downEllipseX -= 10;
      if (downEllipseX <= 350) {
        downEllipseX = 350;
      }
      fill(#14F50A);
    }
    if (downEllipseX == 350 && downEllipseY <= 640) {
      downEllipseY += 10;
      fill(#0A13F5);
    }

    if (topEllipseX == 550 && topEllipseY >= 60) {
      topEllipseY -= 10;
      fill(#0A13F5);
    }

    if (topEllipseX >= 50 && topEllipseY == 50) {
      topEllipseX -= 10;
    }

    if (downEllipseX <= 550 && downEllipseY == 650) {
      downEllipseX += 10;
      fill(#C10AF5);
    }

    ellipse(topEllipseX, topEllipseY, topEllipseW, topEllipseH);
    ellipse(downEllipseX, downEllipseY, downEllipseW, downEllipseH);

    fill(255);
    rect(buttonOpenAndCloseX, buttonOpenAndCloseY, buttonOpenAndCloseW, buttonOpenAndCloseH);
    fill(0);
    textSize(40);
    text("CLOSE", 60, 70);

    image(present, 10, 385, 285, 300);
  }

  if (set == false) {
    buttonOpenAndCloseX = 220;
    buttonOpenAndCloseY = 50;
    buttonOpenAndCloseW = 150;
    buttonOpenAndCloseH = 70;

    fill(255);
    rect(buttonOpenAndCloseX, buttonOpenAndCloseY, buttonOpenAndCloseW, buttonOpenAndCloseH);
    fill(0);
    textSize(40);
    text("Open", 240, 100); 
    textSize(65);
    text("Merry Christmas!", 30, 200);

    stroke(0);
    image(tree, 110, 215, 380, 480);
  }
}

void mousePressed() {
  if (mouseX > buttonOpenAndCloseX && mouseX < buttonOpenAndCloseX + buttonOpenAndCloseW && mouseY > buttonOpenAndCloseY && mouseY < buttonOpenAndCloseY + buttonOpenAndCloseH) {
    set = !set;
  }
}
