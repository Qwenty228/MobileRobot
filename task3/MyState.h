#ifndef MyState_h
#define MyState_h

#include <WString.h>

// virtual state
typedef struct {
  float x;      // meter
  float y;      // meter
  float theta;  // rad
  float mag;    // (magnitude) meter
} state;

#endif