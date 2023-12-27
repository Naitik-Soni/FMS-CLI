# Importing necessary packages for file and folder operations

import os
import shutil
import stat
from datetime import datetime as dt

colors = {
    'blue': '\x1b[94m',
    'bold': '\033[1m',
    'red': '\x1b[91m',
    'reset': '\x1b[0m',
}

# function for changing current working directory
def change_directory(dest):
    try:
        os.chdir(dest)
    except:
        print(f'{colors["red"]} Directory not found {colors["reset"]}')
    else:
        print(f'{colors["blue"]} Directory changed {colors["reset"]}')


# function for creating directory
def create_directory(dir_name):
    try:
        os.mkdir(dir_name)
    except:
        print(f'{colors["red"]} Error in creating directory with name `{dir_name}` {colors["reset"]}')
    else:
        print(f'{colors["blue"]} Directory with name `{dir_name}` created {colors["reset"]}')

# function for deleting directory
def delete_directory(dir_name):
    try:
        shutil.rmtree(dir_name)
    except:
        print(f'{colors["red"]} Error deleting the directory with name `{dir_name}` {colors["reset"]}')
    else:
        print(f'{colors["blue"]} Directory deleted {colors["reset"]}')

# List the files and folders in current directory
def list_files():
    files = os.listdir('.')
    print(f'{colors["bold"]}{"Name".ljust(32," ")}  |  {"Type".ljust(9," ")}  |  Size (bytes){colors["reset"]}')
    print("".join(["-" for i in range(64)]))
    for file in files:
        file_type = "File"
        file_size = os.path.getsize(os.getcwd() + "\\" + file)
        if os.path.isdir(file):
            continue
        print(f'{file.ljust(32," ")[:32]}  |  {file_type.ljust(9," ")}  |  {file_size}')

# move the file or directory to a particular destination
def move_dir(dir_name, dest):
    try:
        shutil.move(dir_name, dest)
    except:
        print(f'{colors["red"]} File or directory not found {colors["reset"]}')
    else:
        print(f'{colors["blue"]} "{dir_name}" moved to "{dest}" {colors["reset"]}')

# copy the file or directory to a particular destination
def copy_dir(dir_name, dest):
    try:
        if len(dir_name.split(".")) == 1:
            shutil.copytree(dir_name, dest+"/"+dir_name)
        else:
            shutil.copy(dir_name, dest)
    except Exception as e:
        print(e)
        print(f'{colors["red"]} File or directory not found {colors["reset"]}')
    else:
        print(f'{colors["blue"]} `{dir_name}` copied to `{dest}` {colors["reset"]}')

# renaming the directory or file
def rename(old_name, new_name):
    try:
        os.rename(old_name, new_name)
    except:
        print(f'{colors["red"]} Error changing name of the file:\n    (1) Might be due to file not exist\n    (2) File with same name already exists{colors["reset"]}')
    else:
        print(f'{colors["blue"]} Name changed {colors["reset"]}')

# Clears the screen
def clear():
    os.system("clear")

# Create a file
def create_file(file_name_wx):
    cwd = os.getcwd()
    try:
        with open(cwd + "\\" + file_name_wx, "w") as f: 
            f.write("Hello")
        f.close()
    except:
        print(f'{colors["Red"]} Unable to create file {colors["reset"]}')
    else:
        print(f'{colors["blue"]} File created Succesfully {colors["reset"]}')

# Delete a file
def delete_file(file_name):
    try:
        os.remove(file_name)
    except:
        print(f'{colors["red"]} Unable to delete file {colors["reset"]}')
    else:
        print(f'{colors["blue"]} File deleted successfully {colors["reset"]}')

# Display the metadata about file
def meta_data():
    try:
        print(f'{colors["blue"]} Current directory: '+os.getcwd()+f'{colors["reset"]}')
        print("".join(["-" for i in range(117)]))
        print("|    Creation date    |    Last modified    | Permission | File type | Size (bytes) |              Name             |")
        print("".join(["-" for i in range(117)]))
        for file in os.listdir('.'):
            stats = os.stat(file)
            # lines 118-122 converts the statistical data into readable format 
            ftype = "Directory" if os.path.isdir(file) else "File"
            fpermission = stat.filemode(stats[0])
            fmodified = dt.fromtimestamp(stats[8]).strftime("%Y-%m-%d %H:%M:%S")
            fcreated = dt.fromtimestamp(stats[9]).strftime("%Y-%m-%d %H:%M:%S")
            fsize = str(stats[6])
            fname = (file[:26] + '...') if len(file) > 28 else file
            print("| " + fcreated + " | " + fmodified + " | " + fpermission + " | " + ftype.ljust(9,' ') + " | " + str(fsize).rjust(12,' ') + " | " + fname.ljust(29,' ')+ " |")
        print("".join(["-" for i in range(117)]))
    except:
        print(f'{colors["red"]} Error: could not read the metadata of files {colors["reset"]}')

# Display content of a file
def display_content(file_name):
    try:
        with open(file_name, "r") as myfile: 
            f_content = myfile.readlines()
            print()
            for lnum, line in enumerate(f_content):
                if line == '\n':
                    print(str(lnum+1)+".")
                else:
                    print(str(lnum+1)+". ",line.rstrip())
        myfile.close()
    except:
        print(f'{colors["red"]} Error reading file {colors["reset"]}')

# Copying content of one file into another file
def copy_file_content(source_file, dest_file):
    try:
        shutil.copyfile(source_file, dest_file)
    except:
        print(f'{colors["red"]} Unable to copy contents of file {colors["reset"]}')
    else:
        print(f'{colors["blue"]} File content copied successfully {colors["reset"]}')

# Writing text to a file
def write_to_file(file_name, text):
    try:
        with open(file_name, "w") as myfile:
            myfile.write(text)
        print(f'{colors["blue"]} Text written to a file {colors["reset"]}')
    except:
        print(f'{colors["red"]} Error writing to the file {colors["reset"]}')

# Finding file from the current directory and all sub-directories
def find_file(file_name):
    try:
        found = 0
        myfiles = file_name.split(".")
        for root, _, files in os.walk(os.getcwd()):
            for file in files:
                this = file.split(".")
                for i in this:
                    if i in myfiles:
                        found=1
                        print(f'{colors["blue"]} File path: {colors["reset"]} {root}'+'\\'+file)
        if found == 0:
            print(f'{colors["blue"]} File not found {colors["reset"]}')
    except:
        print(f'{colors["red"]} Error searching for file {colors["reset"]}')