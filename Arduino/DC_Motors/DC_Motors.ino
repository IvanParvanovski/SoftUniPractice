#include <LiquidCrystal.h>

// Motor
int speedPin = 5;
int directionPin1 = 4;
int directionPin2 = 3;
int motorSpeed;

// Potenciometer
int potenciometerPin = A1;
int potenciometerValue;

// Display 
int rs = 7;
int en = 8;
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Text
int motorMax = 255;
int previousValue;
int textNum = 1;
int textCounter = 0;

void setup() {
  pinMode(speedPin, OUTPUT);
  pinMode(directionPin1, OUTPUT);
  pinMode(directionPin2, OUTPUT);
  pinMode(potenciometerPin, INPUT);
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
  potenciometerValue = analogRead(potenciometerPin);
  motorSpeed = map(potenciometerValue, 0, 1023, 0, 255);

  // Motor
  setupMotor(motorSpeed);
    
  // Display
  setupDisplay();

  previousValue = motorSpeed;
}

void setupMotor(int motorSpeed){
  digitalWrite(directionPin1, HIGH);
  digitalWrite(directionPin2, LOW);
  analogWrite(speedPin, motorSpeed);
}

void setupDisplay(){
  if (textCounter == 5) {
    for (int positionCounter = 0; positionCounter < 16; positionCounter++) {
      // scroll one position left:
      lcd.scrollDisplayRight();
      // wait a bit:
      delay(150);
    }
    lcd.clear();
    textNum++;  
    textCounter = 0;
    if (textNum % 3 == 0) {
      textNum = 1;
    }
  }
  
  if (textNum == 1){
    // First row
    lcd.setCursor(5, 0);
    lcd.print("Motor");
  
    // Second row
    lcd.setCursor(0, 1);
    lcd.print("Speed -> ");
    lcd.print(motorSpeed);
    lcd.print("/");
    lcd.print(motorMax);
    clearText();
  }

  if (textNum == 2) {
    lcd.setCursor(5, 0);
    lcd.print("Time");
    delay(1000);
  } 

  textCounter++;
  
  
}

void clearText() {
if ((previousValue < 10 && motorSpeed > 10) ||
      (previousValue >= 90 && motorSpeed < 110) ||
      (previousValue > 10 && motorSpeed < 15)) {
    
    delay(1000);
    lcd.clear();
  } 
}
