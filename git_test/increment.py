def generate_user_list(num_of_users):
    player_ids = []

    # The loop iterates 'i' from 0 up to (but not including) num_of_users
    for i in range(0, num_of_users):
        # ***Correction is here:***
        # The unique ID is the incrementing value 'i'.
        player_ids.append(i) 
        
        # ***Removed the incorrect line:***
        # The original line 'num_of_users += i' was incorrectly modifying the loop's limit.
        
    return player_ids