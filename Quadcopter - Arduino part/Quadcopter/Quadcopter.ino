#include <Servo.h> 
Servo quad1;
Servo quad2;
Servo quad3;
Servo quad4;

float thrust = 0;

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

    //reads character of sequence
    byte readLine = Serial.read();   
    char data = readLine;
    //Serial.println(data);
    //propeller = select_propeller.read();
    if (data == 'A')
    {        
      thrust = ConCatStringToFloat();
      quad1.write(thrust);
      quad2.write(thrust);
      quad3.write(thrust);
      quad4.write(thrust);
    }
    else if (data == 'X')
    {
      thrust = ConCatStringToFloat();
      quad1.write(thrust);
    }
    else if (data == 'x')
    {
      thrust = ConCatStringToFloat();
      quad2.write(thrust);
    }
    else if (data == 'Y')
    {
      thrust = ConCatStringToFloat();
      quad3.write(thrust);
    }
    else if (data == 'y')
    {
      thrust = ConCatStringToFloat();
      quad4.write(thrust);
    } 
    //delay(1000);
    //Serial.println(thrust);
    data = 'N/A';
  }
  thrust = 0;    
}

float ConCatStringToFloat()
{
  char temp[] = "";  
  char c;  
  byte readLine = Serial.read(); 
  c = readLine;

  while (c != 'e'){               
    strncat(temp, &c, 1);
    readLine = Serial.read(); 
    c = readLine;        
    Serial.println(c);
  }

  Serial.println(temp);
  float result = atof(temp);  
  return result;
}
