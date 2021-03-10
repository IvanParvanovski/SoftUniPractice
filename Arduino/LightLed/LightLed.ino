int redLED = 12;
int sDelay = 50;
int oDelay = 150;
int restartOperationDelay = 1000;

void setup() {
  pinMode(redLED, OUTPUT);
}

void loop() {
  LED_SOS(redLED, sDelay);  
  LED_SOS(redLED, oDelay);
  LED_SOS(redLED, sDelay);

  delay(restartOperationDelay);
}

void LED_SOS(int pin, int letterDelay)
{
  for (int i = 0; i < 3; i++)
  {
    digitalWrite(pin, HIGH);
    delay(letterDelay);

    digitalWrite(pin, LOW);
    delay(letterDelay);
  }
  delay(200);
}
