CREATE DATABASE scheduling_system;
USE scheduling_system;

CREATE TABLE sections(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    grade VARCHAR(100) NOT NULL,
    section_name VARCHAR(100) NOT NULL
);

CREATE TABLE teachers(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    total_minutes INT NOT NULL
);

CREATE TABLE teacher_subjects(
	subject_name VARCHAR(100) NOT NULL,
    teachers_id INT NOT NULL,
    FOREIGN KEY(teachers_id) REFERENCES teachers(id)
);

CREATE TABLE teacher_grades(
	grade VARCHAR(100) NOT NULL,
    teachers_id INT NOT NULL,
    FOREIGN KEY(teachers_id) REFERENCES teachers(id)
);

CREATE TABLE rooms(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    room_name VARCHAR(100) NOT NULL,
    laboratory VARCHAR(100)
);

CREATE TABLE room_grades(
	grade VARCHAR(100) NOT NULL,
    rooms_id INT NOT NULL,
    FOREIGN KEY(rooms_id) REFERENCES rooms(id)
);

CREATE TABLE room_schedule(
	time_in TIME DEFAULT "7:00:00",
    time_out TIME DEFAULT "7:00:00",
    school_year VARCHAR(100) NOT NULL,
    rooms_id INT NOT NULL,
    FOREIGN KEY(rooms_id) REFERENCES rooms(id)
);

CREATE TABLE grades(
	id VARCHAR(100) NOT NULL PRIMARY KEY
);

CREATE TABLE grade_subjects(
	subject_name VARCHAR(100) NOT NULL,
    duration INT NOT NULL,
    grades_id VARCHAR(100) NOT NULL,
    FOREIGN KEY(grades_id) REFERENCES grades(id)
);

CREATE TABLE grade_breaktimes(
	time_in TIME NOT NULL,
    time_out TIME NOT NULL,
    grades_id VARCHAR(100) NOT NULL,
    FOREIGN KEY(grades_id) REFERENCES grades(id)
);

CREATE TABLE section_schedule(
	room_name VARCHAR(100),
    subject_name VARCHAR(100),
    time_in TIME DEFAULT "7:00:00",
    time_out TIME DEFAULT "7:00:00",
    subject_teacher VARCHAR(100),
    school_year VARCHAR(100) NOT NULL,
    rooms_id INT,
    sections_id INT NOT NULL,
    teachers_id INT,
    FOREIGN KEY(rooms_id) REFERENCES rooms(id),
    FOREIGN KEY(sections_id) REFERENCES sections(id),
    FOREIGN KEY(teachers_id) REFERENCES teachers(id)
);

CREATE TABLE teacher_schedule(
	room_name VARCHAR(100),
    subject_name VARCHAR(100),
    section_name VARCHAR(100),
    time_in TIME DEFAULT "7:00:00",
    time_out TIME DEFAULT "7:00:00",
    school_year VARCHAR(100) NOT NULL,
    teachers_id INT NOT NULL,
    rooms_id INT,
    sections_id INT,
    FOREIGN KEY(teachers_id) REFERENCES teachers(id),
    FOREIGN KEY(rooms_id) REFERENCES rooms(id),
    FOREIGN KEY(sections_id) REFERENCES sections(id)
);

CREATE TABLE school_years(
	sy VARCHAR(100) NOT NULL PRIMARY KEY,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);