#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Jan 18, 2020 05:32:14 PM CST  platform: Windows NT

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

import AddRoom_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = RoomsGUI (root)
    AddRoom_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = RoomsGUI (w)
    AddRoom_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class RoomsGUI:
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        window_width = 692
        window_height = 551
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
        self.back_btn.place(relx=0.014, rely=0.018, height=44, width=157)
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
        self.TSeparator1.place(relx=0.0, rely=0.127, relwidth=1.676)

        self.roomName_lbl = tk.Label(top)
        self.roomName_lbl.place(relx=0.007, rely=0.163, height=41, width=114)
        self.roomName_lbl.configure(activebackground="#f9f9f9")
        self.roomName_lbl.configure(activeforeground="black")
        self.roomName_lbl.configure(background="#d9d9d9")
        self.roomName_lbl.configure(disabledforeground="#a3a3a3")
        self.roomName_lbl.configure(font=font10)
        self.roomName_lbl.configure(foreground="#000000")
        self.roomName_lbl.configure(highlightbackground="#d9d9d9")
        self.roomName_lbl.configure(highlightcolor="black")
        self.roomName_lbl.configure(text='''Room Name:''')

        self.roomName_var = tk.StringVar()
        self.roomName_entry = tk.Entry(top)
        self.roomName_entry.place(relx=0.202, rely=0.163, height=40
                , relwidth=0.237)
        self.roomName_entry.configure(background="white")
        self.roomName_entry.configure(disabledforeground="#a3a3a3")
        self.roomName_entry.configure(font="-family {Segoe UI} -size 12")
        self.roomName_entry.configure(foreground="#000000")
        self.roomName_entry.configure(highlightbackground="#d9d9d9")
        self.roomName_entry.configure(highlightcolor="black")
        self.roomName_entry.configure(insertbackground="black")
        self.roomName_entry.configure(selectbackground="#c4c4c4")
        self.roomName_entry.configure(selectforeground="black")
        self.roomName_entry.configure(textvariable=self.roomName_var)

        self.grade_lbl = tk.Label(top)
        self.grade_lbl.place(relx=0.007, rely=0.254, height=41, width=64)
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
        self.grade_entry.place(relx=0.202, rely=0.254, height=40, relwidth=0.237)
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

        self.add_btn = tk.Button(top)
        self.add_btn.place(relx=0.462, rely=0.263, height=34, width=67)
        self.add_btn.configure(activebackground="#ffffff")
        self.add_btn.configure(activeforeground="#000000")
        self.add_btn.configure(background="#ffffff")
        self.add_btn.configure(disabledforeground="#a3a3a3")
        self.add_btn.configure(font="-family {Segoe UI} -size 9")
        self.add_btn.configure(foreground="#000000")
        self.add_btn.configure(highlightbackground="#d9d9d9")
        self.add_btn.configure(highlightcolor="black")
        self.add_btn.configure(pady="0")
        self.add_btn.configure(relief="ridge")
        self.add_btn.configure(text='''Add''')

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.grade_treeview = ScrolledTreeView(top, columns=("grade"), show="headings")
        self.grade_treeview.place(relx=0.029, rely=0.381, relheight=0.448
                , relwidth=0.636)
        self.grade_treeview.heading(0, text="Grade")
        self.grade_treeview.column(0, anchor="center")

        self.addRoom_btn = tk.Button(top)
        self.addRoom_btn.place(relx=0.029, rely=0.871, height=54, width=197)
        self.addRoom_btn.configure(activebackground="#1aff12")
        self.addRoom_btn.configure(activeforeground="#000000")
        self.addRoom_btn.configure(background="#1aff12")
        self.addRoom_btn.configure(disabledforeground="#a3a3a3")
        self.addRoom_btn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.addRoom_btn.configure(foreground="#ffffff")
        self.addRoom_btn.configure(highlightbackground="#d9d9d9")
        self.addRoom_btn.configure(highlightcolor="black")
        self.addRoom_btn.configure(pady="0")
        self.addRoom_btn.configure(relief="ridge")
        self.addRoom_btn.configure(text='''ADD ROOM''')

        self.lab_var = tk.IntVar()
        self.lab_check = tk.Checkbutton(top)
        self.lab_check.place(relx=0.46, rely=0.181, relheight=0.058
                , relwidth=0.168)
        self.lab_check.configure(activebackground="#ececec")
        self.lab_check.configure(activeforeground="#000000")
        self.lab_check.configure(background="#d9d9d9")
        self.lab_check.configure(disabledforeground="#a3a3a3")
        self.lab_check.configure(font=font10)
        self.lab_check.configure(foreground="#000000")
        self.lab_check.configure(highlightbackground="#d9d9d9")
        self.lab_check.configure(highlightcolor="black")
        self.lab_check.configure(justify='left')
        self.lab_check.configure(text='''Laboratory''')
        self.lab_check.configure(variable=self.lab_var)

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





