"""
PYTHON FUNCTION TASKS - 40 EXERCISES
====================================

BASIC FUNCTION CONCEPTS
=======================

SIMPLE TASKS (1-20)
====================

1. Create a function that takes a name and prints "Hello, [name]! Welcome to Python!"

2. Create a function that takes two numbers and prints their sum

3. Create a function that takes a word and prints it 5 times

4. Create a function that takes a number and prints its multiplication table from 1 to 10

5. Create a function that takes a string and prints each character on a separate line

6. Create a function that takes three numbers and prints the largest one

7. Create a function that takes a list of numbers and prints their sum

8. Create a function that takes a sentence and prints the number of words in it

9. Create a function that takes a number and prints all even numbers from 0 to that number

10. Create a function that takes two strings and prints them concatenated with a space between

11. Create a function that takes a number and prints a pattern of stars (that many rows)

12. Create a function that takes a list and prints each element with its index

13. Create a function that takes a string and prints it in reverse

14. Create a function that takes three numbers and prints their average

15. Create a function that takes a word and prints whether it has more than 5 letters

16. Create a function that takes a number and prints all its factors

17. Create a function that takes a list and prints the smallest and largest values

18. Create a function that takes a string and prints how many vowels it contains

19. Create a function that takes two numbers and prints all numbers between them

20. Create a function that takes a list and prints only the even numbers from it

INTERMEDIATE TASKS (21-35)
===========================

21. Create a function that takes a number and prints a triangle pattern with that many rows

22. Create a function that takes two lists and prints elements that appear in both lists

23. Create a function that takes a string and prints it with each word capitalized

24. Create a function that takes three numbers and prints them in ascending order

25. Create a function that takes a list and prints the sum of all positive numbers

26. Create a function that takes a word and prints whether it's a palindrome

27. Create a function that takes a number and prints all prime numbers up to that number

28. Create a function that takes two strings and prints the longer one

29. Create a function that takes a list and prints the most frequent element

30. Create a function that takes a number and prints its factorial

31. Create a function that takes a string and prints it with all spaces removed

32. Create a function that takes three numbers and prints whether they form a triangle

33. Create a function that takes a list and prints it in reverse order

34. Create a function that takes a word and prints it with alternating upper and lower case

35. Create a function that takes two numbers and prints all common factors

ADVANCED TASKS (36-40)
=======================

36. Create a function that takes a list and prints all unique elements (no duplicates)

37. Create a function that takes a string and prints it with each character repeated twice

38. Create a function that takes three numbers and prints whether they can form a right triangle

39. Create a function that takes a list and prints it sorted without using sort()

40. Create a function that takes a word and prints all possible anagrams (rearrangements)

BONUS ERROR HANDLING TASKS
==========================

41. Create a function that takes a number and prints its square root, but handles negative numbers gracefully

42. Create a function that takes a list and prints the average, but handles empty lists gracefully

43. Create a function that takes a string and prints the number of digits, but handles non-string inputs gracefully

44. Create a function that takes two numbers and divides them, but handles division by zero gracefully

45. Create a function that takes a list and prints the element at a given index, but handles invalid indices gracefully

FUNCTION NAMING REQUIREMENTS
===========================

- Use descriptive, meaningful function names
- Avoid generic names like "function1", "test", or "do_something"
- Examples: "greet_user", "calculate_average", "check_palindrome"

PARAMETER REQUIREMENTS
======================

- Functions must take exactly the number of parameters specified
- No default parameters
- Use descriptive parameter names
- Use appropriate data types

ALLOWED OPERATIONS
==================

- print() statements
- input() for user input
- Built-in functions: sum(), len(), min(), max()
- Basic arithmetic: +, -, *, /, //, %, **
- String methods: upper(), lower(), split(), join()
- List methods: append(), remove(), count()
- Comparison operators: ==, !=, <, >, <=, >=
- Logical operators: and, or, not
- if/else statements
- for loops

NOT ALLOWED
===========

- return statements
- Default parameter values
- Complex data structures (dictionaries, sets)
- File operations
- Exception handling (except for bonus tasks)
- Classes or object-oriented programming
- Recursion
- Lambda functions
- List comprehensions

NOTES
=====

- Focus on function structure and calling
- Practice with different data types
- Use descriptive names and parameters 
"""

# 1
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python!")

# 2
def print(sum1, sum2):
    print(sum1 + sum2)

# 3
def print_word_five_times(word):
    for i in range(5):
        print(word)

