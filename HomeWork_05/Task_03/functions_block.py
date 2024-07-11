import sys
from pathlib import Path
from collections import defaultdict

def get_path():
    if len(sys.argv) < 2:
        print("There is no argument in the command line")
        sys.exit(1)
    log_file_path = Path(sys.argv[1])

    not_necessary_arg = sys.argv[2] if len(sys.argv) > 2 else None

    if not log_file_path.exists() or not log_file_path.is_file():
        print(f"The path{log_file_path} does not exist")
        sys.exit(1)
    path_argument = log_file_path, not_necessary_arg
    return path_argument

def parse_log_line(line: str) -> dict:
    dict_data = {}   
    d,t,l,*m = line.split(" ")
    dict_data["date"] = d
    dict_data["time"] = t
    dict_data["level"] = l
    dict_data["message"] = " ".join(m)
    return dict_data


def load_logs(log_file_path: str) -> list:
    lst = []
    try:
        with open(log_file_path, "r", encoding="utf-8") as file:
            for line in file:
                lst.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Under the provided link {log_file_path} any file has been found")
        sys.exit(1)
    except PermissionError:
        print(f"There is no access to the {log_file_path}.")
        sys.exit(1)
    except IOError as e:
        print(f"An error occured by reading the file: {e}.")
        sys.exit(1)
    return lst

def filter_logs_by_level(logs: list, level: str) -> list:
    result = list()
    for log in logs:
        if log["level"].lower() == level.lower():
            result.append(log) 
    return result

def count_logs_by_level(logs: list) -> dict:
    dct = defaultdict(int)
    for log in logs:
        dct[log["level"]] += 1
    return dct

def display_log_counts(counts: dict, log_level = None):
    lev_header = "Рівень логування"
    quant_header = "Кількість"
    print(f"{lev_header}: < 17 | {quant_header}:< 10")
    print("-"*18 + "|" + "-"*10)
    for level, count in counts.items():
        print(f"{level}: < 17 | {count}:< 10")








    
















    






