#include "exercise.h"

float get_average(int x, int y, int z){
  // By casting 'x' to a float first, C is forced to treat the 
  // remaining additions as float math, preventing integer overflow.
  return ((float)x + y + z) / 3;
}