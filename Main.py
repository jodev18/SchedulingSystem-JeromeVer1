from Homepage import *
from Teachers import *
from Rooms import *
from Subjects import *
from SchoolYear import *
from TeacherSchedule import *
from tkinter import filedialog
import csv, time

class Main:
    def __init__(self, master):
        self.master = master
        self.main_window = Homepage(self.master)
        self.db = Query()

        self.main_window.teachers_btn.configure(command=self.teachers_function)
        self.main_window.rooms_btn.configure(command=self.rooms_function)
        self.main_window.subject_btn.configure(command=self.subjectAndBreaktime_function)
        self.main_window.schoolYear_btn.configure(command=self.schoolyear_function)
        self.main_window.teacherSchedule_btn.configure(command=self.teacherSchedule_function)
        self.main_window.selectFile_btn.configure(command=self.selectFile_function)

    def selectFile_function(self):
        self.file = filedialog.askopenfilename(filetypes=[("Csv files", ".csv"), ("Excel files", ".xlsx")])

        with open("{}".format(self.file), "r") as file:
            self.reader = csv.reader(file)
            next(self.reader)

            self.start_time = time.time()

            for line in self.reader:
                self.db.insert_section(line[0], line[1])

                self.subjects = self.db.search_subjectAndDuration(line[0])
                print(self.subjects)
                for i in range(len(self.subjects)):
                    self.a = self.db.insert_schedule(line[0], self.subjects[i][1], self.subjects[i][0])
                    print(self.a)

            print("----- {} seconds -----".format(time.time() - self.start_time))

            messagebox.showinfo("", "Success")

    def teachers_function(self):
        self.teachers_window = tk.Toplevel()
        self.teachers = Teachers(self.teachers_window, self.master)
        self.master.withdraw()

    def rooms_function(self):
        self.rooms_window = tk.Toplevel()
        self.rooms = Rooms(self.rooms_window, self.master)
        self.master.withdraw()

    def subjectAndBreaktime_function(self):
        self.subject_window = tk.Toplevel()
        self.subjects = Subjects(self.subject_window, self.master)
        self.master.withdraw()

    def schoolyear_function(self):
        self.schoolyear_window = tk.Toplevel()
        self.schoolyear = SchoolYear(self.schoolyear_window, self.master)
        self.master.withdraw()

    def teacherSchedule_function(self):
        self.teacherSchedule_window = tk.Toplevel()
        self.teacherSchedule = TeacherSchedule(self.teacherSchedule_window, self.master)
        self.master.withdraw()

if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    root.mainloop()