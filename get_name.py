#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:54:33 2019

@author: juschao
"""

import os


def dir_name(path):
    if os.path.isdir(path):
        dir_list = os.listdir(path)
        print(dir_list)
    else:
        print(os.path.split(path)[1])
        
while os.listdir(path):
    dir_name(path)
    
        