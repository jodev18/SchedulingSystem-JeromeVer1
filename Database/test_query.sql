SHOW TABLES;

DROP TABLE teacher_schedule;
DROP TABLE section_schedule;
DROP TABLE grade_subjects;
DROP TABLE grades;
DROP TABLE room_schedule;
DROP TABLE room_grades;
DROP TABLE rooms;
DROP TABLE teacher_grades;
DROP TABLE teacher_subjects;
DROP TABLE teachers;
DROP TABLE sections;
DROP TABLE school_years;

SELECT * FROM grades;
SELECT * FROM grade_subjects;
SELECT * FROM teachers;
SELECT * FROM teacher_subjects;
SELECT * FROM teacher_grades;
SELECT * FROM teacher_schedule WHERE teachers_id = 1;
SELECT * FROM school_years;
SELECT * FROM rooms;
SELECT * FROM room_grades;
SELECT * FROM room_schedule;
SELECT * FROM sections;
SELECT * FROM section_schedule WHERE sections_id = 2;

SELECT * FROM teacher_schedule WHERE time_in BETWEEN TIME("7:00") AND (TIME("7:00") + INTERVAL 60 MINUTE) - INTERVAL 1 MINUTE
AND teachers_id = 1 AND subject_name IS NOT NULL AND school_year = "2019-2020";

SELECT subject_name FROM grade_subjects WHERE grades_id IN ("1");

SELECT time_out FROM section_schedule WHERE time_in BETWEEN TIME("10:45") AND 
(TIME("10:45") + INTERVAL 30 MINUTE) - INTERVAL 1 MINUTE
AND sections_id = 1 AND subject_name IS NOT NULL;

INSERT INTO section_schedule(subject_name, time_in, time_out, school_year, sections_id)
VALUES ("Filipino", TIME("8:00"), TIME("8:30"), "2019-2020", 1);

INSERT INTO teacher_schedule(subject_name, time_in, time_out, school_year, teachers_id)
VALUES ("Filipino", TIME("8:00"), TIME("9:00"), "2019-2020", 1);

SELECT id FROM teachers
JOIN teacher_grades
	ON id = teacher_grades.teachers_id
JOIN teacher_subjects
	ON id = teacher_subjects.teachers_id
JOIN teacher_schedule
	ON id = teacher_schedule.teachers_id
WHERE grade = "PK1" AND teacher_subjects.subject_name = "Filipino" AND total_minutes >= 60
AND time_in BETWEEN TIME("8:00") AND (TIME("8:00") + INTERVAL 60 MINUTE) - INTERVAL 1 MINUTE;

SELECT * FROM teacher_schedule;

SELECT id FROM teachers
JOIN teacher_grades
	ON id = teacher_grades.teachers_id
JOIN teacher_subjects
	ON id = teacher_subjects.teachers_id
JOIN teacher_schedule
	ON id = teacher_schedule.teachers_id
WHERE grade = 1 AND teacher_subjects.subject_name = "Filipino" AND total_minutes >= 60
GROUP BY id;

SELECT id FROM rooms
JOIN room_grades
	ON id = room_grades.rooms_id
WHERE laboratory = "No" AND room_grades.grade = "PK1"
AND (SELECT COUNT(*) FROM room_schedule WHERE rooms_id = id) <= 1;

SELECT teachers_id FROM teacher_schedule
WHERE time_in NOT BETWEEN TIME("8:00") AND (TIME("8:00") + INTERVAL 60 MINUTE) - INTERVAL 1 MINUTE
AND teachers_id = 1;

SELECT CONCAT_WS(" ", first_name, middle_name, last_name) FROM teachers WHERE id = 1;