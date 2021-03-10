int rectX = 0;
int rectY = 325;
 
void setup(){
  size (800, 800);  
}
 
void draw(){
  background(255);
  strokeWeight(10);
  fill(255);
  rect(rectX, rectY, 150,150);
  rectX = constrain(rectX,0,650);
  rectY = constrain(rectY,0,650);
  
  
  if (keyCode == RIGHT){
    rectX += 5;
  }
  
  if (keyCode == LEFT){
    rectX -= 5;
  }
  
  if (keyCode == DOWN){
    rectY += 5;
  }
  
  if (keyCode == UP){
    rectY -= 5;
  } 
  
}
 
  
