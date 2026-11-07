-- gpa_report.sql

SELECT student,
       matric_no,
       SUM(credit_units) AS graded_units,
       ROUND(SUM(points * credit_units)::NUMERIC / SUM(credit_units), 2) AS gpa
FROM student_grades
WHERE score IS NOT NULL
GROUP BY student_id, matric_no, student
ORDER BY gpa DESC, student;