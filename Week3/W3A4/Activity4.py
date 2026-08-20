"""
Week 3: Activity 4: College enrollment database activity.
==========================================
Develop a database project based on the ER diagram created in W3-A3. Review and update the ER diagram if necessary before implementing the database and you can use the sample code in your Blackboard.
Populate the database with the following sample data:
3 courses
2 lecturers
5 students
Appropriate enrolment records for the students
Any additional records required for the other entities/tables in your ER diagram
Once the database has been developed and populated, use SQL queries to answer the following questions:
How many students are registered in each course?
List the names and student IDs of students who have enrolled in more than one course.
"""
import sqlite3

# --------------------------
# 1. Create a database connection
# --------------------------
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to database:", db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# --------------------------
# 2. Create a table
# --------------------------
def create_table(conn):
    """ create a table from the create_table_sql statement
    """
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Students (
                        Student_Id INTEGER PRIMARY KEY,
                        First_Name VARCHAR(100) NOT NULL,
                        Last_Name VARCHAR(100) NOT NULL,
                        DOB DATE  NULL,
                        Email VARCHAR(100) UNIQUE NOT NULL
                    );''')
        print("Table 'Students' created successfully.")

        c.execute('''CREATE TABLE IF NOT EXISTS Subjects (
                        Subject_Code VARCHAR(10) PRIMARY KEY,
                        Subject_Name VARCHAR(100) NOT NULL,
                        Credits INTEGER NOT NULL
                    );''')
        print("Table 'Subjects' created successfully.")

        c.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
                        Enrollment_Id INTEGER PRIMARY KEY,
                        Student_Id INTEGER NOT NULL,
                        Subject_Code VARCHAR(10) NOT NULL,
                        Enrollment_Date DATE NOT NULL,
                        FOREIGN KEY (Student_Id) REFERENCES Students (Student_Id),
                        FOREIGN KEY (Subject_Code) REFERENCES Subjects (Subject_Code)
                    );''')
        print("Table 'Enrollments' created successfully.")

        c.execute('''CREATE TABLE IF NOT EXISTS Lecturers (
                        Lecturer_Id INTEGER PRIMARY KEY,
                        First_Name VARCHAR(100) NOT NULL,
                        Last_Name VARCHAR(100) NOT NULL,
                        Email VARCHAR(100) UNIQUE NOT NULL,
                        Address VARCHAR(200) NULL
                    );''')
        print("Table 'Lecturers' created successfully.")

        c.execute('''CREATE TABLE IF NOT EXISTS Lectures (
                        Lecture_Id INTEGER PRIMARY KEY,
                        Subject_Code VARCHAR(10) NOT NULL,
                        Lecturer_Id INTEGER NOT NULL,
                        Schedule DATETIME NOT NULL,
                        FOREIGN KEY (Subject_Code) REFERENCES Subjects (Subject_Code),
                        FOREIGN KEY (Lecturer_Id) REFERENCES Lecturers (Lecturer_Id)
                    );''')
        print("Table 'Lectures' created successfully.")
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# --------------------------
# 3. Populate the tables with sample data
# --------------------------
def populate_tables(conn):
    """ populate the tables with sample data """
    try:
        c = conn.cursor()
        # Populate Students table
        students = [
            (1, 'John', 'Doe', '2000-01-15', 'john.doe@example.com'),
            (2, 'Jane', 'Smith', '1999-05-22', 'jane.smith@example.com'),
            (3, 'Alice', 'Johnson', '2001-03-10', 'alice.johnson@example.com'),
            (4, 'Bob', 'Brown', '2000-07-30', 'bob.brown@example.com'),
            (5, 'Charlie', 'Davis', '1998-11-12', 'charlie.davis@example.com')
        ]
        c.executemany('''INSERT OR REPLACE INTO Students (Student_Id, First_Name, Last_Name, DOB, Email) VALUES (?, ?, ?, ?, ?)''', students)
        print("Data inserted into 'Students' table successfully.")

        # Populate Subjects table
        subjects = [
            ('MSE800', 'Professional Software Engineering', 30),
            ('MSE801', 'Research Methods', 15),
            ('MSE802', 'Quantum Physics', 15)
        ]
        c.executemany('''INSERT OR REPLACE INTO Subjects (Subject_Code, Subject_Name, Credits) VALUES (?, ?, ?)''', subjects)
        print("Data inserted into 'Subjects' table successfully.")

        # Populate Enrollments table
        enrollments = [
            (1, 1, 'MSE800', '2023-09-01'),
            (2, 2, 'MSE801', '2023-09-02'),
            (3, 3, 'MSE802', '2023-09-03'),
            (4, 4, 'MSE800', '2023-09-04'),
            (5, 5, 'MSE801', '2023-09-05'),
            (6, 1, 'MSE802', '2023-09-06'),
            (7, 2, 'MSE800', '2023-09-07'),
            (8, 3, 'MSE801', '2023-09-08'),
            (9, 4, 'MSE802', '2023-09-09'),
            (10, 5, 'MSE800', '2023-09-10')
        ]
        
        c.executemany('''INSERT OR REPLACE INTO Enrollments (Enrollment_Id, Student_Id, Subject_Code, Enrollment_Date) VALUES (?, ?, ?, ?)''', enrollments)
        print("Data inserted into 'Enrollments' table successfully.")

        # Populate Lecturers table
        lecturers = [
            (1, 'Dr. Emily', 'Clark', 'emily.clark@example.com'),
            (2, 'Dr. Michael', 'Lee', 'michael.lee@example.com')
        ]
        c.executemany('''INSERT OR REPLACE INTO Lecturers (Lecturer_Id, First_Name, Last_Name, Email) VALUES (?, ?, ?, ?)''', lecturers)
        print("Data inserted into 'Lecturers' table successfully.")
        # Populate Lectures table
        lectures = [
            (1, 'MSE800', 1, '2023-09-01 10:00:00'),
            (2, 'MSE801', 2, '2023-09-02 14:00:00'),
            (3, 'MSE802', 1, '2023-09-03 09:00:00'),
            (4, 'MSE800', 2, '2023-09-04 11:00:00'),
            (5, 'MSE801', 1, '2023-09-05 15:00:00')
        ]
        c.executemany('''INSERT OR REPLACE INTO Lectures (Lecture_Id, Subject_Code, Lecturer_Id, Schedule) VALUES (?, ?, ?, ?)''', lectures)
        print("Data inserted into 'Lectures' table successfully.")
        conn.commit()
    except sqlite3.Error as e:
        print(e)    

