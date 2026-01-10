"""
PYTHON CLASSES HOMEWORK ASSIGNMENT
=====================================

OBJECTIVE: Learn Python classes through interactive examples with planes and passengers
DIFFICULTY: Progressive (Beginner to Intermediate)
TOTAL TASKS: 30

=== PART 1: BASIC CLASS CONCEPTS (Tasks 1-10) ===

Task 1: Create a simple class called 'Person' with:
- __init__ method that takes name and age parameters
- Store name and age as instance variables using self
- Create an instance of Person with your name and age
- Print the person's name and age

Task 2: Add a method called 'introduce' to the Person class that:
- Prints "Hi, I'm [name] and I'm [age] years old"
- Create a Person instance and call the introduce method

Task 3: Create a class called 'Car' with:
- __init__ method taking brand, model, and year
- A method called 'start_engine' that prints "The [brand] [model] engine is running"
- Create a Car instance and call start_engine

Task 4: Add a method called 'get_info' to the Car class that:
- Returns a string with all car information
- Test it by creating a car and printing the result of get_info()

Task 5: Create a class called 'Book' with:
- __init__ method for title, author, and pages
- A method called 'read' that prints "Reading [title] by [author]"
- A method called 'is_long' that returns True if pages > 300, False otherwise
- Test all methods

Task 6: Create a class called 'Student' with:
- __init__ method for name, student_id, and grade
- A method called 'study' that prints "[name] is studying"
- A method called 'get_grade' that returns the grade
- Create 3 different students and test all methods

Task 7: Add a method called 'promote' to the Student class that:
- Increases the grade by 1
- Prints "[name] was promoted to grade [new_grade]"
- Test with a student

Task 8: Create a class called 'BankAccount' with:
- __init__ method for account_holder and initial_balance (default 0)
- A method called 'deposit' that adds money to balance
- A method called 'withdraw' that subtracts money from balance
- A method called 'get_balance' that returns current balance
- Test all methods

Task 9: Add validation to the BankAccount withdraw method:
- Check if withdrawal amount is greater than balance
- If yes, print "Insufficient funds" and don't withdraw
- If no, proceed with withdrawal
- Test with valid and invalid withdrawal attempts

Task 10: Create a class called 'Rectangle' with:
- __init__ method for width and height
- A method called 'area' that returns width * height
- A method called 'perimeter' that returns 2 * (width + height)
- A method called 'is_square' that returns True if width equals height
- Test all methods

=== PART 2: INTERMEDIATE CLASS CONCEPTS (Tasks 11-20) ===

Task 11: Create a class called 'Airplane' with:
- __init__ method for airline, flight_number, and max_passengers
- Instance variables: current_passengers (starts at 0), destination
- A method called 'board_passenger' that increases current_passengers by 1
- A method called 'get_passenger_count' that returns current_passengers
- Test by creating an airplane and boarding 5 passengers

Task 12: Add validation to the Airplane board_passenger method:
- Check if current_passengers < max_passengers
- If yes, board the passenger and print "Passenger boarded. Total: [count]"
- If no, print "Airplane is full! Cannot board more passengers"
- Test with boarding more passengers than the maximum

Task 13: Add a method called 'takeoff' to the Airplane class that:
- Checks if current_passengers > 0
- If yes, prints "Flight [flight_number] taking off to [destination] with [count] passengers"
- If no, prints "Cannot takeoff - no passengers on board"
- Test both scenarios

Task 14: Create a class called 'Passenger' with:
- __init__ method for name, age, and seat_number
- A method called 'board_plane' that prints "[name] is boarding seat [seat_number]"
- A method called 'is_adult' that returns True if age >= 18, False otherwise
- Create 3 passengers and test all methods

Task 15: Add a method called 'get_ticket_info' to the Passenger class that:
- Returns a formatted string with passenger details
- Include name, age, seat number, and adult status
- Test with different passengers

Task 16: Modify the Airplane class to work with Passenger objects:
- Change board_passenger to accept a Passenger object
- Print the passenger's name and seat when boarding
- Update the takeoff method to show passenger names
- Test by creating passengers and boarding them

Task 17: Add a method called 'list_passengers' to the Airplane class that:
- Prints all boarded passengers' information
- If no passengers, prints "No passengers on board"
- Test with empty and occupied airplane

Task 18: Create a class called 'Flight' that manages an Airplane and its Passengers:
- __init__ method takes airline, flight_number, destination, max_passengers
- Create an Airplane instance inside Flight
- Methods: add_passenger, takeoff, get_status
- Test by creating a flight and adding passengers

Task 19: Add validation to the Flight add_passenger method:
- Check if passenger is already on the flight (by name)
- Check if airplane has space
- If both checks pass, add passenger and return True
- If not, return False with appropriate message
- Test with duplicate passengers and full airplane

Task 20: Add a method called 'emergency_landing' to the Flight class that:
- Prints "EMERGENCY LANDING! All passengers must evacuate!"
- Resets passenger count to 0
- Prints "Flight [flight_number] has landed safely"
- Test the emergency landing

=== PART 3: ADVANCED CLASS CONCEPTS (Tasks 21-30) ===

Task 21: Create a class called 'Airport' that manages multiple Flights:
- __init__ method for airport_name
- Instance variable: flights (empty list)
- Methods: add_flight, remove_flight, list_flights
- Test by creating an airport and adding multiple flights

Task 22: Add a method called 'find_flight' to the Airport class that:
- Takes a flight_number as parameter
- Returns the Flight object if found, None if not found
- Test by searching for existing and non-existing flights

Task 23: Add a method called 'get_flight_status' to the Airport class that:
- Takes a flight_number and returns detailed flight information
- Include passenger count, destination, and flight status
- Handle case where flight doesn't exist
- Test with different flights

Task 24: Create a class called 'Pilot' with:
- __init__ method for name, license_number, and flight_hours
- Methods: fly_plane, get_experience_level
- Experience levels: "Junior" (< 1000 hours), "Senior" (1000-5000), "Captain" (> 5000)
- Test with pilots of different experience levels

Task 25: Modify the Flight class to include a Pilot:
- Add pilot parameter to __init__
- Add method called 'assign_pilot' that assigns a pilot to the flight
- Modify takeoff to include pilot information
- Test by creating flights with different pilots

Task 26: Add a method called 'calculate_fuel_needed' to the Flight class that:
- Takes distance as parameter
- Calculates fuel needed based on passenger count and distance
- Formula: (passenger_count * 0.1) + (distance * 0.05)
- Return the fuel amount needed
- Test with different passenger counts and distances

Task 27: Create a class called 'CrewMember' with:
- __init__ method for name, position (pilot, flight_attendant, engineer)
- Methods: work, get_position_info
- Add validation to ensure position is one of the valid options
- Test with different crew members

Task 28: Modify the Flight class to support multiple crew members:
- Change pilot to crew_members (list)
- Add methods: add_crew_member, remove_crew_member, list_crew
- Add validation to ensure at least one pilot is assigned
- Test by adding different crew members

Task 29: Add a method called 'flight_safety_check' to the Flight class that:
- Checks if there's at least one pilot
- Checks if passenger count doesn't exceed maximum
- Checks if all crew members are valid
- Returns True if all checks pass, False otherwise
- Print detailed results of each check
- Test with valid and invalid flight configurations

Task 30: Create a comprehensive test scenario:
- Create an airport
- Create a flight with destination "New York", max 150 passengers
- Create 5 passengers with different ages and seat numbers
- Create 3 crew members (1 pilot, 2 flight attendants)
- Add all passengers and crew to the flight
- Perform safety check
- If safe, take off the flight
- Print final flight status
- Test both safe and unsafe scenarios

=== BONUS CHALLENGES ===

Bonus 1: Add a method to calculate flight cost based on distance and passenger count
Bonus 2: Create a method to simulate flight delays and their impact
Bonus 3: Add weather conditions that affect flight safety
Bonus 4: Create a method to generate flight reports with statistics
Bonus 5: Implement a simple booking system with seat selection

=== EVALUATION CRITERIA ===
- Correct use of __init__ and self
- Proper method definitions and calls
- Appropriate use of instance variables
- Implementation of validation logic
- Clean, readable code structure
- Proper error handling
- Creative problem-solving

Good luck with your Python classes journey! 🚀✈️
"""

