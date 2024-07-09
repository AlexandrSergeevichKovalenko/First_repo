error_massages = {

    "add_contact": "Enter the correct argument for the command as follow: command name number",
    "change_contact": "Incorrect input for changing a number. Please input the command, name and a phone number",
    "show_phone": "Please enter the Name of a person whose number you would like to find",
    "parser": "Incorrect input. Please create a correct request"

}
def input_error(error_message_key):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                return error_massages[error_message_key]
        return inner
    return decorator


