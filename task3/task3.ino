#include <Dynamixel2Arduino.h>
#include <math.h>
#include "MyState.h"

#define DXL_SERIAL Serial3
#define DEBUG_SERIAL Serial
const int DXL_DIR_PIN = 84;  // OpenCR Board's DIR PIN.

const uint8_t RIGHT = 1;
const uint8_t LEFT = 2;


const float DXL_PROTOCOL_VERSION = 2.0;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

//This namespace is required to use Control table item names
using namespace ControlTableItem;


// wheel state
float last_left_wheel_degree = 0.0;
float last_right_wheel_degree = 0.0;


void setup() {
  // put your setup code here, to run once:

  // Use UART port of DYNAMIXEL Shield to debug.
  DEBUG_SERIAL.begin(115200);

  // Set Port baudrate to 1milbps. This has to match with DYNAMIXEL baudrate.
  dxl.begin(1000000);
  // Set Port Protocol Version. This has to match with DYNAMIXEL protocol version.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  // Get DYNAMIXEL information
  dxl.ping(LEFT);

  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(LEFT);
  dxl.setOperatingMode(LEFT, OP_VELOCITY);
  dxl.torqueOn(LEFT);

  dxl.ping(RIGHT);

  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(RIGHT);
  dxl.setOperatingMode(RIGHT, OP_VELOCITY);
  dxl.torqueOn(RIGHT);

  last_left_wheel_degree = dxl.getPresentPosition(LEFT, UNIT_DEGREE);
  last_right_wheel_degree = dxl.getPresentPosition(RIGHT, UNIT_DEGREE);
}




void loop() {


  // inverse_forward_kine(0.30);
  straight(0.3, 0.10);           // 0.1 meter per sec
  rotate(180, 0.05, -3.06 / 2);  // rotate 180 degree clockwise, radius 30
  straight(0.3, 0.10);           // 0.1 meter per sec
  rotate(90, 0.0, 3.14);         // rotate 90 degree counter clock wise
  straight(0.3, 0.10);           // 0.1 meter per sec
  rotate(90, 0.0, 3.14);
  straight(0.6, 0.1);
  // inverse_kine(0.1*3.14/2, 3.14/2);
  // delay(5000);

  dxl.setGoalVelocity(RIGHT, 0, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, 0, UNIT_RPM);
  delay(100000);
}