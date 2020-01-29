from TeacherScheduleGUI import *

class TeacherSchedule:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.teacherSchedule = TeacherScheduleGUI(self.master)

        self.teacherSchedule.back_btn.configure(command=self.back_function)

    def back_function(self):
        self.master.destroy()
        self.main_window.deiconify()