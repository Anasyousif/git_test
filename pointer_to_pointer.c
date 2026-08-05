#include "exercise.h"
#include "stdlib.h"

void allocate_int(int **pointer_pointer, int value) {
  int *new_ptr = malloc(sizeof(int));
  if (new_ptr ==NULL){
    return;
  }

  *new_ptr = value;

  *pointer_pointer = new_ptr;
}
