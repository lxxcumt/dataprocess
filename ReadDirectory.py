import os

PathList = []

def eachFile(filepath):
	pathDir = os.listdir(filepath)
	for allDir in pathDir:
		child = os.path.join('%s\\%s'%(filepath,allDir))
		PathList.append(child)
		#print child.decode('gbk')
	print PathList

filepath = raw_input("Please enter FilePath: ==>")

eachFile(filepath)

