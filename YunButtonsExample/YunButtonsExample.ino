#include <Console.h>
#include <FileIO.h>
#include <Process.h>
#include <YunClient.h>
#include <HttpClient.h>
#include <Bridge.h>
#include <Mailbox.h>
#include <YunServer.h>

/*

Using Yun as a button to control a JEMMA Appliance

This tutorial is based on the Button Tutorial: http://www.arduino.cc/en/Tutorial/Button
 
You should use the same circuit as in the button tutorial:
 * LED attached from pin 13 to ground
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground

 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.

*/

const int buttonPin = 2;     // the number of the pushbutton pin A
const int ledPin =  13;      // the number of the LED pin

// variables to store button status
int oldbuttonState = LOW;         // variable for storing the old pushbutton status
int newbuttonState = LOW;         // variable for reading the pushbutton status


void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pins as an input:
  pinMode(buttonPin, INPUT);

  //yun code to connect the serial interface
  Bridge.begin();   // Initialize the Bridge
  Serial.begin(9600);   // Initialize the Serial

  // Uncomment the following line if you want to wait until a Serial Monitor is connected.
  //while (!Serial);
}

void loop() {
  // read the state of the pushbutton value:
  newbuttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed and previously was low.
  if ((newbuttonState == HIGH) && ( oldbuttonState == LOW)) {
    runCommand();
  }
  else {
    //do nothing
  }

  //storing the new "old" status
  oldbuttonState = newbuttonState;
}

String myout;

void runCommand() {
  Process p;

  //lighitng up the led
  digitalWrite(ledPin, HIGH);

  // this shell command uses https://github.com/ismb/py-jemma-dal-rest-client
  // remember to copy it inside /root of the Yun
  // remember to put the right ip address, port and funcion DAL identifiers for the device
  p.runShellCommand("python /root/py-jemma-dal-rest-client-0.9.2/py-jemma-dal-rest-client.py -a 192.168.10.103 -c operate -d \"ZigBee:EletricHeater:ah.app.3521399293210526015-8\" -f \"OnOff\" -o \"reverse\"");

  // do nothing until the process finishes, so you get the whole output:
  while (p.running());

  // Read command output:
  while (p.available()) {
    char c = p.read();
    myout += c;
  }

  Serial.println(myout);         // print the number as well
  myout = "";

  //turn off the led
  digitalWrite(ledPin, LOW);
}


