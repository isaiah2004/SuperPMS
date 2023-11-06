import sqlite3
from datetime import datetime

# Create a connection to the database
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

# Function to insert 10 dummy values into the adminusers table
def insert_dummy_adminusers_values():
    for i in range(1, 11):
        cur.execute(f'''INSERT INTO adminusers (name, email, password) 
                        VALUES ("Admin Name {i}", "admin{i}@example.com", "admin_password{i}")''')

# Function to insert 10 dummy values into the studentusers table
def insert_dummy_studentusers_values():
    for i in range(1, 11):
        cur.execute(f'''INSERT INTO studentusers (batch, name, email, password) 
                        VALUES (2023, "Student Name {i}", "student{i}@example.com", "student_password{i}")''')

# Function to insert 10 dummy values into the teachers table
def insert_dummy_teachers_values():
    for i in range(1, 11):
        cur.execute(f'''INSERT INTO teachers (name, email, password) 
                        VALUES ("Teacher Name {i}", "teacher{i}@example.com", "teacher_password{i}")''')

# Function to insert 10 dummy values into the courses table
def insert_dummy_courses_values():
    for i in range(1, 11):
        cur.execute(f'''INSERT INTO courses (name, code) 
                        VALUES ("Course Name {i}", "CSE101{i}")''')

# Function to insert 10 dummy values into the semesters table
def insert_dummy_semesters_values():
    for i in range(1, 11):
        cur.execute(f'''INSERT INTO semesters (name, start_date, end_date, year, course_id) 
                        VALUES ("Semester Name {i}", "{datetime.now()}", "{datetime.now()}", 2023, {i})''')

# Function to insert 10 dummy values into the subjects table
def insert_dummy_subjects_values():
    for i in range(1, 11):
        cur.execute(f'''INSERT INTO subjects (name, course_id, semester_id, year) 
                        VALUES ("Subject Name {i}", {i}, {i}, 2023)''')

# Function to insert 10 dummy values into the projects table
def insert_dummy_projects_values():
    for i in range(1, 11):
        cur.execute(f'''INSERT INTO projects (title, course_id, semester_id, status, marks, year, due_date) 
                        VALUES ("Project Title {i}", {i}, {i},"TO BE APPROVED",{i*9+9}, 2023, "{datetime.now()}")''')




# Call each function to insert the dummy values
insert_dummy_adminusers_values()
insert_dummy_studentusers_values()
insert_dummy_teachers_values()
insert_dummy_courses_values()
insert_dummy_semesters_values()
insert_dummy_subjects_values()
insert_dummy_projects_values()



# Commit the changes and close the connection
conn.commit()
conn.close()
