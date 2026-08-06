def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
        if option == "--one":
            result1 = filter_one(content)
            return result1
        elif option == "--two":
            result_2 = filter_two(content)
            return result_2
        elif option == "--three":
            c_result = filter_two(filter_one(content))
            return c_result
        else:
            raise Exception("invalid option")
             
    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
