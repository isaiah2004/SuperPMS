from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()

class AdminUser(Base):
    __tablename__ = 'adminusers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class StudentUser(Base):
    __tablename__ = 'studentusers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)

    projects = relationship("Project", back_populates="course")

class Semester(Base):
    __tablename__ = 'semesters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    year = Column(Integer)
    course_id = Column(Integer, ForeignKey('courses.id'))

    subjects = relationship("Subject", back_populates="semester")
    projects = relationship("Project", back_populates="semester")

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    semester_id = Column(Integer, ForeignKey('semesters.id'))
    year = Column(Integer)

    semester = relationship("Semester", back_populates="subjects")

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    semester_id = Column(Integer, ForeignKey('semesters.id'))
    year = Column(Integer)
    due_date = Column(String)

    course = relationship("Course", back_populates="projects")
    semester = relationship("Semester", back_populates="projects")

# Other model classes

Base.metadata.create_all(engine)
