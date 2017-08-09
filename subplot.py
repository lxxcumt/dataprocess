#-*- coding: UTF-8 -*- 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def eachFile(filepath):
	PathList = []
	pathDir = os.listdir(filepath)
	print pathDir
	for allDir in pathDir:
		child = os.path.join('%s\\%s'%(filepath,allDir))
		rawdata=pd.DataFrame(pd.read_table(child, skiprows = 14, header = 0))
		rawcolumns=rawdata.columns
		Cold = list(rawcolumns)
		Grenade = pd.Series(Cold)
		print Grenade
		Hits = list(input('please select the number of columns that you need(such as 0,1,2,3...)==>'))
		Avril = []
		for j in Hits:
			Avril.append(Grenade[j]) #get these columns that we need 
		
		zita = rawdata.ix[:, Avril]  #选取需要的数据列
		wb_name = raw_input("please enter the name of workbook: ==>") #输入新建的excel文档的名称的名称
		writer = pd.ExcelWriter(os.path.join('%s\\%s'%(filepath, wb_name+'.xlsx'))) 
		zita.to_excel(writer, index = False)
		writer.save()
		
		#生成图表	
		i = pathDir.index(allDir)+1
		plt.sca(plt.subplot(2,2,i))
		for each_column in Avril:
			print each_column
			plt.plot(zita[each_column],label = str(each_column), linewidth=2)
		
		plt.title(allDir)
		plt.xlabel("Time(s)")
		plt.ylabel("Temperature(C)")
		plt.xlim(0, 610)
		
		
filepath = raw_input("Please enter FilePath: ==>")

plt.figure(figsize = (16,8)) 

eachFile(filepath)

fig_name = raw_input("Please enter the name of plot:==> ")
plt.legend()  #显示每条曲线的标签和样式的矩形区域
plt.savefig('%s\\%s'%(filepath, fig_name), fmt = "png")
plt.show() #在plt.show() 之前调用plt.savefig()， 否则生成的图片会一片空白

