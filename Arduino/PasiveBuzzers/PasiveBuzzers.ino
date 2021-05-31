int buzzPin = 11;
int buzzTimeMin = 60;
int buzzTimeMax = 10000;

int potPin = A2;
int potValue;

void setup() {
  Serial.begin(9600);
  pinMode(buzzPin, OUTPUT);
  pinMode(potPin, INPUT);
}

void loop() {
  potValue = analogRead(potPin);
  Serial.println(map(potValue, 0, 1023, buzzTimeMin, buzzTimeMax));
  
  digitalWrite(buzzPin, HIGH);
  delayMicroseconds(map(potValue, 0, 1023, buzzTimeMin, buzzTimeMax));
  digitalWrite(buzzPin, LOW);
  delayMicroseconds(map(potValue, 0, 1023, buzzTimeMin, buzzTimeMax));
}