# --------------------------
# 4. Query to find how many students are registered in each course
# --------------------------   
def query_students_per_course(conn):
    """ Query to find how many students are registered in each course """
    try:
        c = conn.cursor()
        c.execute('''
            SELECT Subjects.Subject_Name, COUNT(Enrollments.Student_Id) AS Student_Count
            FROM Enrollments
            JOIN Subjects ON Enrollments.Subject_Code = Subjects.Subject_Code
            GROUP BY Subjects.Subject_Name;
            ''')
        results = c.fetchall()
        print("\nNumber of students registered in each course:")
        for row in results:
            print(f"Course: {row[0]}, Students Registered: {row[1]}")
    except sqlite3.Error as e:
        print(e)

# --------------------------
# 5. Query to list the names and student IDs of students who have enrolled in more than one course
# --------------------------   
def query_students_multiple_courses(conn):
    """ Query to list the names and student IDs of students who have enrolled in more than one course """
    try:
        c = conn.cursor()
        c.execute('''
            SELECT Students.Student_Id, Students.First_Name, Students.Last_Name, COUNT(Enrollments.Subject_Code) AS Course_Count
            FROM Enrollments
            JOIN Students ON Enrollments.Student_Id = Students.Student_Id
            GROUP BY Students.Student_Id
            HAVING Course_Count > 1;
            ''')
        results = c.fetchall()
        print("\nStudents enrolled in more than one course:")
        for row in results:
            print(f"Student ID: {row[0]}, Name: {row[1]} {row[2]}, Courses Enrolled: {row[3]}")
    except sqlite3.Error as e:
        print(e)

def main():
    database = "college_enrollment.db"

    print("Starting the College Enrollment Database Activity...")

    # Create a database connection
    conn = create_connection(database)

    if conn is not None:
        # Create tables
        create_table(conn)

        # Populate tables with sample data
        populate_tables(conn)

        # Query to find how many students are registered in each course
        query_students_per_course(conn)

        # Query to list the names and student IDs of students who have enrolled in more than one course
        query_students_multiple_courses(conn)

        # Close the database connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()