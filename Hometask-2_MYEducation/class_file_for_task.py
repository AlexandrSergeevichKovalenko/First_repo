from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def phone_validation(self):
        if len(self.value) >=10 and self.value.isdigit():
            return True
        else:
            return False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, value):
        phone = Phone(value)
        if phone.phone_validation() == True:
            self.phones.append(phone)
        else:
            print("Inputted number is incorrect")
        
    def remove_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                self.phones.remove(phone)


    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
        
    def find_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                return value
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, new_record):
        self.data[new_record.name.value] = new_record

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        
        def delete(self, name):
            if name in self.data.keys():
                 del self.data[name]
        
