from decor import input_error

@input_error("add_contact")
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error("change_contact")
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return (f"There is no person with {name} name")

@input_error("show_phone")
def show_phone(args, contacts):
    if len(args) > 0:
        name = args[0]
        if name in contacts.keys():
            return contacts[name]
        else:
            return "The is no the name you have asked"
    else:
        return "A person name is to be inputed"

def show_all(contacts):
    if len(contacts) > 0:
        result = ""
        for key, value in contacts.items():
            result += f"Name: {key}, phone: {value}\n"
        return result
    else:
        return "There is no data to output"







