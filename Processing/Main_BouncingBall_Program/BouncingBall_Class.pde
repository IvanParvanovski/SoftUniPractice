class BouncingBall
{
  //VARIABLES
  
  
  public float X = 0;
  public float Y = 0;
  float speedX = 4;
  float speedY = 0.5;

  //CONSTRUCTOR
  
  BouncingBall(float _x, float _y)
  { 
    X = _x;
    Y = _y;
  }

  //FUNCTIONS
  
  void run()
  {
    move();
    bounce();
    gravity();
    display();
  }
  
  
  void move()
  {
    X += speedX;
    Y += speedY;
  }

  void bounce()
  {
    
    if ((X > width) || (X < 0))
    {
      speedX *= -1;
    } 

    if ((Y > height) || (Y < 0))
    {
      speedY *= -1;
    }
    
  }

  void gravity()
  {
    
    speedY = speedY + 0.2;
    
  }

  void display()
  {
    
    ellipse(X, Y, 20, 20);
    
  }
  
}
