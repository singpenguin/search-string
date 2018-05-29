#!/use/bin/env python
#-*- coding:utf-8 -*-

import sys,os

if sys.version_info < (3, 0): 
    PY2 = True
    PY3 = False
    base_str = (str, unicode)
    text_type = unicode
else:
    PY2 = False
    PY3 = True
    base_str = (bytes, str)
    text_type = str 

filterType = ['gif','png','bmp','jpg','jpeg','rar','zip',
            'ico','apk','ipa','doc','docx','xls',
            'xlsx','ppt','pptx','pdf','gz','pyc','class',
            "swp", "pyc", "exe"]

dirs = [".git", "node_modules", "__pycache__"]

num = 0

def search(path=None,cont=None):
    if not path or not cont:
        print('path or searchString is empty')
        return
    if path[-1] == "/":
        path = path[:-1]
    global num
    if PY3:
        cont = cont.encode("utf-8")
    _loopFolder(path,cont)
    print("%s file find" % num)

def _loopFolder(path,cont):
    foldername = path.split("/")[-1]
    if foldername not in dirs:
        if os.path.isdir(path):
            folderList = os.listdir(path)
            for x in folderList:
                #此处也能检查是否是带.开头的文件或文件夹
                _loopFolder(path+"/"+x,cont)
        elif os.path.isfile(path):
            _verifyContent(path,cont)

def _verifyContent(path,cont):
    if path.split('.')[-1].lower() in filterType:
        return
    global num
    fh = open(path,'rb')
    fhContent = fh.readlines()
    fh.close()
    for index,x in enumerate(fhContent):
        if cont in x:
            num += 1
            print("%s    %s" % (path,index))
            break
    return


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("invalid parameters")
    else:
        search(sys.argv[1],sys.argv[2])
