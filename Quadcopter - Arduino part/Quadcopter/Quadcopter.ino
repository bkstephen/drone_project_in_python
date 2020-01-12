#include <Servo.h> 
Servo quad1;
Servo quad2;
Servo quad3;
Servo quad4;
Servo select_propeller;
Servo set_thurst;

float thrust = 0;

enum Proppellers {  
  All = 0,
  X0 = 1 , 
  X1 = 2, 
  Y0 = 3, 
  Y1 = 4 };
int propeller;

void setup() {
  Serial.begin(9600);

  pinMode(0, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);

  Serial.println("Pin modes set");

  digitalWrite(1, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(0, LOW);
  digitalWrite(3, LOW);
  digitalWrite(8, LOW);
  digitalWrite(11, LOW);
  quad1.attach(2);
  quad2.attach(5);
  quad3.attach(10);
  quad4.attach(13);

  //select_propeller.attach(6);
  //set_thurst.attach(7);

  Serial.println("Pin attachments set");
}



void loop() {   

  if (Serial.available()) {
    byte nr = Serial.read();
    //Serial.print("The following char was received: ");
    //Serial.println(nr, DEC);

    thrust = (nr, DEC);       

    //propeller = select_propeller.read();     

    if (propeller == 0)
    {
      quad1.write(thrust);
      quad2.write(thrust);
      quad3.write(thrust);
      quad4.write(thrust);
    }
    else if (propeller == 1)
    {
      quad1.write(thrust);
    }
    else if (propeller == 2)
    {
      quad2.write(thrust);
    }
    else if (propeller == 3)
    {
      quad3.write(thrust);
    }
    else if (propeller == 4)
    {
      quad4.write(thrust);
    } 
    Serial.print("New thurst set:");
    Serial.println(nr);
    Serial.println(propeller);
    thrust = 0;
    propeller = 6;    
    delay(1000);
  }
}
