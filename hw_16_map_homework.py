"""
- Map -
A. Create a function that takes a list of numbers and uses the map() function to 
double each number in the list.
B. Write a function that takes a list of temperatures in Celsius and uses map() 
to convert them to Fahrenheit using the appropriate conversion formula.
C. Implement a function that takes a list of numbers and uses the map() function to 
D. Write a function that takes a list of names and uses map() to format them as "Hello, {name}!".
E. Create a function that takes a list of numbers and uses the map() function to generate a 
power series for each number, up to a specified exponent.
F. Write a function that takes two lists of strings and uses map() to concatenate the elements 
of the same index from both lists.
G. Create a function that takes a list of floats and uses the map() function to round each float 
to a specified number of decimal places.
H. Write a function that takes a list of prices and uses map() to apply a discount percentage to each price.
I. Implement a function that takes a list of sentences and uses map() to encrypt each sentence using 
a simple encryption algorithm.
J. Create a function that takes a list of words and uses map() to count the number of vowels in each word.
K. Write a function that takes a list of strings and uses map() to return a list of lengths for each string.

- Filter -
A. Create a function that takes a list of numbers and uses the filter() function to 
return a new list containing only the even numbers.
B. Write a function that takes a list of numbers and uses the filter() function to 
return a new list containing only the prime numbers.
C. Implement a function that filters a list of strings to return a new tuple containing 
only the words that are palindromes.
D. Given a list of dictionaries representing employees and their salaries, use filter() 
to create a new list of employees whose salary is above a specified threshold.
E. Write a function that takes a list of file names and filters it to return a new list 
containing only files with a specified file extension.
F. Create a function that takes a dictionary of student names and their corresponding grades, 
and uses filter() to return a new dictionary containing only students who passed (grades above 
a certain threshold).
G. Implement a function that takes a mixed list of data types (integers, strings, floats) and 
filters it to return separate lists for each data type.
H. Prompt the user to enter a condition, then use the filter() function to filter a given list 
of numbers based on the user-provided condition.
I. Write a function that takes a list of strings and filters it to return a new list containing 
only strings that contain a specific substring.
J. Implement a function that takes a list of strings and filters it to return a new list containing 
strings with a specified character appearing a certain number of times.
K. Create a function that takes a list of integers and uses the filter() function to return a 
new list containing only those numbers for which a specified mathematical function (e.g., square, 
cube) yields a prime result.
L. Write a function that takes a list of date objects and filters it to return a new list containing 
dates within a specified range.
M. Given a list of cities and their corresponding countries, use filter() to return a new list 
containing cities from a specific country.
N. Create a function that takes a list of product objects and uses the filter() function to return a 
new list containing only available products.
O. Implement a function that takes a list and uses filter() to return a new list containing only 
the unique elements.
P. Write a function that takes a list of words and filters it to return a new list containing only 
anagrams of a specified word.
Q. Given a list of numeric data, use filter() to return a new list containing elements within a 
specified range.
R. Create a function that takes a list of strings and uses filter() to return a new list containing 
only strings that match a specific regular expression.

- Reversed -
A. Write a function that takes a list of elements and uses the reversed() function to reverse the 
order of elements in the list.
B. Create a function that takes a string and uses reversed() to reverse the characters in the string.
C. Implement a function that takes a tuple and uses reversed() to reverse the order of elements in the tuple.
D. Write a function that takes a sentence and uses reversed() to reverse the order of words in the sentence.
E. Create a function that takes a dictionary and uses reversed() to reverse the order of keys and values.
F. Implement a function that takes a linked list and uses reversed() to reverse the order of nodes in the linked list.
G. Write a function that takes a queue and uses reversed() to reverse the order of elements in the queue.
H. Create a function that takes a stack and uses reversed() to reverse the order of elements in the stack.
I. Implement a function that takes a list of elements and uses reversed() to reverse the elements at odd 
indices, while keeping the elements at even indices unchanged.
J. Write a function that takes a binary number as a string and uses reversed() to reverse the binary digits.
K. Create a function that takes a 2D matrix and uses reversed() to reverse the rows of the matrix.
L. Implement a function that takes a string and uses reversed() to reverse the characters in each substring 
separated by a specific delimiter.

- Sorted -
A. Write a function that takes a list of numbers and uses the sorted() function to return a new list with 
the numbers sorted in ascending order.
B. Create a function that takes a list of numbers and uses the sorted() function to return a new list with 
the numbers sorted in descending order.
C. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
with the strings sorted by their lengths.
D. Write a function that takes a list of tuples and uses the sorted() function to return a new list with 
the tuples sorted based on their second element.
E. Create a function that takes a dictionary and uses the sorted() function to return a new dictionary 
with its items sorted by their values.
F. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
with the strings sorted in a case-insensitive manner.
G. Write a function that takes a list of custom objects and uses the sorted() function to return a new list 
with the objects sorted based on a specified attribute.
H. Create a function that takes a list of date objects and uses the sorted() function to return a new list 
with the dates sorted in chronological order.
I. Implement a function that takes a list of lists and uses the sorted() function to return a new list with 
the lists sorted based on the sum of their elements.
J. Write a function that takes a list of integers and uses the sorted() function to return a new list with 
the integers sorted based on the number of factors they have.
K. Create a function that takes a list of strings and uses the sorted() function to return a new list with 
the strings sorted based on their last characters.
L. Implement a function that takes a list of dictionaries and uses the sorted() function to return a new list 
with the dictionaries sorted based on their keys.
M. Sort the following list of strings alphabetically by the second letter:
string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]

Quiz.
1. What is the purpose of the filter() function in Python?
    A) To remove elements from an iterable based on a given condition
    B) To sort elements in an iterable
    C) To modify elements in an iterable
    D) To combine elements in an iterable

2. Which of the following data types can the filter() function be applied to?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above

3. What does the filter() function return?
    A) A new iterable containing filtered elements
    B) The original iterable with filtered elements
    C) A list of filtered elements
    D) A tuple of filtered elements

4. Which parameter does the filter() function take?
    A) A filter function
    B) An iterable
    C) Both A and B
    D) Neither A nor B

5. In the context of the filter() function, what does the filter function do?
    A) Defines the condition for filtering elements
    B) Specifies the data type of the iterable
    C) Sorts the iterable elements
    D) Combines the iterable elements

6. Which of the following statements is true about the filter() function?
    A) The filter function can only return True or False
    B) The filter function can return any data type
    C) The filter function must return a boolean
    D) The filter function is not required

7. What is the syntax for using the filter() function in Python?
    A) filter(condition, iterable)
    B) filter(iterable, condition)
    C) filter(function, iterable)
    D) filter(iterable, function)

8. When using the filter() function, what happens if the filter function returns False for an element?
    A) The element is removed from the iterable
    B) The element is included in the iterable
    C) An error is raised
    D) None of the above

9. Can the filter() function be used to filter elements based on multiple conditions?
    A) Yes
    B) No

10. In Python 3, what does the filter() function return by default?
    A) A filter object
    B) A list of filtered elements
    C) A tuple of filtered elements
    D) A set of filtered elements

11. What is the purpose of the map() function in Python?
    A) To apply a given function to each item in an iterable
    B) To filter elements from an iterable based on a given condition
    C) To sort elements in an iterable
    D) To combine elements in an iterable

12. Which of the following is an iterable that can be passed to the map() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above

13. What does the map() function return?
    A) A new iterable containing transformed elements
    B) The original iterable with transformed elements
    C) A list of transformed elements
    D) A tuple of transformed elements

14. What parameters does the map() function take?
    A) A mapping function and an iterable
    B) A single iterable
    C) A single mapping function
    D) A mapping function, followed by one or more iterables

15. In the context of the map() function, what does the mapping function do?
    A) Defines the transformation to be applied to each element
    B) Specifies the data type of the iterable
    C) Sorts the iterable elements
    D) Combines the iterable elements

16. Which of the following is true about the map() function?
    A) The mapping function can return any data type
    B) The mapping function must return a boolean
    C) The mapping function is not required
    D) The mapping function must return an integer

17. What is the syntax for using the map() function in Python?
    A) map(mapping_function, iterable)
    B) map(iterable, mapping_function)
    C) map(function, iterable)
    D) map(iterable, function)    

18. When using the map() function, what happens if the mapping function returns None for an element?
    A) The element is removed from the iterable
    B) The element remains unchanged in the iterable
    C) An error is raised
    D) None of the above

19. Can the map() function be used to transform elements from multiple iterables?
    A) Yes
    B) No

20. In Python 3, what does the map() function return by default?
    A) A map object
    B) A list of transformed elements
    C) A tuple of transformed elements
    D) A set of transformed elements

21. What is the purpose of the reversed() function in Python?
    A) To reverse the order of elements in an iterable
    B) To sort elements in an iterable
    C) To remove elements from an iterable
    D) To concatenate elements in an iterable

22. Which of the following is an iterable that can be passed to the reversed() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above

23. What does the reversed() function return?
    A) A new iterable containing reversed elements
    B) The original iterable with reversed elements
    C) A list of reversed elements
    D) A tuple of reversed elements

24. What parameter does the reversed() function take?
    A) An iterable
    B) A single element
    C) A number
    D) A mapping function

25. In the context of the reversed() function, what does "reversed elements" mean?
    A) The elements are in the opposite order
    B) The elements are sorted in ascending order
    C) The elements are concatenated
    D) The elements are multiplied

26. Which of the following is true about the reversed() function?
    A) The reversed elements are returned as a list
    B) The reversed elements are returned as a tuple
    C) The reversed elements are returned as an iterator
    D) The reversed elements are returned as a set

27. What is the syntax for using the reversed() function in Python?
    A) reversed(iterable)
    B) iterable.reversed()
    C) reversed(function, iterable)
   D) reversed(iterable, function)
8. When using the reversed() function, can it be applied to strings?
   A) Yes
   B) No
9. Can the reversed() function be used to reverse a dictionary?
   A) Yes
   B) No
0. In Python 3, what does the reversed() function return by default?
   A) A reversed object
   B) A list of reversed elements
   C) A tuple of reversed elements
   D) A set of reversed elements
1. What is the purpose of the sorted() function in Python?
   A) To sort elements in an iterable and return a sorted list
   B) To reverse the order of elements in an iterable
    C) To remove elements from an iterable
    D) To concatenate elements in an iterable

32. Which of the following is an iterable that can be passed to the sorted() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above
    
33. What does the sorted() function return?
    A) A new iterable containing sorted elements
    B) The original iterable with sorted elements
    C) A list of sorted elements
    D) A tuple of sorted elements

34. What parameters does the sorted() function take?
    A) An iterable
    B) A single element
    C) A mapping function
    D) A mapping function and an iterable

35. In the context of the sorted() function, what does "sorted elements" mean?
    A) The elements are arranged in ascending order
    B) The elements are arranged in descending order
    C) The elements are multiplied
    D) The elements are concatenated

36. Which of the following is true about the sorted() function?
    A) The sorted elements are returned as a tuple
    B) The sorted elements are returned as a set
    C) The sorted elements are returned as an iterator
    D) The sorted elements are returned as a list

37. What is the syntax for using the sorted() function in Python?
    A) sorted(iterable)
    B) iterable.sorted()
    C) sorted(function, iterable)
    D) sorted(iterable, function)

38. When using the sorted() function, can you specify a custom sorting order?
    A) Yes, by providing a custom sorting function
    B) No, the sorting order is always ascending
    C) Yes, by providing a reverse parameter
    D) No, the sorting order is always descending

39. Can the sorted() function be used to sort a dictionary based on its keys or values?
    A) Yes
    B) No

40. In Python 3, what does the sorted() function return by default?
    A) A list of sorted elements
    B) A sorted object
    C) A tuple of sorted elements
    D) A set of sorted elements
"""
# MAP

