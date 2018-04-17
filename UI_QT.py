# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:11:48 2018

@author: Yan Hua
"""
from PyQt5 import QtWidgets  
from readtest import Ui_MainWindow  
from input import *
from PyQt5.QtWidgets import QFileDialog
from plot import *  
      
class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):  
    def __init__(self):  
        super(MyWindow,self).__init__()  
        self.setupUi(self)  
    def read(self):  
        file_name, ok=QFileDialog.getOpenFileName(self,'读取','D:/')
        if file_name:
            para_name=header_input(file_name,sep='\s+')
            para_list=para_name.values[:,23:25].tolist()[0]  #temp
            plot_para(file_name,para_list)
        #self.textBrowser.append(df) 
        #else:
            #self.textBrowser.append("fail") 
                    
if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=MyWindow()  
    myshow.show()  
    sys.exit(app.exec_())  