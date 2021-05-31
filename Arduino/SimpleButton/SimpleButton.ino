int buttonPin = 2;
int buttonValue;
int dt = 100;
void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  digitalWrite(buttonPin, HIGH);
}

void loop() {
  buttonValue = digitalRead(buttonPin);
  Serial.print("Your BUtton is: ");
  Serial.println(buttonValue);
  delay(dt); 
}
