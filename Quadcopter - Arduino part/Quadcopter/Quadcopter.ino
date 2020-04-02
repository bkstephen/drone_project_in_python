#include <Servo.h> 
Servo quad1;
Servo quad2;
Servo quad3;
Servo quad4;

float thrust;

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

  //Serial.println("Pin modes set");

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

  //Serial.println("Pin attachments set");
}
 
void loop() {   

  if (Serial.available()) {

    //reads character of sequence
    byte readLine = Serial.read();   
    char *data = (char*)&readLine;
    Serial.println(*data);    
    
    //propeller = select_propeller.read();
    if (*data == 'A')
    {            
      thrust = ReadFloat();                             
      quad1.write(thrust);
      quad2.write(thrust);
      quad3.write(thrust);
      quad4.write(thrust);
      
      Serial.println(thrust);
    }
    else if (*data == 'X')
    {
      thrust = ReadFloat(); 
      quad1.write(thrust);
    }
    else if (*data == 'x')
    {
      thrust = ReadFloat();  
      quad2.write(thrust);
    }
    else if (*data == 'Y')
    {
      thrust = ReadFloat(); 
      quad3.write(thrust);
    }
    else if (*data == 'y')
    {
      thrust = ReadFloat();  
      quad4.write(thrust);
    }     
  }
  // Serial.println(thrust);
  // thrust = 0;      
}

float ReadFloat()
{  
  delay(150);
  byte readLine = Serial.read();   
  char *data = (char*)&readLine;
  float temp = atof(data);
  for (int i = 0; i <= 1; i++)
  {
    delay(150);
    readLine = Serial.read();   
    data = (char*)&readLine;
    if (*data == '1')
    {
      temp = temp + 0.1;
      return temp;
    }
    else if (*data == '2')
    {
      temp = temp + 0.2;
      return temp;
    }
    else if (*data == '3')
    {
      temp = temp + 0.3;
      return temp;
    }
    else if (*data == '4')
    {
      temp = temp + 0.4;
      return temp;
    }
    else if (*data == '5')
    {
      temp = temp + 0.5;
      return temp;
    }
    else if (*data == '6')
    {
      temp = temp + 0.6;
      return temp;
    }
    else if (*data == '7')
    {
      temp = temp + 0.7;
      return temp;
    }
    else if (*data == '8')
    {
      temp = temp + 0.8;
      return temp;
    }
    else if (*data == '9')
    {
      temp = temp + 0.9;
      return temp;
    }
  }  
  return temp;
}