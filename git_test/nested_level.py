def count_nested_levels(nested_documents, target_document_id, level=1):
    for id in nested_documents:
        if id == target_document_id:
            return level
        sub_documents = nested_documents[id]
        result = count_nested_levels(sub_documents,target_document_id,level + 1)
        if result != -1:
            return result
     
    return -1
            
            