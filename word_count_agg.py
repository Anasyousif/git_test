def word_count_aggregator():
    count = 0
    def count_words(doc):
        nonlocal count
        count += len(doc.split())
        return count
    return count_words
    
