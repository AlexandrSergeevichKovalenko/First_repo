import sys
from pathlib import Path

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


def load_logs(path_argument: str) -> list:
    lst = []
    log_file_path = path_argument[0]
    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:
            lst.append(parse_log_line(line))
    return lst



    






