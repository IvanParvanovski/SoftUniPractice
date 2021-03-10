int greenPin = 12;
int redPin = 11;

int readPin = A2;
int delayTime = 500;
float potentiometerOutVoltage;

void setup() {
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  potentiometerOutVoltage = 5. / 1023. * analogRead(readPin);
  Serial.println(potentiometerOutVoltage);

  if (potentiometerOutVoltage <= 3)
  {
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
    Serial.println("Ok. - Green");
  }

  else
  {
    digitalWrite(greenPin, LOW);
    digitalWrite(redPin, HIGH);
    Serial.println("Danger! - Red");
  }
  
  delay(delayTime);  
}
