"""
Homework Assignment: Introduction to Classes in Python

Instructions:
Create a Python program with two classes that model real-world objects. 
Each class should have attributes, methods, and a main program that demonstrates 
their functionality. Follow the steps below to complete the assignment.

Class 1: Person

Create a class named Person with the following attributes and methods:

Attributes:

name (str) - The name of the person.
age (int) - The age of the person.

Methods:

greeting(self) - A method that prints a greeting message using the person's name.
sleep(self) - A method that prints a message indicating that the person is going to sleep.

Class 2: Animal

Create a class named Animal with the following attributes and methods:

Attributes:

name (str) - The name of the animal.
age (int) - The age of the animal.
color (str) - The color of the animal
Methods:

eat(self) - A method that prints a message indicating that the animal is going to eat.
run(self) - A method that prints a message indicating that the animal is running.

Main Program:

Write a main program that demonstrates the use of the Person and Animal classes. 
Create instances of both classes and use their methods to show their behavior. 
For example, create a person and an animal, set their attributes, and call 
their appropriate methods for each of them.

Ensure that your program is well-documented and follows best practices for Python 
code formatting and style.

Quiz.
1. What is a class in Python?
    a) A class is a built-in function.
    b) A class is an instance of an object.
    c) A class is a blueprint for creating objects.
    d) A class is a reserved keyword in Python.

2. In Python, which keyword is used to define a class?
    a) class
    b) define
    c) struct
    d) object

3. How do you create an instance of a class in Python?
    a) By using the new keyword.
    b) By calling the class as a function.
    c) By using the instance keyword.
    d) By using the class name followed by parentheses.
    
4. Which of the following statements is true regarding attributes in a class?
    a) Attributes are methods defined within a class.
    b) Attributes are used to create instances of a class.
    c) Attributes are variables that store data in a class.
    d) Attributes are not allowed in Python classes.

5. Which keyword is used to access the attributes and methods of a class instance?
    a) access
    b) use
    c) this
    d) dot (.)
    
6. How do you create an instance of a class in Python?
    a) By using the new keyword.
    b) By calling the class as a function.
    
7. Which of the following statements is true regarding attributes in a class?
    a) Attributes are methods defined within a class.
    b) Attributes are variables that store data in a class.
    
8. What is an "object" in the context of classes?
    a) An instance of a class.
    b) A Python module.
    c) A function

9. What is the relationship between a class and an object in Python?
    a) A class is an instance of an object.
    b) An object is an instance of a class.
    
10. What are "attributes" in a class?
    a) Functions defined within a class.
    b) Variables that store data within a class.
    
11. In Python, how do you define a class?
    a) By using the class keyword followed by the class name and a colon.
    b) By using the def keyword followed by the class name and a colon.
"""
"""
Homework Assignment: Introduction to Classes in Python

Instructions:
Create a Python program with two classes that model real-world objects. 
Each class should have attributes, methods, and a main program that demonstrates 
their functionality. Follow the steps below to complete the assignment.

Class 1: Person

Create a class named Person with the following attributes and methods:

Attributes:

name (str) - The name of the person.
age (int) - The age of the person.

Methods:

greeting(self) - A method that prints a greeting message using the person's name.
sleep(self) - A method that prints a message indicating that the person is going to sleep.

Class 2: Animal

Create a class named Animal with the following attributes and methods:

Attributes:

name (str) - The name of the animal.
age (int) - The age of the animal.
color (str) - The color of the animal
Methods:

eat(self) - A method that prints a message indicating that the animal is going to eat.
run(self) - A method that prints a message indicating that the animal is running.

Main Program:

Write a main program that demonstrates the use of the Person and Animal classes. 
Create instances of both classes and use their methods to show their behavior. 
For example, create a person and an animal, set their attributes, and call 
their appropriate methods for each of them.

Ensure that your program is well-documented and follows best practices for Python 
code formatting and style.

Quiz.
1. What is a class in Python?
    a) A class is a built-in function.
    b) A class is an instance of an object.
    c) A class is a blueprint for creating objects.
    d) A class is a reserved keyword in Python.

2. In Python, which keyword is used to define a class?
    a) class
    b) define
    c) struct
    d) object

3. How do you create an instance of a class in Python?
    a) By using the new keyword.
    b) By calling the class as a function.
    c) By using the instance keyword.
    d) By using the class name followed by parentheses.
    
4. Which of the following statements is true regarding attributes in a class?
    a) Attributes are methods defined within a class.
    b) Attributes are used to create instances of a class.
    c) Attributes are variables that store data in a class.
    d) Attributes are not allowed in Python classes.

5. Which keyword is used to access the attributes and methods of a class instance?
    a) access
    b) use
    c) this
    d) dot (.)
    
6. How do you create an instance of a class in Python?
    a) By using the new keyword.
    b) By calling the class as a function.
    
7. Which of the following statements is true regarding attributes in a class?
    a) Attributes are methods defined within a class.
    b) Attributes are variables that store data in a class.
    
8. What is an "object" in the context of classes?
    a) An instance of a class.
    b) A Python module.
    c) A function

9. What is the relationship between a class and an object in Python?
    a) A class is an instance of an object.
    b) An object is an instance of a class.
    
10. What are "attributes" in a class?
    a) Functions defined within a class.
    b) Variables that store data within a class.
    
11. In Python, how do you define a class?
    a) By using the class keyword followed by the class name and a colon.
    b) By using the def keyword followed by the class name and a colon.
"""

