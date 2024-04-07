
# File management  System CLI

### Objective
* Build a command-line-based file management system that allows users to navigate directories, create, delete, copy, move files and folders, and perform basic file operations.

### Features
* It enables the users to navigate through directories (folders) using commands.
* It has functionalities to create, delete, rename, copy, and move files/folders.
* Also it displays the information about files (size, permissions, creation date, etc.).  
* It has a search feature to find files by name or extension.

### Outcomes
* Users can able to navigate through directories
* Users have authority to create delete, rename, copy, moving the files/folders
* Displays the statistics like creation date, last modified, file type, permissions, file size
* User is able to search the files with name/extension

### Architecture 
* The project is using Layered Architecture
* It has 3 modules

(1) Starter.py is an entry point of the project

(2) Main.py file controls the user input and calls the specific logic for a given command

(3) Operations.py file handles the user input, runs the logic and prints the output
