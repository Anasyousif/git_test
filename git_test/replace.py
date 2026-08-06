def replacer(old, new):
    # This layer handles the "old" and "new" strings
    def replace(decorated_func):
        # This layer receives the function being decorated
        def wrapper(text):
            # This layer handles the actual string processing
            modified_text = text.replace(old, new)
            return decorated_func(modified_text)
        return wrapper
    return replace

# Apply the decorators in a series to handle the escape sequences
@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"
