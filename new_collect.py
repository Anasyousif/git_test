def new_collection(initial_docs):
    initial_docs_c = initial_docs.copy()
    def add_doc(doc):
        initial_docs_c.append(doc)
        return initial_docs_c
    return add_doc