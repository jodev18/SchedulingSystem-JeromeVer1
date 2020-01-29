import pymysql

class Query:
    def insert_subject(self, grade, subject):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            INSERT INTO grades(id) VALUES("%s")
        """%(grade))

        self.cursor.execute("""
            SELECT id FROM grades ORDER BY id DESC LIMIT 1
        """)
        self.id = self.cursor.fetchone()[0]

        for i in range(len(subject)):
            subject[i].append(self.id)

        self.cursor.executemany("""
            INSERT INTO grade_subjects(subject_name, duration, grades_id)
            VALUES(%s, %s, %s)
        """, subject)

        self.connection.commit()
        self.connection.close()

    def search_subjects(self, grade):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            SELECT subject_name FROM grade_subjects WHERE grades_id = "%s"
        """%(grade))

        return self.cursor.fetchall()

    def insert_teacher(self, teacher, subject, grade):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.subject = subject
        self.grade = grade

        self.cursor.executemany("""
            INSERT INTO teachers(first_name, middle_name, last_name, total_minutes)
            VALUES(%s, %s, %s, %s)
        """, teacher)

        self.cursor.execute("""
            SELECT id FROM teachers ORDER BY id DESC LIMIT 1
        """)
        self.id = self.cursor.fetchone()[0]

        self.id_list = [self.id] * len(self.subject)
        self.insert_subject = zip(self.subject, self.id_list)

        self.cursor.executemany("""
            INSERT INTO teacher_subjects(subject_name, teachers_id)
            VALUES (%s, %s)
        """, self.insert_subject)

        self.id_list = [self.id] * len(self.grade)
        self.insert_grade = zip(self.grade, self.id_list)

        self.cursor.executemany("""
            INSERT INTO teacher_grades(grade, teachers_id)
            VALUES (%s, %s)
        """, self.insert_grade)

        self.cursor.execute("""
            SELECT sy FROM school_years ORDER BY date_created DESC LIMIT 1
        """)
        self.sy = self.cursor.fetchone()[0]

        self.cursor.execute("""
            INSERT INTO teacher_schedule(school_year, teachers_id)
            VALUES ("%s", %s)
        """%(self.sy, self.id))

        self.connection.commit()
        self.connection.close()

    def insert_schoolyear(self, sy):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            INSERT INTO school_years(sy)
            VALUES ("%s")
        """%(sy))

        self.connection.commit()
        self.connection.close()

    def insert_room(self, name, lab, grade):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()
        self.grade = grade

        self.cursor.execute("""
            INSERT INTO rooms(room_name, laboratory)
            VALUES ("%s", "%s")
        """%(name, lab))

        self.cursor.execute("""
            SELECT id FROM rooms ORDER BY id DESC LIMIT 1
        """)
        self.id = self.cursor.fetchone()[0]

        self.id_list = [self.id] * len(self.grade)
        self.insert_grade = zip(self.grade, self.id_list)

        self.cursor.executemany("""
            INSERT INTO room_grades(grade, rooms_id)
            VALUES (%s, %s)
        """, self.insert_grade)

        self.cursor.execute("""
            SELECT sy FROM school_years ORDER BY date_created DESC LIMIT 1
        """)
        self.sy = self.cursor.fetchone()[0]

        self.cursor.execute("""
            INSERT INTO room_schedule(school_year, rooms_id)
            VALUES ("%s", %s)
        """%(self.sy, self.id))

        self.connection.commit()
        self.connection.close()

    def insert_section(self, grade, section):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            INSERT INTO sections(grade, section_name)
            VALUES ("%s", "%s")
        """%(grade, section))

        self.cursor.execute("""
            SELECT id FROM sections ORDER BY id DESC LIMIT 1
        """)
        self.id = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT sy FROM school_years ORDER BY date_created DESC LIMIT 1
        """)
        self.sy = self.cursor.fetchone()[0]

        self.cursor.execute("""
            INSERT INTO section_schedule(school_year, sections_id)
            VALUES ("%s", "%s")
        """%(self.sy, self.id))

        self.connection.commit()
        self.connection.close()

    def search_subjectAndDuration(self, grade):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            SELECT subject_name, duration FROM grade_subjects WHERE grades_id = "%s"
        """%(grade))

        return self.cursor.fetchall()

    def insert_schedule(self, grade, duration, subject):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.grade = grade
        self.duration = duration
        self.subject = subject

        self.cursor.execute("""
            SELECT id FROM sections ORDER BY id DESC LIMIT 1
        """)
        self.section_id = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT section_name FROM sections WHERE id = %s
        """%(self.section_id))
        self.section_name = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT sy FROM school_years ORDER BY date_created DESC LIMIT 1
        """)
        self.sy = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT id FROM teachers
            JOIN teacher_grades
                ON id = teacher_grades.teachers_id
            JOIN teacher_subjects
                ON id = teacher_subjects.teachers_id
            WHERE grade = "%s" AND subject_name = "%s" AND total_minutes >= %s
        """ % (self.grade, self.subject, self.duration * 5))
        self.id = self.cursor.fetchall()

        self.i = 0

        while self.i < len(self.id):
            self.cursor.execute("""
                SELECT TIME(time_out) FROM teacher_schedule WHERE teachers_id = %s ORDER BY time_out
            """%(self.id[self.i][0]))
            self.teacher_time = self.cursor.fetchall()

            self.j = 0

            while self.j < len(self.teacher_time):
                self.cursor.execute("""
                    SELECT time_out FROM teacher_schedule WHERE time_in BETWEEN TIME("%s") AND (TIME("%s") + INTERVAL %s MINUTE) - INTERVAL 1 MINUTE
                    AND teachers_id = %s AND subject_name IS NOT NULL AND school_year = "%s"
                """%(self.teacher_time[self.j][0], self.teacher_time[self.j][0], self.duration, self.id[self.i][0], self.sy))
                self.available_teacher = self.cursor.fetchone()

                if self.available_teacher is None:
                    self.cursor.execute("""
                        SELECT time_out FROM section_schedule WHERE time_in BETWEEN TIME("%s") AND(TIME("%s") + INTERVAL %s MINUTE) - INTERVAL 1 MINUTE
                        AND sections_id = %s AND subject_name IS NOT NULL AND school_year = "%s"
                    """%(self.teacher_time[self.j][0], self.teacher_time[self.j][0], self.duration, self.section_id, self.sy))
                    self.section_schedule = self.cursor.fetchone()

                    if self.section_schedule is None:
                        self.cursor.execute("""
                            INSERT INTO teacher_schedule(subject_name, section_name, time_in, time_out, school_year, teachers_id, sections_id)
                            VALUES ("%s", "%s", TIME("%s"), TIME("%s") + INTERVAL %s MINUTE, "%s", %s, %s)
                        """%(self.subject, self.section_name, self.teacher_time[self.j][0], self.teacher_time[self.j][0], self.duration, self.sy,
                        self.id[self.i][0], self.section_id))

                        self.cursor.execute("""
                            SELECT CONCAT_WS(" ", first_name, middle_name, last_name) FROM teachers WHERE id = %s
                        """%(self.id[self.i][0]))
                        self.subject_teacher = self.cursor.fetchone()[0]

                        self.cursor.execute("""
                            INSERT INTO section_schedule(subject_name, time_in, time_out, subject_teacher, school_year, sections_id, teachers_id)
                            VALUES ("%s", TIME("%s"), TIME("%s") + INTERVAL %s MINUTE, "%s", "%s", %s, %s)
                        """%(self.subject, self.teacher_time[self.j][0], self.teacher_time[self.j][0], self.duration, self.subject_teacher,
                             self.sy, self.section_id, self.id[self.i][0]))

                        self.cursor.execute("""
                            UPDATE teachers SET total_minutes = total_minutes - %s WHERE id = %s
                        """%(self.duration * 5, self.id[self.i][0]))

                        self.connection.commit()
                        self.connection.close()
                        return

                    else:
                        self.cursor.execute("""
                            SELECT time_out FROM section_schedule
                            WHERE sections_id = %s
                            ORDER BY TIME(time_out) DESC LIMIT 1
                        """%(self.section_id))
                        self.new_section_schedule = self.cursor.fetchone()[0]

                        self.cursor.execute("""
                            SELECT time_out FROM teacher_schedule WHERE time_in BETWEEN TIME("%s") AND (TIME("%s") + INTERVAL %s MINUTE) - INTERVAL 1 MINUTE
                            AND teachers_id = %s AND subject_name IS NOT NULL AND school_year = "%s"
                        """%(self.new_section_schedule, self.new_section_schedule, self.duration, self.id[self.i][0], self.sy))
                        self.new_teacher = self.cursor.fetchone()

                        if self.new_teacher is None:
                            self.cursor.execute("""
                                INSERT INTO teacher_schedule(subject_name, section_name, time_in, time_out, school_year, teachers_id, sections_id)
                                VALUES ("%s", "%s", TIME("%s"), TIME("%s") + INTERVAL %s MINUTE, "%s", %s, %s)
                            """%(self.subject, self.section_name, self.new_section_schedule, self.new_section_schedule, self.duration, self.sy,
                            self.id[self.i][0], self.section_id))

                            self.cursor.execute("""
                                SELECT CONCAT_WS(" ", first_name, middle_name, last_name) FROM teachers WHERE id = %s
                            """%(self.id[self.i][0]))
                            self.subject_teacher = self.cursor.fetchone()[0]

                            self.cursor.execute("""
                                INSERT INTO section_schedule(subject_name, time_in, time_out, subject_teacher, school_year, sections_id, teachers_id)
                                VALUES ("%s", TIME("%s"), TIME("%s") + INTERVAL %s MINUTE, "%s", "%s", %s, %s)
                            """%(self.subject, self.new_section_schedule, self.new_section_schedule, self.duration, self.subject_teacher,
                            self.sy, self.section_id, self.id[self.i][0]))

                            self.cursor.execute("""
                                UPDATE teachers SET total_minutes = total_minutes - %s WHERE id = %s
                            """%(self.duration * 5, self.id[self.i][0]))

                            self.connection.commit()
                            self.connection.close()
                            return

                    self.j += 1
                    continue

                self.j += 1

            self.i += 1


    def test(self, grade, duration, subject):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.grade = grade
        self.duration = duration
        self.subject = subject

        self.cursor.execute("""
            SELECT id FROM sections ORDER BY id DESC LIMIT 1
        """)
        self.section_id = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT sy FROM school_years ORDER BY date_created DESC LIMIT 1
        """)
        self.sy = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT id FROM teachers
            JOIN teacher_grades
                ON id = teacher_grades.teachers_id
            JOIN teacher_subjects
                ON id = teacher_subjects.teachers_id
            JOIN teacher_schedule
                ON id = teacher_schedule.teachers_id
            WHERE grade = "%s" AND teacher_subjects.subject_name = "%s" AND total_minutes >= %s
            GROUP BY id
        """%(self.grade, self.subject, self.duration))
        self.teachers = self.cursor.fetchall()

        self.cursor.execute("""
            SELECT time_out FROM section_schedule ORDER BY time_out WHERE sections_id = %s
        """%(self.section_id))
        self.section_timeout = self.cursor.fetchall()

        self.found = False
        self.i = 0
        while self.i < len(self.section_timeout) and not self.found:
            self.cursor.execute("""
                SELECT time_out FROM section_schedule WHERE time_in BETWEEN TIME("%s")
                AND (TIME("%s") + INTERVAL %s MINUTE) - INTERVAL 1 MINUTE AND subject_name IS NOT NULL
                AND sections_id = %s
            """%(self.section_timeout[self.i][0], self.section_timeout[self.i][0], self.duration, self.section_id))
            self.section_freetime = self.cursor.fetchone()

            if self.section_freetime is None:
                self.cursor.execute("""
                    SELECT id FROM teachers
                    JOIN teacher_grades
                        ON id = teacher_grades.teachers_id
                    JOIN teacher_subjects
                        ON id = teacher_subjects.teachers_id
                    JOIN teacher_schedule
                        ON id = teacher_schedule.teachers_id
                    WHERE grade = "%s" AND teacher_subjects.subject_name = "%s" AND total_minutes >= %s
                    AND time_in BETWEEN TIME("%s") AND (TIME("%s") + INTERVAL %s MINUTE) - INTERVAL 1 MINUTE
                    GROUP BY id
                """%(self.grade, self.subject, self.duration, self.section_timeout[self.i][0], self.section_timeout[self.i][0], self.duration))
                self.notAvailable_teachers = self.cursor.fetchall()

                self.result_teacher = tuple(set(self.teachers) - set(self.notAvailable_teachers))

                self.cursor.execute("""
                    SELECT rooms_id FROM section_schedule WHERE sections_id = "%s"
                """%(self.section_id))
                self.available_room = self.cursor.fetchone()

                if self.available_room is None:

                    if self.subject.lower().startswith("computer"):
                        self.cursor.execute("""
                            SELECT id FROM rooms
                            JOIN room_grades
                                ON id = room_grades.rooms_id
                            WHERE laboratory = "Yes" AND grade = "%s"
                        """%(self.grade))
                        self.available_room = self.cursor.fetchone()[0]

                    else:
                        self.cursor.execute("""
                            SELECT id FROM rooms
                            JOIN room_grades
                                ON id = room_grades.rooms_id
                            WHERE laboratory = "No" AND grade = "%s"
                        """%(self.grade))
                        self.available_room = self.cursor.fetchone()[0]

                self.cursor.execute("""
                    INSERT INTO section_schedule(subject_name, time_in, time_out, school_year, rooms_id, sections_id, teachers_id)
                    VALUES ("%s", TIME("%s), TIME("%s") + INTERVAL %s MINUTE, "%s", %s, %s, %s)
                """%(self.subject, self.section_timeout[self.i][0], self.section_timeout[self.i][0], self.duration, self.sy, self.available_room,
                     self.section_id, self.result_teacher[0]))

                self.cursor.execute("""
                    INSERT INTO teacher_schedule(subject_name, time_in, time_out, school_year, teachers_id, rooms_id, sections_id)
                    VALUES ("%s", TIME("%s"), TIME("%s") + INTERVAL %s MINUTE, "%s", %s, %s, %s)
                """%(self.subject, self.section_timeout[self.i][0], self.section_timeout[self.i][0], self.duration, self.sy,
                     self.result_teacher, self.available_room, self.section_id))

                self.connection.commit()
                self.connection.close()
                self.found = True

            else:
                self.i += 1

    def testing(self):
        self.connection = pymysql.connect(host="localhost", user="root", password="", db="scheduling_system")
        self.cursor = self.connection.cursor()

        self.cursor.executemany("""
            SELECT teachers_id FROM teacher_schedule
            WHERE time_in BETWEEN TIME(%s) AND (TIME(%s) + INTERVAL %s MINUTE) - INTERVAL 1 MINUTE
            AND teachers_id = %s;
        """, [("8:00", "8:00", 60, 2), ("8:00", "8:00", 60, 1)])

        return self.cursor.fetchone()