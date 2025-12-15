def filter_messages(messages):
    dang_filter = []
    count_of_dangs = []

    for message in messages :
        message = message.split()
        good_words=[]
        dang_words = []
        for word in message:
            if word == "dang":
               dang_words.append(word)
            else :
                 good_words.append(message)
                 filtered_message = " ".join(good_words)
                 dang_filter.append(filtered_message)
                 count = len(dang_words)
        
    return dang_filter