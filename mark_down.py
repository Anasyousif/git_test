def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        new_args = list(map(convert_md_to_txt,args))
        def clean_item_tuple(item_tuple):
            key,value  = item_tuple
            return (key,convert_md_to_txt(value))
        new_Kwargs = dict(map(clean_item_tuple,kwargs.items()))
        return func(*new_args,**new_Kwargs)
            

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
