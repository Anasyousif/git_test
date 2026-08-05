#include <stddef.h>
#include <stdbool.h>
#include <stdlib.h>
#include "vm.h"

void trace_mark_object(stack_t *gray_objects, snek_object_t *obj) {
  // If the object is NULL or already marked, return immediately
  if (obj == NULL || obj->is_marked) {
    return;
  }

  // Mark the object and push it onto the gray_objects stack
  obj->is_marked = true;
  stack_push(gray_objects, obj);
}

void trace_blacken_object(stack_t *gray_objects, snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }

  // Check the type of the object
  switch (obj->kind) { 
    case INTEGER:
    case FLOAT:
    case STRING:
      // These don't contain references to other objects, do nothing.
      break;

    case VECTOR3:
      // Accessing via the exact union member 'v_vector3'
      trace_mark_object(gray_objects, obj->data.v_vector3.x);
      trace_mark_object(gray_objects, obj->data.v_vector3.y);
      trace_mark_object(gray_objects, obj->data.v_vector3.z);
      break;

    case ARRAY: 
      // Accessing via the exact union member 'v_array' and its fields 'size' and 'elements'
      for (size_t i = 0; i < obj->data.v_array.size; i++) {
        trace_mark_object(gray_objects, obj->data.v_array.elements[i]);
      }
      break;
  }
}

void trace(vm_t *vm) {
  if (vm == NULL || vm->objects == NULL) {
    return;
  }

  // Create a new stack with a capacity of 8 called gray_objects
  stack_t *gray_objects = stack_new(8);
  if (gray_objects == NULL) {
    return;
  }

  // Iterate over each of the objects in the VM
  for (size_t i = 0; i < vm->objects->count; i++) {
    snek_object_t *obj = (snek_object_t *)vm->objects->data[i];
    
    // If the object is marked, push it onto the gray_objects stack
    if (obj != NULL && obj->is_marked) {
      stack_push(gray_objects, obj);
    }
  }

  // Process the gray objects stack until empty
  while (gray_objects->count > 0) {
    snek_object_t *obj = (snek_object_t *)stack_pop(gray_objects);
    trace_blacken_object(gray_objects, obj);
  }

  // Free the gray_objects stack
  stack_free(gray_objects);
}

// don't touch below this line
// don't touch below this line

void mark(vm_t *vm) {
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_t *frame = vm->frames->data[i];
    for (size_t j = 0; j < frame->references->count; j++) {
      snek_object_t *obj = frame->references->data[j];
      obj->is_marked = true;
    }
  }
}

void frame_reference_object(frame_t *frame, snek_object_t *obj) {
  stack_push(frame->references, obj);
}

vm_t *vm_new() {
  vm_t *vm = malloc(sizeof(vm_t));
  if (vm == NULL) {
    return NULL;
  }

  vm->frames = stack_new(8);
  vm->objects = stack_new(8);
  return vm;
}

void vm_free(vm_t *vm) {
  // Free the stack frames, and then their container
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);

  // Free the objects, and then their container
  for (size_t i = 0; i < vm->objects->count; i++) {
    snek_object_free(vm->objects->data[i]);
  }
  stack_free(vm->objects);

  free(vm);
}

void vm_frame_push(vm_t *vm, frame_t *frame) { stack_push(vm->frames, frame); }

frame_t *vm_new_frame(vm_t *vm) {
  frame_t *frame = malloc(sizeof(frame_t));
  frame->references = stack_new(8);

  vm_frame_push(vm, frame);
  return frame;
}

void frame_free(frame_t *frame) {
  stack_free(frame->references);
  free(frame);
}

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
}
