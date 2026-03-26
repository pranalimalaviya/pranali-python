print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == 1:
        rows = int(input("Enter the number of rows for the Pattern:"))
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        total = 0

        for i in range(start, end + 1):
            if i % 2 == 0:
                print("Number", i, "is Even")
            else:
                print("Number", i, "is Odd")

            total += i

        print("Sum of numbers from", start, "to", end, "is:", total)

    elif choice == 3:
        print("Exiting the program. Goodbye!")
    break
else:
    print("Invalid choice. Try again.")



    