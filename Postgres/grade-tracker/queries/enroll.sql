-- enroll.sql
-- Needs: -v matric=...  -v course=...

INSERT INTO enrollments (student_id, course_id)
SELECT s.student_id, c.course_id
FROM students s
CROSS JOIN courses c
WHERE s.matric_no = :'matric'
  AND c.course_code = :'course'
RETURNING *;