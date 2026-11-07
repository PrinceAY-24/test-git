-- transcript.sql
-- Needs: -v matric=...

SELECT course_code, title, credit_units, score, grade
FROM student_grades
WHERE matric_no = :'matric'
ORDER BY course_code;