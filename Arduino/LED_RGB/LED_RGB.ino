int bluePin = 10;
int greenPin = 11;
int redPin = 12;

String myColorMSG = "What color do you want?";
String myColor;


void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
    
//  Serial.println(myColorMSG);
//  while (Serial.available() == 0){}
//  myColor = Serial.readString();
//  
//  if (myColor == "red") {
//    digitalWrite(redPin, HIGH);
//    digitalWrite(greenPin, LOW);
//    digitalWrite(bluePin, LOW);
//  }
//
//  if (myColor == "blue") {
//    digitalWrite(redPin, LOW);
//    digitalWrite(greenPin, LOW);
//    digitalWrite(bluePin, HIGH);
//  }
//
//  if (myColor == "green"){
//    digitalWrite(redPin, LOW);
//    digitalWrite(greenPin, HIGH);
//    digitalWrite(bluePin, LOW);  
//  }
//
//  if (myColor == "off"){
//    digitalWrite(redPin, LOW);
//    digitalWrite(greenPin, LOW);
//    digitalWrite(bluePin, LOW);
//  }
  
} 