# Task 1 & 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")


person = Person("Alex", 25)
print(person.name, person.age)
person.introduce()


# Task 3 & 4
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine is running")

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"


car = Car("Toyota", "Camry", 2022)
car.start_engine()
print(car.get_info())


# Task 5
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading {self.title} by {self.author}")

    def is_long(self):
        return self.pages > 300


book = Book("Python Mastery", "Jane Smith", 350)
book.read()
print("Is long:", book.is_long())


# Task 6 & 7
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying")

    def get_grade(self):
        return self.grade

    def promote(self):
        self.grade += 1
        print(f"{self.name} was promoted to grade {self.grade}")


s1 = Student("Alice", 1, 3)
s2 = Student("Bob", 2, 4)
s3 = Student("Charlie", 3, 5)

for s in (s1, s2, s3):
    s.study()
    print(s.get_grade())

s1.promote()


# Task 8 & 9
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("John", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
print("Balance:", account.get_balance())


# Task 10
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


rect = Rectangle(5, 5)
print(rect.area(), rect.perimeter(), rect.is_square())

# Task 11–13
class Airplane:
    def __init__(self, airline, flight_number, destination, max_passengers):
        self.airline = airline
        self.flight_number = flight_number
        self.destination = destination
        self.max_passengers = max_passengers
        self.passengers = []

    def board_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f"Passenger boarded: {passenger.name} ({passenger.seat_number})")
        else:
            print("Airplane is full!")

    def get_passenger_count(self):
        return len(self.passengers)

    def takeoff(self):
        if self.passengers:
            names = ", ".join(p.name for p in self.passengers)
            print(f"Flight {self.flight_number} taking off to {self.destination} with {names}")
        else:
            print("Cannot takeoff - no passengers")


