int redPin = 9;
int brightness = 0;

void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
}

void loop() {
  for (; brightness < 256; brightness += 10)
  {
   analogWrite(redPin, brightness);  
   delay(100);
   Serial.println(brightness);
  }

  for (; brightness > 0; brightness -= 10)
  {
   analogWrite(redPin, brightness);  
   delay(100);
   Serial.println(brightness);  
  }
}
