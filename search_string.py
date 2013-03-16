#!/use/bin/env python
#-*- coding:utf-8 -*-

import sys,os

filterType = ['gif','png','bmp','jpg','jpeg','rar','zip',
			'ico','apk','ipa','doc','docx','xls',
			'xlsx','ppt','pptx','pdf','gz','pyc','class']

num = 0

def search(path=None,cont=None):
	if not path or not cont:
		print('path or searchString is empty')
		return
	global num
	_loopFolder(path,cont)
	print("%s file find" % num)

def _loopFolder(path,cont):
	if path.split('/')[-1][0] != '.':
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
	fh = open(path,'r')
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
