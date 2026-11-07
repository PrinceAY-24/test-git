-- filter_scores.sql
-- Needs: -v min=...

SELECT student, course_code, score, grade
FROM student_grades
WHERE score >= CAST(:'min' AS NUMERIC)
ORDER BY score DESC;