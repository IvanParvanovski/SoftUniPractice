#include <Servo.h>

int servoPin = 10;
int servoPos = 0;
Servo myServo;

void setup() {
    Serial.begin(9600);
    myServo.attach(servoPin);
}

void loop() {
  Serial.println("What Angle for the Servo? ");
  while (Serial.available() == 0){}
  myServo.write(Serial.parseInt());
  
}
