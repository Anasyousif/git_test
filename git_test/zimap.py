def zipmap(keys, values):
    # Base Case: If either list is empty, return an empty dictionary
    if not keys or not values:
        return {}

    # Recursive Call: Get the dictionary for the REST of the items
    # We slice both lists starting from index 1
    new_dic = zipmap(keys[1:], values[1:])

    # Update Step: Add the CURRENT first elements to that dictionary
    # keys[0] becomes the key, values[0] becomes the value
    new_dic[keys[0]] = values[0]

    return new_dic