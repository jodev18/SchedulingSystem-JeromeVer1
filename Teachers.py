from TeachersGUI import *
from tkinter import messagebox
from Query import *

class Teachers:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.grade_list = []
        self.subject_list = []

        self.teachers = TeachersGUI(self.master)
        self.db = Query()

        self.teachers.back_btn.configure(command=self.back_function)
        self.teachers.addGrade_btn.configure(command=self.add_grade)
        self.teachers.addSubject_btn.configure(command=self.add_subject)
        self.teachers.subject_box.bind("<Button-1>", self.subjectBox_function)
        self.teachers.addTeacher_btn.configure(command=self.add_teacher)

    def add_teacher(self):
        self.get_firstname = self.teachers.firstName_var.get()
        self.get_middlename = self.teachers.middleName_var.get()
        self.get_lastname = self.teachers.lastName_var.get()
        self.get_minutes = self.teachers.totalHours_var.get()
        self.get_minutes = self.get_minutes * 60

        self.t = [[self.get_firstname, self.get_middlename, self.get_lastname, self.get_minutes]]

        if self.get_firstname == "":
            return messagebox.showerror("Error", "First name field cannot be empty")

        if self.get_middlename == "":
            return messagebox.showerror("Error", "Middle name field cannot be empty")

        if self.get_lastname == "":
            return messagebox.showerror("Error", "Last name field cannot be empty")

        if self.get_minutes == 0:
            return messagebox.showerror("Error", "Total hours field cannot be 0")

        if self.grade_list == []:
            return messagebox.showerror("Error", "Grade is empty")

        if self.subject_list == []:
            return messagebox.showerror("Error", "Subject is empty")

        self.reply = messagebox.askquestion("Add teacher", "Are you sure?")

        if self.reply.lower() == "yes":
            self.db.insert_teacher(self.t, self.subject_list, self.grade_list)
            messagebox.showinfo("", "Success")
            self.teachers.firstName_var.set("")
            self.teachers.middleName_var.set("")
            self.teachers.lastName_var.set("")
            self.teachers.totalHours_var.set(0)
            self.teachers.grade_var.set("")
            self.teachers.subject_var.set("")
            self.teachers.grade_treeview.delete(*self.teachers.grade_treeview.get_children())
            self.teachers.subject_treeview.delete(*self.teachers.subject_treeview.get_children())
            self.grade_list = []
            self.subject_list = []

    def add_grade(self):
        self.get_grade = self.teachers.grade_var.get()

        if self.get_grade == "":
            return messagebox.showerror("Error", "Grade field cannot be empty")

        self.grade_list.append(self.get_grade)
        self.teachers.grade_treeview.insert("", "end", values=(self.get_grade))
        self.teachers.grade_var.set("")

    def subjectBox_function(self, event):
        try:
            self.subjects = []

            for i in range(len(self.grade_list)):
                self.fetch_subjects = self.db.search_subjects(self.grade_list[i])

                for j in range(len(self.fetch_subjects)):
                    self.subjects.append(self.fetch_subjects[j][0])

            print(self.fetch_subjects)
            print(self.subjects)

            self.teachers.subject_box.configure(values=list(self.subjects))

        except:
            messagebox.showerror("Error", "Add grade first")

    def add_subject(self):
        self.get_subject = self.teachers.subject_var.get()

        if self.get_subject == "":
            return messagebox.showerror("Error", "Subject field cannot be empty")

        self.subject_list.append(self.get_subject)
        self.teachers.subject_treeview.insert("", "end", values=(self.get_subject))
        self.teachers.subject_var.set("")

    def back_function(self):
        self.master.destroy()
        self.main_window.deiconify()