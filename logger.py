def get_logger(formatter):
    # Define the inner function that takes the two strings
    def logger(first, second):
        # Call the formatter passed in from the outer scope
        # and print the result
        print(formatter(first, second))
    
    # Return the function itself (don't call it!)
    return logger

# Don't edit below this line

def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")

def colon_delimit(first, second):
    return f"{first}: {second}"

def dash_delimit(first, second):
    return f"{first} - {second}"

def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)

main()