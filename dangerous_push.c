#include "snekstack.h"
#include "stdlib.h"
#include <stdint.h>

void scary_double_push(stack_t *s) {
  stack_push(s,(void*)(uintptr_t)1337);

  int *heap_ptr = malloc(sizeof(int));
  if(heap_ptr== NULL){
    return;
  }
  *heap_ptr = 1024;

  stack_push(s,heap_ptr);
}
