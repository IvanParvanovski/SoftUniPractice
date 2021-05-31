// Pins
int buzzPin = 11;
int potPin = A2;

// Hardcoded values
int dt = 2000;
String msg = "Please Input Your Number";

// Read values
int potVal;
int myNum;

void setup() {
  Serial.begin(9600);
  pinMode(buzzPin, OUTPUT);
  pinMode(potPin, INPUT);
}

void loop() {
  // Ask
  // Serial.println(msg);
  // Wait
  // while (Serial.available() == 0){}
  // Read
  // myNum = Serial.parseInt();
  
  potVal = analogRead(potPin);
  Serial.println(potVal);
  if (potVal > 1000) {
    digitalWrite(buzzPin, HIGH);
  } else {
    digitalWrite(buzzPin, LOW);
  }
}
