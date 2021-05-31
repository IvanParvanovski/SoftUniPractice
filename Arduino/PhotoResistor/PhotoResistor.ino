int readPin = A2;
int readPinValue;

int dt = 250;

int greenPin = 10;
int redPin = 11;

void setup() {
  Serial.begin(9600);
  pinMode(readPin, INPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);
}

void loop() {
  readPinValue = analogRead(readPin);
  Serial.println(readPinValue);
    
  if (readPinValue < 700) {
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
  } else {
    digitalWrite(greenPin, HIGH);

    digitalWrite(redPin, LOW);
  }  
}
