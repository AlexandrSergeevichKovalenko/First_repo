from class_file_for_task import *

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            print ("The contacts list is empty")
        except TypeError:
            return "Inputted name consist of unapproppriate signs"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if not name.isdigit():
        contacts[name] = phone
        return "Contact added."
    else:
        raise TypeError

@input_error
def change_contact(args, contacts):
    name, *phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error    
def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return contacts[name]
    else:
        raise KeyError

@input_error   
def show_all(contacts):
    if len(contacts) >= 1:
        for key, value in contacts.items():
            print(key, value)
    else:
        raise IndexError


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

