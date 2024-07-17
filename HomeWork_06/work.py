from collections import UserDict

class Field:
    def __init__(self, value):
      self.value = value

    def __str__(self):
      return str(self.value)

class Name(Field):
		pass

class Phone(Field):
  @staticmethod
  def validate(number):
    return True if number.isdigit() and len(number) >= 10 else False

class Record:
    def __init__(self, name):
      self.name = Name(name)
      self.phones = []

    def add_phone(self, phone_number: str):
      if Phone.validate(phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)
      else:
        raise ValueError("The entered number is not correct. Please enter the correct one.")

    def remove_phone(self, phone_number: str):
      self.phones = [phone for phone in self.phones if phone.value !=phone_number]

    def edit_phone(self, old_number: str, new_number: str):
      for phone in self.phones:
        if phone.value == old_number:
          phone.value = new_number
          return
      raise ValueError("The phone number you entered does not exist")

    def find_phone(self, num_phone:str):
      for phone in self.phones:
        if phone.value == num_phone:
          return phone
      raise ValueError("The number was not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
  def add_record(self, note: Record):
    self.data[note.name.value] = note

  def find(self,name: str) -> Record:
    if name in self.data:
      return self.data[name]
    return None

  def delete(self, name:str) -> None:
    if name in self.data:
      del self.data[name]

  def __str__(self):
    output = ["AddressBook: "]
    for key in self.data:
      contact_description_line = (
          f"name: {self.data[key].name.value}, phones: {'; '.join(phone.value for phone in self.data[key].phones)}"
      )
      output.append(contact_description_line)
    total_info_line = "\n".join(output)
    return total_info_line