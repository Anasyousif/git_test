def filter_messages(messages):
    # ... lists initialized ...

    for message in messages:
        # 1. Initialization for THIS message
        #    ... good_words = [] etc.

        for word in message:
            # 2. Conditional Sorting
            if word == "dang":
                dang_words.append(word)
            else:
                good_words.append(word) # <--- This line is now correctly indented here!

        # 3. Finalization (MUST BE HERE, after the inner loop is DONE)
        #    Join the words
        #    Append the filtered message to dang_filter
        #    Calculate the count
        #    Append the count to count_of_dangs

    # 4. Final Return
    return ...