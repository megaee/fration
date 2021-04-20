import sys
import re
import copy
from fractions import Fraction
import pprint
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
path="C:\zeus\Correct\input_017"
sys.path.insert(1,path)
pro=0
def get_only_files(path, include_str=''):
    from os import listdir
    from os.path import isfile,join
    onlyfiles = [f for f in listdir(path) if isfile(join(path,f)) and include_str in f]
    return onlyfiles

def create_new(new_state,pro):
    ############################## Profile  ###########################
    no = "Profile"+str(pro)
    nme="test"
    ash = "\n\n############################################################# "+no+" #############################################################\n\n"
    imp = "from fractions import Fraction\n"
    f = open("C:\\zeus\\Correct\\input_017\\"+no+".py",'w')
    f.write(imp+ash+nme+" = "+pprint.pformat(new_state))
    f.close()


input_files = get_only_files(path,include_str='.py')
for files in natural_sort(input_files):
    print(files)
    import importlib
    import os

    b=files.replace('.py','')
    ip55 = importlib.import_module(b)
    new_state=copy.deepcopy(ip55.test)
############################### Made changes ###########################
   ##    os.rename(r''+path+'\\'+files+'',r'D:\\zeus\\Currect\\New folder\\'+'Profile'+str(pro)+''+'.py')
##    if pro >= 9:
##        new_state['crystal']['doubler'] = True
##    'plls': {'A': {'enabled': False,
##                    'valid': True,
##                    'value': {'dco': {'enabled': False, 'value': 'fast'},
    
    for pll in ['A','B','C','D','FT']:
##        if pll=='A':
##            if pro<150:
##                new_state['plls'][pll]['value']['dco']['enabled']=False
##            if pro>=150:
##                new_state['plls'][pll]['value']['dco']['value']="slow"
##                
##        if pll=='B':
##            if pro<177:
##                new_state['plls'][pll]['value']['dco']['enabled']=False
##                
##        if pll=='C':
##            if pro<178:
##                new_state['plls'][pll]['value']['dco']['enabled']=False
##            if pro>=178:
##                new_state['plls'][pll]['value']['dco']['value']="slow"
##                
##        if pll=='D':
##            if pro<180:
##                new_state['plls'][pll]['value']['dco']['enabled']=False
##        
##        if pll=='FT':
##            if pro<48:
##               new_state['plls'][pll]['value']['dco']['enabled']=False
##            if pro>=48:
##                new_state['plls'][pll]['value']['dco']['value']="slow"
##        print(new_state['plls'][pll]['value']['free_running']['value']['dco'])
##        del new_state['plls'][pll]['value']['free_running']['value']['dco']
##        new_state['plls'][pll]['value']['dco']={'enabled': True, 'value': 'fast'}
##        if pll=='C' and pro>177:
##            new_state['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['value']['phase_delta']['value']='75 ns'
        print(new_state['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['value']['phase_delta']['value'])
##    create_new(new_state,pro)
    
    pro+=1
