# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:43:54 2020

@author: Dell
"""

import sys
import re
import gzip
import shutil
import fnmatch
import os
import xlsxwriter 
from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import ignore_list as a  

DEBUG = 1
MANUAL = 0
global ignore_list_manual

sys.stdout = open("nvm_outputs.txt", "w")
page_dict={'0x00':'Generic','0x01':'Generic','0x02':'INPUTSYS','0x03':'OUTSYS','0x04':'OUTSYS','0x05':'INPUT TDC','0x06':'Clock mon sys','0x07':'Clock mon sys','0x0a':'PLLA','0x0b':'PLLB','0x0c':'PLLC','0x0d':'PLLD'}
# Get files given a path that includes a specific string
def get_only_files(path, include_str=''):
    global onlyfiles
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and include_str in f]
    return onlyfiles

   
ignore_list_manual = ['i2c.i2cw(0x69,0x09,0x00)','i2c.i2cw(0x6d,0x09,0x00)','i2c.i2cw(0x55,0x09,0x00)']

    
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def get_diffs():
    # Get the list of input and output files
    # Open files one by one and compare line by line
    # Skip comments
    # if the line contains strings from ignore_list then skip and take the next line

    import itertools
    import re
    files2check = []

    input_file_path     = r'input'
    output_file_path    = r'output'
    
    input_files     = get_only_files(input_file_path)
    output_files    = get_only_files(output_file_path)
    
    same_file_list=list(set(input_files)&set(output_files))
    input_files=same_file_list
    input_files.sort(key=natural_keys)
    output_files=same_file_list
    output_files.sort(key=natural_keys)

    
    import difflib
    text1 = open(input_file_path+'/'+input_files[0]).readlines()
    text2 = open(output_file_path+'/'+output_files[0]).readlines()
#    ignore_list=[]
#    ignore_list2display =[]
    lines_deleted = []
#                    lines_deleted.append(line1)
            
# Pop up window
    root = Tk()
    root.title('New lines')
    scrollbar = Scrollbar(root) 
    scrollbar.pack( side = RIGHT, fill = Y ) 
    mylist = Listbox(root, width=100, height=40, yscrollcommand = scrollbar.set ) 

    #Create a popup window       
    for line in a.ignore_lines: 
        mylist.insert(END, str(line)) 
    mylist.pack( side="top", fill="x", pady=10 ) 
    B1 = ttk.Button(root, text="Proceed", command = root.destroy)
    B1.pack(side = BOTTOM)
    mainloop()
        

    # if len(input_files)==len(output_files):

    for i in range(len(input_files)):
        inl_list    = []
        outl_list   = []
        found_end_of_defaults = False
        #check if the files are same before comparing
        # if input_files[i] == output_files[i]:
        file_type = ''
        if 'nvm.py' in input_files[i]: # this covers both nvm and efuse
            file_type = 'nvm'
        with open(input_file_path+'/'+input_files[i]) as fin, open(output_file_path+'/'+output_files[i]) as fout:
            if DEBUG>0:
                print('##############################################################################')
                print('comparing %s and %s'%(input_files[i],output_files[i]))
                # print('output_files=',output_files[i])                        
            if "nvm.py" in input_files[i]:
                found_end_of_defaults = True
            for line in fin:
                res = False
                if "#END OF DEFAULTS / INPUTS FROM UI RevA UI" in line:
                    found_end_of_defaults = True
                if found_end_of_defaults: 
                    inl_str=str(line)
                    skip = type(re.search('^\s',inl_str))!=type(None)
                    inl=inl_str.strip() # removing white spaces from both ends of a string
                    variable_ignore = list(filter(inl.startswith, a.ignore_variables)) != [] # ignore variables
                    if file_type == 'nvm':
                        res=any(ele in line for ele in a.ignore_register_data)
                        if res:
                            print("")
                    if inl not in a.ignore_lines:
                        if not (inl.startswith('#') or inl == '' or variable_ignore or res or skip or inl.startswith('elif')): # ignore comment lines and null lines        
                            inl_list.append(inl)
            found_end_of_defaults = False
            if "nvm.py" in output_files[i]:
                found_end_of_defaults = True
            for line in fout:
                res = False
                if "#END OF DEFAULTS / INPUTS FROM UI RevA UI" in line:
                    found_end_of_defaults = True
                if found_end_of_defaults: 
                    outl_str=str(line)
                    skip = type(re.search('^\s',outl_str))!=type(None)
                    outl=outl_str.strip() # removing white spaces from both ends of a string
                    variable_ignore = list(filter(outl.startswith, a.ignore_variables)) != [] # ignore variables
                    if file_type == 'nvm':
                        res=any(ele in line for ele in a.ignore_register_data)
                    if outl not in a.ignore_lines:
                    # if not any(outl in mystring for mystring in a.ignore_lines):
                        # if not (outl.startswith('#') or outl == '' or skip or outl.startswith('elif')):
                        if not (outl.startswith('#') or outl == '' or variable_ignore or res or skip or outl.startswith('elif')): # ignore comment lines
                            outl_list.append(outl)
            if DEBUG>2:
                print('comparing %s and %s',[input_files[i],output_files[i]])
            # if inl_list!=outl_list:
            #     diff_lines=set(inl_list)-set(outl_list)
            #     for i in diff_lines:
            #         print(i)
            #     print('##############################################################################')
            #     files2check.append(input_files[i])
                    
                    
            lines_diff=[]
            large_list=[]
            list1=[]
            comm_type=''
            if inl_list!=outl_list:
                page_append=False
                comm_type_found=False
                comm_type=''
                lines_diff=[]
                large_list=[]
                if len(inl_list)>len(outl_list):
                    mult=int(len(inl_list)-len(outl_list))
                    list1=['']*mult # making list size same
                    outl_list+=list1
                    large_list=inl_list
                if len(inl_list)<len(outl_list):
                    mult=int(len(outl_list)-len(inl_list))
                    list1=['']*mult # making list size same
                    inl_list+=list1
                    large_list=outl_list
                if len(inl_list)==len(outl_list):
                    large_list=inl_list
                for i in range(len(large_list)):
                    if not (comm_type_found):
                        if 'i2c' in large_list[i]:
                            comm_type='i2c'
                        else:
                            comm_type='spi'
                        comm_type_found=True
                        
                    if comm_type=='spi':
                        if 'time.sleep' not in large_list[i]:
                            if large_list[i]!='':
                                if '(0xff' in large_list[i]:
                                    page_append=True
                                    page=large_list[i].split(',')[1].replace(")","").strip()
                    else:    
                        if 'time.sleep' not in large_list[i]:
                            # print(large_list[i])
                            if large_list[i]!='':
                                page_line=large_list[i].split(',')[1].strip()
                                if page_line=='0xff':
                                    page = large_list[i].split(',')[2].replace(")","").strip()
                                    page_append=True
                            
                        # lines_diff.append('##### page num = %s ####'%page)
                    if outl_list[i]!=inl_list[i]:
                        if page_append:
                            lines_diff.append('##### page num = %s ####'%page)
                            lines_diff.append('---- %s ----'%page_dict[page])
                            page_append=False
                        
                        lines_diff.append(large_list[i])
            for ln in lines_diff:
                print(ln)



                        
        if len(files2check)==0:
            if DEBUG>2:
                print('Files are macthing and has no diffs')
        else:
            if DEBUG>2:
                print('***********The following files have diffs*********')
                for file in files2check:
                    print(file)
    # else:
    #     if DEBUG>2:
    #         print('***********Length of input_files and output_files do not match*********')
    #         print('***********Please fix this inorder to proceed*********')
                                        
if __name__ == "__main__": 
#    mainloop()                
    get_diffs()
    sys.stdout.close()


    