# 4
def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# 5
def print_characters_seperately(string):
    for char in string:
        print(char)

# 6
def print_largest_of_three(num1, num2, num3):
    print(max(num1, num2, num3))

# 7
def print_list_of_numbers_sum(numbers):
    print(sum(numbers))

# 8
def print_sentence_word_count(sentence):
    words = sentence.split()
    print(len(words))

# 9
def print_even_numbers_up_to(number):
    for i in range(0, number + 1, 2):
        print(i)

# 10
def print_concnatenated_strings(str1, str2):
    print(str1 + " " + str2)

# 11
def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# 12
def print_each_element_with_index(list):
    for index, element in enumerate(list):
        print(f"{index}: {element}")

# 13
def print_reversed_String(string):
    print(string[::-1])

# 14
def print_average_of_three_numbers(num1, num2, num3):
    print((num1 + num2 + num3) / 3)

# 15
def print_word_length_check(word):
    if len(word) > 5:
        print("The word has more than 5 letters")
    else:
        print("The word is less than or equal to 5 letters")

# 16
def print_factors_of_number(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# 17
def print_the_smallest_and_largest_value(lst):
    print(min(lst), max(lst))

# 18
def print_vowels_count(string):
    vowels = 'aeouAEOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
            print(count)

# 19
def print_numbers_between(num1, num2):
    for i in range(num1 + 1, num2):
        print(i)

# 20
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

# 21
def print_triangle_pattern(numbers):
    for i in range(1, n + 1):
        print('*' * i)

# 22
def print_common_elements(lst1, lst2):
    for element in lst1:
        if element in lst2:
            print(element)

# 23
def print_capitalized_string(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    print(' ' .join(capitalized_words))

# 24
def print_numbers_in_ascending_order(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    for number in numbers:
        print(number)

# 25
def print_sum_of_positive_numbers(lst):
    total = 0
    for num in lst:
        if num > 0:
            total += num
            print(total)

# 26
def print_palindrome_check(word):
    if word == word[::-1]:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")

# 27
def print_prime_numbers_up_to(number):
   for num in range(2, num + 1):
       is_prime = True
    

# 28
def print_longer_string(str1, str2):
    if (len(str1) > len(str2)):
        print(str1)
    else:
        print(str2)

# 29
def print_most_frequent_element(lst):
    max_count = 0
    most_freqent = None
    for element in lst:
        count = lst.count()
        if count > max.count():
            max_count = count
            most_frequent = element
        print(most_frequent)

# 30
def print_factorial_of(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(factorial)

# 31
def print_string_without_spaces(string):
    print(string.replace(" ", ""))

# 32
def print_triangle_check(num1, num2, num3):
    if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
        print("The numbers can form triangle")
    else:
       print("The numbers can not form triangle")

# 33
def print_reversed_list(lst):
    for element in reversed(lst):
       print(element)

# 34
def print_alternating_case(word):
    result = ''
    for index, char in enumerate(word):
        if index % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
        print(result)

# 35
def print_all_common_factors(num1, num2):
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            print(i)

# 36
def print_unique_elements(lst):
    unique_element = []
    for element in lst:
        if element not in unique_element:
            unique_element.append(element)
            print(element)

# 37
def print_string_with_repeated_characters(string):
    result = ''
    for char in string:
        result += char * 2
    print(result)

# 38
def print_right_triangle_check(a, b, c):
    if (a**a + b**b == c*c) or (a**a + c**c == b**b) or (b**b + c**c == a**a):
        print("The numbers can form a right triangle")
    else:
        print("The numbers can not form a right triangle")

# 39
def print_sorted_list(lst):
    sorted_list = []
    while lst:
        min_value = min(lst)
        sorted_list.append(min_value)
        lst.remove(min_value)
    for element in sorted_list:
        print(element)

# 40
def print_all_possible_anagrams(word):
  
# Bonus tasks
# 41
 
 def print_square_root(number):
     if number < 0:
         print("Can not compute square root of negative number")
     else:
         print(number ** 0.5)

# 42
def print_average_of_list(lst):
    if len(lst) == 0:
        print("Can not computer average of empty list")
    else:
        print(sum(lst) / len(lst)) 


    

# 44
def print_division(num1, num2):
    if num2 == 0:
        print("Can not divide by zero")
    else:
        print(num1 / num2)

# 45
def print_element_given_index(lst, index):
    if index < 0 or index >= len(lst):
        print("Invalid index")
    else:
        print(lst[index])
     

          



    


