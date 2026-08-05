import functools

def join(doc_so_far, sentence):
    # Add both the period AND the space here
    return doc_so_far + ". " + sentence

def join_first_sentences(sentences, n):
    if n == 0:
        return "" # Empty string
        
    # reduce() combines the first n sentences
    combined = functools.reduce(join, sentences[:n])
    
    # Add the final period here before returning
    return combined + "."