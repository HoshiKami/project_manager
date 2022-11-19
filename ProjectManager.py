import pathlib
import shutil
import numpy as np
import os

data = {0:"", 1:"", 2:"", 3:"", 4:"",5:""}

def getCommands():
    u_input = str(input(">> "))
    u_output = u_input.split()
    i = 0
    for x in u_output:
        data[i] = x
        i = i + 1
    return data

try:
    logo = open("logo.txt", "r")
    logo_rend = logo.read()
    print(logo_rend)
    while data[0] != "quit":
        getCommands()
        if data[0] == "create":
            path = pathlib.Path(data[2])
            new_dir = path / data[1]
            if new_dir.is_dir() != True:
                new_dir.mkdir(exist_ok=True)
                pack_dir = new_dir / f"{data[1]}_lib"
                pack_dir.mkdir(exist_ok=True)
                if data[3] == "python":
                    main_file = open(f"{new_dir}/{data[4]}.py", "w+")
                    pack_file = open(f"{pack_dir}/__init__.py","w+")
                    main_file,pack_file.write("")
                    if data[5] != "":
                        main_file.write(f"import {data[5]}")
                        main_file.close()
                    pack_file,main_file.close()
                    print(">> Project created succesfully")
            else:
                print("Invalid Input\n")
        elif data[0] == "delete":
            del_path = pathlib.Path(data[1])
            if del_path.is_dir() == True:
                shutil.rmtree(del_path)
                print("Project Deleted Succsesfully\n")
        elif data[0] == "help":
            print(">> command guide:\n1. create <name> <path> <project_type> <main_scrpit_name> <module1,module2...>\n2. delete <path>\n3. quit\n")
            getCommands()
        elif data[0] == "quit":
            print(">> quitting Program...\n")
        else:
            print(">> this command don't exist")
except IndexError:
        print(">> invalid input")