# A
def double_numbers(nums):
    return list(map(lambda x: x * 2, nums))

# B
def celsius_to_fahrenheit(celsius):
    return list(map(lambda c: (c * 9/5) + 32, celsius))

# C
def square_numbers(nums):
    return list(map(lambda x: x ** 2, nums))

# D
def greet_names(names):
    return list(map(lambda name: f"Hello, {name}!", names))

# E
def power_series(nums, exp):
    return list(map(lambda x: [x ** i for i in range(1, exp + 1)], nums))

# F
def concatenate_lists(list1, list2):
    return list(map(lambda a, b: a + b, list1, list2))

# G
def round_floats(nums, decimals):
    return list(map(lambda x: round(x, decimals), nums))

# H
def apply_discount(prices, discount):
    return list(map(lambda p: p - (p * discount / 100), prices))

# I (Caesar Cipher)
def encrypt_sentences(sentences, shift=3):
    def encrypt(text):
        return ''.join(chr((ord(c) + shift)) if c.isalpha() else c for c in text)
    return list(map(encrypt, sentences))

# J
def count_vowels(words):
    vowels = "aeiouAEIOU"
    return list(map(lambda w: sum(1 for c in w if c in vowels), words))

# K
def string_lengths(strings):
    return list(map(len, strings))

