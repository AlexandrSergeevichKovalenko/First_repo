from pathlib import Path
import re
#determine the current directory
current_dir = Path(__file__).parent
#subordinate function(just because i wanted to try regex in a purpose of learning) to find salary in the line
def search_number(line:str):
    pattern = re.compile(r"\d+")
    match = pattern.search(line)
    if match:
        only_number = match.group()
        return int(only_number)
    else:
        raise ValueError("No number found in the string")
#open file and calculating average and total salary 
def total_salary(path:str):
    try:
        with open(current_dir/path,"r", encoding="utf-8") as file:
            content = list(map(search_number, file.readlines()))
            print(f"Загальна сума заробітної плати: {sum(content)}, Середня заробітна плата: {sum(content)/len(content)}")
        
    except FileNotFoundError:
        print("The file you are trying to open does not exist, or the path is wrong")


total_salary("salary.txt")
