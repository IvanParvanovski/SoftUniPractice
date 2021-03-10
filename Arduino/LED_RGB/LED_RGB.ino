int redPin = 8;
int greenPin = 9;
int bluePin = 10;
String color;
String message = "What colour do you want?";

void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  Serial.println(message);
  while (Serial.available() == 0) {}
  
  color = Serial.readString();

  bool isRed = color.equals("red");  
  bool isGreen = color.equals("green");
  bool isBlue = color.equals("blue");

  Serial.println(isRed);
  Serial.println(isGreen);
  Serial.println(isBlue);
  
//      
//  if (color.equals("red"))
//  {
//    Serial.println("in red");
//    digitalWrite(redPin, HIGH);
//  }
//
//  else if (color == "green")
//  {
//    Serial.println("in green");
//    digitalWrite(greenPin, HIGH);
//  }
//
//  else if (color == "blue") 
//  {
//    Serial.println("in blue");
//    digitalWrite(bluePin, HIGH);
//  }
//  delay(500);
//  digitalWrite(redPin, LOW);
//  digitalWrite(greenPin, LOW);
//  digitalWrite(bluePin, LOW);

}
