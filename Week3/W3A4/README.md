# College Enrollment Database Activity

## Overview
This project implements a college enrollment database using SQLite. The database is designed based on an Entity-
Relationship (ER) diagram and includes tables for Students, Subjects, Enrollments, Lecturers, and Lectures. 
The project populates the database with sample data and performs SQL queries to analyze student enrollments.

## Database Structure
The database consists of the following tables:
- **Students**: Stores information about students.
- **Subjects**: Stores information about subjects/courses.
- **Enrollments**: Links students to the subjects they are enrolled in.
- **Lecturers**: Stores information about lecturers.
- **Lectures**: Links lecturers to the subjects they teach.
## Sample Data
The database is populated with the following sample data:
### Students
| Student_Id | First_Name | Last_Name | DOB        | Email                     |
|------------|------------|-----------|------------|---------------------------|
| 1          | John       | Doe       | 2000-01-01 | john.doe@example.com      |
| 2          | Jane       | Smith     | 2000-02-02 | jane.smith@example.com    |
| 3          | Bob        | Johnson   | 2000-03-03 | bob.johnson@example.com   |
### Subjects
| Subject_Code | Subject_Name | Credits |
|--------------|--------------|---------|
| MSE800       | Professional Software Engineering | 30 |
| MSE801       | Research Methods | 15 |
| MSE802       | Quantum Computing | 15 |
### Enrollments
| Enrollment_Id | Student_Id | Subject_Code | Enrollment_Date |
|---------------|------------|--------------|-----------------|
| 1          | 1          | MSE800       | 2023-01-01      |
| 2          | 1          | MSE801       | 2023-01-01      |
| 3          | 2          | MSE800       | 2023-01-02      |
| 4          | 2          | MSE802       | 2023-01-02      |
| 5          | 3          | MSE801       | 2023-01-03      |
| 6          | 3          | MSE802       | 2023-01-03      | 
### Lecturers
| Lecturer_Id | First_Name | Last_Name | Email                     |
|-------------|------------|-----------|---------------------------|
| 1          | Dr.        | Smith     | dr.smith@example.com      |
| 2          | Prof.      | Johnson   | prof.johnson@example.com  |
### Lectures
| Lecture_Id | Subject_Code | Lecturer_Id | Schedule           |
|------------|--------------|-------------|--------------------|
| 1          | MSE800       | 1          | Mon 10:00-12:00    |
| 2          | MSE801       | 2          | Tue 14:00-16:00    |
| 3          | MSE802       | 1          | Wed 10:00-12:00    |

## SQL Queries
The following SQL queries are executed to analyze the data in the database:
### Query 1: Number of Students Registered in Each Course
```sql
SELECT s.Subject_Name, COUNT(e.Student_Id) AS NumberOfStudents
FROM Subjects s
LEFT JOIN Enrollments e ON s.Subject_Code = e.Subject_Code
GROUP BY s.Subject_Name;
```
### Query 2: Students Enrolled in More Than One Course
```sql
SELECT st.Student_Id, st.First_Name, st.Last_Name, COUNT(e.Subject_Code) AS NumberOfCourses
FROM Students st
JOIN Enrollments e ON st.Student_Id = e.Student_Id
GROUP BY st.Student_Id, st.First_Name, st.Last_Name
HAVING COUNT(e.Subject_Code) > 1;
```
### Populated Data
The results of the queries are as follows:

#### Query 1 Results
| Subject_Name | NumberOfStudents |
|--------------|------------------|
| Professional Software Engineering | 2 |
| Research Methods | 2 |
| Quantum Computing | 2 |

#### Query 2 Results
| Student_Id | First_Name | Last_Name | NumberOfCourses |
|------------|------------|-----------|-----------------|
| 1          | John       | Doe       | 2               |
| 2          | Jane       | Smith     | 2               |
| 3          | Bob        | Johnson   | 2               |
