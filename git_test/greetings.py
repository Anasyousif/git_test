def format_full_name(first_name, last_name):
    full_name = first_name +" "+ last_name
    return full_name


def make_greeting(name, title):
    return "Welcome, "+ title + " " + name + "!"

def create_profile_greeting(first_name, last_name, title):
    full_name = format_full_name(first_name, last_name)
    greeting = make_greeting(full_name,title)
    
    return greeting