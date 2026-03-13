"""
PYTHON FUNCTIONS BASIC HOMEWORK - 80 PRACTICAL TASKS
=======================================================

DESCRIPTION:
This homework focuses on fundamental Python function concepts including:
- Basic function creation with parameters and return values
- String manipulation and list operations
- Conditional logic and mathematical operations
- Default parameters and multiple return values
- Docstrings and documentation
- Date/time operations
- Financial calculations
- File path operations

The tasks progress from simple function creation to more complex operations,
helping master the core concepts of Python functions.

TASKS:
======

BASIC FUNCTION OPERATIONS (1-20)
================================

1. Write a function that takes a name as a parameter and prints "Hello, <name>".

2. Write a function that takes two numbers and prints their sum.

3. Write a function that takes two numbers and returns their sum.

4. Write a function that returns the string "Python is fun!".

5. Write a function that takes a string and returns it in uppercase.

6. Write a function that takes a string and returns it in lowercase.

7. Write a function that takes two strings and concatenates them.

8. Write a function that takes a number and returns its square.

9. Write a function that takes a list and prints each item.

10. Write a function that takes a list of numbers and returns their sum.

11. Write a function that takes a list and returns its length.

12. Write a function that takes a list and returns the first element.

13. Write a function that takes a list and returns the last element.

14. Write a function that returns True if a list is empty, False otherwise.

15. Write a function that takes a list and a value, and returns True if the value exists in the list.

16. Write a function that takes a list and returns it reversed (without using reverse()).

17. Write a function that returns the maximum of three numbers.

18. Write a function that takes a list of strings and returns them joined with spaces.

19. Write a function that takes a number and checks if it is even.

20. Write a function that takes a number and checks if it is odd.

CONDITIONAL LOGIC & MATHEMATICS (21-40)
========================================

21. Write a function that takes an age and returns "Adult" if age >= 18 else "Minor".

22. Write a function that takes a temperature in Celsius and returns Fahrenheit.

23. Write a function that takes a temperature in Fahrenheit and returns Celsius.

24. Write a function that takes a number and returns "Positive", "Negative", or "Zero".

25. Write a function that takes two numbers and returns the larger one.

26. Write a function that takes two numbers and returns the smaller one.

27. Write a function that returns the absolute value of a number.

28. Write a function that returns the last character of a string.

29. Write a function that takes a string and returns its length.

30. Write a function that takes a string and returns True if it contains the word "Python".

31. Write a function that counts vowels in a string.

32. Write a function that takes a sentence and returns it split into words.

33. Write a function that capitalizes the first letter of a string.

34. Write a function that returns the title-cased version of a string.

35. Write a function that removes spaces from a string.

36. Write a function that replaces all commas with semicolons in a string.

37. Write a function that counts how many times "a" appears in a string.

38. Write a function that checks if a string is empty.

39. Write a function with a default parameter "guest" for name, and print "Welcome <name>".

40. Write a function with three default parameters (city, country, age).

DEFAULT PARAMETERS & MENU (41-44)
==================================

41. Write a function that prints today's menu with default "Pizza".

MULTIPLE RETURN VALUES (45-60)
===============================

42. Write a function that returns both min and max of a list.

43. Write a function that returns both uppercase and lowercase version of a string.

44. Write a function that returns both length and reversed version of a string.

45. Write a function that returns both square and cube of a number.

46. Write a function that returns name and age together in a tuple.

47. Write a function that returns first and last item of a list.

48. Write a function that returns True/False and explanation string.

49. Write a function that takes 2 numbers and returns sum and difference.

50. Write a function that returns (username, email) dictionary.

51. Write a function that returns multiple values packed in a dict.

DOCSTRINGS (52-53)
==================

52. Write a function with a docstring that explains what it does.

53. Write a function with parameters and include a docstring for them.

DATE & TIME OPERATIONS (54-63)
==============================

54. Write a function that prints the current year.

55. Write a function that prints the current day of week.

56. Write a function that prints the current time.

57. Write a function that returns current date as string.

58. Write a function that returns current month as string.

59. Write a function that prints today's date in "YYYY-MM-DD".

60. Write a function that takes a datetime and returns only the year.

61. Write a function that takes a datetime and returns only the month.

62. Write a function that takes a datetime and returns only the day.

63. Write a function that returns today's date and time as dictionary.

FINANCIAL CALCULATIONS (64-73)
===============================

64. Write a function that takes a price and returns price with VAT (add 18%).

65. Write a function that takes a salary and returns yearly salary.

66. Write a function that takes a bill amount and tip percent, returns total.

67. Write a function that takes a discount percent and price, returns final price.

68. Write a function that takes a list of prices and returns total.

69. Write a function that applies a fixed discount (default 10%) to a price.

70. Write a function that takes a balance and expense, and returns remaining balance.

71. Write a function that formats a number as currency string.

72. Write a function that takes hours worked and rate, returns salary.

73. Write a function that takes prices and tax percent, returns total.

FILE OPERATIONS (74-80)
========================

74. Write a function that takes a filename and prints it.

75. Write a function that takes a filename and returns its extension.

76. Write a function that takes a path and returns only the filename.

77. Write a function that takes a filename and returns True if ends with ".txt".

78. Write a function that takes a filename and adds ".bak" extension.

79. Write a function that takes a file content string and counts lines.

80. Write a function that takes filename and returns it uppercased.

REQUIREMENTS:
=============

- All functions must be properly defined with def keyword
- Use descriptive function names following Python naming conventions
- Include appropriate parameters and return statements
- Test all functions with different inputs
- For docstring tasks, use triple quotes and explain purpose, parameters, and return values
- Handle edge cases appropriately
- Use meaningful variable names

BONUS CHALLENGES:
=================

- Add type hints to function parameters and return values
- Include error handling for invalid inputs
- Create unit tests for each function
- Optimize functions for performance
- Add logging for debugging purposes 
"""
# 1
def say_hello(name: str) -> None:
    print(f"Hello,{name}")

