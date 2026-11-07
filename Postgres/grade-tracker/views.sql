-- views.sql: one combined, readable table of every grade.

CREATE OR REPLACE VIEW student_grades AS
SELECT
    s.student_id,
    s.matric_no,
    s.first_name || ' ' || s.last_name AS student,
    d.name AS department,
    c.course_code,
    c.title,
    c.credit_units,
    e.score,
    CASE
        WHEN e.score IS NULL THEN NULL
        WHEN e.score >= 70 THEN 'A'
        WHEN e.score >= 60 THEN 'B'
        WHEN e.score >= 50 THEN 'C'
        WHEN e.score >= 45 THEN 'D'
        WHEN e.score >= 40 THEN 'E'
        ELSE 'F'
    END AS grade,
    CASE
        WHEN e.score IS NULL THEN NULL
        WHEN e.score >= 70 THEN 5
        WHEN e.score >= 60 THEN 4
        WHEN e.score >= 50 THEN 3
        WHEN e.score >= 45 THEN 2
        WHEN e.score >= 40 THEN 1
        ELSE 0
    END AS points
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses  c ON c.course_id  = e.course_id
LEFT JOIN departments d ON d.department_id = s.department_id;