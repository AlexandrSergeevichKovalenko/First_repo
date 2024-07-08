from typing import Callable, Generator
import re
from pathlib import Path

def generator_numbers(text:str) -> Generator[float, None, None]:
    pattern = re.compile(r"\s\d+\.?\d*\s")
    matchs = re.findall(pattern, text)
    for match in matchs:
        yield float(match.strip())
    
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total = sum(func(text))
    
    return total
    

current_dir = Path(__file__).parent
with open(current_dir/"just_text.txt", "r", encoding="utf-8") as file:
    text = file.read()


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")