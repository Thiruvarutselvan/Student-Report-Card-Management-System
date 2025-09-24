from student import Student 
from utils import load_students, save_students,search_student

def add_student():
    roll_no = input("enter roll no")
    name = input("enter Name")
    subjects = ["maths","science","English"]
    marks = {}
    for subject in subjects:
        marks[subject] = int(input(f"Enter mark for {subject}"))

    #create student object 
    student = Student(roll_no, name, marks)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)

def view_students():
    students = load_students() 
    for s in students:
        print(s)

def main():
    while True:
        print("\n--- Student Report Card System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by roll No")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice")        

if __name__ == "__main__":
    main()

