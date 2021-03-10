int elip1X = 400;
int elip1Y = 100;
int elip2X = 400;
int elip2Y = 400;
int elip3X = 80;
int elip3Y = 100;
int elip4X = 80;
int elip4Y = 400;

int x = 200;
int y = 200;
int w = 80;
int h = 80;

String s = "EXIT";


void setup(){
size(500,500);
}

void draw(){
  

  
  fill(255);
  stroke(143, 19, 10);
ellipse(elip1X, elip1Y, 50, 50);
  fill(255);
  stroke(8, 120, 31);
ellipse(elip2X, elip2Y, 50, 50);
  fill(255); 
  stroke(8, 60, 133);
ellipse(elip3X, elip3Y, 50, 50);
  fill(255);
  stroke(186, 145, 9);
ellipse(elip4X, elip4Y, 50, 50);


elip1X -= 1;
elip2Y -= 1;
elip3Y += 1;
elip4X += 1;
 
 if (elip1X <= 80){
   elip1X = 80;
 }
 
 if (elip2Y <= 100 ){
  elip2Y = 100;
 }
 
 if (elip3Y >= 400){
 elip3Y = 400;
 }
 
 if (elip4X >= 400){
 elip4X = 400;
 }
 
 if (elip1X == 80){
   
 stroke(4,61,145);
 fill(255);
 rect(x,y,w,h);
textSize(32);
fill(4, 61, 145);
text("Exit", 210, 245);
 
 
 }
}


void mousePressed(){
    if(mouseX>x && mouseX < x+w && mouseY>y && mouseY<y+h){
      exit();
    }
}
