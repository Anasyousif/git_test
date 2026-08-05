#include "snekstack.h"
#include "stdlib.h"
#include <string.h>

void stack_push_multiple_types(stack_t *s) {
  float *float_ptr = malloc(sizeof(float));
  if(float_ptr != NULL){
    *float_ptr = 3.14f;
    stack_push(s,float_ptr);
  }
  const char *str_const = "Sneklang is blazingly slow!";
  size_t str_len =  strlen(str_const) + 1;
  char *str_copy = malloc(str_len * sizeof(char));
  if(str_copy != NULL){
  strcpy(str_copy,str_const);
  stack_push(s,str_copy);
  }
}
