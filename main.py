import Operation as ops
import os

def main_operator():
    ops.clear()
    display_help()
    while True:
        try:
            command = input("\n$$$ "+os.getcwd()+">").split()
            if len(command) == 0:
                continue
            if command[0].lower() == "ls": #
                ops.list_files()
            elif command[0].lower() == "clear": #
                ops.clear()
            elif command[0].lower() == "cd": #
                ops.change_directory(command[1].lower())
            elif command[0].lower() == "cdir": #
                ops.create_directory(command[1])
            elif command[0].lower() == "ddir": #
                ops.delete_directory(command[1])
            elif command[0].lower() == "cfile": #
                ops.create_file(command[1])
            elif command[0].lower() == "dfile": #
                ops.delete_file(command[1])
            elif command[0].lower() == "fstat": #
                ops.meta_data()
            elif command[0].lower() == "find": #
                ops.find_file(command[1])
            elif command[0].lower() == "dis": #
                ops.display_content(command[1])
            elif command[0].lower() == "copy": #
                ops.copy_file_content(command[1], command[2])
            elif command[0].lower() == "write": #
                ops.write_to_file(command[1],  " ".join(command[2:]))
            elif command[0].lower() == "rn": #
                ops.rename(command[1], command[2])
            elif command[0].lower() == "mv": #
                ops.move_dir(command[1], command[2])
            elif command[0].lower() == "cp": #
                ops.copy_dir(command[1], command[2])
            elif command[0].lower() == "help": #
                display_help()
            elif command[0].lower() == "exit": #
                break
            else:
                print(f"\x1b[91m Cannot recognize command - '{command[0].lower()}' \n Type 'help' for reference of commands \x1b[0m")
        except:
            print(f"\x1b[91m Error in '{command[0].lower()}' \n Type 'help' for reference of command syntax \x1b[0m")

    os.system("taskkill /F /IM cmd.exe")

def display_help():
    print(f"\x1b[94m")
    print("    --------------------------------------------------------------------------------------------------")
    print("    |CD __name__                 | Changes the current directory                                     |")
    print("    |CDIR __name__               | Creates directory with specified name                             |")
    print("    |CFILE __name__              | Creates file with specified name                                  |")
    print("    |CLEAR                       | Clears the screen                                                 |")
    print("    |COPY __name1__  __name2__   | Copies content of one file to another                             |")
    print("    |CP __name__  __dest__       | Copies file to specific destination                               |")
    print("    |DDIR __name__               | Deletes the directory                                             |")
    print("    |DFILE __name__              | Deletes the file                                                  |")
    print("    |DIS __name__                | Displays content of a file                                        |")
    print("    |EXIT                        | Exits the File Management System                                  |")
    print("    |FIND __name__ , FIND __et__ | Finds the file in current working directory and sub-directories   |")
    print("    |FSTAT                       | Displays the metadata about files in current directory            |")
    print("    |HELP                        | Displays the command help                                         |")
    print("    |MV __name__  __dest__       | Moves the file or directory to a destination                      |")
    print("    |LS                          | List files of current directory                                   |")
    print("    |WRITE __name__  __text__    | Writes the text to a file                                         |")
    print("    |RN __name1__  __name2__     | Renames the file or folder                                        |")
    print("    --------------------------------------------------------------------------------------------------")
    print(f"\x1b[0m")

if __name__ == "__main__":
    main_operator()