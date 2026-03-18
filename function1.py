students = []

def add_student():
    student = {}
    student["id"] = input("Student ID: ")
    student["name"] = input("Name: ")
    student["age"] = input("Age: ")
    student["grade"] = input("Grade: ")
    student["dob"] = input("Date of Birth (YYYY-MM-DD): ")
    
    subjects = input("Subjects (comma-separated): ")
    student["subjects"] = [s.strip() for s in subjects.split(",")]
    
    students.append(student)
    print("Student added successfully!\n")


def display_students():
    print("\n--- Display All Students ---")
    for s in students:
        print(f"Student ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {', '.join(s['subjects'])}")
    print()


def delete_student():
    sid = input("Enter student ID to delete: ")
    global students
    students = [s for s in students if s["id"] != sid]
    print("Student deleted (if found).\n")


def display_subjects():
    subject_set = set()
    for s in students:
        subject_set.update(s["subjects"])
    
    print("\nSubjects Offered:")
    for sub in subject_set:
        print(sub)
    print()


print("Welcome to the Student Data Organizer")

def menu():
    while True:
        print("\nSelect an option:")
        print("1. Add student")
        print("2. Display all students")
        print("3. Delete student")
        print("4. Display subjects offered")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_subjects()
        elif choice == "5":
            print("Thank you for using the Student Data Organizer!")
            break
        else:
            print("Invalid choice.\n")
        
menu()
