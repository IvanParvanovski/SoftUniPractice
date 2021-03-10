PImage laptop;
PImage duck;

//Lines Variables
int top_LineX1 = 0;
int top_LineY1 = 0;
int top_LineX2 = 800;
int top_LineY2 = 0;

int left_LineX1 = 0;
int left_LineY1 = 0;
int left_LineX2 = 0;
int left_LineY2 = 800;

int right_LineX1 = 800;
int right_LineY1 = 0;
int right_LineX2 = 800;
int right_LineY2 = 800;

int down_LineX1 = 0;
int down_LineY1 = 800;
int down_LineX2 = 800;
int down_LineY2 = 800;

//Buttons Variables
int topButton_TriangleX1 = 300;
int topButton_TriangleY1 = 200;
int topButton_TriangleX2 = 500;
int topButton_TriangleY2 = 200;
int topButton_TriangleX3 = 400;
int topButton_TriangleY3 = 100;

int pythonRectX = 0;
int pythonRectY = 90;
int pythonRectW = 650;
int pythonRectH = 0;

int javaRectX = 0;
int javaRectY = 190;
int javaRectW = 550;
int javaRectH = 0;

int c_SharpRectX = 0;
int c_SharpRectY = 380;
int c_SharpRectW = 350;
int c_SharpRectH = 0;

int javaScriptRectX = 0;
int javaScriptRectY = 290;
int javaScriptRectW = 450;
int javaScriptRectH = 0;

int phpRectX = 0;
int phpRectY = 475;
int phpRectW = 250;
int phpRectH = 0;

boolean checkLinePosition = false;
boolean screenSet = false;
boolean backgroundSet = false;


void setup()
{
  background(255);
  size(800,800);
  
  duck = loadImage("duck.jpg");
  laptop = loadImage("laptop.jpg");
}

void draw()
{  
  if(screenSet == false)
  {
  
   lineGenerate();
   lineAction();
  
    if(checkLinePosition == true)
    {
     buttonGenerate();
     images();
    }
    
  } else
  {
    checkLinePosition = false;
    top_LineX1 = 0;
    top_LineY1 = 0;
    top_LineX2 = 800;
    top_LineY2 = 0;

    left_LineX1 = 0;
    left_LineY1 = 0;
    left_LineX2 = 0;
    left_LineY2 = 800;

    right_LineX1 = 800;
    right_LineY1 = 0;
    right_LineX2 = 800;
    right_LineY2 = 800;

    down_LineX1 = 0;
    down_LineY1 = 800;
    down_LineX2 = 800;
    down_LineY2 = 800;
    
    if(backgroundSet == false)
   {
    background(255);
   }
   
    table();
  }
  
}

void lineGenerate()
{
 strokeWeight(10);
 
 stroke(102, 179, 255);
 line(top_LineX1, top_LineY1, top_LineX2, top_LineY2);
 stroke(0, 172, 230);
 line(left_LineX1, left_LineY1, left_LineX2, left_LineY2);
 stroke(0, 136, 204);
 line(right_LineX1, right_LineY1, right_LineX2, right_LineY2);
 stroke(51, 204, 255);
 line(down_LineX1, down_LineY1, down_LineX2, down_LineY2);
}

void buttonGenerate()
{
  stroke(0);
  fill(40, 141, 191);
  triangle(topButton_TriangleX1, topButton_TriangleY1, topButton_TriangleX2, topButton_TriangleY2, topButton_TriangleX3, topButton_TriangleY3);
  fill(0);
  textSize(25);
  text("Click", 370, 170);
}

void lineAction()
{
  if(top_LineX2 >= 0 && top_LineY2 <= 800)
  {
    top_LineX2 -= 1;
    top_LineY2 += 1;
  }
  
  if(down_LineX1 <= 800 && down_LineY1 >= 0)
  {
    down_LineX1 += 1;
    down_LineY1 -= 1;
  }
  
  if(right_LineX2 >= 0 && right_LineY2 >= 0)
  {
    right_LineX2 -= 1;
    right_LineY2 -= 1;
  }
  
  if(left_LineX1 <= 800 && left_LineY1 <= 800)
  {
    left_LineX1 += 1;
    left_LineY1 += 1;
  }
  
  if (top_LineX2 == 0 && top_LineY2 == 800)
  {
    checkLinePosition = true;
  }
    
}

void images()
{
 fill(0);
 rect(8,275,236,236);
 image(duck,10,280,230,230);
 rect(538, 275, 236, 236);
 image(laptop,540,280,230,230);
}

void table()
{ 
 tableTexts();
 rect(pythonRectX, pythonRectY, pythonRectW, pythonRectH);
 rect(javaRectX, javaRectY, javaRectW, javaRectH);
 rect(javaScriptRectX, javaScriptRectY, javaScriptRectW, javaScriptRectH);
 rect(c_SharpRectX, c_SharpRectY, c_SharpRectW, c_SharpRectH);
 rect(phpRectX, phpRectY, phpRectW, phpRectH); 
}

void tableTexts()
{
 fill(0);
 text("Python", 50, 50);
 text("Java", 50, 150);
 text("JavaScript", 50, 250);
 text("C#", 50, 350);
 text("Php", 50, 450);
 
 textSize(20);
 text("Ада Ловелас, дъщерята на английския поет Лорд Байрон,  ", 1, 604);
 text("се смята за първият компютърен програмист. През 1843 г.", 1, 625);
 text("тя работи с Чарлз Беббъд, изобретателят на някои ранни механични компютри, ", 1, 646);
 text("за да създаде първата програма за една от неговите машини -", 1, 667);
 text("Аналитичния двигател.", 1, 688);
}

void mousePressed()
{
  if(checkLinePosition == true)
  {
    
   if(mouseX >= topButton_TriangleX1 && mouseY <= topButton_TriangleY1 && mouseX <= topButton_TriangleX2 && mouseY <= topButton_TriangleY2 && mouseY >= topButton_TriangleY3)
   {
    screenSet = !screenSet;
   }   
   
  }
  
}
