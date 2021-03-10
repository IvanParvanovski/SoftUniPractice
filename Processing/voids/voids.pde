
void setup() {
  size(100, 100);
  String name = "Bob";
  int num = 0;

  Text_Hello(name, num);
  Text_GoodBye(name);
}

void draw() {
}

void Text_Hello(String name,int num) {
  num = 5;
  print("Hello" , name, num);
  printPeriod();
}

void Text_GoodBye(String name) {
  print("GoodBye", name);
  printPeriod();
}

void printPeriod() {
  println("!");
}
