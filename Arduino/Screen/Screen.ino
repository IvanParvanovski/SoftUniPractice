
#include <LiquidCrystal.h>
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() 
{
  lcd.begin(16, 2);  
  lcd.setCursor(0, 0);
  lcd.print("My name is Ivan");
  
  lcd.setCursor(0, 1);
  lcd.print("Nice to meet you! 1234567890 -1234567890-");
} 

void loop()
{
//  lcd.scrollDisplayRight();
//  delay(800);
//  lcd.autoscroll();
//  delay(400);
}
