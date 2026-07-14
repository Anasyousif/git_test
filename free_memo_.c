#include "snekobject.h"

void snek_object_free(snek_object_t *obj) {
  if(obj== NULL){
    return;
  }
  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
    break;
  case STRING:
    if(obj->data.v_string != NULL){
      free(obj->data.v_string);
    }
    break;
  case VECTOR3: {
    break;
  }
  case ARRAY: {
    if(obj->data.v_array.elements != NULL){
      free(obj->data.v_array.elements);
      
    }
    break;
  }
  }
  free(obj);
}
