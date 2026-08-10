"""
Week 2 - Activity 3: Data type with description
-------------------------------------------------------------
OOP project to collect personal information for students(full name, age, address, student id) from user input,
then sort by age and display the results. Works for 70 students or an unknown number of students.
"""

#Step 1: Define the template for one student.
class Student():
    def __init__(self, full_name: str , age: int, address: str, student_id: str):
        self.full_name = full_name
        self.age = age
        self.address = address
        self.student_id = student_id
    
    def show(self):
        print(f"ID:{self.student_id} | Name: {self.full_name} | Age: {self.age} | Address: {self.address}")

#Step 2: A function that ask for and creates one student.
def create_student():
    full_name = input("Fullname: ")
    age = int(input("Age: "))
    address = input("Address: ")
    student_id = input("Student ID: ")
    return Student(full_name, age, address, student_id)

#Step 3: To collects student info in a list
def collect_students():
    students = []

    number_of_students = input("How many students? (type a number, or 'unknown'): ")
    if number_of_students.lower() == "unknown":
        # As we don't know the number, so keep asking until type 'done'.
        while True:
            name_check = input("\n Type 'done' to stop, else press Enter to add a student: ")
            if name_check.lower() == "done":
                break
            student = create_student()
            students.append(student)
    else:
        #Know number like, 70.
        total = int(number_of_students)
        for i in range(total):
            print(f"\nStudent {i + 1} of {total}")
            student = create_student()
            students.append(student)
    
    return students

#Step 4: To print all students info.
def display_students(students):
    print("\n----- Students sorted by age ----")
    for s in students:
        s.show()

#Step 5: where programs gets run
def main():
    students = collect_students()
    students.sort(key=lambda s: s.age)
    display_students(students)

if __name__ == "__main__":
    main()

    
