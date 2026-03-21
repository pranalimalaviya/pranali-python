from datetime import datetime
print("Welcome to the interactive Personal data collector!\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = input("Please enter your height in meter: ")
number = input("Please enter your favorite number: ")

print("Thank You! Here is the information we collected:\n")

print(f"Name: {name}, Type: {type(name)}, Id: {id(name)} ")
print(f"Age: {age}, Type: {type(age)}, Id: {id(age)} ")
print(f"Height: {height}, Type: {type(height)}, Id: {id(height)} ")
print(f"Number: {number}, Type: {type(number)}, Id: {id(number)} ")



current_year = datetime.now().year
birth_year = current_year - age

print(f"Your birth is approximately: {birth_year} based on your age of {age}")

print("Thank you for using the Personal Data Collector. Goodbye!")

