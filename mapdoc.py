def change_bullet_style(document):
    list_lines = document.split("\n")
    
    convereted_style = map(convert_line,list_lines)
    
    joined_list = "\n".join(convereted_style)
    return joined_list

# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line