# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:11:48 2018

@author: Yan Hua
"""
from PyQt5 import QtWidgets  
from ReadTree import *  
from input_function import *
from PyQt5.QtWidgets import QFileDialog
from plot import *  
      
class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):  
    def __init__(self):  
        super(MyWindow,self).__init__()  
        self.setupUi(self)  
    def read(self):  
        file_name, ok=QFileDialog.getOpenFileName(self,'读取','D:/')
        if file_name:
            para_name=header_input(file_name,sep='\s+') #DataFrame: input the first row of data file
            pos=file_name.rindex('/')
            root_name=file_name[pos+1:]  #select filename without path
            root=QtWidgets.QTreeWidgetItem(self.treeWidget) #QTreeWidgetItem object: root
            root.setText(0,root_name) #set text of treewidget
            para_list=para_name.values.tolist()[0] #ndarray to list
            for i in range(len(para_list)):
                child=QtWidgets.QTreeWidgetItem(root)  #child of root
                child.setText(0,para_list[i])
            self.filename=file_name  #property filename for other function use
            
    def getitem(self, item,column):
        pos=self.filename.rindex('/')
        root_name=self.filename[pos+1:]
        if item.text(0)!=root_name:
            self.para=[item.text(0).encode()]  #self.para for plot all use str here
        else:
            self.para=None
            
    def plot(self):
        if self.para!=None and self.para!=['time']:
            plot_para(self.filename,self.para)
    #self.textBrowser.append(df) 
        #else:
            #self.textBrowser.append("fail") 
                    
if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=MyWindow()  
    myshow.show()  
    sys.exit(app.exec_())  