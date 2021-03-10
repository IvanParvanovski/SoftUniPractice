

void setup(){
size(500,500);
}
void draw(){}

void mousePressed(){
  float rectX = random(500);
  float rectY = random(500);
  float ellipseX = random(500);
  float ellipseY = random(500);
  println("MouseX =" + mouseX);
  println("MouseY =" + mouseY);
stroke(0);
fill(21, 143, 62);
rect(rectX,rectY, 16, 16);
fill(139, 143, 21);
ellipse(ellipseX, ellipseY, 16, 16);

}

void keyPressed(){
println("KeyPressed!");
}
