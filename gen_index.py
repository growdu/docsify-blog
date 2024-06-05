#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def write_index(path, file, num, schar):
    if os.path.basename(path)[0] == '.' and len(os.path.basename(path)) > 1:
        return

    num = 1
    allfilelist=os.listdir(path)
    for f in allfilelist:
        tempf = os.path.join(path, f)
        #判断是不是文件夹
        if os.path.isdir(tempf):
            if (f == ".git") or f == "code":
                continue
            temp = "\n"
            for n in range(num):
                temp = temp + schar
            temp = temp + " " + os.path.basename(tempf) + "\n"
            if (f != "." and f != ".." and num < 4) :
                file.write(temp)
            write_index(tempf,file,num,schar)
        elif tempf.endswith("_sidebar.md") or tempf.endswith("README.md") or tempf.endswith("_coverpage.md"):
            continue;
        elif tempf.endswith(".md"): 
            tempf=tempf.replace(" ","_").replace("-","_").replace("-","_")
            temp = "  * " + "[" + os.path.basename(tempf).split('.')[0] + "]" + "(" + tempf + ")" + "\n"
            temp = temp.replace("\\", "/")
            file.write(temp)

filepath = "_sidebar.md"
# 判断文件是否存在
if (os.path.exists(filepath)) :
	#存在，则删除文件
	os.remove(filepath)

with open(filepath,'a', encoding="UTF-8") as f:
    write_index(".", f, 1, "*")

readme="README.md"
# 判断文件是否存在
if (os.path.exists(readme)) :
	#存在，则删除文件
	os.remove(readme)
with open(readme,'a', encoding="UTF-8") as f:
    write_index(".", f, 1, "#")