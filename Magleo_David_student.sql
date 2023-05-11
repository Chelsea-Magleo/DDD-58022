CREATE SCHEMA student;

SELECT*FROM student.students_info;

SELECT * FROM students_info WHERE city = 'Laguna';

SELECT * FROM students_info WHERE sem_grade = 80;

SELECT * FROM students_info WHERE gender = 'F';

SELECT * FROM students_info WHERE entry_age = '17';

SELECT * FROM students_info WHERE final_exam = '100';

SELECT * FROM students_info WHERE NOT status = '4TH YEAR';

SELECT * FROM students_info ORDER BY sem_grade DESC;

SELECT * FROM students_info WHERE gender = 'M' AND status = '1ST YEAR';