"""
Homework Assignment: Introduction to Classes in Python
Author: Student
Description:
This program demonstrates the use of classes in Python by creating
two real-world models: Person and Animal.
"""
"""
Homework Assignment: Introduction to Classes in Python
This program demonstrates the use of two classes: Person and Animal.
Each class has attributes and methods that model real-world behavior.
"""


class Person:
    """Represents a person with a name and age."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self):
        """Prints a greeting message."""
        print(f"Hello, my name is {self.name}.")

    def sleep(self):
        """Prints a sleeping message."""
        print(f"{self.name} is going to sleep.")


class Animal:
    """Represents an animal with a name, age, and color."""

    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        """Prints an eating message."""
        print(f"{self.name} is eating.")

    def run(self):
        """Prints a running message."""
        print(f"{self.name} is running.")


def main():
    """Main function to demonstrate class usage."""

    # Create a Person object
    person1 = Person("Alice", 25)
    person1.greeting()
    person1.sleep()

    print()  # Blank line for readability

    # Create an Animal object
    animal1 = Animal("Buddy", 3, "Brown")
    animal1.eat()
    animal1.run()


# Run the main program
if __name__ == "__main__":
    main()

# Quiz Answers
1. # c
2. # a
3. # d
4. # c
5. # d
6. # b
7. # b
8. # a
9. # b
10. # b
11. # a

"""
Homework Assignment: Introduction to Classes in Python
Author: Student

Description:
This program demonstrates the use of classes in Python by modeling
two real-world objects: a Person and an Animal.
"""


class Person:
    """Represents a person with a name and age."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self):
        """Prints a greeting message using the person's name."""
        print(f"Hello! My name is {self.name}.")

    def sleep(self):
        """Prints a message indicating the person is going to sleep."""
        print(f"{self.name} is going to sleep.")


class Animal:
    """Represents an animal with a name, age, and color."""

    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        """Prints a message indicating the animal is eating."""
        print(f"{self.name} is eating.")

    def run(self):
        """Prints a message indicating the animal is running."""
        print(f"{self.name} is running.")


def main():
    """Main program demonstrating the Person and Animal classes."""

    # Create a Person object
    person = Person("John", 20)
    person.greeting()
    person.sleep()

    print()  # Blank line for readability

    # Create an Animal object
    animal = Animal("Max", 5, "Black")
    animal.eat()
    animal.run()


# Execute the main program
if __name__ == "__main__":
    main()
# Quiz Answers
1. # c
2. # a
3. # d
4. # c
5. # d
6. # b
7. # b
8. # a
9. # b
10. # b
11. # a


