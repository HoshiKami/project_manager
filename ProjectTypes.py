import pathlib
import shutil
import numpy as np
import os

def PyProj():
    from ProjectManager import data, new_dir, pack_dir
    main_file = open(f"{new_dir}/{data[4]}.py", "w+")
    pack_file = open(f"{pack_dir}/__init__.py","w+")
    main_file,pack_file.write("")
    if data[5] != "":
        main_file.write(f"import {data[5]}")
        main_file.close()
    pack_file,main_file.close()


def CProj():
    from ProjectManager import data, new_dir, pack_dir
    main_file = open(f"{new_dir}/{data[4]}.c", "w+")
    pack_file = open(f"{pack_dir}/{data[1]}_lib.c","w+")
    second_file = open(f"{pack_dir}/{data[1]}_lib.h","w+")
    second_file,main_file,pack_file.write("")
    if data[5] != "":
        main_file.write(f"#inculde <{data[5]}>")
        main_file.close()
    pack_file,main_file,second_file.close()


def JSProj():
    from ProjectManager import data, new_dir, pack_dir
    main_file = open(f"{new_dir}/{data[4]}.js", "w+")
    pack_file = open(f"{pack_dir}/{data[1]}_lib.js","w+")
    second_file = open(f"{pack_dir}/sec_{data[1]}_lib.js","w+")
    second_file,main_file,pack_file.write("")
    if data[5] != "":
        main_file.write(f"#inculde <{data[5]}>")
        main_file.close()
    pack_file,main_file,second_file.close()