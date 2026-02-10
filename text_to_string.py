def file_to_prompt(file, to_string):
    file_string = to_string(file)
    return f"```\n{file_string}\n```"
    
