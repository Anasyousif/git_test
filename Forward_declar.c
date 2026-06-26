typedef struct SnekObject snekobject_t;
 struct SnekObject {
  char *name;
  snekobject_t *child;
  snekobject_t;
 };

snekobject_t new_node(char *name);