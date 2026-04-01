"""
PYTHON BASIC CLASSES HOMEWORK
=============================

OBJECTIVE: Create simple classes for everyday objects
DIFFICULTY: Beginner
TOTAL TASKS: 15

=== BASIC CLASS CREATION TASKS ===

Task 1: Create a simple class called 'Cat' with:
- __init__ method that takes name and age parameters
- Store name and age as instance variables using self
- Create an instance of Cat with name "Whiskers" and age 3
- Print the cat's name and age

Task 2: Create a simple class called 'Dog' with:
- __init__ method that takes name and breed parameters
- Store name and breed as instance variables using self
- Create an instance of Dog with name "Buddy" and breed "Golden Retriever"
- Print the dog's name and breed

Task 3: Create a simple class called 'Person' with:
- __init__ method that takes name and age parameters
- Store name and age as instance variables using self
- Create an instance of Person with your name and age
- Print the person's name and age

Task 4: Create a simple class called 'Location' with:
- __init__ method that takes city and country parameters
- Store city and country as instance variables using self
- Create an instance of Location with city "Paris" and country "France"
- Print the location's city and country

Task 5: Create a simple class called 'Product' with:
- __init__ method that takes name and price parameters
- Store name and price as instance variables using self
- Create an instance of Product with name "Laptop" and price 999
- Print the product's name and price

Task 6: Create a simple class called 'User' with:
- __init__ method that takes username and email parameters
- Store username and email as instance variables using self
- Create an instance of User with username "john_doe" and email "john@email.com"
- Print the user's username and email

Task 7: Create a simple class called 'Book' with:
- __init__ method that takes title and author parameters
- Store title and author as instance variables using self
- Create an instance of Book with title "Python Guide" and author "Jane Smith"
- Print the book's title and author

Task 8: Create a simple class called 'Car' with:
- __init__ method that takes make and model parameters
- Store make and model as instance variables using self
- Create an instance of Car with make "Toyota" and model "Camry"
- Print the car's make and model

Task 9: Create a simple class called 'Phone' with:
- __init__ method that takes brand and model parameters
- Store brand and model as instance variables using self
- Create an instance of Phone with brand "iPhone" and model "14"
- Print the phone's brand and model

Task 10: Create a simple class called 'House' with:
- __init__ method that takes address and rooms parameters
- Store address and rooms as instance variables using self
- Create an instance of House with address "123 Main St" and rooms 4
- Print the house's address and number of rooms

Task 11: Create a simple class called 'Student' with:
- __init__ method that takes name and grade parameters
- Store name and grade as instance variables using self
- Create an instance of Student with name "Alice" and grade "A"
- Print the student's name and grade

Task 12: Create a simple class called 'Restaurant' with:
- __init__ method that takes name and cuisine parameters
- Store name and cuisine as instance variables using self
- Create an instance of Restaurant with name "Pizza Palace" and cuisine "Italian"
- Print the restaurant's name and cuisine type

Task 13: Create a simple class called 'Movie' with:
- __init__ method that takes title and year parameters
- Store title and year as instance variables using self
- Create an instance of Movie with title "The Matrix" and year 1999
- Print the movie's title and year

Task 14: Create a simple class called 'Game' with:
- __init__ method that takes name and genre parameters
- Store name and genre as instance variables using self
- Create an instance of Game with name "Minecraft" and genre "Sandbox"
- Print the game's name and genre

Task 15: Create a simple class called 'Plant' with:
- __init__ method that takes species and height parameters
- Store species and height as instance variables using self
- Create an instance of Plant with species "Rose" and height 2.5
- Print the plant's species and height

=== EVALUATION CRITERIA ===
- Correct use of __init__ and self
- Proper instance variable assignment
- Clean, readable code structure
- Correct class instantiation
- Proper use of print statements

Good luck with your basic Python classes! 🌟
"""

# Task 1
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat = Cat("Whiskers", 3)
print(cat.name, cat.age)


# Task 2
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(dog.name, dog.breed)


# Task 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("YourName", 20)  # change to your name and age
print(person.name, person.age)


# Task 4
class Location:
    def __init__(self, city, country):
        self.city = city
        self.country = country

location = Location("Paris", "France")
print(location.city, location.country)


# Task 5
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 999)
print(product.name, product.price)


# Task 6
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user = User("john_doe", "john@email.com")
print(user.username, user.email)


# Task 7
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("Python Guide", "Jane Smith")
print(book.title, book.author)


# Task 8
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car = Car("Toyota", "Camry")
print(car.make, car.model)


# Task 9
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

phone = Phone("iPhone", "14")
print(phone.brand, phone.model)


# Task 10
class House:
    def __init__(self, address, rooms):
        self.address = address
        self.rooms = rooms

house = House("123 Main St", 4)
print(house.address, house.rooms)


# Task 11
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

student = Student("Alice", "A")
print(student.name, student.grade)


# Task 12
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

restaurant = Restaurant("Pizza Palace", "Italian")
print(restaurant.name, restaurant.cuisine)


# Task 13
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

movie = Movie("The Matrix", 1999)
print(movie.title, movie.year)


# Task 14
class Game:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

game = Game("Minecraft", "Sandbox")
print(game.name, game.genre)


# Task 15
class Plant:
    def __init__(self, species, height):
        self.species = species
        self.height = height

plant = Plant("Rose", 2.5)
print(plant.species, plant.height)
