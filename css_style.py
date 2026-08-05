import copy

def css_styles(initial_styles):
    # Use the copy module to create a deep copy of the nested dict
    styles_copy = copy.deepcopy(initial_styles)

    def add_style(selector, property, value):
        # Step 1: Check if the selector exists, if not, create it
        if selector not in styles_copy:
            styles_copy[selector] = {}
        
        # Step 2: Add or update the property inside the selector's dict
        styles_copy[selector][property] = value
        
        # Step 3: Return the entire updated dictionary
        return styles_copy

    # Step 4: Return the inner function (the closure)
    return add_style