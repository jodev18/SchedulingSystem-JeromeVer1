from RoomsGUI import *
from tkinter import messagebox
from Query import *

class Rooms:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.grade_list = []

        self.rooms = RoomsGUI(self.master)
        self.db = Query()

        self.rooms.back_btn.configure(command=self.back_function)
        self.rooms.add_btn.configure(command=self.add_grade)
        self.rooms.addRoom_btn.configure(command=self.addRoom_function)

    def add_grade(self):
        self.get_grade = self.rooms.grade_var.get()

        if self.get_grade == "":
            return messagebox.showerror("Error", "Grade field cannot be empty")

        self.grade_list.append(self.get_grade)
        self.rooms.grade_treeview.insert("", "end", values=(self.get_grade))
        self.rooms.grade_var.set("")

    def addRoom_function(self):
        self.get_roomname = self.rooms.roomName_var.get()
        self.get_lab = self.rooms.lab_var.get()

        if self.get_roomname == "":
            return messagebox.showerror("Error", "Room name field cannot be empty")

        if self.get_lab == 0:
            self.get_lab = "No"

        else:
            self.get_lab = "Yes"

        if self.grade_list == []:
            return messagebox.showerror("Error", "Grade is empty")

        self.reply = messagebox.askquestion("Add room", "Are you sure?")

        if self.reply.lower() == "yes":
            self.db.insert_room(self.get_roomname, self.get_lab, self.grade_list)
            messagebox.showinfo("", "Success")
            self.rooms.roomName_var.set("")
            self.rooms.lab_var.set(0)
            self.rooms.grade_var.set("")
            self.rooms.grade_treeview.delete(*self.rooms.grade_treeview.get_children())
            self.grade_list = []

    def back_function(self):
        self.master.destroy()
        self.main_window.deiconify()