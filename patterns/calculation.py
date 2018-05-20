# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:15:22 2018

@author: Yan Hua
"""
class calculation(object):
    def __init__(df):
        self.df=df
    def __add__(self,other):
        self.df+other
        
def calculation(method):
    global exec(method)

method="""
a=1+2
b=cos(a)
"""
calculation(method)