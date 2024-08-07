from contextlib import contextmanager
from classes_for_program import *

@contextmanager
def record_manager():
    book = load_data()
    try:
        yield book
    finally:
        save_data(book)
