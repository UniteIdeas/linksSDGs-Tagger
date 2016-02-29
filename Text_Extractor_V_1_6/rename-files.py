# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:49:18 2015

@author: Jorge
"""

import os

#configurations
source = './originals/'
destination = './fixed_name/'

#cleaning filename, remove spaces
def rem_space(filename):
    return ''.join(filename.split())


file_list = os.listdir(source)

def iterdir():
    for i in range(len(file_list)):
        os.rename(source + file_list[i] , destination + rem_space(file_list[i]))
    print(' ......done removing whitespace from filenames ...')
    
#run-it       
iterdir()
