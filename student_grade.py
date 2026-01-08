# Student Grade Checker program
students = {}

while True:
    print("\n1. Add Student")
    print("\n2. UpdateStudent Grade")
    print("\n3.Print All Student Grades")
    print("\n4. Exit")

    choice = int(input("\nEnter your choice: ") )

    if choice == 1:
        name = input("\nEnter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print(f"\nStudent {name} with grade {grade} added.")    
    
    elif choice == 2:
        name = input("\nEnter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"\nStudent {name}'s grade updated to {grade}.")
        else:
            print(f"\nStudent {name} not found.")

    elif choice == 3:
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")

    elif choice == 4:
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid choice. Please try again.")
# Student Grade Checker program