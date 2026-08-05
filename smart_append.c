#include "exercise.h"
#include <string.h>

int smart_append(TextBuffer *dest, const char *src) {
  if (dest == NULL || src == NULL){
    return 1;
  }

  const int MAX_BUFFER_SIZE = 64;

  size_t src_len = strlen(src);

   int max_chars_allowed = MAX_BUFFER_SIZE - 1;
   int remaining_space = max_chars_allowed - dest->length;

   if(src_len > (size_t)remaining_space) {

     strncat(dest->buffer,src,remaining_space);

     dest->length = max_chars_allowed;

     return 1;
   }
  else {
    strcat(dest->buffer,src);
    dest->length += src_len;
    return 0;
  }
}