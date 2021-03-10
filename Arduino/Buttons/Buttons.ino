int ledPin = 8;

int digitalButtonPin = 12;
int digitalButtonRead;

int delayTime = 500;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(digitalButtonPin, INPUT);
}

void loop() {
  digitalButtonRead = digitalRead(digitalButtonPin);
  
  Serial.print("Digital Result: ");
  Serial.println(digitalButtonRead);

  if (digitalButtonRead == 0)
  {
    digitalWrite(ledPin, HIGH);
  }
  else 
  {
    digitalWrite(ledPin, LOW);
  }
  
  delay(delayTime);
}
