# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:49:18 2015

@author: Jorge
"""

import os

#configurations
source = './fixed_name/'
destination = './text/'

#cleaning filename, remove spaces
def rem_space(filename):
    return ''.join(filename.split())


file_list = os.listdir(source)

def iterdir():
    for i in range(len(file_list)):
        os.popen('pdf2txt.py -o ' + destination + file_list[i] + '.txt ' + source + file_list[i])
        print ('done ' + file_list[i])
    print(' ......All done ...')
    
#run-it       
iterdir()
