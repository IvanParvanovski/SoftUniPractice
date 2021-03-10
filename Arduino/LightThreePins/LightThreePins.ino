int ledPin8 = 8;
int ledPin9 = 9;
int ledPin10 = 10;

void setup() {
  pinMode(ledPin8, OUTPUT);
  pinMode(ledPin9, OUTPUT);
  pinMode(ledPin10, OUTPUT);
}

void loop() {
  LED_Functionality(ledPin8, 100, 5);
  LED_Functionality(ledPin9, 100, 10);
  LED_Functionality(ledPin10, 100, 15);
}

void LED_Functionality(int pin, int userDelay, int times)
{
  for (int i = 0; i < times; i++)
  {
    digitalWrite(pin, HIGH);
    delay(userDelay);
  
    digitalWrite(pin, LOW);
    delay(userDelay);
  }
}
