'''Write a decorator 'timer' that calculates how long a function takes to execute.
Test it with a function that sums numbers from 1 to 1,000,000'''

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
    return wrapper

@timer
def sum_numbers(n):
    return sum(range(1, n + 1))     

sum_numbers(1000000)