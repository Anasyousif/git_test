class HashMap:
    def insert(self, key, value):
        # Resize before inserting to ensure there is enough space
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def current_load(self):
        # If the list is empty, return 1 as per instructions
        if len(self.hashmap) == 0:
            return 1
        
        # Count buckets that are not None
        filled_buckets = 0
        for bucket in self.hashmap:
            if bucket is not None:
                filled_buckets += 1
        
        # Return the ratio of filled buckets to total buckets
        return filled_buckets / len(self.hashmap)

    def resize(self):
        # Handle the case of an empty hashmap
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return

        # Check if we need to resize (load >= 5%)
        if self.current_load() < 0.05:
            return

        # Store current hashmap and create a new one 10x the size
        temp_hashmap = self.hashmap
        new_size = len(self.hashmap) * 10
        self.hashmap = [None for _ in range(new_size)]

        # Re-insert all key-value pairs into the new larger hashmap
        for pair in temp_hashmap:
            if pair is not None:
                # We call key_to_index again because the length of self.hashmap 
                # has changed, which changes the modulo result
                key, value = pair
                index = self.key_to_index(key)
                self.hashmap[index] = (key, value)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final