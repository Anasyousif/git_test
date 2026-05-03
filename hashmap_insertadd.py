class HashMap:
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True

        # Loop while the slot is full and the key is different
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            
            # Linear Probing: move to the next slot and wrap around
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
            
        # Place the key-value pair in the found slot
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True

        while self.hashmap[index] is not None:
            # Check if the key at this slot is what we're looking for
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            
            # If we've looped back to the start, the key isn't here
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            
            index = (index + 1) % len(self.hashmap)
            first_iteration = False

        # If the loop hits a None slot, the key definitely isn't in the map
        raise Exception("sorry, key not found")

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