def available_quests(quest_levels,player_level):
    available_quests_list = []
    for quest_evel in quest_levels:
        if quest_evel <= player_level:
            available_quests_list.append(quest_evel)
    return available_quests_list