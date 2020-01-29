#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Jan 13, 2020 11:19:03 AM CST  platform: Windows NT

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

import AddTeacher_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TeachersGUI (root)
    AddTeacher_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = TeachersGUI (w)
    AddTeacher_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class TeachersGUI:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        window_width = 1154
        window_height = 414
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        top.resizable(False, False)
        top.title("Scheduling System")
        top.configure(background="#d9d9d9")

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.0, rely=0.169, relwidth=0.0)

        self.firstName_lbl = tk.Label(top)
        self.firstName_lbl.place(relx=0.0, rely=0.217, height=41, width=124)
        self.firstName_lbl.configure(background="#d9d9d9")
        self.firstName_lbl.configure(disabledforeground="#a3a3a3")
        self.firstName_lbl.configure(font=font9)
        self.firstName_lbl.configure(foreground="#000000")
        self.firstName_lbl.configure(text='''First Name:''')

        self.firstName_var = tk.StringVar()
        self.firstName_entry = tk.Entry(top)
        self.firstName_entry.place(relx=0.147, rely=0.217, height=40
                , relwidth=0.159)
        self.firstName_entry.configure(background="white")
        self.firstName_entry.configure(disabledforeground="#a3a3a3")
        self.firstName_entry.configure(font=font10)
        self.firstName_entry.configure(foreground="#000000")
        self.firstName_entry.configure(insertbackground="black")
        self.firstName_entry.configure(textvariable=self.firstName_var)

        self.back_btn = tk.Button(top)
        self.back_btn.place(relx=0.009, rely=0.024, height=44, width=157)
        self.back_btn.configure(activebackground="#ffffff")
        self.back_btn.configure(activeforeground="#000000")
        self.back_btn.configure(background="#ffffff")
        self.back_btn.configure(disabledforeground="#a3a3a3")
        self.back_btn.configure(font=font10)
        self.back_btn.configure(foreground="#000000")
        self.back_btn.configure(highlightbackground="#d9d9d9")
        self.back_btn.configure(highlightcolor="black")
        self.back_btn.configure(pady="0")
        self.back_btn.configure(relief="ridge")
        self.back_btn.configure(text='''Back''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.0, rely=0.169, relwidth=1.008)

        self.middleName_lbl = tk.Label(top)
        self.middleName_lbl.place(relx=0.009, rely=0.386, height=41, width=124)
        self.middleName_lbl.configure(activebackground="#f9f9f9")
        self.middleName_lbl.configure(activeforeground="black")
        self.middleName_lbl.configure(background="#d9d9d9")
        self.middleName_lbl.configure(disabledforeground="#a3a3a3")
        self.middleName_lbl.configure(font="-family {Segoe UI} -size 14")
        self.middleName_lbl.configure(foreground="#000000")
        self.middleName_lbl.configure(highlightbackground="#d9d9d9")
        self.middleName_lbl.configure(highlightcolor="black")
        self.middleName_lbl.configure(text='''Middle Name:''')

        self.middleName_var = tk.StringVar()
        self.middleName_entry = tk.Entry(top)
        self.middleName_entry.place(relx=0.147, rely=0.386, height=40
                , relwidth=0.159)
        self.middleName_entry.configure(background="white")
        self.middleName_entry.configure(disabledforeground="#a3a3a3")
        self.middleName_entry.configure(font=font10)
        self.middleName_entry.configure(foreground="#000000")
        self.middleName_entry.configure(highlightbackground="#d9d9d9")
        self.middleName_entry.configure(highlightcolor="black")
        self.middleName_entry.configure(insertbackground="black")
        self.middleName_entry.configure(selectbackground="#c4c4c4")
        self.middleName_entry.configure(selectforeground="black")
        self.middleName_entry.configure(textvariable=self.middleName_var)

        self.lastName_lbl = tk.Label(top)
        self.lastName_lbl.place(relx=0.0, rely=0.556, height=41, width=124)
        self.lastName_lbl.configure(activebackground="#f9f9f9")
        self.lastName_lbl.configure(activeforeground="black")
        self.lastName_lbl.configure(background="#d9d9d9")
        self.lastName_lbl.configure(disabledforeground="#a3a3a3")
        self.lastName_lbl.configure(font="-family {Segoe UI} -size 14")
        self.lastName_lbl.configure(foreground="#000000")
        self.lastName_lbl.configure(highlightbackground="#d9d9d9")
        self.lastName_lbl.configure(highlightcolor="black")
        self.lastName_lbl.configure(text='''Last Name:''')

        self.lastName_var = tk.StringVar()
        self.lastName_entry = tk.Entry(top)
        self.lastName_entry.place(relx=0.147, rely=0.556, height=40
                , relwidth=0.159)
        self.lastName_entry.configure(background="white")
        self.lastName_entry.configure(disabledforeground="#a3a3a3")
        self.lastName_entry.configure(font="-family {Segoe UI} -size 12")
        self.lastName_entry.configure(foreground="#000000")
        self.lastName_entry.configure(highlightbackground="#d9d9d9")
        self.lastName_entry.configure(highlightcolor="black")
        self.lastName_entry.configure(insertbackground="black")
        self.lastName_entry.configure(selectbackground="#c4c4c4")
        self.lastName_entry.configure(selectforeground="black")
        self.lastName_entry.configure(textvariable=self.lastName_var)

        self.totalHours_lbl = tk.Label(top)
        self.totalHours_lbl.place(relx=0.004, rely=0.725, height=41, width=124)
        self.totalHours_lbl.configure(activebackground="#f9f9f9")
        self.totalHours_lbl.configure(activeforeground="black")
        self.totalHours_lbl.configure(background="#d9d9d9")
        self.totalHours_lbl.configure(disabledforeground="#a3a3a3")
        self.totalHours_lbl.configure(font="-family {Segoe UI} -size 14")
        self.totalHours_lbl.configure(foreground="#000000")
        self.totalHours_lbl.configure(highlightbackground="#d9d9d9")
        self.totalHours_lbl.configure(highlightcolor="black")
        self.totalHours_lbl.configure(text='''Total Hours:''')

        self.totalHours_var = tk.IntVar()
        self.totalHours_entry = tk.Entry(top)
        self.totalHours_entry.place(relx=0.147, rely=0.725, height=40
                , relwidth=0.159)
        self.totalHours_entry.configure(background="white")
        self.totalHours_entry.configure(disabledforeground="#a3a3a3")
        self.totalHours_entry.configure(font=font10)
        self.totalHours_entry.configure(foreground="#000000")
        self.totalHours_entry.configure(highlightbackground="#d9d9d9")
        self.totalHours_entry.configure(highlightcolor="black")
        self.totalHours_entry.configure(insertbackground="black")
        self.totalHours_entry.configure(selectbackground="#c4c4c4")
        self.totalHours_entry.configure(selectforeground="black")
        self.totalHours_entry.configure(textvariable=self.totalHours_var)

        self.grade_lbl = tk.Label(top)
        self.grade_lbl.place(relx=0.312, rely=0.217, height=41, width=124)
        self.grade_lbl.configure(activebackground="#f9f9f9")
        self.grade_lbl.configure(activeforeground="black")
        self.grade_lbl.configure(background="#d9d9d9")
        self.grade_lbl.configure(disabledforeground="#a3a3a3")
        self.grade_lbl.configure(font="-family {Segoe UI} -size 14")
        self.grade_lbl.configure(foreground="#000000")
        self.grade_lbl.configure(highlightbackground="#d9d9d9")
        self.grade_lbl.configure(highlightcolor="black")
        self.grade_lbl.configure(text='''Grade:''')

        self.grade_var = tk.StringVar()
        self.grade_entry = tk.Entry(top)
        self.grade_entry.place(relx=0.407, rely=0.217, height=40, relwidth=0.159)
        self.grade_entry.configure(background="white")
        self.grade_entry.configure(disabledforeground="#a3a3a3")
        self.grade_entry.configure(font="-family {Segoe UI} -size 12")
        self.grade_entry.configure(foreground="#000000")
        self.grade_entry.configure(highlightbackground="#d9d9d9")
        self.grade_entry.configure(highlightcolor="black")
        self.grade_entry.configure(insertbackground="black")
        self.grade_entry.configure(selectbackground="#c4c4c4")
        self.grade_entry.configure(selectforeground="black")
        self.grade_entry.configure(textvariable=self.grade_var)

        self.addGrade_btn = tk.Button(top)
        self.addGrade_btn.place(relx=0.581, rely=0.229, height=34, width=67)
        self.addGrade_btn.configure(activebackground="#ffffff")
        self.addGrade_btn.configure(activeforeground="#000000")
        self.addGrade_btn.configure(background="#ffffff")
        self.addGrade_btn.configure(disabledforeground="#a3a3a3")
        self.addGrade_btn.configure(foreground="#000000")
        self.addGrade_btn.configure(highlightbackground="#d9d9d9")
        self.addGrade_btn.configure(highlightcolor="black")
        self.addGrade_btn.configure(pady="0")
        self.addGrade_btn.configure(relief="ridge")
        self.addGrade_btn.configure(text='''Add''')

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.grade_treeview = ScrolledTreeView(top, columns=("grade"), show="headings")
        self.grade_treeview.place(relx=0.338, rely=0.338, relheight=0.476
                , relwidth=0.303)
        self.grade_treeview.heading(0, text="Grade")
        self.grade_treeview.column(0, anchor="center")

        self.subject_lbl = tk.Label(top)
        self.subject_lbl.place(relx=0.65, rely=0.217, height=41, width=124)
        self.subject_lbl.configure(activebackground="#f9f9f9")
        self.subject_lbl.configure(activeforeground="black")
        self.subject_lbl.configure(background="#d9d9d9")
        self.subject_lbl.configure(disabledforeground="#a3a3a3")
        self.subject_lbl.configure(font="-family {Segoe UI} -size 14")
        self.subject_lbl.configure(foreground="#000000")
        self.subject_lbl.configure(highlightbackground="#d9d9d9")
        self.subject_lbl.configure(highlightcolor="black")
        self.subject_lbl.configure(text='''Subject:''')

        self.subject_var = tk.StringVar()
        self.subject_box = ttk.Combobox(top)
        self.subject_box.place(relx=0.745, rely=0.217, height=40
                , relwidth=0.159)
        self.subject_box.configure(font=font11)
        self.subject_box.configure(foreground="#000000")
        self.subject_box.configure(textvariable=self.subject_var)
        self.subject_box.configure(state="readonly")

        self.addSubject_btn = tk.Button(top)
        self.addSubject_btn.place(relx=0.919, rely=0.229, height=34, width=67)
        self.addSubject_btn.configure(activebackground="#ffffff")
        self.addSubject_btn.configure(activeforeground="#000000")
        self.addSubject_btn.configure(background="#ffffff")
        self.addSubject_btn.configure(disabledforeground="#a3a3a3")
        self.addSubject_btn.configure(foreground="#000000")
        self.addSubject_btn.configure(highlightbackground="#d9d9d9")
        self.addSubject_btn.configure(highlightcolor="black")
        self.addSubject_btn.configure(pady="0")
        self.addSubject_btn.configure(relief="ridge")
        self.addSubject_btn.configure(text='''Add''')

        self.subject_treeview = ScrolledTreeView(top, columns=("subject"), show="headings")
        self.subject_treeview.place(relx=0.676, rely=0.338, relheight=0.476
                , relwidth=0.303)
        self.subject_treeview.heading(0, text="Subject")
        self.subject_treeview.column(0, anchor="center")

        self.addTeacher_btn = tk.Button(top)
        self.addTeacher_btn.place(relx=0.815, rely=0.845, height=54, width=187)
        self.addTeacher_btn.configure(activebackground="#1aff12")
        self.addTeacher_btn.configure(activeforeground="#ffffff")
        self.addTeacher_btn.configure(background="#1aff12")
        self.addTeacher_btn.configure(disabledforeground="#a3a3a3")
        self.addTeacher_btn.configure(font=font13)
        self.addTeacher_btn.configure(foreground="#ffffff")
        self.addTeacher_btn.configure(highlightbackground="#d9d9d9")
        self.addTeacher_btn.configure(highlightcolor="black")
        self.addTeacher_btn.configure(pady="0")
        self.addTeacher_btn.configure(relief="ridge")
        self.addTeacher_btn.configure(text='''ADD TEACHER''')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()




