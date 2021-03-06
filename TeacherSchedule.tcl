#############################################################################
# Generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#  Jan 18, 2020 06:24:53 PM CST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m52" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1200x651+239+140
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4336 881
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Scheduling System"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but43 \
        -activebackground #ffffff -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief ridge -text Back 
    vTcl:DefineAlias "$top.but43" "back_btn" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe44
    vTcl:DefineAlias "$top.tSe44" "TSeparator1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {First Name:} 
    vTcl:DefineAlias "$top.lab45" "firstName_lbl" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent46 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black 
    vTcl:DefineAlias "$top.ent46" "firstName_entry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Middle Name:} 
    vTcl:DefineAlias "$top.lab47" "middleName_lbl" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent48 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black 
    vTcl:DefineAlias "$top.ent48" "middleName_entry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Last Name:} 
    vTcl:DefineAlias "$top.lab49" "lastName_lbl" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent50 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black 
    vTcl:DefineAlias "$top.ent50" "lastName_entry" vTcl:WidgetProc "Toplevel1" 1
    button $top.but51 \
        -activebackground #ffffff -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief ridge -text Search 
    vTcl:DefineAlias "$top.but51" "search_btn" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure Treeview.Heading -background $vTcl(pr,guicomplement_color)
    ttk::style configure Treeview.Heading -font "$vTcl(actual_gui_font_dft_desc)"
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $top.scr52 \
        -background $vTcl(actual_gui_bg) -height 127 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 770 
    vTcl:DefineAlias "$top.scr52" "teachers_treeview" vTcl:WidgetProc "Toplevel1" 1
        .top42.scr52.01 configure -columns {Col1}
        .top42.scr52.01 heading #0 -text {Tree}
        .top42.scr52.01 heading #0 -anchor center
        .top42.scr52.01 column #0 -width 375
        .top42.scr52.01 column #0 -minwidth 20
        .top42.scr52.01 column #0 -stretch 1
        .top42.scr52.01 column #0 -anchor w
        .top42.scr52.01 heading Col1 -text {Col1}
        .top42.scr52.01 heading Col1 -anchor center
        .top42.scr52.01 column Col1 -width 376
        .top42.scr52.01 column Col1 -minwidth 20
        .top42.scr52.01 column Col1 -stretch 1
        .top42.scr52.01 column Col1 -anchor w
    button $top.but53 \
        -activebackground #ffffff -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief ridge -text {Select Teacher} 
    vTcl:DefineAlias "$top.but53" "selectTeacher_btn" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab55 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text SCHEDULE 
    vTcl:DefineAlias "$top.lab55" "schedule_lbl" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure Treeview.Heading -background $vTcl(pr,guicomplement_color)
    ttk::style configure Treeview.Heading -font "$vTcl(actual_gui_font_dft_desc)"
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $top.scr56 \
        -background $vTcl(actual_gui_bg) -height 267 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 770 
    vTcl:DefineAlias "$top.scr56" "schedule_treeview" vTcl:WidgetProc "Toplevel1" 1
        .top42.scr56.01 configure -columns {Col1}
        .top42.scr56.01 heading #0 -text {Tree}
        .top42.scr56.01 heading #0 -anchor center
        .top42.scr56.01 column #0 -width 375
        .top42.scr56.01 column #0 -minwidth 20
        .top42.scr56.01 column #0 -stretch 1
        .top42.scr56.01 column #0 -anchor w
        .top42.scr56.01 heading Col1 -text {Col1}
        .top42.scr56.01 heading Col1 -anchor center
        .top42.scr56.01 column Col1 -width 376
        .top42.scr56.01 column Col1 -minwidth 20
        .top42.scr56.01 column Col1 -stretch 1
        .top42.scr56.01 column Col1 -anchor w
    label $top.lab44 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {School Year:} 
    vTcl:DefineAlias "$top.lab44" "sy_lbl" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo48 \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$top.tCo48" "TCombobox1" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe49 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe49" "TSeparator2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text RESULT 
    vTcl:DefineAlias "$top.lab50" "result_lbl" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe51
    vTcl:DefineAlias "$top.tSe51" "TSeparator3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m52
    menu $site_3_0 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but43 \
        -in $top -x 10 -y 10 -width 157 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tSe44 \
        -in $top -x -10 -y 70 -width 1210 -anchor nw -bordermode inside 
    place $top.lab45 \
        -in $top -x 6 -y 170 -width 100 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 160 -y 160 -width 164 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 8 -y 250 -width 120 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 160 -y 240 -width 164 -height 40 -anchor nw \
        -bordermode ignore 
    place $top.lab49 \
        -in $top -x 10 -y 330 -width 90 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 160 -y 320 -width 164 -height 40 -anchor nw \
        -bordermode ignore 
    place $top.but51 \
        -in $top -x 70 -y 510 -width 157 -height 44 -anchor nw \
        -bordermode ignore 
    place $top.scr52 \
        -in $top -x 380 -y 123 -width 770 -relwidth 0 -height 127 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but53 \
        -in $top -x 380 -y 260 -width 157 -height 44 -anchor nw \
        -bordermode ignore 
    place $top.lab55 \
        -in $top -x 375 -y 340 -width 104 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.scr56 \
        -in $top -x 380 -y 380 -width 770 -relwidth 0 -height 267 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 7 -y 410 -width 110 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo48 \
        -in $top -x 160 -y 400 -width 164 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tSe49 \
        -in $top -x 340 -y 70 -height 580 -anchor nw -bordermode inside 
    place $top.lab50 \
        -in $top -x 377 -y 80 -width 74 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tSe51 \
        -in $top -x 340 -y 330 -width 860 -anchor nw -bordermode inside 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

