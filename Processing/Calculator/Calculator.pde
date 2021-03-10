//-------------------------------------------------------------------------------------------//

//B A S I C   S E T T I N G S
PImage Arrow;
boolean OnAndOff = false;
int FirstNum = 0;
int SecondNum = 0;
String ViewText = "0";
int counter = 0;
boolean FirstAndSecondNum = false;
int sum = 0;
int deff = 0;
int multiplication = 0;
int division = 0;
String calculationSymbols = "";

String firstSymbol = "";
String secondSymbol = "";
String thirdSymbol = "";
String fourthSymbol = "";
String fifthSymbol = "";
String sixthSymbol = "";
String seventhSymbol = "";
String eightSymbol = "";
String ninethSymbol = "";
String tenthSymbol = "";

String firstSymbol2 = "";
String secondSymbol2 = "";
String thirdSymbol2 = "";
String fourthSymbol2 = "";
String fifthSymbol2 = "";
String sixthSymbol2 = "";
String seventhSymbol2 = "";
String eightSymbol2 = "";
String ninethSymbol2 = "";
String tenthSymbol2 = "";


//-------------------------------------------------------------------------------------------//

// N U M B E R S   V A R I A B L E S   [B U T T O N S]

//Button1
int Button1X = 5;
int Button1Y = 240;
int Button1W = 165;
int Button1H = 140;

//Button2
int Button2X = 175;
int Button2Y = 240;
int Button2W = 165;
int Button2H = 140;

//Button3
int Button3X = 345;
int Button3Y = 240;
int Button3W = 165;
int Button3H = 140;

//Button4-Fixed
int Button4X = 5;
int Button4Y = 385;
int Button4W = 165;
int Button4H = 140;

//Button5
int Button5X = 175;
int Button5Y = 385;
int Button5W = 165;
int Button5H = 140;

//Button6
int Button6X = 345;
int Button6Y = 385;
int Button6W = 165;
int Button6H = 140;

//Button7
int Button7X = 5;
int Button7Y = 530;
int Button7W = 165;
int Button7H = 140;

//Button8
int Button8X = 175;
int Button8Y = 530;
int Button8W = 165;
int Button8H = 140;

//Button9
int Button9X = 345;
int Button9Y = 530;
int Button9W = 165;
int Button9H = 140;

//Button0
int Button0X = 175;
int Button0Y = 675;
int Button0W = 165;
int Button0H = 140;

//-------------------------------------------------------------------------------------------//

// S Y M B O L S   A N D  O T H E R S   V A R I A B L E S   [B U T T O N S]

//ButtonMinus
int ButtonMinusX = 345;
int ButtonMinusY = 675;
int ButtonMinusW = 165;
int ButtonMinusH = 140;

//ButtonPlus
int ButtonPlusX = 5;
int ButtonPlusY = 675;
int ButtonPlusW = 165;
int ButtonPlusH = 140;

//ButtonClearOne
int ButtonClearOneX = 20;
int ButtonClearOneY = 160;
int ButtonClearOneW = 80;
int ButtonClearOneH = 70;

//ButtonClearAll
int ButtonClearAllX = 105;
int ButtonClearAllY = 160;
int ButtonClearAllW = 150;
int ButtonClearAllH = 70;

//ButtonEqual
int ButtonEqualX = 530;
int ButtonEqualY = 530;
int ButtonEqualW = 150;
int ButtonEqualH = 286;

//ButtonOn/Off
int ButtonOnAndOffX = 260;
int ButtonOnAndOffY = 160;
int ButtonOnAndOffW = 110;
int ButtonOnAndOffH = 70;

//ButtonMultiplication
int ButtonMultiplicationX = 530;
int ButtonMultiplicationY = 245;
int ButtonMultiplicationW = 145;
int ButtonMultiplicationH = 135;

//ButtonPartition
int ButtonPartitionX = 530;
int ButtonPartitionY = 387;
int ButtonPartitionW = 145;
int ButtonPartitionH = 135;

//ButtonProcent
int ButtonProcentX = 375;
int ButtonProcentY = 160;
int ButtonProcentW = 100;
int ButtonProcentH = 70;

//ButtonDot
int ButtonDotX = 480;
int ButtonDotY = 160;
int ButtonDotW = 100;
int ButtonDotH = 70;

//ButtonExit
int ButtonExitX = 585;
int ButtonExitY = 160;
int ButtonExitW = 100;
int ButtonExitH = 70;

//V I E W  T E X T 
int ViewSumX = 5;
int ViewSumY = 5;
int ViewSumW = 690;
int ViewSumH = 145;  

void setup() {


  //-------------------------------------------------------------------------------------------//

  //..............................[ V  O  I  D     S   E  T  U  P]..............................

  //-------------------------------------------------------------------------------------------// 

  size(700, 820);
  Arrow = loadImage("LeftArrow.jpg");
}