# 2
def print_sum(a: float, b: float) -> None:
    print(a + b)

# 3
def get_sum(a: float, b: float) -> float:
    return a + b

# 4
def python_is_fun() -> str:
    return "Python is fun!"

# 5
def to_upper(text: str) -> str:
    return text.upper()

# 6
def to_lower(text: str) -> str:
    return text.lower()

# 7
def concat_string(a: str, b: str):
    return a + b

# 8
def square_number(n: float) -> float:
    return n * n

# 9
def print_list_items(items: list[any]) -> None:
    for item in items:
        print(item)

# 10
def sum_list(numbers: list[float]) -> float:
    return sum(numbers)


# 11
def length_list(items: list[any]) -> str:
    return len(items)

# 12
def first_element(items: list[any]) -> any:
    return items[0]

# 13
def last_element(items: list[any]) -> any:
    return items[-1]

# 14
def is_list_empty(items: list[any]) -> bool:
    return len(items) == 0

# 15
def list_contains(items: list[any], value: any) -> bool:
    return value in items

# 16
def reversed_list(items: list[any]) -> str:
    return items[::-1]

# 17
def get_max(a: float, b: float, c: float) -> float:
    return max(a, b, c)

# 18
def join_strings_with_spaces(words: list[str]) -> str:
    return " ".join(words)

# 19
def is_even(number: int) -> bool:
    return number % 2 == 0

# 20
def is_odd(number: int) -> bool:
    return number % 2 != 0

# conditonal logic and mathematics
# 21
def age_group(age: int) -> str:
    return "Adult" if age >= 18 else "Minor"

# 22
def celcius_to_fahranheit(c: float) -> float:
    return 9/5 * c + 32

# 23
def fahrenheit_to_celcius(f: float) -> float:
    return 5/9 * (f - 32)

# 24
def get_number(number: float) -> str:
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# 25
def max_numbers(a: float, b: float) -> float:
    return max_numbers(a, b)

# 26
def min_numbers(a: float, b: float) -> float:
    return min_numbers(a, b)

# 27
def absolute_value(number: float) -> float:
    return absolute_value(number)

# 28
def last_character(text:  str) -> str:
    return text[-1]

# 29
def string_length(text: str) -> str:
    return len(text)

# 30
def contains_python(text: str) -> bool:
    return "Python" in text

# 31
def count_vowels(text: str) -> int:

# 32
 def  split_sentence(sentence: str) -> str:
    return sentence.split()
 
