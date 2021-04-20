# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:02:17 2020

@author: Dell
"""

from fractions import Fraction
DEBUG=2
import sys
sys.stdout = open("output_json.txt", "w+")

def get_only_files(path, include_str=''):
    global onlyfiles
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and include_str in f]
    return onlyfiles
    

def pairs(d):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from pairs(v)
        else:
            yield '{}={}'.format(k, v)

def nested_keys(d):
    for k, v in d.items():
        if isinstance(v, dict):
            yield '{}'.format(k)
            yield from nested_keys(v)
        else:
            yield '{}'.format(k)


def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)
    
def diff_dic(state1, state2, new_state_added,rem_path=""):
    diff_output =[]
    for k in state1:
        if (k not in state2):
            if DEBUG>0:
                print (rem_path, ":")
            if new_state_added:
                if DEBUG>0:
                    print (k + " key newly added in state2", "\n")
            else:
                if DEBUG>0:
                    print (k + " key not in state2", "\n")
            diff_output.append(k)
        else:
            if type(state1[k]) is dict:
                if rem_path == "":
                    new_path = k
                else:
                    new_path = rem_path + "->" + k
                # myfirsttime=True
                #     rem_list.append(k)
                    
                diff_ret = diff_dic(state1[k],state2[k],new_state_added, new_path)
                diff_output.extend(diff_ret)
            else:
                if state1[k] != state2[k]:
                    if DEBUG>0:
                        print (rem_path, ":")
                        print (" - ", k," : ", state1[k])
                        print (" + ", k," : ", state2[k])
                    diff_output.extend([rem_path+'->' if rem_path!= '' else '' +k])
    return diff_output

# diff_dic(dict1, dict2, new_state_added=False)

def compare_state(dict1, dict2, rem_path=""):
    

    # step 0: Compare 2 dictionaries
        # If same return Null and quit
    # step 1: Find if any keys are different
      # - report the keys and no further processing of these keys
      # We will only compare the key that are in both
    if dict1==dict2:
        return
    else:
        
        keys_state1=list(nested_keys(dict1)) # Get keys of state1
        keys_state2=list(nested_keys(dict2)) # Get keys of state2
        
        # step 1: Find if any keys are different
          # - report the keys and no further processing of these keys
        if len(keys_state2)>len(keys_state1):
            new_state_added=True
        if len(keys_state2)<len(keys_state1):
            new_state_added=False
        if len(keys_state2)==len(keys_state1):
            new_state_added=False
            
        if not(new_state_added):
            a = diff_dic(dict1, dict2, new_state_added,rem_path="")
            if DEBUG>3:
                print(f'Final a = {a}')
        else:
            a = diff_dic(dict2, dict1, new_state_added,rem_path="")
            if DEBUG>3:
                print(f'Final a = {a}')
    return a

# compare_state(dict1, dict2)            
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def json_load():
    ''' Function used to load json'''
    import json 
  
    input_file_path     = r'output_pre//json'
    output_file_path    = r'output//json'
    
    input_files     = get_only_files(input_file_path)
    input_files.sort(key=natural_keys)
    output_files    = get_only_files(output_file_path)
    output_files.sort(key=natural_keys)
    
    json_needed=[]
    dummy_nvm_list=[]
    
    same_file_list=list(set(input_files)&set(output_files))
    in_files=same_file_list
    in_files.sort(key=natural_keys)
    out_files=same_file_list
    out_files.sort(key=natural_keys)
    
    
    # for i in range(len(in_files)):
                
    # JSON file 
    print('##############################################################################')
    print('Processing file %s vs %s'%(in_files[-1],out_files[-1]))
    f1 = open (input_file_path+'//'+in_files[-1]) 
    f2 = open (output_file_path+'//'+out_files[-1]) 
      
    # Reading from file 
    data1 = json.load(f1) 
    data2 = json.load(f2) 
    compare_state(data1, data2)
    print('##############################################################################')
    print("\n")
    f1.close() 
    f2.close() 

# json_load()        
    # sys.stdout.close()
   