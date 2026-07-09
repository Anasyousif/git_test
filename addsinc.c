snek_object_t *snek_add(snek_object_t *a, snek_object_t *b) {
  if (a == NULL || b == NULL) {
    return NULL;
  }

  switch (a->kind) {
    case INTEGER: {
      if (b->kind == INTEGER) {
        return new_snek_integer(a->data.v_int + b->data.v_int);
      } else if (b->kind == FLOAT) {
        return new_snek_float((float)a->data.v_int + b->data.v_float);
      }
      return NULL;
    }
    
    case FLOAT: {
      if (b->kind == INTEGER) {
        return new_snek_float(a->data.v_float + (float)b->data.v_int);
      } else if (b->kind == FLOAT) {
        return new_snek_float(a->data.v_float + b->data.v_float);
      }
      return NULL;
    }
    
    case STRING: {
      if (b->kind != STRING) {
        return NULL;
      }

      size_t len_a = strlen(a->data.v_string);
      size_t len_b = strlen(b->data.v_string);
      size_t total_len = len_a + len_b + 1;

      char *temp_str = calloc(total_len, sizeof(char));
      if (temp_str == NULL) {
        return NULL;
      }
      strcat(temp_str, a->data.v_string);
      strcat(temp_str, b->data.v_string);

      snek_object_t *new_obj = new_snek_string(temp_str);
      free(temp_str);
      return new_obj; 
    }

    case VECTOR3: {
      if (b->kind != VECTOR3) { // Fixed typo
        return NULL;
      }
      snek_object_t *new_x = snek_add(a->data.v_vector3.x, b->data.v_vector3.x);
      snek_object_t *new_y = snek_add(a->data.v_vector3.y, b->data.v_vector3.y);
      snek_object_t *new_z = snek_add(a->data.v_vector3.z, b->data.v_vector3.z);

      if (new_x == NULL || new_y == NULL || new_z == NULL) {
        return NULL;
      }
      return new_snek_vector3(new_x, new_y, new_z); // Fixed function name
    }

    case ARRAY: {
      if (b->kind != ARRAY) {
        return NULL;
      }
      size_t size_a = a->data.v_array.size;
      size_t size_b = b->data.v_array.size;
      size_t combined_size = size_a + size_b;

      snek_object_t *new_arr = new_snek_array(combined_size);
      if (new_arr == NULL) {
        return NULL;
      }

      for (size_t i = 0; i < size_a; i++) {
        snek_object_t *item = snek_array_get(a, i);
        snek_array_set(new_arr, i, item);
      }

      for (size_t i = 0; i < size_b; i++) {
        snek_object_t *item = snek_array_get(b, i);
        snek_array_set(new_arr, size_a + i, item); // Fixed dynamic offset indexing
      }

      return new_arr;
    }

    default:
      return NULL;
  } // Properly closed the switch block here
}