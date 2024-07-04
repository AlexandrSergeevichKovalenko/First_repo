def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return(f"There is no person with {name} name")


def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return contacts[name]
    else:
        return("The is no the name you have asked")

def show_all(contacts):
    if len(contacts) > 0:
        result = ""
        for key, value in contacts.items():
            result += f"Name:{key}, phone:{value}\n"
        return result
    else:
        return "There is no data to output"







