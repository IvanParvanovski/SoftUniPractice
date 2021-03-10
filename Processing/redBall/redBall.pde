int elipX = 250;
int elipY = 330;
float pillarX = random(350,1200);
float pillar2X = random(350,1200);
int time = 0;
int score = 0;
int pillarSpeed = -10;


int ButtonJumpX = 100;
int ButtonJumpY = 500;
int HigherPillarSpeedX = 600;
int LowerPillarSpeedX = 1000;
int PillarSpY = 600;
int widht = 200;
int heigh = 200;



int pillarY1 = 400;
int pillarY2 = 350;

void setup(){
size(1200,800);

}

void draw(){
  
elipY += 5;
pillar2X += pillarSpeed;
pillarX += pillarSpeed;

  
background(255);
fill(0);
rect(0,400,1200,400);
fill(120, 127, 207);
stroke(0);
ellipse(elipX,elipY,40,40);
strokeWeight(10);
  
//KeySettings
  if (keyPressed){    
    
    //CoolDown
    time += 4;
    if (time == 4){
    elipY = 372 ;
    }
    
 //ElipJump
 elipY -= 35;
 if (elipY == 327){
 elipY += 10;
  }
 }
    
//TopLine              //N E E D    F I X
if(elipY <= 250){ 
  elipY = 249;
}

//DownLine
if (elipY >= 367){
elipY = 368;
}

//Pillar1
if (pillarX > (elipX + 40)){
line(pillarX,pillarY1,pillarX,pillarY2);
}
if (elipY < pillarY1 && elipX > pillarX+30 ){
pillarX = random(0,1200);
}

if (pillar2X > (pillarX + 40)){
line(pillar2X, pillarY1,pillar2X,pillarY2);
}
if (pillar2X <= pillarX){
pillar2X = random(0,1200);
}





//Score                     


fill(#4a4a4a);
rect(400,50,200,80);

fill(120, 127, 207);
textSize(80);
text(score,475,120);
 
if (elipX > pillarX && pillarY2 >= elipY){
score++;
}

//PillarSpeed
fill(#4a4a4a);
rect(600,50,200,80);

fill(120,127,207);
textSize(80);
text(pillarSpeed, 625,120);




//Jump Button 
fill(#4a4a4a);
stroke(#2c2c2e);
rect (ButtonJumpX, ButtonJumpY, widht,heigh);
fill(255);
textSize(50);
text("Jump",130,575);
text("Button",123,650);
fill(#4a4a4a);

if (mouseX > ButtonJumpX && mouseX < ButtonJumpX + widht && mouseY > ButtonJumpY && mouseY < ButtonJumpY + heigh && mousePressed){
    //CoolDown
    time += 4;
    if (time == 4){
    elipY = 372 ;
    }
    
 //ElipJump
 elipY -= 35;
 if (elipY == 327){
 elipY += 10;
  }
}




//Higher PillarSpeed
if (mouseX > HigherPillarSpeedX && mouseX < HigherPillarSpeedX + widht && mouseY > PillarSpY && mouseY < PillarSpY + heigh && mousePressed){
pillarSpeed -= 10;
}
ellipse(HigherPillarSpeedX,PillarSpY,widht,heigh);
fill(255);
textSize(100);
text("<",550,625);
fill(#4a4a4a);

//Lower PillarSpeed
if (mouseX > LowerPillarSpeedX && mouseX < LowerPillarSpeedX + widht && mouseY > PillarSpY && mouseY < PillarSpY + heigh && mousePressed){
pillarSpeed += 10;
}
ellipse(LowerPillarSpeedX,PillarSpY,widht,heigh);
fill(255);
textSize(100);
text(">",970,625);






stroke(0);
}
