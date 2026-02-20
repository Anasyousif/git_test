default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    c_commands = commands.copy()
    c_commands[new_command] = function
    return c_commands


def add_format(formats, format): 
    format_l = [format]
    combined = formats + format_l
    return combined


def save_document(docs, file_name, doc):
    c_docs = docs.copy()
    c_docs[file_name] = doc
    return c_docs


def add_line_break(line):
    return f"{line}\n\n"
