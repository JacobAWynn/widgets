#!usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
import ttkbootstrap as ttk
import time
import os

# $filepath
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# $functionality
def currdotbeattime():
    epochmilli = round(time.time() * 1000)
    epochsec = int(epochmilli / 1000)
    timetup = time.gmtime(epochsec)
    utchour = timetup[3]
    bielhour = (utchour + 1) % 24
    min = timetup[4]
    sec = timetup[5]
    milli = epochmilli % 1000
    bielmsm = milli + 1000 * (sec + 60 * (min + 60 * bielhour))
    dotbeattime = bielmsm / 86400
    dotbeatstr = "{:06.2f}".format(dotbeattime)
    labelstr = f"@{dotbeatstr}"
    dotbeattime_l.config(text = labelstr)
    dotbeattime_l.after(144, currdotbeattime)

# $createwin
try:
    dotbeat_root = ttk.Window(themename = "darkmaterial2")
except tkinter.TclError:
    dotbeat_root = ttk.Window(themename = "darkly")
dotbeat_root.overrideredirect(1)
dotbeat_root.geometry("400x150")

# $title
title_l = ttk.Label(master = dotbeat_root, text = ".beat time", font = "Ubuntu 24")
title_l.pack()

# $dotbeattime
dotbeattime_l = ttk.Label(master = dotbeat_root, font = "Ubuntu 64")
dotbeattime_l.pack()

# $runfunc
currdotbeattime()

# $runwin
dotbeat_root.mainloop()
