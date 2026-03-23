print("Telecome Calling System")
print("1. English")
print("2. Hindi")
print("3. Gujarati")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("\nYou have selected English")
        print("1. Balance check")
        print("2. Recharge")
        
        sub = int(input("Enter your choice: "))
        
        match sub:
            case 1:
                print("Your balance is $100")
            case 2:
                amt = int(input("Enter recharge amount: "))
                print(f"Recharge of ${amt} successful")
            case _:
                print("Invalid option")
                
    case 2:
        print("\nYou have selected Hindi")
        print("1. Balance check")
        print("2. Recharge")
        
        sub = int(input("Enter yoyr choice: "))
        
        match sub:
            case 1:
                print("Your balance is $100")
            case 2:
                amt = int(input("Enter recharge amount: "))
                print(f"Recharge of ${amt} successful")
            case _:
                print("Invalid option")
                
    case 3:
         print("\nYou have selected Gujarati")
         print("1. Balance check")
         print("2. Recharge")
        
         sub = int(input("Enter your choice: "))
        
         match sub:
            case 1:
                print("Your balance is $100")
            case 2:
                amt = int(input("Enter recharge amount: "))
                print(f"Recharge of ${amt} successful")
            case _:
                print("Invalid option")
        