void draw() {
  //-------------------------------------------------------------------------------------------//

  //..............................[ V  O  I  D     D  R  A  W]..............................

  //-------------------------------------------------------------------------------------------//

  background(138, 7, 13);
  strokeWeight(2);
  stroke(0);

  //-------------------------------------------------------------------------------------------//

  //N U M B E R S   O U T  S H A P E / R E C T S

  //Button1
  fill(255);
  rect(Button1X, Button1Y, Button1W, Button1H, 10);

  //Button2
  fill(255);
  rect(Button2X, Button2Y, Button2W, Button2H, 10);

  //Button3
  fill(255);
  rect(Button3X, Button3Y, Button3W, Button3H, 10);

  //Button4
  fill(255);
  rect(Button4X, Button4Y, Button4W, Button4H, 10);

  //Button5 
  fill(255);
  rect(Button5X, Button5Y, Button5W, Button5H, 10);

  //Button6
  fill(255);
  rect(Button6X, Button6Y, Button6W, Button6H, 10);

  //Button7
  fill(255);
  rect(Button7X, Button7Y, Button7W, Button7H, 10);

  //Button8
  fill(255);
  rect(Button8X, Button8Y, Button8W, Button8H, 10);

  //Button9
  fill(255);
  rect(Button9X, Button9Y, Button9W, Button9H, 10);

  //Button0
  fill(255);
  rect(Button0X, Button0Y, Button0W, Button0H, 10);

  //-------------------------------------------------------------------------------------------//

  // S Y M B O L S  A N D  O T H E R S   O U T  S H A P E / R E C T S

  //ButtonEqual
  fill(255);
  rect(ButtonEqualX, ButtonEqualY, ButtonEqualW, ButtonEqualH, 10);

  //ButtonDot
  fill(255);
  rect(ButtonDotX, ButtonDotY, ButtonDotW, ButtonDotH, 10);

  //ButtonPlus
  fill(255);
  rect(ButtonPlusX, ButtonPlusY, ButtonPlusW, ButtonPlusH, 10);
  fill(191, 11, 20);
  rect(ButtonPlusX+42, ButtonPlusY+25, 80, 80,100,15,100,15);

  //ButtonMinus
  fill(255);
  rect(ButtonMinusX, ButtonMinusY, ButtonMinusW, ButtonMinusH, 10);
  fill(191, 11, 20);
  rect(ButtonMinusX+42, ButtonMinusY+25, 80, 80, 15, 100, 15, 100);

  //ButtonClearOne
  fill(255);
  rect(ButtonClearOneX, ButtonClearOneY, ButtonClearOneW, ButtonClearOneH, 10);

  //ButtonClearAll 
  fill(255);
  rect(ButtonClearAllX, ButtonClearAllY, ButtonClearAllW, ButtonClearAllH, 10);

  //ButtonOn/Off
  fill(255);
  rect(ButtonOnAndOffX, ButtonOnAndOffY, ButtonOnAndOffW, ButtonOnAndOffH, 10);

  //ButtonMultiplication
  fill(255);
  rect(ButtonMultiplicationX, ButtonMultiplicationY, ButtonMultiplicationW, ButtonMultiplicationH, 10);

  //ButtonPartition
  fill(255);
  rect(ButtonPartitionX, ButtonPartitionY, ButtonPartitionW, ButtonPartitionH, 10);

  //ButtonProcent
  fill(255);
  rect(ButtonProcentX, ButtonProcentY, ButtonProcentW, ButtonProcentH, 10);

  //ButtonExit
  fill(255);
  rect(ButtonExitX, ButtonExitY, ButtonExitW, ButtonExitH, 10);

  //-------------------------------------------------------------------------------------------//

  //T E X T  V I E W   O U T  S H A P E / R E C T S

  fill(255);
  strokeWeight(5);
  stroke(0);
  rect(ViewSumX, ViewSumY, ViewSumW, ViewSumH);

  //-------------------------------------------------------------------------------------------// 

  //N U M B E R S   T E X T S

  //NumberText[1]
  fill(0);
  textSize(65);
  text("1", 60, 335);

  //NumberText[2]
  fill(0);
  textSize(65);
  text("2", 235, 335);

  //NumberText[3]
  fill(0);
  textSize(65);
  text("3", 405, 335);

  //NumberText[4]
  fill(0);
  textSize(65);
  text("4", 60, 475);

  //NumberText[5]
  fill(0);
  textSize(65);
  text("5", 235, 475);

  //NumberText[6]
  fill(0);
  textSize(65);
  text("6", 405, 475);

  //NumberText[7]
  fill(0);
  textSize(65);
  text("7", 60, 625);

  //NumberText[8]
  fill(0);
  textSize(65);
  text("8", 235, 625);

  //NumberText[9]
  fill(0);
  textSize(65);
  text("9", 405, 625);

  //NumberText0
  fill(0);
  textSize(65);
  text("0", 235, 765);

  //-------------------------------------------------------------------------------------------// 

  // S Y M B O L S   A N D   O T H E R S   T E X T S



  //TextPlus
  textSize(120);
  text("+", 40, 775);

  //TextMinus
  textSize(120);
  text("-", 392, 775);

  //TextClearAll
  textSize(45);
  text("Clear!", 115, 210);

  //ImageClearOne
  image(Arrow, 35, 170, 50, 50);

  //TextEqual
  textSize(150);
  text("=", 545, 720);

  //TextOnAndOff
  textSize(35);
  text("On", 262, 192);
  textSize(45);
  text("/", 300, 212);
  textSize(35);
  text("Off", 312, 225);

  //TextMultiplication
  textSize(135);
  text("*", 572, 385);

  //TextPartition
  textSize(100);
  text("/", 572, 485);

  //TextProcent
  textSize(65);
  text("%", 402, 220);

  //TextDot
  textSize(100);
  text(".", 512, 205);

  //TextExit
  textSize(35);
  text("Exit", 605, 205);

  //-------------------------------------------------------------------------------------------//

  //O T H E R S

  if (OnAndOff == false) {
  ViewText = "Off!";
  }
  
  if (OnAndOff == true && counter == 0){
  ViewText = "0";
  }


  fill(0); 
  textSize(65);
  text(ViewText, 10, 100);
}


