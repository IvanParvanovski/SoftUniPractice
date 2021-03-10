int right_LineX1 = 800;
int right_LineY1 = 0;
int right_LineX2 = 800;
int right_LineY2 = 800;
boolean first_rightLine_action = false;

int left_LineX1 = 0;
int left_LineY1 = 0;
int left_LineX2 = 0;
int left_LineY2 = 800;
boolean first_leftLine_action = false;

int down_LineX1 = 0;
int down_LineY1 = 800;
int down_LineX2 = 800;
int down_LineY2 = 800;
boolean first_downLine_action = false;

int top_LineX1 = 0;
int top_LineY1 = 0;
int top_LineX2 = 800;
int top_LineY2 = 0;
boolean first_topLine_action = false;

int ellipseX = 400;
int ellipseY = 400;
int ellipseH = 120;
int ellipseW = 120;
int background_check;

int r = 255;
int g = 255;
int b = 255;

boolean set = false; 
boolean eye = false;
boolean table_set = false;

int button_X = 350;
int button_Y = 330;
int button_W = 100;
int button_H = 100;

int pythonRectW = 10;
int javaRectW = 10;
int javaScriptW = 10;
int c_SharpW = 10;
int c_plusW = 10;

boolean button_background_check = false;

void setup()
{
  size(800, 800);
}

void draw()
{
  if (set == false) 
  {  
    lineAction();
  } else 
   {
    if (background_check == 0)
    {
      background_check = 1;
      background(255);
    } else 
     {
      
      if(table_set == false)
      {
        face();
        texts();
         
      } else
       {
        for(int rectY = 100; rectY <= 500;)
        {
          if (button_background_check == false)
          {
            background_check = 0;
            button_background_check = true;
          } else 
           {
             if(pythonRectW <= 600)
             {
               pythonRectW += 5;
             }else
             {
              rectY += 100;
             }
             rect(0, rectY, pythonRectW, 50);
           
             if(pythonRectW >= 600 && javaRectW <= 400)
             {
               javaRectW += 5;
             }
             rect(0,rectY, javaRectW, 50); 
         }      
        }
       }
    
    }
    
  }
  
}

void face()
{
  eye(290, 150);
  eye(515, 150);
  button();
  mouth();
}

void eye(int ellipseX, int ellipseY) 
{
  strokeWeight(5);
  if (eye == false) 
  {
    ellipseH -= 2;
    r -= 5;
    g -= 5;
    b -= 5;
    ellipseW += 1;
    stroke(0);
    fill(r, g, b);

    if (ellipseH <= 5)
    {
      eye = true;
    }
  } else {
    ellipseH += 2;   
    r += 5;
    g += 5;
    b += 5;
    ellipseW -= 1;
    stroke(0);
    fill(r, g, b);

    if (ellipseH >= 120)
    {
      eye = false;
    }
  }
  ellipse(ellipseX, ellipseY, ellipseW, ellipseH);
  fill(0);
  ellipse(ellipseX, ellipseY, ellipseW - 50, ellipseH - 50);
}

void mouth()
{
  int mouthX = 300;
  int mouthY = 500;
  int mouthW = 500;
  int mouthH = 150;

  strokeWeight(20);
  fill(255);               // applies no fill to the mouth
  arc(mouthX, mouthY, mouthW, mouthH, PI/6, PI/2 ); // position of the mouse
}

void lineAction()
{
  strokeWeight(4);
  line(right_LineX1, right_LineY1, right_LineX2, right_LineY2);
  line(left_LineX1, left_LineY1, left_LineX2, left_LineY2);
  line(down_LineX1, down_LineY1, down_LineX2, down_LineY2);
  line(top_LineX1, top_LineY1, top_LineX2, top_LineY2);   

  if (right_LineX1 >= 0 && first_rightLine_action == false)
  {
    right_LineX1 -= 5; 
    if (right_LineX1 <= 0)
    {
      first_rightLine_action = true;
    }
  }

  if (right_LineX1 >= 0 && first_rightLine_action == true)
  {
    right_LineX2 -= 5;
  }


  if (left_LineX1 <= 800 && first_leftLine_action == false)
  {
    left_LineX1 += 5; 
    if (left_LineX1 >= 800)
    {
      first_leftLine_action = true;
    }
  }


  if (left_LineX1 <= 800 && first_leftLine_action == true)
  {
    left_LineX2 += 5;
  }

  if (down_LineY1 >= 0 && first_downLine_action == false)
  {
    down_LineY1 -= 5; 

    if (down_LineY1 <= 0)
    {
      first_downLine_action = true;
    }
  }


  if (down_LineY1 >= 0 && first_downLine_action == true)
  {
    down_LineY2 -= 5;

    if (down_LineY2 <= 0)
    {
      set = true;
    }
  }

  if (top_LineY1 <= 800 && first_topLine_action == false)
  {
    top_LineY1 += 5; 

    if (top_LineY1 >= 800)
    {
      first_topLine_action = true;
    }

    if (top_LineX1 <= 800 && first_topLine_action == true)
    {
      top_LineY2 += 5;
    }
  }
}

void button()
{
  fill(255, 0, 0);
  rect(button_X, button_Y, button_W, button_H, 60);
}

void texts()
{
  strokeWeight(1);
  fill(0);
  textSize(60);
  text("+====>",0, 400);
  text("<====+",515, 400);
  textSize(20);
  text("Click me!", 355, 385); 
}

void mousePressed()
{
  if (mouseX > button_X && mouseX < button_X + button_W && mouseY > button_Y && mouseY < button_Y + button_H)
  {
   if(set == true)
   {
     table_set = true; 
   }
   
  }

}
