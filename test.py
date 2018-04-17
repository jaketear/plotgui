# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:21:33 2018

@author: admin
"""

import matplotlib.pyplot as plt
import pandas as pd
import time
time1=time.time()


#excel does not have chunk load
def all_input(f,sep='\s+'):    #sep='\s+','\t',',',';','all'
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

def chunk_input(f,sep='\s+',chunksize=50000):
    loop = True
    #chunksize = 50000
    chunks = []
    with open(filename,'rb') as f:
        if filename.endswith(('.txt','.csv')):
            if sep=='all':
                df=pd.read_table(f,sep='\s+|\t|,|;',engine='python',iterator=True)
            else:
                df=pd.read_table(f,sep='\s+',engine='c',iterator=True)
            while loop:
                try:
                    chunk = df.get_chunk(chunksize)
                    chunks.append(chunk)
                except StopIteration:
                    loop = False
                    print "Iteration is stopped."
            df = pd.concat(chunks, ignore_index=True)
        if filename.endswith(('.xls','.xlsx')):
            df=pd.read_excel(f)
    return df

def header_input(f,sep='\s+'): #input the para name first,use with col_input
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

def file_input(filename,sep='\s+',mode=0):
    mode_dict={0:header_input,1:chunk_input,2:all_input}
    if filename.endswith(('.txt','.csv','.xls','.xlsx')):
        with open(filename,'rb') as f:
            df=mode_dict.get(mode)(f,sep)

if __name__ == "__main__":
    #filename=u"D:/flightdata/FTPD-C919-10101-PD-170318-G-02-CAOWEN-664002-16.txt"
    #filename=u"D:/flightdata/FTPD-C919-10101-PD-170318-G-02-CAOWEN-664003-16.txt"
    filename=u"C:/Users/admin/Desktop/5008问题汇总.xlsx"
    df=chunk_input(filename,sep='all')
    #df=all_input(filename)
    #df=header_input(filename,sep='all')
   # df=cols_input(filename,["time","HF_FSECU_1_L354_HLS_OMS_Status_Flap_Inoperative","FCM3_Voted_True_Airspeed"])
    #df=cols_input(filename,[u"日期"])
    time2=time.time()
    print time2-time1        