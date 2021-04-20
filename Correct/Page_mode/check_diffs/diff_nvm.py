# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:43:54 2020

@author: Dell
"""

import sys
import re
import ignore_list as a  
import os

DEBUG = 1
MANUAL = 0
global ignore_list_manual

sys.stdout = open("processed_data.txt", "w+")
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

def get_diffs(num):
    # Get the list of input and output files
    # Open files one by one and compare line by line
    # Skip comments
    # if the line contains strings from ignore_list then skip and take the next line
    input_index = 0
    output_index = 0
    
    print('------------------------------- NVM COMPARISON  --------------------------------')

    import re

    # Keep the input and output files in the input directory and output directory respectively
    input_file_path     = r'output_pre//nvm'
    output_file_path    = r'output//nvm'
    
    # Get list of input and output files
    input_files     = get_only_files(input_file_path)
    output_files    = get_only_files(output_file_path)
    
    # Sorting by name
    same_file_list=list(set(input_files)&set(output_files))
    input_files=same_file_list
    input_files.sort(key=natural_keys)
    output_files=same_file_list
    output_files.sort(key=natural_keys)
    
    #corrent running file
    run_file_name = num+"_nvm.nvm.py"
    # print(input_files)
    # print(output_files)
    try:
        input_index = input_files.index(run_file_name)
        output_index = output_files.index(run_file_name)
    except ValueError:
        print('************* No output files found in %s ***********'%output_file_path)
        print('--------------------------------------------------------------------------------')
        print("\n")
        print('################################################################################')
        print("\n")
        return                

    if len(output_files)>0:
        inl_list    = []
        outl_list   = []
        # i = len(input_files)-1

        
        # This is not needed since I have sorted by taking set of input and output files
        my_path = os.path.exists(output_file_path+'/'+input_files[input_index])
        if not(my_path):
            print('%s file not found in %s'%(input_files[input_index],output_file_path))
        else:
            with open(input_file_path+'/'+input_files[input_index]) as fin, open(output_file_path+'/'+output_files[output_index]) as fout:
    
                if DEBUG>0:
                    # print('------------------------------- NVM COMPARISON  --------------------------------')
                    print('comparing %s and %s'%(input_files[input_index],output_files[output_index]))
                    # print('output_files=',output_files[i])                        
                for line in fin:
                    res = False # Bool to tell if rgister data exists in the ignore list
                    inl_str=str(line)
                    skip = type(re.search('^\s',inl_str))!=type(None)
                    inl=inl_str.strip() # removing white spaces from both ends of a string
                    variable_ignore = list(filter(inl.startswith, a.ignore_variables)) != [] # ignore variables
                    res=any(ele in line for ele in a.ignore_register_data)
                    if inl not in a.ignore_lines:
                        if not (inl.startswith('#') or inl == '' or variable_ignore or res or skip or inl.startswith('elif')): # ignore comment lines and null lines        
                            inl_list.append(inl)
    
                for line in fout:
                    res = False  # Bool to tell if rgister data exists in the ignore list
                    outl_str=str(line)
                    skip = type(re.search('^\s',outl_str))!=type(None)
                    outl=outl_str.strip() # removing white spaces from both ends of a string
                    variable_ignore = list(filter(outl.startswith, a.ignore_variables)) != [] # ignore variables
                    res=any(ele in line for ele in a.ignore_register_data)
                    if outl not in a.ignore_lines:
                    # if not any(outl in mystring for mystring in a.ignore_lines):
                        # if not (outl.startswith('#') or outl == '' or skip or outl.startswith('elif')):
                        if not (outl.startswith('#') or outl == '' or variable_ignore or res or skip or outl.startswith('elif')): # ignore comment lines
                            outl_list.append(outl)
                if DEBUG>2:
                    print('comparing %s and %s',[input_files[input_index],output_files[output_index]])                    
                        
    
                # Process data
                lines_diff=[]
                large_list=[]
                list1=[]
                comm_type=''
                if inl_list!=outl_list:
                    page_append=False
                    comm_type_found=False
                    comm_type=''
                    lines_deleted = False # This is to check if lines are deleted in the output file
                    lines_added = False # This is to check if new lines are added in the output file
                    lines_modified = False
                    lines_diff=[]
                    large_list=[]
                    if len(inl_list)>len(outl_list):
                        large_list = inl_list
                        lines_deleted = True
                    if len(inl_list)<len(outl_list):
                        large_list = outl_list
                        lines_added = True
                    if len(inl_list)==len(outl_list):
                        large_list = outl_list
                        lines_modified = True
                    
                    j=0 # remember line number
                    for i in range(len(large_list)):
                        if not (comm_type_found):
                            if 'i2c' in large_list[i]:
                                comm_type='i2c'
                                comm_type_found=True
                            if 'spi' in large_list[i]:
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
                            
                        if lines_deleted:
                            try: # To avoid list out of range error
                                if inl_list[i+j]!=outl_list[i]:
                                    if page_append:
                                        lines_diff.append('##### page num = %s ####'%page)
                                        try:
                                            lines_diff.append('---- %s ----'%page_dict[page])
                                        except:
                                            lines_diff.append('##### page key not found ####')
                                        page_append=False
                                    lines_diff.append(outl_list[i])
                                
                                    if inl_list[i+j+1]==outl_list[i+1]:
                                        pass
                                    else:
                                        # Checking if next line is same else append all lines that are added
                                        str1="Following lines are missing in the output file"
                                        lines_diff.append(str1)                            
                                        while inl_list[i+j+1]!=outl_list[i+1]:
                                            lines_diff.append(inl_list[i+j+1])
                                            j+=1
                            except:
                                pass
                            
                        
                        if lines_added:
                            try: # To avoid list out of range error
                                if outl_list[i+j]!=inl_list[i]:
                                    if page_append:
                                        lines_diff.append('##### page num = %s ####'%page)
                                        try:
                                            lines_diff.append('---- %s ----'%page_dict[page])
                                        except:
                                            lines_diff.append('##### page key not found ####')
                                        page_append=False
                                    lines_diff.append(outl_list[i+j])
                                    
                                    if outl_list[i+j+1]==inl_list[i+1]:
                                        pass
                                    else:
                                        # Checking if next line is same else append all lines that are added
                                        str1="Following lines are added newly in the output file"
                                        lines_diff.append(str1)                           
                                        while outl_list[i+j+1]!=inl_list[i+1]:
                                            lines_diff.append(outl_list[i+j+1])
                                            j+=1
                            except:
                                pass
                                
                        if lines_modified:
                            try: # To avoid list out of range error
                                if outl_list[i]!=inl_list[i]:
                                    if page_append:
                                        lines_diff.append('##### page num = %s ####'%page)
                                        try:
                                            lines_diff.append('---- %s ----'%page_dict[page])
                                        except:
                                            lines_diff.append('##### page key not found ####')
                                        page_append=False
                                    lines_diff.append(outl_list[i])
                            except:
                                pass
                else:
                    print("No diff found")
                            
                for ln in lines_diff:
                    print(ln)        
    # else:
    #     print('***********Length of input_files and output_files do not match*********')
    #     print('***********Please fix this inorder to proceed*********')
    print('--------------------------------------------------------------------------------')
    print("\n")
    print('################################################################################')
    print("\n")

                                        
# if __name__ == "__main__": 
#     sys.stdout = open("nvm_outputs.txt", "w")
# get_diffs()
    # sys.stdout.close()


    
