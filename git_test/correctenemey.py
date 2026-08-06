def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    winner_name = None
    for name , count in enemies_dict.items():
        if max_so_far < count:
           max_so_far = count
           winner_name = name

    return winner_name