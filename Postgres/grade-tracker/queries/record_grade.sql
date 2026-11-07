-- record_grade.sql
-- Needs: -v matric=...  -v course=...  -v score=...

UPDATE enrollments
SET score = CAST(:'score' AS NUMERIC)
WHERE student_id = (SELECT student_id FROM students WHERE matric_no   = :'matric')
  AND course_id  = (SELECT course_id  FROM courses  WHERE course_code = :'course')
RETURNING enrollment_id, student_id, course_id, score;