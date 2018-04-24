# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:11:48 2018

@author: Yan Hua
"""
from PyQt5 import QtWidgets  
from ReadTree import *  
from input_function import *
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView
from plot import *  
      
class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):  
    def __init__(self):  
        super(MyWindow,self).__init__()  
        self.setupUi(self)
        self.filename=None
        self.name_time=None
        self.para=None
        
    def read(self):  
        file_name, ok=QFileDialog.getOpenFileName(self,'读取','D:/')
        if file_name:
            para_name=header_input(file_name,sep='\s+') #DataFrame: input the first row of data file
            pos=file_name.rindex('/')
            root_name=file_name[pos+1:]  #select filename without path
            self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection) #set multi select mode
            root=QtWidgets.QTreeWidgetItem(self.treeWidget) #QTreeWidgetItem object: root
            
            root.setText(0,root_name) #set text of treewidget
            para_list=para_name.values.tolist()[0] #ndarray to list
            for i in range(len(para_list)):
                child=QtWidgets.QTreeWidgetItem(root)  #child of root
                child.setText(0,para_list[i])
            self.filename=file_name  #property filename for other function use
            self.name_time=para_list[0] #name of time column
            
    def getitem(self, item,column):
        pos=self.filename.rindex('/')
        root_name=self.filename[pos+1:]
        Item_list=self.treeWidget.selectedItems()  #return the selected item as a list
        self.select_list=[]
        for ii in Item_list:
            if ii.text(0)!=root_name and ii.text(0)!=self.name_time:
                self.select_list.append(ii.text(0).encode())  #all use str here(py2)
        self.select_list.insert(0,self.name_time)  #insert the "time" column
            
    #        if item.text(0)!=root_name:
    #            self.para=[item.text(0).encode()]  #self.para for plot all use str here
    #        else:
    #            self.para=None
            
    def plot(self):
#        if self.para!=None and self.para!=[self.name_time]:
#            self.para.insert(0,self.name_time)
#            plot_para(self.filename,self.para)
        if len(self.select_list)>1:
            plot_para(self.filename,self.select_list)
    #self.textBrowser.append(df) 
        #else:
            #self.textBrowser.append("fail") 
    
    def subplot(self):
        if len(self.select_list)>1:
            subplot_para(self.filename,self.select_list)
                    
if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=MyWindow()  
    myshow.show()  
    sys.exit(app.exec_())  