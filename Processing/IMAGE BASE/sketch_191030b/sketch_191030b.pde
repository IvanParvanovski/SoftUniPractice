PImage photo1;
PImage photo2;
PImage photo3;
PImage photo4;
PImage photo5;
PImage photo6;
PImage photo7;
PImage photo8;
PImage photo9;



int num = 0;

void setup(){
size(200,200);
photo1 = loadImage("1.jpg");
photo2 = loadImage("2.jpg");
photo3 = loadImage("3.jpg");
photo4 = loadImage("4.jpg");
photo5 = loadImage("1.jpg");
photo6 = loadImage("2.jpg");
photo7 = loadImage("3.jpg");
photo8 = loadImage("4.jpg");
photo9 = loadImage("1.jpg");

}

void draw(){

}

void keyPressed(){
if (keyCode == '1'){
  num = 1;
  image(photo1,0,0,200,200);
  println("The key is: " + num);
}

if (key == '2'){
  num = 2;
  image(photo2,0,0,200,200);
  println("The key is: " + num);
}

if (key == '3'){
  num = 3;
  image(photo3,0,0,200,200);
  println("The key is: " + num);
}

if (key == '4'){
  num = 4;
  image(photo4,0,0,200,200);
  println("The key is: " + num);
}

if (key == '5'){
  num = 5;
  image(photo5,0,0,200,200);
  println("The key is: " + num);
}

if (key == '6'){
  num = 6;
  image(photo6,0,0,200,200);
  println("The key is: " + num);
}

if (key == '7'){
  num = 7;
  image(photo7,0,0,200,200);
  println("The key is: " + num);
  }

if (key == '8'){
  num = 8;
  image(photo8,0,0,200,200);
  println("The key is: " + num);
}

if (key == '9'){
  num = 9;
  image(photo9,0,0,200,200);
  println("The key is: " + num);
}

}
