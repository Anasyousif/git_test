def list_files(parent_directory, current_filepath=""):
    list_paths = []
    for key in parent_directory:
       new_path =  current_filepath + "/" + key
       value = parent_directory[key]
       if isinstance(value,dict):
          list_paths.extend(list_files(value,new_path))
       else:
            list_paths.append(new_path)
    return list_paths       
        