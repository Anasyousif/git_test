def find_longest_word(document, longest_word=""):
    # 1. Base case for empty string
    if document == "":
        return longest_word
        
    parts = document.split(maxsplit=1)
    first_word = parts[0]

    # 2. Update the record holder if needed
    if len(first_word) > len(longest_word):
        longest_word = first_word

    # 3. Decide: Are we done, or do we keep going?
    # (This should be outside the word-length check)
    if len(parts) == 1:
        return longest_word
    else:
        # ADD THE MISSING 'RETURN' HERE
        return find_longest_word(parts[1], longest_word)