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
                import module_pm.ProjectTypes
                if data[3] == "python":
                    module_pm.ProjectTypes.PyProj()
                elif data[3] == "c":
                    module_pm.ProjectTypes.CProj()
                elif data[3] == "javascript":
                    module_pm.ProjectTypes.JSProj()
                print(">> Project created succesfully")
            else:
                print(">> Project creation faild\n>>")
        elif data[0] == "delete":
            del_path = pathlib.Path(data[1])
            if del_path.is_dir() == True:
                shutil.rmtree(del_path)
                print(">> Project Deleted Succsesfully\n>>")
        elif data[0] == "help":
            print(">> command guide:\n1. create <name> <path> <project_type> <main_scrpit_name> <module1,module2...>\n2. delete <path>\n3. quit\n")
            getCommands()
        elif data[0] == "quit":
            print(">> quitting Program...\n>>")
        else:
            print(">> this command don't exist")
except IndexError:
        print(">> invalid input")
