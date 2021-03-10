int latchPin = 12;
int clockPin = 13;
int dataPin = 11;

void setup() {
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
}

void loop() {
  byte x = 0x01;
  for (int j = 0; j < 8; j++)
  {
    digitalWrite(latchPin, LOW);
    shiftOut(dataPin, clockPin, LSBFIRST, x);
    digitalWrite(latchPin, HIGH);
    x <<= 1;
    delay(100);
  }
}
