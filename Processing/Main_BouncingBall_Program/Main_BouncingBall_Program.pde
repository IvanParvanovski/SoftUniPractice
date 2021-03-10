BouncingBall[] BouncingBallCollection = new  BouncingBall [1000];
int X = 0;
int Y = 0;

void setup()
{
  background(0);
  size(600, 600);
  smooth();

  for (int i = 0; i < BouncingBallCollection.length; i++)
  {
    BouncingBallCollection[i] = new BouncingBall (random(width), random(height));
    X += 20;
    Y += 20;
  }
}

void draw()
{
  background(0);

  //we call cycle to run all of our 
  int i = 0;
  for (i = 0; i < BouncingBallCollection.length; i++)
  {
    if (i <= BouncingBallCollection.length / 3)
    {
      fill(#00ff1a);
    } else if (i <= BouncingBallCollection.length / 2) {
      fill(255);
    } else {
      fill(255,0,0);
    }

    BouncingBallCollection[i].run();
  }
}
