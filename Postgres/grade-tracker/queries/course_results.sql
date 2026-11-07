-- course_results.sql
-- Needs: -v course=...

SELECT student, score, grade
FROM student_grades
WHERE course_code = :'course'
ORDER BY score DESC NULLS LAST;