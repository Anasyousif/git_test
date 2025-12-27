def get_character_record(name, server, level, rank):
    character = {
        "name":name,
        "server":server,
        "level":level,
        "rank":rank,
        "id": name +"#"+ server
    }

    return character   
