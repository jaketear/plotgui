# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 20:30:39 2018
DataIO.py
Pattern DataIO
@author: Yan Hua
"""
import matplotlib.pyplot as plt
import pandas as pd
import time
time1=time.time()
#——————class IO_Files————————数据文件的导入导出功能
#properties：
#filename: 输入输出的文件名
#sep: 定义文件的分隔符，sep='\s+' '\t' ',' ';' 'all', 其中'all'为匹配任意分隔符
#datatype: 定义输入文件的数据类型，用于配置函数
class IO_Files(object):
    def __init__(self,filename="",sep="\s+",datatype=""):
        self.filename=filename
        self.sep=sep
        self.datatype=datatype
#all_input:一次导入整个数据文件（文件过大时会卡死），如不指定filename，sep会使用类属性        
    def all_input(self,filename="",sep=""):
        if filename=="":
            filename=self.filename
        if sep=="":
            sep=self.sep
        if filename.endswith(('.txt','.csv')):
            with open(filename,'rb') as f:
                if sep=='all':
                    df=pd.read_table(f,sep='\s+|\t|,|;',engine='python')
                else:
                    df=pd.read_table(f,sep=sep,engine='c')
        if filename.endswith(('.xls','.xlsx')):
            with open(filename,'rb') as f:
                df=pd.read_excel(f)
        return df

#chunk_input: 分段导入整个数据文件，chunksize指定每次读入的行数,返回完整的dataframe
    def chunkAll_input(self,filename="",sep="",chunksize=50000):
        if filename=="":
            filename=self.filename
        if sep=="":
            sep=self.sep
        loop = True
        #chunksize = 50000
        chunks = []
        with open(filename,'rb') as f:
            if filename.endswith(('.txt','.csv')):
                if sep=='all':
                    reader=pd.read_table(f,sep='\s+|\t|,|;',engine='python',iterator=True)
                else:
                    reader=pd.read_table(f,sep='\s+',engine='c',iterator=True)
                while loop:
                    try:
                        chunk = reader.get_chunk(chunksize)
                        chunks.append(chunk)
                    except StopIteration:
                        loop = False
                        print "Iteration is stopped."
                df = pd.concat(chunks, ignore_index=True)
            if filename.endswith(('.xls','.xlsx')):
                df=pd.read_excel(f)
        return df
    
#chunk_input: 分段导入数据文件，chunksize指定每次读入的行数，返回每一段读取的chunk
        #使用Yield使函数返回generator，可通过迭代获取yield指定的chunk，chunk为dataframe类型
    def chunk_input(self,filename="",sep="",chunksize=50000):
        if filename=="":
            filename=self.filename
        if sep=="":
            sep=self.sep
        loop=True
        with open(filename,'rb') as f:
            if filename.endswith(('.txt','.csv')):
                if sep=='all':
                    reader=pd.read_table(f,sep='\s+|\t|,|;',engine='python',iterator=True)
                else:
                    reader=pd.read_table(f,sep='\s+',engine='c',iterator=True)
                while loop:
                    try:
                        chunk = reader.get_chunk(chunksize)
                        yield chunk
                    except StopIteration:
                        loop = False
                        print "Iteration is stopped."
            if filename.endswith(('.xls','.xlsx')):
                Nskip=0
                while loop:
                        chunk=pd.read_excel(f,header=None,skiprows=Nskip,nrows=chunksize)
                        if chunk.empty:
                            break
                        Nskip+=chunksize
                        yield chunk
                    


#header_input: 仅导入数据文件的第一行即参数名行，可与 cols_input函数一起使用
    def header_input(self,filename="",sep=""): 
        if filename=="":
            filename=self.filename
        if sep=="":
            sep=self.sep
        with open(filename,'rb') as f:
            if filename.endswith(('.txt','.csv')):
                if sep=='all':
                    #Use str or object to preserve and not interpret dtype
                    df=pd.read_table(f,sep='\s+|\t|,|;',header=None,nrows=1,engine='python',dtype=object)
                    #or only input the columns index:nrows=0,remove header=None
                else:
                    df=pd.read_table(f,sep=sep,header=None,nrows=1,engine='c',dtype=object)
            if filename.endswith(('.xls','.xlsx')):
                df=pd.read_excel(f,header=None)
                df=df.iloc[0,:]  #select the first row
        return df       

#cols_input: 按列读取数据文件，cols指定参数名列表，按cols指定的参数名列读取数据    
    def cols_input(self,filename="",cols=[],sep="\s+"):  #without chunkinput now!!
        if filename=="":
            filename=self.filename
        if sep=="":
            sep=self.sep
        with open(filename,'rb') as f:
            if filename.endswith(('.txt','.csv')):
                if sep=='all':
                    df=pd.read_table(f,sep='\s+|\t|,|;',usecols=cols,engine='python')
                else:
                    df=pd.read_table(f,sep=sep,usecols=cols,engine='c')
            if filename.endswith(('.xls','.xlsx')):
                df=pd.read_excel(f,usecols=cols)
        return df

#save_file: 保存数据到文件，保存的数据格式为df:pandas dataframe或series    
    def save_file(self,filename,df,sep='\t'):
        df.to_csv(filename,sep,index=False,encoding="utf-8")

#DftoList:  将dataframe类型数据转换为二维列表[[],[],...]        
    def DftoList(self,df):
        return df.values.tolist()
    
    def config(self):
        pass



if __name__ == "__main__":
    #filename=u"D:/flightdata/FTPD-C919-10101-PD-170318-G-02-CAOWEN-664002-16.txt"
    #filename=u"D:/flightdata/FTPD-C919-10101-PD-170318-G-02-CAOWEN-664003-16.txt"
    filename=u"C:/Users/admin/Desktop/5008问题汇总.xlsx"
    iofile=IO_Files(filename)
    reader=iofile.chunk_input(chunksize=50)
    for chunk in reader:
        print chunk
    #df=all_input(filename)
    #df=header_input(filename,sep='all')
   # df=cols_input(filename,["time","HF_FSECU_1_L354_HLS_OMS_Status_Flap_Inoperative","FCM3_Voted_True_Airspeed"])
    #df=cols_input(filename,[u"日期"])
    #iofile.save_file(u"C:/Users/admin/Desktop/exp.txt",df)
    time2=time.time()
    print time2-time1        
    
   