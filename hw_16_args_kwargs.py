"""
===============================
=   *args & **kwargs TASKS    =
===============================

# EASY

1. Write a function that accepts any number of positional arguments and prints them.

2. Write a function that sums all the numbers passed via *args.

3. Create a function that multiplies all numbers using *args.

4. Write a function that accepts any number of keyword arguments and prints them in key=value format.

5. Write a function that prints only the values from **kwargs.

6. Create a function that prints a greeting message using **kwargs with keys: name and age.

7. Write a function that combines *args and **kwargs and prints both.

8. Write a function that checks if a specific key exists in **kwargs.

9. Create a function that returns the longest word passed in *args.

10. Create a function that prints a formatted address using **kwargs (e.g., street, city, zip).

# MEDIUM

11. Write a function that filters only even numbers from *args.

12. Create a function that returns a dictionary combining both *args (as values) and **kwargs.

13. Create a function that takes a default tax rate via **kwargs and applies it to all *args prices.

14. Write a function that accepts student scores via **kwargs and returns the average.

15. Create a logger function that accepts *args as log messages and **kwargs for metadata (e.g., level, timestamp).

16. Build a function that uses *args to take any strings and **kwargs for formatting options like upper=True, reverse=True.

17. Create a function that finds the max of numbers from both *args and values in **kwargs.

18. Write a function that accepts any number of named configurations (**kwargs) and validates that required keys exist.

19. Write a decorator that uses *args and **kwargs to wrap and log function calls.

20. Implement a function that creates a formatted table where columns are defined via **kwargs and values via *args.

# HARD

21. Create a class with a method that accepts *args for dynamic field names and **kwargs for their values.

22. Write a function that groups items passed via **kwargs based on data type.

23. Design a function that builds a nested dictionary structure from **kwargs with dot notation (e.g., 'user.name': 'Ali').

24. Write a function that recursively sums all numbers passed via nested **kwargs.

25. Create a dynamic API router simulator function where *args represent endpoints and **kwargs represent methods and handlers.

"""

# EASY
# 1
def print_args(*args):
    for arg in args:
        print(arg)

# 2
def sum_args(*args):
    return sum(args)

# 3
def multiply_args(*args):
    result = 1
    for num in args:
        result *= num
    return result

# 4
def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}={v}")

# 5
def print_kwargs_values(**kwargs):
    for value in kwargs.values():
        print(value)

# 6
def greet(**kwargs):
    print(f"Hello {kwargs.get('name')}, you are {kwargs.get('age')} years old.")

# 7
def print_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# 8
def has_key(key, **kwargs):
    return key in kwargs

# 9
def longest_word(*args):
    return max(args, key=len)

# 10
def print_address(**kwargs):
    print(f"{kwargs.get('street')}, {kwargs.get('city')} {kwargs.get('zip')}")

# MEDIUM
# 11
def even_numbers(*args):
    return [x for x in args if x % 2 == 0]

# 12
def combine_args_kwargs(*args, **kwargs):
    result = dict(enumerate(args))
    result.update(kwargs)
    return result

# 13
def apply_tax(*prices, **kwargs):
    tax = kwargs.get('tax', 0.0)
    return [price + price * tax for price in prices]

# 14
def average_scores(**kwargs):
    return sum(kwargs.values()) / len(kwargs) if kwargs else 0

# 15
def logger(*args, **kwargs):
    level = kwargs.get('level', 'INFO')
    timestamp = kwargs.get('timestamp', 'N/A')
    for msg in args:
        print(f"[{level}] [{timestamp}] {msg}")

# 16
def format_strings(*args, **kwargs):
    result = list(args)
    if kwargs.get('upper'):
        result = [s.upper() for s in result]
    if kwargs.get('reverse'):
        result = [s[::-1] for s in result]
    return result

# 17
def max_from_args_kwargs(*args, **kwargs):
    return max(list(args) + list(kwargs.values()))

# 18
def validate_config(required_keys, **kwargs):
    missing = [k for k in required_keys if k not in kwargs]
    return missing if missing else "All keys present"

# 19
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

# 20
def formatted_table(*args, **kwargs):
    headers = kwargs.keys()
    print(" | ".join(headers))
    print("-" * 20)
    for row in args:
        print(" | ".join(str(v) for v in row))

# HARD
# 21
class DynamicObject:
    def __init__(self, *args, **kwargs):
        for name in args:
            setattr(self, name, None)
        for k, v in kwargs.items():
            setattr(self, k, v)

# 22
def group_by_type(**kwargs):
    result = {}
    for value in kwargs.values():
        result.setdefault(type(value).__name__, []).append(value)
    return result

# 23
def build_nested_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        keys = key.split('.')
        current = result
        for k in keys[:-1]:
            current = current.setdefault(k, {})
        current[keys[-1]] = value
    return result

# 24
def recursive_sum(**kwargs):
    total = 0
    for value in kwargs.values():
        if isinstance(value, dict):
            total += recursive_sum(**value)
        elif isinstance(value, (int, float)):
            total += value
    return total

# 25
def api_router(*endpoints, **kwargs):
    routes = {}
    for endpoint in endpoints:
        routes[endpoint] = kwargs.get(endpoint, {})
    return routes

