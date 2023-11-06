import sqlite3

# Create a connection to the database
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

# SQL commands
sql_commands = [
    '''CREATE TABLE adminusers (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        email VARCHAR,
        password VARCHAR
    )''',
    '''CREATE TABLE studentusers (
        id INTEGER PRIMARY KEY,
        batch INTEGER,
        name VARCHAR,
        email VARCHAR,
        password VARCHAR
    )''',
    '''CREATE TABLE teachers (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        email VARCHAR,
        password VARCHAR
    )''',
    '''CREATE TABLE courses (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        code VARCHAR
    )''',
    '''CREATE TABLE student_course_association (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES studentusers(id),
        FOREIGN KEY(course_id) REFERENCES courses(id),
        PRIMARY KEY (student_id, course_id)
    )''',
    '''CREATE TABLE semesters (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        start_date VARCHAR,
        end_date VARCHAR,
        year INTEGER,
        course_id INTEGER,
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )''',
    '''CREATE TABLE subjects (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        course_id INTEGER,
        semester_id INTEGER,
        year INTEGER,
        FOREIGN KEY(course_id) REFERENCES courses(id),
        FOREIGN KEY(semester_id) REFERENCES semesters(id)
    )''',
    '''CREATE TABLE student_subject_association (
        student_id INTEGER,
        subject_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES studentusers(id),
        FOREIGN KEY(subject_id) REFERENCES subjects(id),
        PRIMARY KEY (student_id, subject_id)
    )''',
    '''CREATE TABLE projects (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        course_id INTEGER,
        semester_id INTEGER,
        year INTEGER,
        due_date VARCHAR,
        status VARCHAR,
        marks INTEGER CHECK (marks >= 0 AND marks <= 100),
        FOREIGN KEY(course_id) REFERENCES courses(id),
        FOREIGN KEY(semester_id) REFERENCES semesters(id)
    )''',
    '''CREATE TABLE student_project_association (
        student_id INTEGER,
        project_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES studentusers(id),
        FOREIGN KEY(project_id) REFERENCES projects(id),
        PRIMARY KEY (student_id, project_id)
    )'''
]

# Execute the SQL commands
for command in sql_commands:
    cur.execute(command)

# Commit the changes and close the connection
conn.commit()
conn.close()
