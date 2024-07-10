from decor import input_error

@input_error(expected_arg_count=2)
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error(expected_arg_count=2)
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"There is no person with {name} name"

@input_error(expected_arg_count=1)
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"The name {name} you have asked for does not exist."

def show_all(contacts):
    if contacts:
        result = ""
        for key, value in contacts.items():
            result += f"Name: {key}, phone: {value}\n"
        return result
    else:
        return "There is no data to output."








