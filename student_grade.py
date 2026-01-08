# Student Grade Checker program
students = {}

while True:
    print("\n1. Add Student")
    print("\n2. UpdateStudent Grade")
    print("\n3.Print All Student Grades")
    print("\n4. Exit")

    choice = int(input("\nEnter your choice: ") )

    if choice == 1:
        name = input("Enter Student Name: ")

        grade = input("Enter Student Grade: ")
        students[name] = grade
        print("Student added successfully.")

    elif choice == 2:
        name = input("Enter Student Name to Update : ")
        if name in students:
            grade = input("Enter New Grade: ")
            students[name] = grade
            print("Student grade updated to .")
        else:
            print("Student not found.")

    elif choice == 3:
        if students:
            print("\nStudent Grades:")
            for name, grade in students.items():
                print(name, ":" ,grade)
        else:
            print("No student records found.")

    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    

         