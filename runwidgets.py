#!usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import subprocess

# $filepath
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# $runall
all_py_files = []
for root, dirs, files in os.walk(script_directory):
    for file in files:
        if (os.path.splitext(file)[1] == ".py") & (file != "runwidgets.py"):
            all_py_files.append(os.path.join(root, file))

for file in all_py_files:
    subprocess.Popen(["python3", file])