op = input("Enter operator (+, -, *, /): ")

a = float(input("Enter a number:"))
b = float(input("Enter a number:"))

match op:
    case '+':
        print("Result:", a + b)
    case '-':
        print("Result:", a - b)
    case '*':
        print("Result:", a * b)
    case '/':
        print("Result:", a + b)
    case _:
        print("Invalid Statement")
