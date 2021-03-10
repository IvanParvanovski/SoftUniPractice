//Line1
int lineOneX1 = 0;
int lineOneY1 = 500;
int lineOneX2 = 500;
int lineOneY2 = 500;

//Line2
int lineTwoX1 = 0;
int lineTwoY1 = 500;
int lineTwoX2 = 500;
int lineTwoY2 = 500;

//Line3

int lineThreeX1 = 0;
int lineThreeY1 = 0;
int lineThreeX2 = 500;
int lineThreeY2 = 0;

//Line4

int lineFourX1 = 0;
int lineFourY1 = 0;
int lineFourX2 = 500;
int lineFourY2 = 0;

//Button1
int Button1X = 35;
int Button1Y = 50;
int Button1W = 100;
int Button1H = 100;

//Button2

int Button2X = 365;
int Button2Y = 50;
int Button2W = 100;
int Button2H = 100;



//Ellipse1

int elipOneX = 250;
int elipOneY = 50;
int elipOneW = 50;
int elipOneH = 50;

//Ellipse2

int elipTwoX = 50;
int elipTwoY = 450;
int elipTwoW = 50;
int elipTwoH = 50;

//Ellipse3

int elipThreeX = 450;
int elipThreeY = 450;
int elipThreeW = 50;
int elipThreeH = 50;


void setup(){
size(800,800);
}

void draw(){
  stroke(0);
line(lineOneX1,lineOneY1,lineOneX2,lineOneY2);
lineOneX1++;
lineOneY1--;

line(lineTwoX1,lineTwoY1,lineTwoX2,lineTwoY2);
lineTwoY2--;
lineTwoX2--;

line(lineThreeX1,lineThreeY1,lineThreeX2,lineThreeY2);
lineThreeX2--;
lineThreeY2++;

line(lineFourX1,lineFourY1,lineFourX2,lineFourY2);
lineFourX1++;
lineFourY1++;



if(lineOneX1 >= 500){
  fill(0);
  stroke(255);
  stroke(#F00F0F);
ellipse(elipOneX,elipOneY,elipOneW,elipOneH);
elipOneX--;
elipOneY += 2;
if(elipOneX <= 50){
elipOneX = 50;
elipOneY = 450;
}
stroke(#EFF011);
ellipse(elipTwoX,elipTwoY,elipTwoW,elipTwoH);
elipTwoX += 2;
if(elipTwoX >= 450){
elipTwoX = 450;
}
stroke(#241195);
ellipse(elipThreeX,elipThreeY,elipThreeW,elipThreeH);
elipThreeX --;
elipThreeY -= 2;
if(elipThreeX <= 250){
elipThreeX = 250;
elipThreeY = 50;
 }
 
 lineOneX1 = 500;
 lineOneY1 = 0;
 }
 
if (elipThreeX == 250){

 fill(#312E2C);
 stroke(#F07511);
 rect(Button1X,Button1Y,Button1W,Button1H);
 rect(Button2X,Button2Y,Button2W,Button2H);
 
 fill(255);
  stroke(255);
  textSize(30);
text("E X I T", 40, 110); 

textSize(30);
text("Q U I T", 365, 110); 

 

if (mouseX > Button1X && mouseX < Button1X + Button1W && mouseY > Button1Y && mouseY < Button1Y+Button1H && mousePressed) {
  exit();
}
if (mouseX > Button2X && mouseX < Button2X + Button2W && mouseY > Button2Y && mouseY < Button2Y+Button2H && mousePressed){
  exit();
}
}
}
