void setup(){
size(1000,1000);

}

void draw(){
  if(mousePressed){
translate(mouseX,mouseY);

background(17, 31, 51);
fill(255);
//Body
ellipseMode(CENTER);
fill(0);
stroke(255);
ellipse(100,100,50,100);
//Head
fill(255);
ellipse(100,70,60,60);
//Eyes
fill(0);
ellipse(81,70,16,32); 
ellipse(119,70,16,32);
//ArmsAndLegs
stroke(255);
line(90,150,80,160);
line(110,150,120,160);
line(60,65,75,110);
line(125,110,150,110);


//Body
fill(0);
stroke(255);
ellipse(350,235,50,100);
//Head
fill(255);
ellipse(350,205,60,60);
//Eyes
fill(0);
ellipse(331,205,16,32);
ellipse(362,205,16,32);
//Legs
stroke(255);
line(380,300,360,280);
line(315,300,337,280);
//Arms
stroke(255);
line(300,260,324,230);
line(350,260,375,230);
//Sword
stroke(255);
line(285,261,380,261);
line(300,250,300,270);}
}