# FILTER

# A
def even_numbers(nums):
    return list(filter(lambda x: x % 2 == 0, nums))

# B
def prime_numbers(nums):
    def is_prime(n):
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    return list(filter(is_prime, nums))

# C
def palindrome_words(words):
    return tuple(filter(lambda w: w == w[::-1], words))

# D
def high_salary(employees, threshold):
    return list(filter(lambda e: e['salary'] > threshold, employees))

# E
def filter_extension(files, ext):
    return list(filter(lambda f: f.endswith(ext), files))

# F
def passed_students(students, pass_mark):
    return dict(filter(lambda item: item[1] > pass_mark, students.items()))

# G
def separate_types(data):
    return (
        list(filter(lambda x: isinstance(x, int), data)),
        list(filter(lambda x: isinstance(x, float), data)),
        list(filter(lambda x: isinstance(x, str), data))
    )

# H
def filter_with_condition(nums, condition):
    return list(filter(condition, nums))

# I
def contains_substring(strings, sub):
    return list(filter(lambda s: sub in s, strings))

# J
def char_count(strings, char, count):
    return list(filter(lambda s: s.count(char) == count, strings))

# K
def math_prime_filter(nums, func):
    def is_prime(n):
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    return list(filter(lambda x: is_prime(func(x)), nums))

