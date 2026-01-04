"""""
=========================
=       ZIP TASKS       =
=========================

# EASY

1. Write a function that takes two lists and returns a list of tuples by zipping them together.

2. Create a function that zips three lists and prints each tuple on a separate line.

3. Write a function that zips two lists and returns a dictionary (first list as keys, second as values).

4. Create a function that accepts two lists and returns only the elements where both lists have the same index.

5. Write a function that takes two lists of numbers and returns a list of their sums using zip.

6. Write a function that zips two strings and returns a list of concatenated characters.

7. Create a function that zips a list of names with a list of ages and prints "Name is Age years old" for each pair.

8. Write a function that zips two lists and returns only the pairs where the first element is greater than the second.

9. Write a function that unzips a list of tuples into two separate lists.

10. Create a function that takes a list of tuples and prints each tuple in "key: value" format.

# MEDIUM

11. Write a function that zips multiple lists of different lengths and fills missing values with None.

12. Create a function that zips a list of students with a list of scores and returns a dictionary only for students with scores above 50.

13. Write a function that zips two lists and multiplies each paired element together.

14. Create a function that takes a list of products and a list of prices, zips them, and returns the most expensive product.

15. Write a function that zips three lists and returns a new list of tuples where the sum of elements in each tuple is even.

16. Create a function that zips a list of dates with a list of events and prints them in "Date -> Event" format.

17. Write a function that zips two lists and returns a list sorted by the second element of each tuple.

18. Create a function that zips two lists and returns a dictionary, but only includes keys where the value is not None.

19. Write a function that zips a list of names, scores, and grades and prints only the top 3 students based on scores.

20. Implement a function that zips multiple lists and returns a list of dictionaries with keys provided by a separate list.

# HARD

21. Write a function that takes multiple lists and zips them recursively into nested tuples.

22. Create a function that zips multiple lists of different lengths and returns a dictionary of lists, filling missing values with a default.

23. Write a function that zips a list of tuples with another list and merges them into a single list of dictionaries.

24. Create a function that zips multiple lists and calculates the cumulative sum of each zipped tuple.

25. Write a function that simulates a CSV reader: takes headers and multiple rows (lists), zips them, and returns a list of dictionaries.

"""

# 1
def zip_two_lists(a, b):
    return list(zip(a, b))


# 2
def zip_three_lists(a, b, c):
    for item in zip(a, b, c):
        print(item)


# 3
def zip_to_dict(keys, values):
    return dict(zip(keys, values))


# 4
def same_index_elements(a, b):
    return list(zip(a, b))


# 5
def sum_lists(a, b):
    return [x + y for x, y in zip(a, b)]


# 6
def zip_strings(s1, s2):
    return [a + b for a, b in zip(s1, s2)]


# 7
def names_and_ages(names, ages):
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")


# 8
def greater_pairs(a, b):
    return [(x, y) for x, y in zip(a, b) if x > y]


# 9
def unzip_tuples(tuples):
    return list(zip(*tuples))


# 10
def print_key_value(pairs):
    for k, v in pairs:
        print(f"{k}: {v}")

from itertools import zip_longest

# 11
def zip_fill_none(*lists):
    return list(zip_longest(*lists, fillvalue=None))


# 12
def students_above_50(students, scores):
    return {s: sc for s, sc in zip(students, scores) if sc > 50}


# 13
def multiply_lists(a, b):
    return [x * y for x, y in zip(a, b)]


# 14
def most_expensive_product(products, prices):
    return max(zip(products, prices), key=lambda x: x[1])[0]


# 15
def even_sum_tuples(a, b, c):
    return [t for t in zip(a, b, c) if sum(t) % 2 == 0]


# 16
def print_events(dates, events):
    for d, e in zip(dates, events):
        print(f"{d} -> {e}")


# 17
def sort_by_second(a, b):
    return sorted(zip(a, b), key=lambda x: x[1])


# 18
def dict_without_none(keys, values):
    return {k: v for k, v in zip(keys, values) if v is not None}


# 19
def top_3_students(names, scores, grades):
    top = sorted(zip(names, scores, grades), key=lambda x: x[1], reverse=True)[:3]
    for n, s, g in top:
        print(n, s, g)


# 20
def list_of_dicts(keys, *lists):
    return [dict(zip(keys, values)) for values in zip(*lists)]

# 21
def recursive_zip(*lists):
    if len(lists) == 1:
        return lists[0]
    return list(zip(lists[0], recursive_zip(*lists[1:])))


# 22
def zip_to_dict_of_lists(default, *lists):
    result = {}
    for i, values in enumerate(zip_longest(*lists, fillvalue=default)):
        result[i] = list(values)
    return result


# 23
def merge_tuples_with_list(tuples, values):
    return [{**dict(t), "extra": v} for t, v in zip(tuples, values)]


# 24
def cumulative_sum(*lists):
    result = []
    total = 0
    for values in zip(*lists):
        total += sum(values)
        result.append(total)
    return result


# 25
def csv_reader(headers, rows):
    return [dict(zip(headers, row)) for row in rows]
