import sqlite3

# Create a connection to the database
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

# Function to create the adminusers table
def create_adminusers_table():
    cur.execute('''CREATE TABLE adminusers (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        email VARCHAR,
        password VARCHAR
    )''')

# Function to create the studentusers table
def create_studentusers_table():
    cur.execute('''CREATE TABLE studentusers (
        id INTEGER PRIMARY KEY,
        batch INTEGER,
        name VARCHAR,
        email VARCHAR,
        password VARCHAR
    )''')

# Function to create the teachers table
def create_teachers_table():
    cur.execute('''CREATE TABLE teachers (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        email VARCHAR,
        password VARCHAR
    )''')

# Function to create the courses table
def create_courses_table():
    cur.execute('''CREATE TABLE courses (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        code VARCHAR
    )''')

# Function to create the student_course_association table
def create_student_course_association_table():
    cur.execute('''CREATE TABLE student_course_association (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES studentusers(id),
        FOREIGN KEY(course_id) REFERENCES courses(id),
        PRIMARY KEY (student_id, course_id)
    )''')

# Function to create the semesters table
def create_semesters_table():
    cur.execute('''CREATE TABLE semesters (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        start_date VARCHAR,
        end_date VARCHAR,
        year INTEGER,
        course_id INTEGER,
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )''')

# Function to create the subjects table
def create_subjects_table():
    cur.execute('''CREATE TABLE subjects (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        course_id INTEGER,
        semester_id INTEGER,
        year INTEGER,
        FOREIGN KEY(course_id) REFERENCES courses(id),
        FOREIGN KEY(semester_id) REFERENCES semesters(id)
    )''')

# Function to create the student_subject_association table
def create_student_subject_association_table():
    cur.execute('''CREATE TABLE student_subject_association (
        student_id INTEGER,
        subject_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES studentusers(id),
        FOREIGN KEY(subject_id) REFERENCES subjects(id),
        PRIMARY KEY (student_id, subject_id)
    )''')

# Function to create the projects table
def create_projects_table():
    cur.execute('''CREATE TABLE projects (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        course_id INTEGER,
        semester_id INTEGER,
        year INTEGER,
        due_date VARCHAR,
        FOREIGN KEY(course_id) REFERENCES courses(id),
        FOREIGN KEY(semester_id) REFERENCES semesters(id)
    )''')

# Function to create the student_project_association table
def create_student_project_association_table():
    cur.execute('''CREATE TABLE student_project_association (
        student_id INTEGER,
        project_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES studentusers(id),
        FOREIGN KEY(project_id) REFERENCES projects(id),
        PRIMARY KEY (student_id, project_id)
    )''')

# Call each function to create the tables
create_adminusers_table()
create_studentusers_table()
create_teachers_table()
create_courses_table()
create_student_course_association_table()
create_semesters_table()
create_subjects_table()
create_student_subject_association_table()
create_projects_table()
create_student_project_association_table()

# Commit the changes and close the connection
conn.commit()
conn.close()
