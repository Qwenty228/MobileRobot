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



  float width_from_c = 1.0 / 2.0;
  float wheel_radius = 1.0 / 2.0;

  // float forward_vel = 1.0;
  // float turining_vel = 0.0;

  float x = 0, y = 0, angle = 0;
  float left_vel, right_vel;

  once();
}


void get_pos(int dt) {
  x += wheel_radius * (right_vel + left_vel) * cos(angle) / 2 * dt;
  y += wheel_radius * (right_vel + left_vel) * sin(angle) / 2 * dt;
  angle += wheel_radius * (right_vel - left_vel) / (2 * width_from_c) * dt;
}

void once() {
  int w1 = (forward_vel - turning_vel * width_from_c) / wheel_radius;
  int w2 = (forward_vel + turning_vel * width_from_c) / wheel_radius;


  dxl.setGoalVelocity(RIGHT, w1, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, -w2, UNIT_RPM);
  DEBUG_SERIAL.print("Present Velocity(raw) : ");
  left_vel = dxl.getPresentVelocity(LEFT, UNIT_RPM);
  right_vel = dxl.getPresentVelocity(RIGHT, UNIT_RPM);
  DEBUG_SERIAL.print(left_vel);
  DEBUG_SERIAL.print(" ");
  DEBUG_SERIAL.println(right_vel);
  delay(1000);
  DEBUG_SERIAL.println(get_pos(1));



  dxl.setGoalVelocity(RIGHT, 0, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, 0, UNIT_RPM);
}