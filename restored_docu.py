def restore_documents(originals, backups):
    return {doc.upper() for doc in (originals + backups) if not doc.isdigit()}