def summarize_loot(loot):
    # 1. Create an empty result list (Done in your original code)
    result = []
    
    # Optional: Handle empty input list gracefully
    if not loot:
        return result 
        
    # 2. Loop over each item in the input loot list
    for item in loot:
        found = False # Flag to track if the item was found in 'result'
        
        # Loop over the current result list to find a match
        for entry in result:
            # entry will be like ['sword', 1]
            existing_item_name = entry[0]
            
            # Check if it is already in result
            if existing_item_name == item:
                # If it is already in result, increase that entry's count by 1
                entry[1] += 1
                found = True
                break # Exit the inner loop, we found and updated the count
        
        # If the inner loop finished and the item wasn't found
        if not found:
            # If it is not in result, add a new entry like [item, 1]
            result.append([item, 1])
            
    return result

# Example Usage:
loot_items = ['Gold Coin', 'Sword', 'Gold Coin', 'Shield', 'Sword', 'Gold Coin', 'Potion']
summary = summarize_loot(loot_items)
print(summary)
# Output: [['Gold Coin', 3], ['Sword', 2], ['Shield', 1], ['Potion', 1]]