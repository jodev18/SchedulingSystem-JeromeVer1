from SchoolYearGUI import *
from Query import *
from tkinter import messagebox

class SchoolYear:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window

        self.schoolYear = SchoolYearGUI(self.master)
        self.db = Query()

        self.schoolYear.back_btn.configure(command=self.back_function)
        self.schoolYear.addSY_btn.configure(command=self.addSchoolYear_function)

    def addSchoolYear_function(self):
        self.get_sy = self.schoolYear.newSY_var.get()

        if self.get_sy == "":
            return messagebox.showerror("Error", "School year field cannot be empty")

        self.reply = messagebox.askquestion("Add school year", "Are you sure?")

        if self.reply.lower() == "yes":
            self.db.insert_schoolyear(self.get_sy)
            messagebox.showinfo("", "Success")
            self.schoolYear.newSY_var.set("")

    def back_function(self):
        self.master.destroy()
        self.main_window.deiconify()