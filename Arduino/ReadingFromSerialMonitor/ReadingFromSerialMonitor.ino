int numBlinks;
int redPin = 12;
int dt = 150;

String msg = "How Many Blinks Do You Want: ";
String msg2 = "Your number is: ";

void setup() 
{
  pinMode(redPin, OUTPUT);
  Serial.begin(9600);
} 

void loop()
{
  Serial.println(msg);
  while (Serial.available() == 0) {}
  numBlinks = Serial.parseInt();
  Serial.print(msg2);
  Serial.println(numBlinks);

  for (int i = 1; i < numBlinks; i++)
  {
    digitalWrite(redPin, HIGH);
    delay(dt);
    digitalWrite(redPin, LOW);
    delay(dt);
  } 
}
