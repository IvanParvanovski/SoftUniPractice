int buttonPin = 8;
int redPin = 9;
bool LEDState = false;
int buttonNew;
int buttonOld = 1;
int dt = 100;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  pinMode(redPin, OUTPUT);
}

void loop() {
   buttonNew = digitalRead(buttonPin);

   if (buttonOld == 0 && buttonNew == 1) {
      if (LEDState == 0) {
        digitalWrite(redPin, HIGH);
        LEDState = 1;
      } else {
        digitalWrite(redPin, LOW);
        LEDState = 0;
      }
   }
   buttonOld = buttonNew;
   Serial.print("ButtonOld = ");
   Serial.println(buttonOld);
   
   Serial.print("ButtonNew = ");
   Serial.println(buttonNew);
   Serial.println();
}
