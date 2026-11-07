-- schema.sql: builds all tables from scratch.
-- Safe to re-run: it deletes the old tables first.
-- Order matters: children are dropped before parents.

DROP VIEW  IF EXISTS student_grades;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    name          VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE students (
    student_id    SERIAL PRIMARY KEY,
    matric_no     VARCHAR(20) NOT NULL UNIQUE,
    first_name    VARCHAR(50) NOT NULL,
    last_name     VARCHAR(50) NOT NULL,
    email         TEXT UNIQUE,
    enrolled_on   DATE NOT NULL DEFAULT CURRENT_DATE,
    is_active     BOOLEAN NOT NULL DEFAULT TRUE,
    department_id INTEGER REFERENCES departments (department_id)
);

CREATE TABLE courses (
    course_id    SERIAL PRIMARY KEY,
    course_code  VARCHAR(10) NOT NULL UNIQUE,
    title        VARCHAR(100) NOT NULL,
    credit_units INTEGER NOT NULL CHECK (credit_units BETWEEN 1 AND 6)
);

CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id    INTEGER NOT NULL REFERENCES students (student_id),
    course_id     INTEGER NOT NULL REFERENCES courses (course_id),
    score         NUMERIC(5,2) CHECK (score BETWEEN 0 AND 100),
    UNIQUE (student_id, course_id)
);