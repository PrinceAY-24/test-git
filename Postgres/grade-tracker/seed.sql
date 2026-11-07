-- seed.sql: fills the tables with sample data.
-- Run it right after schema.sql.

INSERT INTO departments (name) VALUES
    ('Physics'), ('Mathematics'), ('Computer Science');

INSERT INTO students (matric_no, first_name, last_name, email, department_id) VALUES
    ('CSC/2024/001', 'Ada',    'Obi',      'ada.obi@example.com',       3),
    ('CSC/2024/002', 'Tunde',  'Bello',    'tunde.bello@example.com',   3),
    ('PHY/2024/003', 'Chidi',  'Okeke',    NULL,                        1),
    ('PHY/2024/004', 'Zainab', 'Musa',     'zainab.musa@example.com',   1),
    ('MTH/2024/005', 'Peter',  'O''Neil',  NULL,                        2),
    ('PHY/2024/006', 'Fatima', 'Yusuf',    'fatima.yusuf@example.com',  1),
    ('CSC/2024/007', 'Kunle',  'Adeyemi',  NULL,                        NULL),
    ('MTH/2024/008', 'Sade',   'Williams', 'sade.williams@example.com', 2),
    ('PHY/2024/009', 'Hauwa',  'Ibrahim',  NULL,                        1);

INSERT INTO courses (course_code, title, credit_units) VALUES
    ('PHY101', 'Mechanics', 3),
    ('PHY102', 'Electricity and Magnetism', 3),
    ('MTH101', 'Calculus I', 4),
    ('CSC101', 'Intro to Programming', 3),
    ('CSC201', 'Data Structures', 4),
    ('GST101', 'Use of English', 2);

INSERT INTO enrollments (student_id, course_id, score) VALUES
    (1, 1, 78.5), (1, 3, 85),   (1, 4, 92),
    (2, 4, 67),   (2, 5, 71.5), (2, 3, 58),
    (3, 1, 88),   (3, 2, 74),
    (4, 1, 91),   (4, 2, 83.5), (4, 3, 77),
    (5, 3, 45),
    (6, 2, 62),   (6, 4, NULL);