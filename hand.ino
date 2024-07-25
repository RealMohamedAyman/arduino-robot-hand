#include<Servo.h>

Servo finger[5];

void setup() {
  Serial.begin(9600);

  finger[0].attach(6);
  finger[1].attach(5);
  finger[2].attach(4);
  finger[3].attach(3);
  finger[4].attach(2);

  for(int i = 0; i < 5; i++)
  {
    finger[i].write(180);
    delay(500);
  }
}

void loop() {
  if (Serial.available() > 0) 
  {
    String c = Serial.readStringUntil('p');
    for(int i = 0; i < 5; i++)
    {
      if (c[i+1]=='1') {
        finger[i].write(0);
      } else {
        finger[i].write(180);
      }
    }
  }
}

