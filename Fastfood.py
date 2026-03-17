print("FAST FOOD MANU")
print("1. Sandwich")
print ("2. Pizza")
print ("3. Burger")

choice = int(input("Enter ypur choice:"))

match choice:
    case 1:
        print("Sandwich Menu")
        print("1. Veg Sandwich")
        print("2. Grilled Sandwich")

        sub = int(input("Enter your choice:"))

        match sub:
            case 1:
                print("You ordered Veg Sandwich")
            case 2:
                print("You ordered Grilled Sandwich")
            case _:
                print("Invalid choice")

    case 2:
        print("PIZZA MENU")
        print("1. Thin Crust Pizza")
        print("2. Cheese Brust Pizza")
        print("3. Fresh dough Pizza")

        sub = int(input("Enter Your choice:"))

        match sub:
            case 1:
                print("You ordered Thin Crust Pizza")
            case 2:
                print("You ordered Cheese Brust Pizza")
            case 3:
                print("You ordered fresh dough pizza")
            case _:
                print("Invalid choice")

    case 3:
        print("BURGER MENU")
        print("1. Veg burger") 
        print("2. chicken burger")

        sub = int(input("Enter your choice:"))
        match sub:
           case 1:
                print("You ordered Veg burger")
           case 2:
                print("You ordered chicken burger")
           case _:
                print("Invalid choice")

    case _:
        print("Invalid menu choice")
           