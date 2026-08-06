#include "exercise.h"

codefile_t change_filetype(codefile_t *f, int new_filetype) {
    // 1. Declare a regular struct variable (not a pointer)
    // 2. Dereference the pointer 'f' to make a copy of the entire struct
    codefile_t new_f = *f;
    
    // 3. Update the filetype on the copy
    new_f.filetype = new_filetype;
    
    // 4. Return the updated copy (the original remains completely untouched!)
    return new_f;
}