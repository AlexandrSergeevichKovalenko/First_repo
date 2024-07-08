from typing import Callable

def caching_fibonacci()-> Callable[[int], int]:
    cache = dict()
    
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache.keys():
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    # creation of the function to see what is inside of the dictionary
    def get_cache():
        return cache

    return fibonacci, get_cache

fib, get_cache = caching_fibonacci()

# calling function
print(fib(10)) 
print(fib(15))
print(fib(10))
print(fib(1))

print(get_cache())


