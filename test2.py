# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 21:36:34 2018

@author: admin
"""
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.dates import AutoDateLocator
import pandas as pd
import numpy as npy
#from input import *
def header_input(filename,sep='\s+'): #input the para name first,use with col_input
    with open(filename,'rb') as f:
        if filename.endswith(('.txt','.csv')):
            if sep=='all':
                df=pd.read_table(f,sep='\s+|\t|,|;',header=None,nrows=1,engine='python')
                #or only input the columns index:nrows=0,remove header=None
            else:
                df=pd.read_table(f,sep=sep,header=None,nrows=1,engine='c')
        if filename.endswith(('.xls','.xlsx')):
            df=pd.read_excel(f,header=None)
            df=df.iloc[0,:]  #select the first row
    return df

def cols_input(filename,cols,sep='\s+'):  #without chunkinput now!!
    with open(filename,'rb') as f:
        if filename.endswith(('.txt','.csv')):
            if sep=='all':
                df=pd.read_table(f,sep='\s+|\t|,|;',usecols=cols,engine='python')
            else:
                df=pd.read_table(f,sep=sep,usecols=cols,engine='c')
        if filename.endswith(('.xls','.xlsx')):
            df=pd.read_excel(f,usecols=cols)
    return df
#filename=u"D:/flightdata/FTPD-C919-10101-PD-170318-G-02-CAOWEN-664002-16.txt"
filename=u"D:/flightdata/FTPD-C919-10101-PD-170318-G-02-CAOWEN-664003-16.txt"
    #filename=u"C:/Users/admin/Desktop/5008问题汇总.xlsx"
    #df=chunk_input(filename,sep='all')
    #df=all_input(filename)
para_name=header_input(filename,sep='all')
    #df=cols_input(filename,["time","HF_FSECU_1_L354_HLS_OMS_Status_Flap_Inoperative","FCM3_Voted_True_Airspeed"])
        #df=cols_input(filename,[u"日期"]
    #df.plot("time","FCM3_Voted_True_Airspeed")
    #plt.show()
    #plt.figure()
    #plt.plot(df["time"],df["FCM3_Voted_True_Airspeed"])
    #plt.show()
para_list=["HF_FSECU_1_L354_HLS_OMS_Status_Flap_Inoperative","FCM3_Voted_True_Airspeed"]
para_list=para_name.values[:,233:235].tolist()[0]
   # plot_para(filename,para_list)
if para_list:
    para_list.insert(0,"time")
df=cols_input(filename,para_list)
def on_pick3(event):
    print("my position:" ,event.button,event.xdata, event.ydata)
class LineBuilder: 
    def __init__(self, line): 
        self.line = line 
        self.xs = list(line.get_xdata()) 
        self.ys = list(line.get_ydata()) 
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self) 
    def __call__(self, event): 
        print('click', event.button,event.ind) 
        if event.inaxes!=self.line.axes: 
            return 
        self.xs.append(event.xdata) 
        self.ys.append(event.ydata) 
        self.line.set_data(self.xs, self.ys) 
        self.line.figure.canvas.draw()

#def onpick3(event):
#        ind = event.ind
#        print 'onpick3 scatter:', ind, df[], npy.take(y, ind)
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
df.plot("time",ax=ax1)
line, = ax1.plot([0], [100000])  # empty line
linebuilder = LineBuilder(line)

#fig1.canvas.mpl_connect('button_press_event', on_pick3)
plt.show()




   