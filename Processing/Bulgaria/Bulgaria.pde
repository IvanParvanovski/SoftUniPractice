//Top_Rectangle(Variables)

//Flag_Rectangle(White)
int whiteRectTopX = 0;
int whiteRectTopY = 0;
//Flag_Rectangle(Green)
int greenRectTopX = 0;
int greenRectTopY = 20;
//Flag_Rectangle(Red)
int redRectTopX = 0;
int redRectTopY = 40;

//Down_Rectangle(Variables)

//Flag_Rectangle(White)
int whiteRectDownX = 0;
int whiteRectDownY = 740;
//Flag_Rectangle(Green)
int greenRectDownX = 0;
int greenRectDownY = 760;
//Flag_Rectangle(Red)
int redRectDownX = 0;
int redRectDownY = 780;

//Flag_Rectangle(Settings)
int RectW = 20;
int RectH = 20;

//Button_Rectangle(Variables)
int buttonSwapX = 100;
int buttonSwapY = 250;
int buttonSwapW = 150;
int buttonSwapH = 75;

//Images(Variables)
PImage rose;
PImage flag;
PImage church;
PImage lakes;

//Screen(Booleans)
boolean set = false;
boolean imagechange = false;

void setup() {
  //Basic(Settings)
  size(800, 800);
  background(0);
  //LoadImages
  rose = loadImage("rose-bulgarian-wax.jpg");
  flag = loadImage("Day_of_Bulgaria_unition.jpg");
  church = loadImage("93.jpg");
  lakes = loadImage("lakes.jpg");
}

void draw() {
  //Void(Generation)
  rectSettings();
  flagMovement();
  if (set == true) {
    texts();
    button();

    if (imagechange == false) {
      imagesFalse();
    } else {
      imagesTrue();
    }
  }
}

void rectSettings() {
  //Rectangle(Settings)
  strokeWeight(5);
  stroke(0);

  //WhiteRectangle(Generation)                                                                                                       
  fill(255);
  rect(whiteRectTopX, whiteRectTopY, RectW, RectH);
  rect(whiteRectDownX, whiteRectDownY, RectW, RectH);
  fill(#07DE2F);
  //GreenRectangle(Generation)
  rect(greenRectTopX, greenRectTopY, RectW, RectH);
  rect(greenRectDownX, greenRectDownY, RectW, RectH);
  fill(#F20707);
  //RedRectangle(Generation)
  rect(redRectTopX, redRectTopY, RectW, RectH);
  rect(redRectDownX, redRectDownY, RectW, RectH);
}

void flagMovement() {
  //Check_FlagRectangles(Position)
  if (whiteRectTopX <= 790 && whiteRectTopY == 0) {
    whiteRectTopX += 10;
    greenRectTopX += 10;
    redRectTopX += 10;

    whiteRectDownX += 10;
    greenRectDownX += 10;
    redRectDownX += 10;
  }
  //Screen(Swap)
  if (whiteRectTopX == 800) {
    set = true;
  }
}

void texts() {
  stroke(245, 145, 150);
  //Text_Rectangles(Display)
  strokeWeight(10);
  fill(0);
  rect(215, 105, 355, 60);
  rect(365, 563, 407, 50);

  //Images_Rectangles(Display)
  strokeWeight(20);
  rect(460, 220, 250, 250);
  rect(60, 450, 250, 250);

  //Texts(Display)
  textSize(40);
  fill (245, 145, 150);  
  text("We love Bulgaria!", 230, 150);
  textSize(35);
  fill (245, 145, 150);  
  text("Our beautiful country!", 380, 600);
}

void imagesFalse() {
  //Load_FirstImages
  image(rose, 60, 450, 250, 250);
  image(flag, 460, 220, 250, 250);
}

void imagesTrue() {
  //Load_SecondImages
  image(lakes, 460, 220, 250, 250);
  image(church, 60, 450, 250, 250);
}

void button() {
  //Button_Rectangle(Settings)
  strokeWeight(10);
  fill(0);
  rect(buttonSwapX, buttonSwapY, buttonSwapW, buttonSwapH);
  //Button_Texts(Settings)
  fill(245, 145, 150);
  textSize(40);
  text("Swap!", 122, 300);
}

void mousePressed() {
  //Check_Mouse(Position)
  if (mouseX > buttonSwapX && mouseX < buttonSwapX + buttonSwapW && mouseY > buttonSwapY && mouseY < buttonSwapY + buttonSwapH) {
    imagechange = !imagechange;
  }
}
