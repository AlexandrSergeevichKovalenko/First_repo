def input_error(error_messages, expected_arg_count = None):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                if not args or not args[0]:
                    raise IndexError(error_messages.get("IndexError", "You did not provide enough arguments."))
                if expected_arg_count is not None and len(args[0]) != expected_arg_count:
                    raise ValueError(error_messages.get("ValueError", "Please provide exactly two arguments: name and phone."))
                if func.__name__ in ["add_contact", "change_contact"]:
                    if not args[0][0].isalpha():
                        raise ValueError(error_messages.get("ValueError", "Invalid format for name. Please use alphabetic characters only."))
                    if not args[0][1].isdigit():
                        raise ValueError(error_messages.get("ValueError", "Invalid format for phone. Please use numeric characters only."))
                return func(*args, **kwargs)
            except Exception as e:
                error_type = type(e).__name__
                return error_messages.get(error_type, str(e))
        return inner
    return decorator

