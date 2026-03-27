Students = []

while True:
    print("Welcome to student Data Organizer!")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")
        Students_id = int(input("Student ID: "))
        Name = input("Name: ")
        Age = int(input("Age: "))
        Grade = input("Grade: ")
        Dob = input("Date od Birth (YYYY-MM-DD): ")
        Subjects = input("Subjects (comma separated): ").split(",")

        Student = {
            "id": Students_id,
            "Name": Name,
            "Age": Age,
            "Grade": Grade,
            "DOB": Dob,
            "Subjects": Subjects
        }
        Students.append(Student)
        print("Student added Successfully!")

    elif choice == "2":
        print("---Display all students---")
        for s in Students:
            print(f"Student ID: {s['id']} | Name: {s['Name']} | Age: {s['Age']} | Grade: {s['Grade']} | Dob: {s['DOB']} | Subjects: {s['Subjects']}")

    elif choice == "3":
        Students_id = int(input("\nEnter student ID to update: "))

        for s in Students:
            if s["id"] == Students_id:
               s["Name"] = input("Enter new Name: ")
               s["Age"] = input("Enter new Age: ")
               s["Grade"] = input("Enter new Grade: ")
               s["Subjects"] = input("Enter new Subjects: ").split(",")
               print("Student updated Successfully!")
               break
            else:
                print("Student not found!")

    elif choice == "4":
         Students_id = int(input("\nEnter student ID to Delete: "))
         for s in Students:
            if s["id"] == Students_id:
                Students.remove(s)
                print("Student deleted Successfully!")
                break
            else:
                print("Student not found!")

    elif choice == "5":
        all_subjects = []
        for s in Students:
            for sub in s["Subjects"]:
                if sub not in all_subjects:
                    all_subjects.append(sub)
        
        print("Subjects Offered:",",".join(all_subjects))


    elif choice == "6":
        print("Thank You for using Student Data Organizer!")
        break
    else:
        print("Invalid choicd, Try Again!")
