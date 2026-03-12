def args_logger(*args, **kwargs):
    for i, arg in enumerate(args,start=1):
        print(f"{i}. {arg}")
    for key in sorted(kwargs.keys()):
        value = kwargs[key]
        print(f"* {key}: {value}")