#include <IRremote.h>

int ip = 2;
int led = 13;
char i;
IRrecv irrecv(ip);
decode_results results;

int a = 1;
int b = 1;

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
  pinMode(led, OUTPUT);
}

void loop(){
  if (irrecv.decode(&results)) {
     Serial.println(results.value, HEX); 
     digitalWrite(led, HIGH);
     delay(50);
     digitalWrite(led, LOW);   
     irrecv.resume();
  }   
}
