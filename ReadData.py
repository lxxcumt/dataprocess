import pandas as pd
import numpy as np
import os

def eachFile(filepath):
	PathList = []
	pathDir = os.listdir(filepath)
	for allDir in pathDir:
		child = os.path.join('%s\\%s'%(filepath,allDir))
		print pd.read_table(child, skiprows = 14, header = 0)
		#PathList.append(child)
		#print child.decode('gbk')
	#print PathList

filepath = raw_input("Please enter FilePath: ==>")

eachFile(filepath)


#pd.read_table("D:\dataprocess\MRT_log\EB2-SH-003&004_03,15,17_02,27,50PM", skiprows = 14,header = 0)

#print df

#print df.columns

