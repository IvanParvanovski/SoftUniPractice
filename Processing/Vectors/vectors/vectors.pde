boolean setStartScreen = true;
PImage spiroLogo;
int startScreenTimer = 0;

int systemRect1X = 0;
int systemRect1Y = 200;
int systemRect1W = 25;
int systemRect1H = 25;

int mainLinesX = 0;
int mainLinesY = 0;
int mainLinesY2 = 900;



void setup() {
  size(900, 900);
  background(255);
  spiroLogo = loadImage("Spiro(Logo).png");
}

void draw() {

  // if (setStartScreen == false) {
  //  image(spiroLogo, -80, -50, 1000, 1000);
  // startScreenTimer++;

  // if (startScreenTimer == 50) {
  //  setStartScreen = true;
  //  }
  //}

  if (setStartScreen == true) {
    
    strokeWeight(15);
    line(mainLinesX + 450,mainLinesY,mainLinesX + 450,mainLinesY2);
        


    

    if (systemRect1X <= 900) {
      strokeWeight(2);
      for (int colums = 1; colums <= 30; ) {

        rect(systemRect1X, systemRect1Y, systemRect1W, systemRect1H);
        systemRect1Y += 20; 
        colums++;

        if (systemRect1Y >= 900) {
          systemRect1Y = 200;
          systemRect1X += 20;
        }
      }
    }
  }
}