void mousePressed() {

  //-------------------------------------------------------------------------------------------//


  //..............................[ M  O  U  S  E     P  R  E  S  S  E  D].......................


  //-------------------------------------------------------------------------------------------//
  
 
  //Plus Button
  
  if (mouseX > ButtonPlusX && mouseX < ButtonPlusX + ButtonPlusW && mouseY > ButtonPlusY && mouseY < ButtonPlusY + ButtonPlusH){
  FirstAndSecondNum = !FirstAndSecondNum;
    
    calculationSymbols = "+";
    sum = FirstNum + SecondNum;
    
  }
  
  //Minus Button
  
    if (mouseX > ButtonMinusX && mouseX < ButtonMinusX + ButtonMinusW && mouseY > ButtonMinusY && mouseY < ButtonMinusY + ButtonMinusH){
  FirstAndSecondNum = !FirstAndSecondNum;
    firstSymbol = "";
    secondSymbol = "";
    thirdSymbol = "";
    fourthSymbol = "";
    fifthSymbol = "";
    sixthSymbol = "";
    seventhSymbol = "";
    eightSymbol = "";
    ninethSymbol = "";
    tenthSymbol = "";
    counter = 0;
    
  }
  
  if (mouseX > ButtonEqualX && mouseX < ButtonEqualX + ButtonEqualW && mouseY > ButtonEqualY && mouseY < ButtonEqualY + ButtonEqualH){
    sum = FirstNum + FirstNum;
    println(sum);
  }


  //O N / O F F  B U T T O N

  if (mouseX > ButtonOnAndOffX && mouseX < ButtonOnAndOffX + ButtonOnAndOffW && mouseY > ButtonOnAndOffY && mouseY < ButtonOnAndOffY + ButtonOnAndOffH) {
    OnAndOff = !OnAndOff;
  }  

  //C L E A R  B U T T O N


  if (mouseX > ButtonClearAllX && mouseX < ButtonClearAllX + ButtonClearAllW && mouseY > ButtonClearAllY && mouseY < ButtonClearAllY + ButtonClearAllH && OnAndOff == true) {
    ViewText = "0";
    firstSymbol = "";
    secondSymbol = "";
    thirdSymbol = "";
    fourthSymbol = "";
    fifthSymbol = "";
    sixthSymbol = "";
    seventhSymbol = "";
    eightSymbol = "";
    ninethSymbol = "";
    tenthSymbol = "";
    counter = 0;
    FirstNum = 0;
    SecondNum = 0;
  }

  // A R R O W  B U T T O N

  if (mouseX > ButtonClearOneX && mouseX < ButtonClearOneX + ButtonClearOneW && mouseY > ButtonClearOneY && mouseY < ButtonClearOneY + ButtonClearOneH && counter > 0) {
    counter--;

    if (counter == 0) {
      firstSymbol = "";
    } else if (counter == 1) {
      secondSymbol = "";
    } else if (counter == 2) {
      thirdSymbol = "";
    } else if (counter == 3) {
      fourthSymbol = "";
    } else if (counter == 4) {
      fifthSymbol = "";
    } else if (counter == 5) {
      sixthSymbol = "";
    } else if (counter == 6) {
      seventhSymbol = "";
    } else if (counter == 7) {
      eightSymbol = "";
    } else if (counter == 8) {
      ninethSymbol = "";
    } else if (counter == 9) {
      tenthSymbol = "";
    }
  }

  //E X I T  B U T T O N

  if (mouseX > ButtonExitX && mouseX < ButtonExitX + ButtonExitW && mouseY > ButtonExitY && mouseY < ButtonExitY + ButtonExitH) {
    exit();
  }

  //-------------------------------------------------------------------------------------------//   

  //N U M B E R S  B U T T O N


  if (counter <= 8 && OnAndOff == true && FirstAndSecondNum == false) {

    //CheckNumber '1'

    if (mouseX > Button1X && mouseX < Button1X + Button1W && mouseY > Button1Y && mouseY < Button1Y + Button1H) {
      counter++;
      println(counter);
      if (counter == 1) {
        firstSymbol = "1";
      } else if (counter == 2) {
        secondSymbol = "1";
      } else if (counter == 3) {
        thirdSymbol = "1";
      } else if (counter == 4) {
        fourthSymbol = "1";
      } else if (counter == 5) {
        fifthSymbol = "1";
      } else if (counter == 6) {
        sixthSymbol = "1";
      } else if (counter == 7) {
        seventhSymbol = "1";
      } else if (counter == 8) {
        eightSymbol = "1";
      } else if (counter == 9) {
        ninethSymbol = "1";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '2'

    if (mouseX > Button2X && mouseX < Button2X + Button2W && mouseY > Button2Y && mouseY < Button2Y + Button2H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "2";
      } else if (counter == 2) {
        secondSymbol = "2";
      } else if (counter == 3) {
        thirdSymbol = "2";
      } else if (counter == 4) {
        fourthSymbol = "2";
      } else if (counter == 5) {
        fifthSymbol = "2";
      } else if (counter == 6) {
        sixthSymbol = "2";
      } else if (counter == 7) {
        seventhSymbol = "2";
      } else if (counter == 8) {
        eightSymbol = "2";
      } else if (counter == 9) {
        ninethSymbol = "2";
      } 
    }

    //-------------------------------------------------------------------------------------------// 

    //CheckNumber '3'

    if (mouseX > Button3X && mouseX < Button3X + Button3W && mouseY > Button3Y && mouseY < Button3Y + Button3H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "3";
      } else if (counter == 2) {
        secondSymbol = "3";
      } else if (counter == 3) {
        thirdSymbol = "3";
      } else if (counter == 4) {
        fourthSymbol = "3";
      } else if (counter == 5) {
        fifthSymbol = "3";
      } else if (counter == 6) {
        sixthSymbol = "3";
      } else if (counter == 7) {
        seventhSymbol = "3";
      } else if (counter == 8) {
        eightSymbol = "3";
      } else if (counter == 9) {
        ninethSymbol = "3";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '4'

    if (mouseX > Button4X && mouseX < Button4X + Button4W && mouseY > Button4Y && mouseY < Button4Y + Button4H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "4";
      } else if (counter == 2) {
        secondSymbol = "4";
      } else if (counter == 3) {
        thirdSymbol = "4";
      } else if (counter == 4) {
        fourthSymbol = "4";
      } else if (counter == 5) {
        fifthSymbol = "4";
      } else if (counter == 6) {
        sixthSymbol = "4";
      } else if (counter == 7) {
        seventhSymbol = "4";
      } else if (counter == 8) {
        eightSymbol = "4";
      } else if (counter == 9) {
        ninethSymbol = "4";
      } 
    }

    //-------------------------------------------------------------------------------------------// 

    //CheckNumber '5'

    if (mouseX > Button5X && mouseX < Button5X + Button5W && mouseY > Button5Y && mouseY < Button5Y + Button5H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "5";
      } else if (counter == 2) {
        secondSymbol = "5";
      } else if (counter == 3) {
        thirdSymbol = "5";
      } else if (counter == 4) {
        fourthSymbol = "5";
      } else if (counter == 5) {
        fifthSymbol = "5";
      } else if (counter == 6) {
        sixthSymbol = "5";
      } else if (counter == 7) {
        seventhSymbol = "5";
      } else if (counter == 8) {
        eightSymbol = "5";
      } else if (counter == 9) {
        ninethSymbol = "5";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //ChechNumber '6'

    if (mouseX > Button6X && mouseX < Button6X + Button6W && mouseY > Button6Y && mouseY < Button6Y + Button6H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "6";
      } else if (counter == 2) {
        secondSymbol = "6";
      } else if (counter == 3) {
        thirdSymbol = "6";
      } else if (counter == 4) {
        fourthSymbol = "6";
      } else if (counter == 5) {
        fifthSymbol = "6";
      } else if (counter == 6) {
        sixthSymbol = "6";
      } else if (counter == 7) {
        seventhSymbol = "6";
      } else if (counter == 8) {
        eightSymbol = "6";
      } else if (counter == 9) {
        ninethSymbol = "6";
      } 
    }


    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '7' 

    if (mouseX > Button7X && mouseX < Button7X + Button7W && mouseY > Button7Y && mouseY < Button7Y + Button7H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "7";
      } else if (counter == 2) {
        secondSymbol = "7";
      } else if (counter == 3) {
        thirdSymbol = "7";
      } else if (counter == 4) {
        fourthSymbol = "7";
      } else if (counter == 5) {
        fifthSymbol = "7";
      } else if (counter == 6) {
        sixthSymbol = "7";
      } else if (counter == 7) {
        seventhSymbol = "7";
      } else if (counter == 8) {
        eightSymbol = "7";
      } else if (counter == 9) {
        ninethSymbol = "7";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '8'

    if (mouseX > Button8X && mouseX < Button8X + Button8W && mouseY > Button8Y && mouseY < Button8Y + Button8H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "8";
      } else if (counter == 2) {
        secondSymbol = "8";
      } else if (counter == 3) {
        thirdSymbol = "8";
      } else if (counter == 4) {
        fourthSymbol = "8";
      } else if (counter == 5) {
        fifthSymbol = "8";
      } else if (counter == 6) {
        sixthSymbol = "8";
      } else if (counter == 7) {
        seventhSymbol = "8";
      } else if (counter == 8) {
        eightSymbol = "8";
      } else if (counter == 9) {
        ninethSymbol = "8";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '9' 

    if (mouseX > Button9X && mouseX < Button9X + Button9W && mouseY > Button9Y && mouseY < Button9Y + Button9H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "9";
      } else if (counter == 2) {
        secondSymbol = "9";
      } else if (counter == 3) {
        thirdSymbol = "9";
      } else if (counter == 4) {
        fourthSymbol = "9";
      } else if (counter == 5) {
        fifthSymbol = "9";
      } else if (counter == 6) {
        sixthSymbol = "9";
      } else if (counter == 7) {
        seventhSymbol = "9";
      } else if (counter == 8) {
        eightSymbol = "9";
      } else if (counter == 9) {
        ninethSymbol = "9";
      } 
    }

    if (mouseX > Button0X && mouseX < Button0X + Button0W && mouseY > Button0Y && mouseY < Button0Y + Button0H) {
      counter++;
      if (counter == 1) {
        counter = 0;
      }
      if (counter == 2) {
        secondSymbol = "0";
      } else if (counter == 3) {
        thirdSymbol = "0";
      } else if (counter == 4) {
        fourthSymbol = "0";
      } else if (counter == 5) {
        fifthSymbol = "0";
      } else if (counter == 6) {
        sixthSymbol = "0";
      } else if (counter == 7) {
        seventhSymbol = "0";
      } else if (counter == 8) {
        eightSymbol = "0";
      } else if (counter == 9) {
        ninethSymbol = "0";
      } 
    }
      ViewText = firstSymbol + secondSymbol + thirdSymbol + " " + fourthSymbol + fifthSymbol + sixthSymbol + " " + seventhSymbol + eightSymbol + ninethSymbol;
      FirstNum = int(firstSymbol + secondSymbol + thirdSymbol + " " + fourthSymbol + fifthSymbol + sixthSymbol + " " + seventhSymbol + eightSymbol + ninethSymbol);
    //-------------------------------------------------------------------------------------------//
  }
  
   if (counter <= 8 && OnAndOff == true && FirstAndSecondNum == true) {
    firstSymbol2 = "";
    secondSymbol2 = "";
    thirdSymbol2 = "";
    fourthSymbol2 = "";
    fifthSymbol2 = "";
    sixthSymbol2 = "";
    seventhSymbol2 = "";
    eightSymbol2 = "";
    ninethSymbol2 = "";
    tenthSymbol2 = "";
    counter = 0;

    //CheckNumber '1'

    if (mouseX > Button1X && mouseX < Button1X + Button1W && mouseY > Button1Y && mouseY < Button1Y + Button1H) {
      counter++;
      println(counter);
      if (counter == 1) {
        firstSymbol2 = "1";
      } else if (counter == 2) {
        secondSymbol2 = "1";
      } else if (counter == 3) {
        thirdSymbol2 = "1";
      } else if (counter == 4) {
        fourthSymbol2 = "1";
      } else if (counter == 5) {
        fifthSymbol2 = "1";
      } else if (counter == 6) {
        sixthSymbol2 = "1";
      } else if (counter == 7) {
        seventhSymbol2 = "1";
      } else if (counter == 8) {
        eightSymbol2 = "1";
      } else if (counter == 9) {
        ninethSymbol2 = "1";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '2'

    if (mouseX > Button2X && mouseX < Button2X + Button2W && mouseY > Button2Y && mouseY < Button2Y + Button2H) {
      counter++;

      if (counter == 1) {
        firstSymbol2 = "2";
      } else if (counter == 2) {
        secondSymbol2 = "2";
      } else if (counter == 3) {
        thirdSymbol2 = "2";
      } else if (counter == 4) {
        fourthSymbol2 = "2";
      } else if (counter == 5) {
        fifthSymbol2 = "2";
      } else if (counter == 6) {
        sixthSymbol2 = "2";
      } else if (counter == 7) {
        seventhSymbol2 = "2";
      } else if (counter == 8) {
        eightSymbol2 = "2";
      } else if (counter == 9) {
        ninethSymbol2 = "2";
      } 
    }

    //-------------------------------------------------------------------------------------------// 

    //CheckNumber '3'

    if (mouseX > Button3X && mouseX < Button3X + Button3W && mouseY > Button3Y && mouseY < Button3Y + Button3H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "3";
      } else if (counter == 2) {
        secondSymbol = "3";
      } else if (counter == 3) {
        thirdSymbol = "3";
      } else if (counter == 4) {
        fourthSymbol = "3";
      } else if (counter == 5) {
        fifthSymbol = "3";
      } else if (counter == 6) {
        sixthSymbol = "3";
      } else if (counter == 7) {
        seventhSymbol = "3";
      } else if (counter == 8) {
        eightSymbol = "3";
      } else if (counter == 9) {
        ninethSymbol = "3";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '4'

    if (mouseX > Button4X && mouseX < Button4X + Button4W && mouseY > Button4Y && mouseY < Button4Y + Button4H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "4";
      } else if (counter == 2) {
        secondSymbol = "4";
      } else if (counter == 3) {
        thirdSymbol = "4";
      } else if (counter == 4) {
        fourthSymbol = "4";
      } else if (counter == 5) {
        fifthSymbol = "4";
      } else if (counter == 6) {
        sixthSymbol = "4";
      } else if (counter == 7) {
        seventhSymbol = "4";
      } else if (counter == 8) {
        eightSymbol = "4";
      } else if (counter == 9) {
        ninethSymbol = "4";
      } 
    }

    //-------------------------------------------------------------------------------------------// 

    //CheckNumber '5'

    if (mouseX > Button5X && mouseX < Button5X + Button5W && mouseY > Button5Y && mouseY < Button5Y + Button5H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "5";
      } else if (counter == 2) {
        secondSymbol = "5";
      } else if (counter == 3) {
        thirdSymbol = "5";
      } else if (counter == 4) {
        fourthSymbol = "5";
      } else if (counter == 5) {
        fifthSymbol = "5";
      } else if (counter == 6) {
        sixthSymbol = "5";
      } else if (counter == 7) {
        seventhSymbol = "5";
      } else if (counter == 8) {
        eightSymbol = "5";
      } else if (counter == 9) {
        ninethSymbol = "5";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //ChechNumber '6'

    if (mouseX > Button6X && mouseX < Button6X + Button6W && mouseY > Button6Y && mouseY < Button6Y + Button6H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "6";
      } else if (counter == 2) {
        secondSymbol = "6";
      } else if (counter == 3) {
        thirdSymbol = "6";
      } else if (counter == 4) {
        fourthSymbol = "6";
      } else if (counter == 5) {
        fifthSymbol = "6";
      } else if (counter == 6) {
        sixthSymbol = "6";
      } else if (counter == 7) {
        seventhSymbol = "6";
      } else if (counter == 8) {
        eightSymbol = "6";
      } else if (counter == 9) {
        ninethSymbol = "6";
      } 
    }


    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '7' 

    if (mouseX > Button7X && mouseX < Button7X + Button7W && mouseY > Button7Y && mouseY < Button7Y + Button7H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "7";
      } else if (counter == 2) {
        secondSymbol = "7";
      } else if (counter == 3) {
        thirdSymbol = "7";
      } else if (counter == 4) {
        fourthSymbol = "7";
      } else if (counter == 5) {
        fifthSymbol = "7";
      } else if (counter == 6) {
        sixthSymbol = "7";
      } else if (counter == 7) {
        seventhSymbol = "7";
      } else if (counter == 8) {
        eightSymbol = "7";
      } else if (counter == 9) {
        ninethSymbol = "7";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '8'

    if (mouseX > Button8X && mouseX < Button8X + Button8W && mouseY > Button8Y && mouseY < Button8Y + Button8H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "8";
      } else if (counter == 2) {
        secondSymbol = "8";
      } else if (counter == 3) {
        thirdSymbol = "8";
      } else if (counter == 4) {
        fourthSymbol = "8";
      } else if (counter == 5) {
        fifthSymbol = "8";
      } else if (counter == 6) {
        sixthSymbol = "8";
      } else if (counter == 7) {
        seventhSymbol = "8";
      } else if (counter == 8) {
        eightSymbol = "8";
      } else if (counter == 9) {
        ninethSymbol = "8";
      } 
    }

    //-------------------------------------------------------------------------------------------//  

    //CheckNumber '9' 

    if (mouseX > Button9X && mouseX < Button9X + Button9W && mouseY > Button9Y && mouseY < Button9Y + Button9H) {
      counter++;

      if (counter == 1) {
        firstSymbol = "9";
      } else if (counter == 2) {
        secondSymbol = "9";
      } else if (counter == 3) {
        thirdSymbol = "9";
      } else if (counter == 4) {
        fourthSymbol = "9";
      } else if (counter == 5) {
        fifthSymbol = "9";
      } else if (counter == 6) {
        sixthSymbol = "9";
      } else if (counter == 7) {
        seventhSymbol = "9";
      } else if (counter == 8) {
        eightSymbol = "9";
      } else if (counter == 9) {
        ninethSymbol = "9";
      } 
    }

    if (mouseX > Button0X && mouseX < Button0X + Button0W && mouseY > Button0Y && mouseY < Button0Y + Button0H) {
      counter++;
      if (counter == 1) {
        counter = 0;
      }
      if (counter == 2) {
        secondSymbol = "0";
      } else if (counter == 3) {
        thirdSymbol = "0";
      } else if (counter == 4) {
        fourthSymbol = "0";
      } else if (counter == 5) {
        fifthSymbol = "0";
      } else if (counter == 6) {
        sixthSymbol = "0";
      } else if (counter == 7) {
        seventhSymbol = "0";
      } else if (counter == 8) {
        eightSymbol = "0";
      } else if (counter == 9) {
        ninethSymbol = "0";
      } 
    }
    
    //-------------------------------------------------------------------------------------------//
  }
ViewText = firstSymbol + secondSymbol + thirdSymbol + " " + fourthSymbol + fifthSymbol + sixthSymbol + " " + seventhSymbol + eightSymbol + ninethSymbol;
SecondNum = int(firstSymbol + secondSymbol +thirdSymbol + fourthSymbol + fifthSymbol + sixthSymbol + seventhSymbol + eightSymbol + ninethSymbol + tenthSymbol);
}

void keyPressed() {

  //-------------------------------------------------------------------------------------------// 

  //B A C K S P A C E

  if (key == BACKSPACE && counter > 0) {
    counter--;

    if (counter == 0) {
      firstSymbol = "";
    } else if (counter == 1) {
      secondSymbol = "";
    } else if (counter == 2) {
      thirdSymbol = "";
    } else if (counter == 3) {
      fourthSymbol = "";
    } else if (counter == 4) {
      fifthSymbol = "";
    } else if (counter == 5) {
      sixthSymbol = "";
    } else if (counter == 6) {
      seventhSymbol = "";
    } else if (counter == 7) {
      eightSymbol = "";
    } else if (counter == 8) {
      ninethSymbol = "";
    } 
  }

  //-------------------------------------------------------------------------------------------// 
  // N U M B E R S

  if (counter <= 8 && OnAndOff == true && FirstAndSecondNum == false) {

    if (key == '1') {
      counter++;

      if (counter == 1) {
        firstSymbol = "1";
      } else if (counter == 2) {
        secondSymbol = "1";
      } else if (counter == 3) {
        thirdSymbol = "1";
      } else if (counter == 4) {
        fourthSymbol = "1";
      } else if (counter == 5) {
        fifthSymbol = "1";
      } else if (counter == 6) {
        sixthSymbol = "1";
      } else if (counter == 7) {
        seventhSymbol = "1";
      } else if (counter == 8) {
        eightSymbol = "1";
      } else if (counter == 9) {
        ninethSymbol = "1";
      } 
    }  

    if (key == '2') {
      counter++;

      if (counter == 1) {
        firstSymbol = "2";
      } else if (counter == 2) {
        secondSymbol = "2";
      } else if (counter == 3) {
        thirdSymbol = "2";
      } else if (counter == 4) {
        fourthSymbol = "2";
      } else if (counter == 5) {
        fifthSymbol = "2";
      } else if (counter == 6) {
        sixthSymbol = "2";
      } else if (counter == 7) {
        seventhSymbol = "2";
      } else if (counter == 8) {
        eightSymbol = "2";
      } else if (counter == 9) {
        ninethSymbol = "2";
      } 
    }  

    if (key == '3') {
      counter++;

      if (counter == 1) {
        firstSymbol = "3";
      } else if (counter == 2) {
        secondSymbol = "3";
      } else if (counter == 3) {
        thirdSymbol = "3";
      } else if (counter == 4) {
        fourthSymbol = "3";
      } else if (counter == 5) {
        fifthSymbol = "3";
      } else if (counter == 6) {
        sixthSymbol = "3";
      } else if (counter == 7) {
        seventhSymbol = "3";
      } else if (counter == 8) {
        eightSymbol = "3";
      } else if (counter == 9) {
        ninethSymbol = "3";
      } 
    }  

    if (key == '4') {
      counter++;

      if (counter == 1) {
        firstSymbol = "4";
      } else if (counter == 2) {
        secondSymbol = "4";
      } else if (counter == 3) {
        thirdSymbol = "4";
      } else if (counter == 4) {
        fourthSymbol = "4";
      } else if (counter == 5) {
        fifthSymbol = "4";
      } else if (counter == 6) {
        sixthSymbol = "4";
      } else if (counter == 7) {
        seventhSymbol = "4";
      } else if (counter == 8) {
        eightSymbol = "4";
      } else if (counter == 9) {
        ninethSymbol = "4";
      } 
    }  

    if (key == '5') {
      counter++;

      if (counter == 1) {
        firstSymbol = "5";
      } else if (counter == 2) {
        secondSymbol = "5";
      } else if (counter == 3) {
        thirdSymbol = "5";
      } else if (counter == 4) {
        fourthSymbol = "5";
      } else if (counter == 5) {
        fifthSymbol = "5";
      } else if (counter == 6) {
        sixthSymbol = "5";
      } else if (counter == 7) {
        seventhSymbol = "5";
      } else if (counter == 8) {
        eightSymbol = "5";
      } else if (counter == 9) {
        ninethSymbol = "5";
      } 
    }  

    if (key == '6') {
      counter++;

      if (counter == 1) {
        firstSymbol = "6";
      } else if (counter == 2) {
        secondSymbol = "6";
      } else if (counter == 3) {
        thirdSymbol = "6";
      } else if (counter == 4) {
        fourthSymbol = "6";
      } else if (counter == 5) {
        fifthSymbol = "6";
      } else if (counter == 6) {
        sixthSymbol = "6";
      } else if (counter == 7) {
        seventhSymbol = "6";
      } else if (counter == 8) {
        eightSymbol = "6";
      } else if (counter == 9) {
        ninethSymbol = "6";
      } 
    }  

    if (key == '7') {
      counter++;

      if (counter == 1) {
        firstSymbol = "7";
      } else if (counter == 2) {
        secondSymbol = "7";
      } else if (counter == 3) {
        thirdSymbol = "7";
      } else if (counter == 4) {
        fourthSymbol = "7";
      } else if (counter == 5) {
        fifthSymbol = "7";
      } else if (counter == 6) {
        sixthSymbol = "7";
      } else if (counter == 7) {
        seventhSymbol = "7";
      } else if (counter == 8) {
        eightSymbol = "7";
      } else if (counter == 9) {
        ninethSymbol = "7";
      } 
    }  

    if (key == '8') {
      counter++;

      if (counter == 1) {
        firstSymbol = "8";
      } else if (counter == 2) {
        secondSymbol = "8";
      } else if (counter == 3) {
        thirdSymbol = "8";
      } else if (counter == 4) {
        fourthSymbol = "8";
      } else if (counter == 5) {
        fifthSymbol = "8";
      } else if (counter == 6) {
        sixthSymbol = "8";
      } else if (counter == 7) {
        seventhSymbol = "8";
      } else if (counter == 8) {
        eightSymbol = "8";
      } else if (counter == 9) {
        ninethSymbol = "8";
      } 
    }  

    if (key == '9') {
      counter++;

      if (counter == 1) {
        firstSymbol = "9";
      } else if (counter == 2) {
        secondSymbol = "9";
      } else if (counter == 3) {
        thirdSymbol = "9";
      } else if (counter == 4) {
        fourthSymbol = "9";
      } else if (counter == 5) {
        fifthSymbol = "9";
      } else if (counter == 6) {
        sixthSymbol = "9";
      } else if (counter == 7) {
        seventhSymbol = "9";
      } else if (counter == 8) {
        eightSymbol = "9";
      } else if (counter == 9) {
        ninethSymbol = "9";
      } 
    }  

    if (key == '0') {
      counter++;

      if (counter == 2) {
        secondSymbol = "0";
      } else if (counter == 3) {
        thirdSymbol = "0";
      } else if (counter == 4) {
        fourthSymbol = "0";
      } else if (counter == 5) {
        fifthSymbol = "0";
      } else if (counter == 6) {
        sixthSymbol = "0";
      } else if (counter == 7) {
        seventhSymbol = "0";
      } else if (counter == 8) {
        eightSymbol = "0";
      } else if (counter == 9) {
        ninethSymbol = "0";
      } 
     }
     
  
  ViewText = firstSymbol + secondSymbol + thirdSymbol + " " + fourthSymbol + fifthSymbol + sixthSymbol + " " + seventhSymbol + eightSymbol + ninethSymbol;
  FirstNum = int(firstSymbol + secondSymbol + thirdSymbol + fourthSymbol + fifthSymbol + sixthSymbol + seventhSymbol + eightSymbol + ninethSymbol);
  //-------------------------------------------------------------------------------------------//
}

  if (counter <= 8 && OnAndOff == true && FirstAndSecondNum == true) {

    if (key == '1') {
      counter++;

      if (counter == 1) {
        firstSymbol = "1";
      } else if (counter == 2) {
        secondSymbol = "1";
      } else if (counter == 3) {
        thirdSymbol = "1";
      } else if (counter == 4) {
        fourthSymbol = "1";
      } else if (counter == 5) {
        fifthSymbol = "1";
      } else if (counter == 6) {
        sixthSymbol = "1";
      } else if (counter == 7) {
        seventhSymbol = "1";
      } else if (counter == 8) {
        eightSymbol = "1";
      } else if (counter == 9) {
        ninethSymbol = "1";
      } 
    }  

    if (key == '2') {
      counter++;

      if (counter == 1) {
        firstSymbol = "2";
      } else if (counter == 2) {
        secondSymbol = "2";
      } else if (counter == 3) {
        thirdSymbol = "2";
      } else if (counter == 4) {
        fourthSymbol = "2";
      } else if (counter == 5) {
        fifthSymbol = "2";
      } else if (counter == 6) {
        sixthSymbol = "2";
      } else if (counter == 7) {
        seventhSymbol = "2";
      } else if (counter == 8) {
        eightSymbol = "2";
      } else if (counter == 9) {
        ninethSymbol = "2";
      } 
    }  

    if (key == '3') {
      counter++;

      if (counter == 1) {
        firstSymbol = "3";
      } else if (counter == 2) {
        secondSymbol = "3";
      } else if (counter == 3) {
        thirdSymbol = "3";
      } else if (counter == 4) {
        fourthSymbol = "3";
      } else if (counter == 5) {
        fifthSymbol = "3";
      } else if (counter == 6) {
        sixthSymbol = "3";
      } else if (counter == 7) {
        seventhSymbol = "3";
      } else if (counter == 8) {
        eightSymbol = "3";
      } else if (counter == 9) {
        ninethSymbol = "3";
      } 
    }  

    if (key == '4') {
      counter++;

      if (counter == 1) {
        firstSymbol = "4";
      } else if (counter == 2) {
        secondSymbol = "4";
      } else if (counter == 3) {
        thirdSymbol = "4";
      } else if (counter == 4) {
        fourthSymbol = "4";
      } else if (counter == 5) {
        fifthSymbol = "4";
      } else if (counter == 6) {
        sixthSymbol = "4";
      } else if (counter == 7) {
        seventhSymbol = "4";
      } else if (counter == 8) {
        eightSymbol = "4";
      } else if (counter == 9) {
        ninethSymbol = "4";
      } 
    }  

    if (key == '5') {
      counter++;

      if (counter == 1) {
        firstSymbol = "5";
      } else if (counter == 2) {
        secondSymbol = "5";
      } else if (counter == 3) {
        thirdSymbol = "5";
      } else if (counter == 4) {
        fourthSymbol = "5";
      } else if (counter == 5) {
        fifthSymbol = "5";
      } else if (counter == 6) {
        sixthSymbol = "5";
      } else if (counter == 7) {
        seventhSymbol = "5";
      } else if (counter == 8) {
        eightSymbol = "5";
      } else if (counter == 9) {
        ninethSymbol = "5";
      } 
    }  

    if (key == '6') {
      counter++;

      if (counter == 1) {
        firstSymbol = "6";
      } else if (counter == 2) {
        secondSymbol = "6";
      } else if (counter == 3) {
        thirdSymbol = "6";
      } else if (counter == 4) {
        fourthSymbol = "6";
      } else if (counter == 5) {
        fifthSymbol = "6";
      } else if (counter == 6) {
        sixthSymbol = "6";
      } else if (counter == 7) {
        seventhSymbol = "6";
      } else if (counter == 8) {
        eightSymbol = "6";
      } else if (counter == 9) {
        ninethSymbol = "6";
      } 
    }  

    if (key == '7') {
      counter++;

      if (counter == 1) {
        firstSymbol = "7";
      } else if (counter == 2) {
        secondSymbol = "7";
      } else if (counter == 3) {
        thirdSymbol = "7";
      } else if (counter == 4) {
        fourthSymbol = "7";
      } else if (counter == 5) {
        fifthSymbol = "7";
      } else if (counter == 6) {
        sixthSymbol = "7";
      } else if (counter == 7) {
        seventhSymbol = "7";
      } else if (counter == 8) {
        eightSymbol = "7";
      } else if (counter == 9) {
        ninethSymbol = "7";
      } 
    }  

    if (key == '8') {
      counter++;

      if (counter == 1) {
        firstSymbol = "8";
      } else if (counter == 2) {
        secondSymbol = "8";
      } else if (counter == 3) {
        thirdSymbol = "8";
      } else if (counter == 4) {
        fourthSymbol = "8";
      } else if (counter == 5) {
        fifthSymbol = "8";
      } else if (counter == 6) {
        sixthSymbol = "8";
      } else if (counter == 7) {
        seventhSymbol = "8";
      } else if (counter == 8) {
        eightSymbol = "8";
      } else if (counter == 9) {
        ninethSymbol = "8";
      } 
    }  

    if (key == '9') {
      counter++;

      if (counter == 1) {
        firstSymbol = "9";
      } else if (counter == 2) {
        secondSymbol = "9";
      } else if (counter == 3) {
        thirdSymbol = "9";
      } else if (counter == 4) {
        fourthSymbol = "9";
      } else if (counter == 5) {
        fifthSymbol = "9";
      } else if (counter == 6) {
        sixthSymbol = "9";
      } else if (counter == 7) {
        seventhSymbol = "9";
      } else if (counter == 8) {
        eightSymbol = "9";
      } else if (counter == 9) {
        ninethSymbol = "9";
      } 
    }  

    if (key == '0') {
      counter++;

      if (counter == 2) {
        secondSymbol = "0";
      } else if (counter == 3) {
        thirdSymbol = "0";
      } else if (counter == 4) {
        fourthSymbol = "0";
      } else if (counter == 5) {
        fifthSymbol = "0";
      } else if (counter == 6) {
        sixthSymbol = "0";
      } else if (counter == 7) {
        seventhSymbol = "0";
      } else if (counter == 8) {
        eightSymbol = "0";
      } else if (counter == 9) {
        ninethSymbol = "0";
      } 
     }
     
  
  ViewText = firstSymbol + secondSymbol + thirdSymbol + " " + fourthSymbol + fifthSymbol + sixthSymbol + " " + seventhSymbol + eightSymbol + ninethSymbol;
  SecondNum = int(firstSymbol + secondSymbol + thirdSymbol + " " + fourthSymbol + fifthSymbol + sixthSymbol + " " + seventhSymbol + eightSymbol + ninethSymbol);
  //-------------------------------------------------------------------------------------------//
 }
} //<>//
