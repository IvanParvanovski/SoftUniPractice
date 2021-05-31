int firstButtonPin = 8;
int secondButtonPin = 9;
int firstButtonValue;
int secondButtonValue;
int redPin = 11;
int buzzPin = 10;

int LEDbright = 0;
int dt = 500;

void setup() {
  Serial.begin(9600);
  pinMode(firstButtonPin, INPUT);
  pinMode(secondButtonPin, INPUT);
  pinMode(redPin, OUTPUT);
  pinMode(buzzPin, OUTPUT);
}

void loop() {
    firstButtonValue = digitalRead(firstButtonPin);
    secondButtonValue = digitalRead(secondButtonPin);
  
    Serial.print("Button 1 = "); 
    Serial.println(firstButtonValue);

    Serial.print("Button 2 = ");
    Serial.println(secondButtonValue);
    Serial.println();
    delay(dt);

    if (firstButtonValue == 0) {
      LEDbright += 25;
    }

    if (secondButtonValue == 0) {
      LEDbright -= 25;  
    }

    Serial.println(LEDbright);
    
    if (LEDbright > 255){
      LEDbright = 255;
      digitalWrite(buzzPin, HIGH);
      delay(dt);
      digitalWrite(buzzPin, LOW);
      delay(dt);
    }

    if (LEDbright < 0) {
      LEDbright = 0;
      digitalWrite(buzzPin, HIGH);
      delay(dt);
      digitalWrite(buzzPin, LOW);
      delay(dt);
    }
    
    analogWrite(redPin, LEDbright);
}
