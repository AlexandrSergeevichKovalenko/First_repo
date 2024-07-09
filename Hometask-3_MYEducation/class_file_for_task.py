from collections import UserDict
from datetime import datetime, date
import datetime as dt
from collections import defaultdict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self.value)

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = datetime.strptime(self.value, '%d.%m.%Y') 
    
    def birthday_validation(self):
        pass  

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
        self.birthday = 0

    def add_birthday(self, date):
        self.birthday = Birthday(date)
    
    def add_phone(self, value):
        phone = Phone(value)
        if phone.phone_validation() == True:
            self.phones.append(phone)
        else:
            raise ValueError
        
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

    def get_birthdays_per_week (self):
        congrat_list_of_names = defaultdict(list)
        today = date.today()
        day_of_week = today.weekday()
        for user in self.data.keys():
            name = self.data[user]
            birthday = self.data[user].birthday.value.date()
            birthday_this_year = birthday.replace(year = today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year = today.year + 1)
            delta_days = (birthday_this_year-today).days
            if delta_days < 7:
                if birthday_this_year.weekday() == 5 or birthday_this_year.weekday() == 6 or birthday_this_year.weekday() == 0:
                    congrat_list_of_names ["Monday"].append(name)
                elif birthday_this_year.weekday() == 1:
                    congrat_list_of_names ["Tuesday"].append(name)
                elif birthday_this_year.weekday() == 2:
                    congrat_list_of_names ["Wednesday"].append(name)
                elif birthday_this_year.weekday() == 3:
                    congrat_list_of_names ["Thursday"].append(name)
                elif birthday_this_year.weekday() == 4:
                    congrat_list_of_names ["Friday"].append(name)
        return congrat_list_of_names
    
    def set_data(self, contact):
        self.data[contact.name.value] = contact
  

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        
    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]

    def add_contact(self, name, phone):
        contact = Record(name)
        contact.add_phone(phone)
        self.data[name] = contact
        
