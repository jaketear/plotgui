# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:36:58 2018

@author: Yan Hua
"""
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.dates import AutoDateLocator
import pandas as pd
from input_function import *
from PyQt5.QtWidgets import QSizePolicy

class PlotCanvas(FigureCanvas):
    
    def __init__(self,parent=None,width=5,height=4,dpi=100):
        self.fig=Figure(figsize=(width,height),dpi=dpi)
        #self.axes = fig.add_subplot(111)# 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        #self.axes = fig.add_axes([0,0,1,1])
        FigureCanvas.__init__(self, self.fig)# 初始化父类
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
    def plot_para_time(self,source=None,para_list=[]):
        if isinstance(source,(str,unicode)): #！！！！python 2
            df=cols_input(source,para_list)
        elif isinstance(source,pd.DataFrame):
            df=source
        else:
            return
        df[para_list[0]]=pd.to_datetime(df[para_list[0]],format='%H:%M:%S:%f')
        ax1 = self.fig.add_subplot(1,1,1)
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S:%f'))#设置时间标签显示格式
        #plt.xticks(pd.date_range('2014-09-01','2014-09-30'),rotation=90)
        #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S.%f')) # 显示时间坐标的格式
    
        #autodates= AutoDateLocator()                # 时间间隔自动选取
        #plt.gca().xaxis.set_major_locator(autodates)
        df.plot(para_list[0],ax=ax1)
        #self.draw()
        self.show()
        
    def plot_para(self,source=None,para_list=[]):
        if isinstance(source,(str,unicode)): #！！！！python 2
            df=cols_input(source,para_list)
        elif isinstance(source,pd.DataFrame):
            df=source
        else:
            return
        ax1 = self.fig.add_subplot(1,1,1)
        df.plot(para_list[0],ax=ax1)
        #self.draw()
        self.show()
        
    def add_toolbar(self,parent=None):
        toolbar=NavigationToolbar(self,parent)
        return toolbar
    
    def show_toolbar(self,toolbar):
        toolbar.show()
        
    def hide_toolbar(self,toolbar):
        toolbar.hide()

def plot_para(filename,para_list=[]):
    df=cols_input(filename,para_list)
    #df.plot(x="time")
#    time=df.time
#    time_translation=[datetime.strptime(d).date() for d in time]
#    y = df[para_list[1]].values
#    
    # 配置时间坐标轴
    df[para_list[0]]=pd.to_datetime(df[para_list[0]],format='%H:%M:%S:%f')
    fig1=plt.figure()
    ax1 = fig1.add_subplot(1,1,1)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S:%f'))#设置时间标签显示格式
    #plt.xticks(pd.date_range('2014-09-01','2014-09-30'),rotation=90)
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S.%f')) # 显示时间坐标的格式

    #autodates= AutoDateLocator()                # 时间间隔自动选取
    #plt.gca().xaxis.set_major_locator(autodates)
    df.plot(para_list[0],ax=ax1)
    plt.show()
    
def subplot_para(filename,para_list=[]):
    df=cols_input(filename,para_list)
    picNum=len(para_list)-1
    df[para_list[0]]=pd.to_datetime(df[para_list[0]],format='%H:%M:%S:%f')
#    fig2=plt.figure()
#    ax2=fig2.add_subplot(1,1,1)
    
    ax=df.plot(para_list[0],subplots=True,layout=(picNum,1),sharex=True)
    ax[0][0].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S:%f'))
    plt.show()
if __name__ == "__main__":
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
    para_list=["time","HF_FSECU_1_L354_HLS_OMS_Status_Flap_Inoperative","FCM3_Voted_True_Airspeed"]
    #para_list=para_name.values[:,233:235].tolist()[0]
    #plot_para(filename,para_list)
    subplot_para(filename,para_list)
    #para_list=para_name.values[:,23:25].tolist()[0]
    #plot_para(filename,para_list)