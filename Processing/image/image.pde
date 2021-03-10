PImage photo0;
PImage photo1;

int PhX1 = 400;
int PhX2 = 400;
int PhY1 = 300;
int PhY2 = 500;

void setup (){
size(800,800);
photo0 = loadImage("name.png");
photo1 = loadImage("go.jpg");

}

void draw(){
background(255);
imageMode(CENTER);
image(photo0,PhX1,PhY1,200,200);
image(photo1,PhX2,PhY2,200,200);

PhX1++;
PhX2--;
if(PhX1 >= 699){
PhX1 = 700;
PhX2 = 100;
PhY1++;
PhY2--;
if (PhY1 >= 699){
 PhY1 = 700;
 PhY2 = 100;
 PhX1 -= 2;
 PhX2 += 2;
}
}

}
