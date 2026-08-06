def get_median_font_size(font_sizes):
    if font_sizes == []:
        return None
    else:     
        new_font = sorted(font_sizes)
        middle_index = (len(new_font)-1) //2
        return new_font[middle_index]
