import re
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
def add_contact(args, contacts:AddressBook):
    name, phone = args

    if not name.isdigit():
        contacts.add_contact(name, phone)
        return "Contact added."
    else:
        raise TypeError

@input_error
def change_contact(args, contacts):
    name, *phone = args
    if name in contacts.data.keys():
        contact = contacts.find(name)
        contact.edit_phone(*phone)
        contacts.set_data(contact)
        return "Contact updated."
    else:
        raise KeyError

@input_error    
def show_phone(args, contacts:AddressBook):
    name = args[0]
    if name in contacts.data.keys():
        return contacts.data[name].phones
    else:
        raise KeyError

@input_error   
def show_all(contacts:AddressBook):
    if len(contacts.data) >= 1:
        for key, value in contacts.data.items():
            print(key, value.phones)
    else:
        raise IndexError
    
@input_error 
def add_birthday(contacts, name, birthday_date):
    birthday_date = re.findall(r'\d{2}\.\d{2}\.\d{4}$',birthday_date)
    if len(birthday_date) == 1:
        birthday_date = birthday_date[0]
        n = contacts.find(name)
        n.add_birthday(birthday_date)
        contacts.set_data(n)
        return "Birthday has been added"
    else:
        raise ValueError

@input_error 
def show_birthday(contacts, name):
    if name in contacts.data.keys():
        n = contacts.find(name)
        birthday = n.birthday.value
        return str(birthday.strftime('%d.%m.%Y'))
        
      
    else:
        raise KeyError
    
def main():
    book = AddressBook()
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
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            phones = show_phone(args, book)
            for i in phones:
                print (i)
        elif command == "all":
            show_all(book)
        elif command == "add-birthday":
            print(add_birthday(book, *args))
        elif command == "show-birthday":
            print (show_birthday(book, *args))
        elif command == "birthdays":
            birthdays_per_week = book.get_birthdays_per_week()
            for day_of_week in birthdays_per_week.keys():
                print(f"{day_of_week}: {list(map(lambda x: x.name.value, birthdays_per_week[day_of_week]))} ")



        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()

