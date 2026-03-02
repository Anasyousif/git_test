def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_func(filename,content):
        parts = filename.split('.')
        extension = parts[-1]
        if extension in valid_formats:
            return conversion_function(content)
        if extension not in valid_formats:
            raise ValueError("invalid file format")
    return inner_func    
        


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