# L
def dates_in_range(dates, start, end):
    return list(filter(lambda d: start <= d <= end, dates))

# M
def cities_by_country(cities, country):
    return list(filter(lambda c: c[1] == country, cities))

# N
def available_products(products):
    return list(filter(lambda p: p['available'], products))

# O
def unique_elements(lst):
    seen = set()
    return list(filter(lambda x: not (x in seen or seen.add(x)), lst))

# P
def anagrams(words, target):
    return list(filter(lambda w: sorted(w) == sorted(target), words))

# Q
def within_range(nums, low, high):
    return list(filter(lambda x: low <= x <= high, nums))

# R
import re
def regex_filter(strings, pattern):
    return list(filter(lambda s: re.match(pattern, s), strings))

# REVERSED
# A
def reverse_list(lst):
    return list(reversed(lst))

# B
def reverse_string(s):
    return ''.join(reversed(s))

# C
def reverse_tuple(t):
    return tuple(reversed(t))

# D
def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split()))

# E
def reverse_dict(d):
    return dict(reversed(list(d.items())))

# I
def reverse_odd_indices(lst):
    result = lst[:]
    odds = list(reversed([lst[i] for i in range(len(lst)) if i % 2 != 0]))
    idx = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            result[i] = odds[idx]
            idx += 1
    return result

# J
def reverse_binary(binary):
    return ''.join(reversed(binary))

# K
def reverse_matrix_rows(matrix):
    return list(reversed(matrix))

# L
def reverse_substrings(s, delimiter):
    return delimiter.join(''.join(reversed(part)) for part in s.split(delimiter))

# SORTED
# A
def sort_asc(nums):
    return sorted(nums)

# B
def sort_desc(nums):
    return sorted(nums, reverse=True)

# C
def sort_by_length(strings):
    return sorted(strings, key=len)

# D
def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1])

# E
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

# F
def case_insensitive_sort(strings):
    return sorted(strings, key=str.lower)

# G
def sort_objects(objects, attr):
    return sorted(objects, key=lambda x: getattr(x, attr))

# H
def sort_dates(dates):
    return sorted(dates)

# I
def sort_by_sum(lists):
    return sorted(lists, key=sum)

# J
def sort_by_factors(nums):
    def factors(n):
        return sum(1 for i in range(1, n+1) if n % i == 0)
    return sorted(nums, key=factors)

# K
def sort_by_last_char(strings):
    return sorted(strings, key=lambda s: s[-1])

# L
def sort_dicts_by_keys(dicts):
    return sorted(dicts, key=lambda d: list(d.keys()))

# M
string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]
sorted_strings = sorted(string_list, key=lambda s: s[1])

# QUIZ ANSWERS
1. # A
2. # D
3. # A
4. # C
5. # A
6. # C
7. # C
8. # A
9. # A
10. # A
11. # A
12. # D
13. # A
14. # D
15. # A
16. # A
17. # A
18. # D
19. # A
20. # A
21. # A
22. # D
23. # A
24. # A
25. # A
26. # C
27. # A
28. # A
29. # A
30. # A
31. # A
32. # D
33. # C
34. # A
35. # A
36. # D
37. # A
38. # A
39. # A
40. # A


