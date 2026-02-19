def word_count_memo(document, memos):
    n_memos = memos.copy()
    if document in n_memos:
        return n_memos[document],n_memos
    count = word_count(document)
    n_memos[document] = count
    return  count, n_memos
    


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
