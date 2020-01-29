#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Jan 18, 2020 06:24:51 PM CST  platform: Windows NT

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

import TeacherSchedule_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TeacherScheduleGUI (root)
    TeacherSchedule_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = TeacherScheduleGUI (w)
    TeacherSchedule_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class TeacherScheduleGUI:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        window_width = 1200
        window_height = 651
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        top.resizable(False, False)
        top.title("Scheduling System")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.back_btn = tk.Button(top)
        self.back_btn.place(relx=0.008, rely=0.015, height=44, width=157)
        self.back_btn.configure(activebackground="#ffffff")
        self.back_btn.configure(activeforeground="#000000")
        self.back_btn.configure(background="#ffffff")
        self.back_btn.configure(disabledforeground="#a3a3a3")
        self.back_btn.configure(font="-family {Segoe UI} -size 12")
        self.back_btn.configure(foreground="#000000")
        self.back_btn.configure(highlightbackground="#d9d9d9")
        self.back_btn.configure(highlightcolor="black")
        self.back_btn.configure(pady="0")
        self.back_btn.configure(relief="ridge")
        self.back_btn.configure(text='''Back''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=-0.008, rely=0.108, relwidth=1.008)

        self.firstName_lbl = tk.Label(top)
        self.firstName_lbl.place(relx=0.004, rely=0.261, height=21, width=100)
        self.firstName_lbl.configure(activebackground="#f9f9f9")
        self.firstName_lbl.configure(activeforeground="black")
        self.firstName_lbl.configure(background="#d9d9d9")
        self.firstName_lbl.configure(disabledforeground="#a3a3a3")
        self.firstName_lbl.configure(font="-family {Segoe UI} -size 14")
        self.firstName_lbl.configure(foreground="#000000")
        self.firstName_lbl.configure(highlightbackground="#d9d9d9")
        self.firstName_lbl.configure(highlightcolor="black")
        self.firstName_lbl.configure(text='''First Name:''')

        self.firstName_var = tk.StringVar()
        self.firstName_entry = tk.Entry(top)
        self.firstName_entry.place(relx=0.133, rely=0.246, height=40
                , relwidth=0.137)
        self.firstName_entry.configure(background="white")
        self.firstName_entry.configure(disabledforeground="#a3a3a3")
        self.firstName_entry.configure(font="-family {Segoe UI} -size 12")
        self.firstName_entry.configure(foreground="#000000")
        self.firstName_entry.configure(highlightbackground="#d9d9d9")
        self.firstName_entry.configure(highlightcolor="black")
        self.firstName_entry.configure(insertbackground="black")
        self.firstName_entry.configure(selectbackground="#c4c4c4")
        self.firstName_entry.configure(selectforeground="black")
        self.firstName_entry.configure(textvariable=self.firstName_var)

        self.middleName_lbl = tk.Label(top)
        self.middleName_lbl.place(relx=0.004, rely=0.384, height=21, width=120)
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
        self.middleName_entry.place(relx=0.133, rely=0.369, height=40
                , relwidth=0.137)
        self.middleName_entry.configure(background="white")
        self.middleName_entry.configure(disabledforeground="#a3a3a3")
        self.middleName_entry.configure(font="-family {Segoe UI} -size 12")
        self.middleName_entry.configure(foreground="#000000")
        self.middleName_entry.configure(highlightbackground="#d9d9d9")
        self.middleName_entry.configure(highlightcolor="black")
        self.middleName_entry.configure(insertbackground="black")
        self.middleName_entry.configure(selectbackground="#c4c4c4")
        self.middleName_entry.configure(selectforeground="black")
        self.middleName_entry.configure(textvariable=self.middleName_var)

        self.lastName_lbl = tk.Label(top)
        self.lastName_lbl.place(relx=0.008, rely=0.507, height=21, width=90)
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
        self.lastName_entry.place(relx=0.133, rely=0.492, height=40
                , relwidth=0.137)
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

        self.search_btn = tk.Button(top)
        self.search_btn.place(relx=0.058, rely=0.783, height=44, width=157)
        self.search_btn.configure(activebackground="#ffffff")
        self.search_btn.configure(activeforeground="#000000")
        self.search_btn.configure(background="#ffffff")
        self.search_btn.configure(disabledforeground="#a3a3a3")
        self.search_btn.configure(font="-family {Segoe UI} -size 12")
        self.search_btn.configure(foreground="#000000")
        self.search_btn.configure(highlightbackground="#d9d9d9")
        self.search_btn.configure(highlightcolor="black")
        self.search_btn.configure(pady="0")
        self.search_btn.configure(relief="ridge")
        self.search_btn.configure(text='''Search''')

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.teachers_treeview = ScrolledTreeView(top, columns=("firstname", "middlename", "lastname", "id"), show="headings")
        self.teachers_treeview.place(relx=0.317, rely=0.186, relheight=0.195
                , relwidth=0.642)
        self.teachers_heading = ["First Name", "Middle Name", "Last Name", "ID"]
        for i in range(len(self.teachers_heading)):
            self.teachers_treeview.heading(i, text="{}".format(self.teachers_heading[i]))
            self.teachers_treeview.column(i, anchor="center", width=50)

        self.selectTeacher_btn = tk.Button(top)
        self.selectTeacher_btn.place(relx=0.317, rely=0.399, height=44
                , width=157)
        self.selectTeacher_btn.configure(activebackground="#ffffff")
        self.selectTeacher_btn.configure(activeforeground="#000000")
        self.selectTeacher_btn.configure(background="#ffffff")
        self.selectTeacher_btn.configure(disabledforeground="#a3a3a3")
        self.selectTeacher_btn.configure(font="-family {Segoe UI} -size 12")
        self.selectTeacher_btn.configure(foreground="#000000")
        self.selectTeacher_btn.configure(highlightbackground="#d9d9d9")
        self.selectTeacher_btn.configure(highlightcolor="black")
        self.selectTeacher_btn.configure(pady="0")
        self.selectTeacher_btn.configure(relief="ridge")
        self.selectTeacher_btn.configure(text='''Select Teacher''')

        self.schedule_lbl = tk.Label(top)
        self.schedule_lbl.place(relx=0.313, rely=0.522, height=41, width=104)
        self.schedule_lbl.configure(activebackground="#f9f9f9")
        self.schedule_lbl.configure(activeforeground="black")
        self.schedule_lbl.configure(background="#d9d9d9")
        self.schedule_lbl.configure(disabledforeground="#a3a3a3")
        self.schedule_lbl.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.schedule_lbl.configure(foreground="#000000")
        self.schedule_lbl.configure(highlightbackground="#d9d9d9")
        self.schedule_lbl.configure(highlightcolor="black")
        self.schedule_lbl.configure(text='''SCHEDULE''')

        self.schedule_treeview = ScrolledTreeView(top, show="headings", columns=("gradeAndSection", "subject",
                                                                                 "time_in", "time_out", "room"))
        self.schedule_treeview.place(relx=0.317, rely=0.584, relheight=0.41
                , relwidth=0.642)
        self.schedule_headings = ["Grade and Section", "Subject", "Time In", "Time Out", "Room"]
        for i in range(len(self.schedule_headings)):
            self.schedule_treeview.heading(i, text="{}".format(self.schedule_headings[i]))
            self.schedule_treeview.column(i, anchor="center")

        self.sy_lbl = tk.Label(top)
        self.sy_lbl.place(relx=0.004, rely=0.63, height=21, width=110)
        self.sy_lbl.configure(activebackground="#f9f9f9")
        self.sy_lbl.configure(activeforeground="black")
        self.sy_lbl.configure(background="#d9d9d9")
        self.sy_lbl.configure(disabledforeground="#a3a3a3")
        self.sy_lbl.configure(font="-family {Segoe UI} -size 14")
        self.sy_lbl.configure(foreground="#000000")
        self.sy_lbl.configure(highlightbackground="#d9d9d9")
        self.sy_lbl.configure(highlightcolor="black")
        self.sy_lbl.configure(text='''School Year:''')

        self.sy_var = tk.StringVar()
        self.sy_box = ttk.Combobox(top)
        self.sy_box.place(relx=0.133, rely=0.614, relheight=0.061
                , relwidth=0.137)
        self.sy_box.configure(textvariable=self.sy_var)
        self.sy_box.configure(takefocus="")
        self.sy_box.configure(state="readonly")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.283, rely=0.108, relheight=0.891)
        self.TSeparator2.configure(orient="vertical")

        self.result_lbl = tk.Label(top)
        self.result_lbl.place(relx=0.313, rely=0.123, height=41, width=74)
        self.result_lbl.configure(activebackground="#f9f9f9")
        self.result_lbl.configure(activeforeground="black")
        self.result_lbl.configure(background="#d9d9d9")
        self.result_lbl.configure(disabledforeground="#a3a3a3")
        self.result_lbl.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.result_lbl.configure(foreground="#000000")
        self.result_lbl.configure(highlightbackground="#d9d9d9")
        self.result_lbl.configure(highlightcolor="black")
        self.result_lbl.configure(text='''RESULT''')

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.283, rely=0.507, relwidth=0.717)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

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





