#-*- coding: UTF-8 -*- 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def CopyToExcel(filepath):
	PathList = []
	pathDir = os.listdir(filepath) #读取指定目录下的文档名称
	for allDir in pathDir:
		child = os.path.join('%s\\%s'%(filepath,allDir)) #讲文档名称与文档路径组成完整的文档路径
		rawdata=pd.DataFrame(pd.read_table(child, skiprows = 14, header = 0)) 
		rawcolumns=rawdata.columns #提取所有数据列的名词
		Cold = list(rawcolumns)
		Grenade = pd.Series(Cold)
		print Grenade
		Hits = list(input('please select the number of columns that you need(such as 0,1,2,3...)==>')) #选择需要的数据列
		print Hits
		Avril = []
		for j in Hits:
			Avril.append(Grenade[j]) #get these columns that we need 
		
		zita = rawdata.ix[:, Avril]
		writer = pd.ExcelWriter(os.path.join('%s\\%s'%(filepath,raw_input("please enter the name of workbook, such as ***.xlsx: ==>")))) #将选定的数据列读入特定的excel文件
		zita.to_excel(writer, index = False) 
		writer.save() #保存excel文件

filepath = raw_input("Please enter FilePath: ==>") #输入需要处理数据的目录地址

CopyToExcel(filepath)


#please enter the columns that you need (such as 0,1,2,3):

