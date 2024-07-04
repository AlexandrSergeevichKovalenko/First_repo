from parser_inputed_line import parse_input
from functions_block import add_contact, change_contact, show_phone, show_all

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except:
            print("Incorrect input. Please create a correct request")

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except:
                print("Incorrect input for adding a number. Please input the command, name and a phone number")
        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except:
                print("Incorrect input for changing a number. Please inpu the the commnd, name and a phone number")
        elif command == "phone":
            try:
                print(show_phone(args, contacts))
            except:
                print("Please enter the Name of a person whose number you would like to find")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
