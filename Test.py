import datetime
print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name:")
age = int(input("Please enter your age:"))
height = float(input("Please enter your height in meters:"))
number = int(input("Please enter your favourite number:"))

print("Thank you! Here is the information we collected")

print(f"Name: {name} (Type: {type(name)}, memory address:{id(name)} )")
print(f"Age: {age} (Type: {type(age)}, memory address:{id(age)} )")
print(f"Height: {height} (Type: {type(height)}, memory address:{id(height)} )")
print(f"Number: {number} (Type: {type(number)}, memory address:{id(number)} )")

current_year= datetime.datetime.now().year
birth_year = current_year - age

print(f"Your birth year is approximately: {birth_year} (based on your age of {age})")
print("Thank you for using the Personal Data Collector. Goodbye!")
