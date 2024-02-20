#include "MyState.h"

#define DEG_TO_RAD (M_PI / 180.0)
#define RAD_TO_DEG (180.0 / M_PI)
#define MPS2RPM (60 / (2 * M_PI))

float width_from_c = 0.16 / 2.0;
float wheel_radius = 0.066 / 2.0;

float forward_vel = 0;
float turning_speed = 0;


state car = { 0.0, 0.0, 0.0, 0.0 };

void inverse_kine(float v, float w){
  forward_vel = v * MPS2RPM;
  turning_speed = w;

  int w1 = (forward_vel - turning_speed * width_from_c) / wheel_radius;
  int w2 = (forward_vel + turning_speed * width_from_c) / wheel_radius;

  dxl.setGoalVelocity(RIGHT, w1, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, w2, UNIT_RPM);
}
// moving indefinetely second with v meter/sec and +w degree/sec counter clockwise
// updating robot position every 0.1 seconds
void move(float v, float w, state *substate) {
  // inverse kinematic
  // convert from meter per second to radiants per minute
  forward_vel = v * MPS2RPM;
  turning_speed = w;

  int w1 = (forward_vel - turning_speed * width_from_c) / wheel_radius;
  int w2 = (forward_vel + turning_speed * width_from_c) / wheel_radius;

  dxl.setGoalVelocity(RIGHT, w1, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, w2, UNIT_RPM);

  // checking position every 100 milliseconds
  delay(100);

  // forward kinematic
  float left_wheel_degree = dxl.getPresentPosition(LEFT, UNIT_DEGREE);
  float right_wheel_degree = dxl.getPresentPosition(RIGHT, UNIT_DEGREE);

  float l_vel = (left_wheel_degree - last_left_wheel_degree) * DEG_TO_RAD;
  float r_vel = (right_wheel_degree - last_right_wheel_degree) * DEG_TO_RAD;

  last_left_wheel_degree = left_wheel_degree;
  last_right_wheel_degree = right_wheel_degree;

  float delta_p = (wheel_radius / 2) * (r_vel + l_vel);
  float delta_theta = (wheel_radius / (2 * width_from_c)) * (r_vel - l_vel);

  // overall position
  car.theta += delta_theta;
  // state per function call
  substate->theta += delta_theta * RAD_TO_DEG;


  float delta_x = delta_p * cos(car.theta);
  float delta_y = delta_p * sin(car.theta);

  substate->mag += delta_p;

  car.x += delta_x;
  car.y -= delta_y;

  // verbose
  print_state();
}

// print car current state
void print_state() {

  DEBUG_SERIAL.print("T: ");
  DEBUG_SERIAL.print(car.theta * RAD_TO_DEG);
  DEBUG_SERIAL.print(" ,X:");
  DEBUG_SERIAL.print(car.x);
  DEBUG_SERIAL.print(" ,Y:");
  DEBUG_SERIAL.print(car.y);
  DEBUG_SERIAL.println();
}


/**
 * Move in straight line.
 * 
 * @param meter distance.
 *               Data Type: float
 *               Purpose: Represents the distance to travel.
 *               Constraints: Must be a positive value.
 * 
 * @param speed meter/second.
 *              Data Type: float
 *              Purpose: Represents robot speed.
 */
void straight(float meter, float speed) {
  state c = { 0.0, 0.0, 0.0, 0.0 };
  while (abs(c.mag) < abs(meter)) {
    move(speed, 0.0, &c);
  }
  dxl.setGoalVelocity(RIGHT, 0, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, 0, UNIT_RPM);
  delay(500);
  print_state();
}
/**
 * Rotate the robot.
 * 
 * @param degree degree.
 *               Data Type: float
 *               Purpose: Represents robot rotation.
 *               Constraints: Must be a positive value.
 * 
 * @param speed degree/second.
 *              Data Type: float
 *              Purpose: Represents the turning speed.
 *
 * @param radius meter.
 *               Data Type: float
 *               Purpose: Represent the ICC radius.   
 */
void rotate(float degree, float v, float w) {
  state c = { 0.0, 0.0, 0.0, 0.0 };

  // float time = abs(degree / speed);
  // float fw = degree*radius / time;

  while (abs(c.theta) < abs(degree)) {
    move(v, w, &c);
  }
  dxl.setGoalVelocity(RIGHT, 0, UNIT_RPM);
  dxl.setGoalVelocity(LEFT, 0, UNIT_RPM);
  delay(500);
  print_state();
}
