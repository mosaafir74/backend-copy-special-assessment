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
__author__ = "???"


# +++your code here+++
# Write functions and modify main() to call them



def get_special_paths(dir):
    """ returns a list of the absolute paths of the special files in the given directory """
    file_list = os.listdir(dir)
    file_string = ' '.join(file_list)
    special_files = re.findall(r'\w+__\w+__\.\w+', file_string)
    special_paths = [os.path.abspath(path) for path in special_files]
    print(special_paths)
    return special_paths


def copy_to(paths, dir):
    """ given a list of paths, copies those files into the given directory """
    if not os.path.exists(dir):
        os.makedirs(dir)
    for path in paths:
        shutil.copy(path, dir)

def zip_to(paths, zippath):
    """ given a list of paths, zip those files up into the given zipfile """
    first_path , second_path = paths[0], paths[1]
    subprocess.call(['zip', '-j', zippath, first_path, second_path])
    return

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('from_dir', help='the target dirctory for searching for special files')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    special_paths = get_special_paths(args.from_dir)
    if args.todir:
        copy_to(special_paths, args.todir)
    if args.tozip:
        zip_to(special_paths, args.tozip)
if __name__ == "__main__":
    main()
