import sys
from pathlib import Path
from colorama import Fore, Back, Style

#find the current dir 
def find_the_path():
    #check if the command line exists
    if len(sys.argv) < 2:
        print("Usage: python print_path.py <path>")
        sys.exit(1)
    #get the path from the command line argument
    path = Path(sys.argv[1])

    #check if the path exists
    if not path.exists():
        print(f"The path {path} does not exists")
        sys.exit(1)
    if path.is_file():
        directory = path.parent
    else:
        directory = path
    return directory

def print_dir_content(current_dir = find_the_path(), shift=0, extensions_colors=None):
    if extensions_colors is None:
        extensions_colors = {'.py': Fore.YELLOW + Back.BLUE, '.txt': Fore.GREEN + Back.YELLOW}

    for path in current_dir.iterdir():
        if path.is_dir():
            print(' ' * shift + f'- {path.name}')
            print_dir_content(path, shift + 2)
        elif path.suffix in extensions_colors:
            styles = extensions_colors[path.suffix]
            print(' ' * shift + styles + path.name + Style.RESET_ALL)
        else:
            print(' ' * shift + path.name)


print_dir_content()


    
    






