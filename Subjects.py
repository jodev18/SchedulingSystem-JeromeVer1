from SubjectsGUI import *
from tkinter import messagebox
from datetime import *
from Query import *

class Subjects:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.subject_list = []

        self.subjects = SubjectsGUI(self.master)
        self.db = Query()

        self.subjects.back_btn.configure(command=self.back_function)
        self.subjects.addSubject_btn.configure(command=self.add_subject)
        self.subjects.submit_btn.configure(command=self.submit_function)

    def submit_function(self):
        self.get_grade = self.subjects.grade_var.get()

        if self.get_grade == "":
            return messagebox.showerror("Error", "Grade field must not be empty")

        if self.subject_list == []:
            return messagebox.showerror("Error", "No subject")

        self.reply = messagebox.askquestion("Submit", "Are you sure?")

        if self.reply.lower() == "yes":
            self.db.insert_subject(self.get_grade, self.subject_list)
            messagebox.showinfo("", "Success")
            self.subjects.grade_var.set("")
            self.subjects.subject_treeview.delete(*self.subjects.subject_treeview.get_children())
            self.subject_list = []

    def add_subject(self):
        self.get_subject = self.subjects.subject_var.get()
        self.get_duration = self.subjects.duration_var.get()

        if self.get_subject == "" or self.get_duration == "":
            return messagebox.showerror("Error", "Field cannot be blank")

        if self.get_duration.isalpha():
            return messagebox.showerror("Error", "Duration must be a number of minutes")

        self.subject_list.append([self.get_subject, self.get_duration])
        self.subjects.subject_treeview.insert("", "end", values=(self.get_subject, self.get_duration))

        self.subjects.subject_var.set("")
        self.subjects.duration_var.set("")

    def back_function(self):
        self.master.destroy()
        self.main_window.deiconify()