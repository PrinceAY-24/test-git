-- add_student.sql
-- Needs: -v matric=...  -v fname=...  -v lname=...

INSERT INTO students (matric_no, first_name, last_name)
VALUES (:'matric', :'fname', :'lname')
RETURNING student_id, matric_no, first_name, last_name;