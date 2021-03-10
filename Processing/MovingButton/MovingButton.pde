int buttonX = 345;
int buttonY = 350;
int buttonW = 100;
int buttonH = 100;

boolean buttonPressed = false;
boolean buttonMoving = false;

color background1 = color(24, 37, 120);
color buttonBackground = color(24, 37, 120);
color buttonStroke = color(87, 20, 77);



void setup(){
size(800,800);
}

void draw(){
  
  //BACKGROUND
  background(background1);
  
  //BUTTON SETTINGS
  strokeWeight(10);
  stroke(buttonStroke);
  fill(buttonBackground);
  rect(buttonX,buttonY,buttonW,buttonH);
  noStroke();

  //BUTTON TEXT
  fill(background1);
  text("Smash!",(buttonX+5),(buttonY+60));
  textSize(26);
    
  //ButtonMoving
   if (buttonMoving == false){
    buttonY -= 5;
    
   if(buttonY == 0){
     buttonMoving = true;
   }
  }
  
  if (buttonMoving == true){
  buttonY += 5;
   
   if (buttonY == 725){
   buttonMoving = false;
   }
  }
  
  
  
  
  //ButtonFunction
  if (buttonPressed == true){
  buttonBackground = color(24, 37, 120);
  background1 = color(49, 214, 211);
  }else{
  buttonBackground = color(49, 214, 211);
  background1 = color(24, 37, 120);
  }

}

void mousePressed(){
  
  //CHECH FOR THE BUTTON 
if (mouseX > buttonX && mouseX < buttonX + buttonW && mouseY > buttonY && mouseY < buttonY + buttonH){
buttonPressed = !buttonPressed;
}
}
