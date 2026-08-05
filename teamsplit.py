def split_players_into_teams(players):
    odd_words = players[1::2]
    even_words = players[0::2]

    return even_words,odd_words