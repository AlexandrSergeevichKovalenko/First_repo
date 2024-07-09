import datetime
from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week (users):
    congrat_list_of_names = defaultdict(list)
    today = datetime.today().date()
    day_of_week = today.weekday()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
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
    
    
    for key in congrat_list_of_names.keys():
        print(f"{key}: {' ,'.join(congrat_list_of_names[key])}")
                



users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}, {"name": "Gaiduchik Svitlana", "birthday": datetime(2020, 4, 11 )}, {"name": "Ilon Mask", "birthday": datetime(1958, 5, 20)}, {"name": "Jeff Bezos", "birthday": datetime(1985, 11, 15)}, {"name": "Britney Spiers", "birthday": datetime(1985, 11, 13)}, {"name": "Kovalenko Sasha", "birthday": datetime(1981, 11, 12)}]

get_birthdays_per_week(users)