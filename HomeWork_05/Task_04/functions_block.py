from decor import input_error

@input_error(
    {
        "ValueError": "Please provide a valid name and phone number.",
        "TypeError": "Invalid input type.",
        "IndexError": "You did not provide enough arguments."
    },
    expected_arg_count=2
)
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error(
    {
        "ValueError": "Please provide a valid name and phone number.",
        "TypeError": "Invalid input type.",
        "IndexError": "You did not provide enough arguments."
    },
    expected_arg_count=2
)
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return (f"There is no person with {name} name")

@input_error(
    {
        "ValueError": "Please provide a valid name.",
        "TypeError": "Invalid input type.",
        "IndexError": "You did not provide enough arguments."
    },
    expected_arg_count=1
)
def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return contacts[name]
    else:
        return "The is no the name you have asked"

def show_all(contacts):
    if len(contacts) > 0:
        result = ""
        for key, value in contacts.items():
            result += f"Name: {key}, phone: {value}\n"
        return result
    else:
        return "There is no data to output"







