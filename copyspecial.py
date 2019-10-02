#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Will collab with Brett"


# +++your code here+++
special_paths = []
def get_special_paths(directory):
    special_paths = []
    path = os.getcwd() 
    #new_dir_log = os.listdir(path)
    new_dir_log = os.listdir(directory)
    #print(new_dir_log)
    for filename in new_dir_log:
        specials = re.search(r'__(\w+)__', filename)
        if specials:
            special_paths.append(os.path.abspath(filename))
        


    return special_paths
def copy_to(new_dir_log, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    for f in new_dir_log:
        file_name = os.path.basename(f)
        shutil.copy(f,os.path.join(directory, file_name))

def zip_to(new_dir_log, zippath):
    cmd= 'zip -j ' + zippath +' '+' '.join(new_dir_log)
    print("Command is:" + cmd)
    cmd_split = cmd.split()
    try:
        subprocess.check_output(cmd_split)
    except subprocess.CalledProcessError as e:
        
        print(e.output)
        exit(1)
    
    
    
# Write functions and modify main() to call them

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('from_dir', help="directory with special files")
    args = parser.parse_args()
    print(args)
    directory = args.from_dir
    todir = args.todir
    tozip = args.tozip
    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    get_path =  get_special_paths(directory)
    new_path = []

    
    targetdir = ''
    if todir:
        copy_to(get_path, todir)
    elif tozip:
        zip_to(get_path, tozip)
    else:
        print("\n".join(get_path))

if __name__ == "__main__":
    main()