# 33
def first_letter(text: str) -> str:
    return text.capitalize()

# 34
def title_case(text: str) -> str:
    return text.title()

# 35
def remove_spaces(text: str) -> str:
    return text.replace(" ", "")

# 36
def replace_comma_with_semicolon(text: str) -> str:
    return text.replace(",", ";")

# 37
def count_a(text: str) -> int:
    return text.count("a")


# 38
def is_string_empty(text: str) -> bool:
    return len(text) == 0

# 39
def welcome_name(name: str = "guest") -> None:
    print(f"Welcome {name}")

# 40
def  print_person_info(age: int = 21, city: str = "Baku", country: str = "Azerbaijan") -> None:
    print(f"Age: {age}, City: {city}, Country: {country}")
# 41
def print_menu(item: str = "Pizza") -> None:
    print(f"Today's menu: {item}")

# 42
def get_min_max(numbers: list[int]) -> int:
    return min(numbers), max(numbers)

# 43
def string_cases(text: str) -> str:
    return text.upper(), text.lower()

# 44
def length_and_reverse(text: str) -> list[int, str]:
    return len(text), text[::-1]

# 45
def square_and_cube(n: float) -> float:
    return (n * n), (n * n * n)

# 46
def  name_and_age(name: str, age: int) -> tuple[str, int]:
    return name, age

# 47
def first_and_last(item: list[any]) -> str:
    return item[0], item[-1]

# 48
def validate_age(age: int) -> bool:
    if age >= 18:
         return True, "Adult"
         return False, "Minor"
    
# 49
def sum_and_difference(a: float, b: float) -> float:
    return (a + b), (a - b)

# 50
def user_dict(username: str, email: str) -> dict[str, str]:
    return {username, email}

# 51

# 54
from datetime import datetime

def print_current_year() -> None:
    print(datetime.now().year)

# 55
def print_day_of_week() -> None:
    print(datetime.now().strftime("%A"))

# 56
def print_current_time() -> None:
    print(datetime.now().strftime("%H:%M:%S"))

# 57
def current_date_string() -> str:
    return datetime.now().strftime("%Y-%m-%d")

# 58
def current_month_string() -> str:
    return datetime.now().strftime("%B")

# 59
def print_today_iso() -> None:
    print(datetime.now().strftime("%Y-%m-%d"))

# 60
def get_year(dt: datetime) -> int:
    return dt.year

# 61
def get_month(dt: datetime) -> int:
    return dt.month

# 62
def get_day(dt: datetime) -> int:
    return dt.day

# 63
def datetime_dict() -> Dict[str, int]:
    now = datetime.now()
    return {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute
    }

# 64
def price_with_vat(price: float) -> float:
    return price * 1.18

# 65
def yearly_salary(monthly_salary: float) -> float:
    return monthly_salary * 12

# 66
def bill_with_tip(amount: float, tip_percent: float) -> float:
    return amount + (amount * tip_percent / 100)

# 67
def discounted_price(price: float, discount_percent: float) -> float:
    return price * (1 - discount_percent / 100)

# 68
def total_prices(prices: List[float]) -> float:
    return sum(prices)

# 69
def fixed_discount(price: float, discount: float = 10) -> float:
    return price * (1 - discount / 100)

# 70
def remaining_balance(balance: float, expense: float) -> float:
    return balance - expense

# 71
def format_currency(amount: float) -> str:
    return f"${amount:,.2f}"

# 72
def calculate_salary(hours: float, rate: float) -> float:
    return hours * rate

# 73
def prices_with_tax(prices: List[float], tax_percent: float) -> float:
    return sum(prices) * (1 + tax_percent / 100)

# 74
import os

def print_filename(filename: str) -> None:
    print(filename)

#75

def file_extension(filename: str) -> str:
    return os.path.splitext(filename)[1]

# 76
def extract_filename(path: str) -> str:
    return os.path.basename(path)

# 77
def is_text_file(filename: str) -> bool:
    return filename.endswith(".txt")

# 78
def add_backup_extension(filename: str) -> str:
    return filename + ".bak"

# 79
def count_lines(content: str) -> int:
    return len(content.splitlines())

# 80
def uppercase_filename(filename: str) -> str:
    return filename.upper()



