#include <Servo.h> 
Servo quad1;
Servo quad2;
Servo quad3;
Servo quad4;

void setup() {
  // put your setup code here, to run once:
  pinMode(0, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  digitalWrite(1, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(0, LOW);
  digitalWrite(3, LOW);
  digitalWrite(6, LOW);
  digitalWrite(9, LOW);
  quad1.attach(2);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i<=1000; i += 10)
  {
    quad1.write(i);
    delay(1000);
  }    
}
