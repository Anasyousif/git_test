#include "vm.h"
#include <stdlib.h>
vm_t *vm_new() {
  vm_t *vm = malloc(sizeof(vm_t)); 
  if (vm == NULL){
    return NULL;
  }
  vm->frames = stack_new(8);
  vm->objects = stack_new(8);

  if(vm->frames == NULL || vm->objects == NULL){
    if(vm->frames !=NULL) stack_free(vm->frames);
    if(vm->objects !=NULL) stack_free(vm->objects);
    free(vm);
    return NULL;
  }
  return vm;
}

void vm_free(vm_t *vm) {
  if(vm->frames != NULL) {
    stack_free(vm->frames);
  }
   if(vm->objects != NULL) {
    stack_free(vm->objects);
  }
  free(vm);
}
