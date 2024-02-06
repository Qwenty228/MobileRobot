#include <Dynamixel2Arduino.h>

#define DXL_SERIAL Serial3
#define DEBUG_SERIAL Serial
const int DXL_DIR_PIN = 84;  // OpenCR Board's DIR PIN.

const uint8_t RIGHT = 1;
const uint8_t LEFT = 2;


const float DXL_PROTOCOL_VERSION = 2.0;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

//This namespace is required to use Control table item names
using namespace ControlTableItem;

void setup() {
  // put your setup code here, to run once:

  // Use UART port of DYNAMIXEL Shield to debug.
  DEBUG_SERIAL.begin(115200);

  // Set Port baudrate to 57600bps. This has to match with DYNAMIXEL baudrate.
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

  once();
}

void once(){
  dxl.setGoalVelocity(RIGHT, 25.8, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, 25.8, UNIT_RPM);
  delay(1000);
  dxl.setGoalVelocity(RIGHT, 0, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, 0, UNIT_RPM);
  delay(1000);
}

void loop() {

}