# Task 14 & 15
class Passenger:
    def __init__(self, name, age, seat_number):
        self.name = name
        self.age = age
        self.seat_number = seat_number

    def board_plane(self):
        print(f"{self.name} is boarding seat {self.seat_number}")

    def is_adult(self):
        return self.age >= 18

    def get_ticket_info(self):
        return f"{self.name}, Age: {self.age}, Seat: {self.seat_number}, Adult: {self.is_adult()}"


# Task 16 & 17
plane = Airplane("Delta", "DL100", "Paris", 2)
p1 = Passenger("Alice", 30, "1A")
p2 = Passenger("Bob", 15, "1B")

plane.board_passenger(p1)
plane.board_passenger(p2)
plane.takeoff()


# Task 18–20
class Flight:
    def __init__(self, airline, flight_number, destination, max_passengers):
        self.airplane = Airplane(airline, flight_number, destination, max_passengers)

    def add_passenger(self, passenger):
        if passenger.name in [p.name for p in self.airplane.passengers]:
            print("Passenger already on flight")
            return False
        self.airplane.board_passenger(passenger)
        return True

    def takeoff(self):
        self.airplane.takeoff()

    def emergency_landing(self):
        print("EMERGENCY LANDING! All passengers must evacuate!")
        self.airplane.passengers.clear()
        print(f"Flight {self.airplane.flight_number} has landed safely")

# Task 21–23
class Airport:
    def __init__(self, airport_name):
        self.airport_name = airport_name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def find_flight(self, flight_number):
        for flight in self.flights:
            if flight.airplane.flight_number == flight_number:
                return flight
        return None

    def list_flights(self):
        for flight in self.flights:
            print(flight.airplane.flight_number, flight.airplane.destination)


# Task 24
class Pilot:
    def __init__(self, name, license_number, flight_hours):
        self.name = name
        self.license_number = license_number
        self.flight_hours = flight_hours

    def get_experience_level(self):
        if self.flight_hours < 1000:
            return "Junior"
        elif self.flight_hours <= 5000:
            return "Senior"
        return "Captain"


# Task 27
class CrewMember:
    def __init__(self, name, position):
        if position not in ["pilot", "flight_attendant", "engineer"]:
            raise ValueError("Invalid position")
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} working as {self.position}")
