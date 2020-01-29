#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Jan 13, 2020 05:14:51 PM CST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import AddSchoolYear_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = SchoolYearGUI (root)
    AddSchoolYear_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = SchoolYearGUI (w)
    AddSchoolYear_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class SchoolYearGUI:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        window_width = 740
        window_height = 483
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        top.resizable(False, False)
        top.title("Scheduling System")
        top.configure(background="#d9d9d9")

        self.back_btn = tk.Button(top)
        self.back_btn.place(relx=0.014, rely=0.021, height=44, width=157)
        self.back_btn.configure(activebackground="#ffffff")
        self.back_btn.configure(activeforeground="#000000")
        self.back_btn.configure(background="#ffffff")
        self.back_btn.configure(disabledforeground="#a3a3a3")
        self.back_btn.configure(font=font9)
        self.back_btn.configure(foreground="#000000")
        self.back_btn.configure(highlightbackground="#d9d9d9")
        self.back_btn.configure(highlightcolor="black")
        self.back_btn.configure(pady="0")
        self.back_btn.configure(relief="ridge")
        self.back_btn.configure(text='''Back''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.0, rely=0.145, relwidth=1.014)

        self.newSY_lbl = tk.Label(top)
        self.newSY_lbl.place(relx=0.243, rely=0.435, height=21, width=164)
        self.newSY_lbl.configure(background="#d9d9d9")
        self.newSY_lbl.configure(disabledforeground="#a3a3a3")
        self.newSY_lbl.configure(font=font10)
        self.newSY_lbl.configure(foreground="#000000")
        self.newSY_lbl.configure(text='''New School Year:''')

        self.newSY_var = tk.StringVar()
        self.newSY_entry = tk.Entry(top)
        self.newSY_entry.place(relx=0.5, rely=0.414,height=40, relwidth=0.222)
        self.newSY_entry.configure(background="white")
        self.newSY_entry.configure(disabledforeground="#a3a3a3")
        self.newSY_entry.configure(font=font9)
        self.newSY_entry.configure(foreground="#000000")
        self.newSY_entry.configure(insertbackground="black")
        self.newSY_entry.configure(textvariable=self.newSY_var)

        self.addSY_btn = tk.Button(top)
        self.addSY_btn.place(relx=0.338, rely=0.58, height=44, width=217)
        self.addSY_btn.configure(activebackground="#1aff12")
        self.addSY_btn.configure(activeforeground="#FFFFFF")
        self.addSY_btn.configure(background="#1aff12")
        self.addSY_btn.configure(disabledforeground="#a3a3a3")
        self.addSY_btn.configure(font=font12)
        self.addSY_btn.configure(foreground="#FFFFFF")
        self.addSY_btn.configure(highlightbackground="#d9d9d9")
        self.addSY_btn.configure(highlightcolor="black")
        self.addSY_btn.configure(pady="0")
        self.addSY_btn.configure(relief="ridge")
        self.addSY_btn.configure(text='''ADD SCHOOL YEAR''')

if __name__ == '__main__':
    vp_start_gui()




