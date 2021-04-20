import sys
import copy
import pprint
from fractions import Fraction
import re
import random
import json
import importlib
import os

pro=231
path='D:\\zeus\\Correct\\json'
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

sys.path.insert(1,path)
def get_only_files(path, include_str=''):
    from os import listdir
    from os.path import isfile,join
    onlyfiles = [f for f in listdir(path) if isfile(join(path,f)) and include_str in f]
    return onlyfiles

input_files = get_only_files(path,include_str='.json')
for files in natural_sort(input_files):
    print(files)

    #b=files.replace('.json','')
    #ip55 = importlib.import_module(b)
    with open('D:/zeus/Correct/json/'+files) as f:
        data = json.load(f)
    #f = open(files,"r")
    #data = json.load(f)
    new_state=data["user_inputs"]
    #new_state=copy.deepcopy(ip55.test)
############################### Made changes ###########################
    # os.rename(r''+path+'\\'+files+'',r'D:\\GUI_state_rname\\'+'Profile'+str(pro)+''+'.py')
    #print(new_state)
############################## Profile crest ###########################
    no = "Profile"+str(pro)
    print(pro)
    if no+'_json.json'==files:
        print("##")
        nme = "test"
        ash = "\n\n############################################################# "+no+" #############################################################\n\n"
        imp = "from fractions import Fraction\n"
        f = open("D:\\zeus\\Correct\\json_py\\"+no+".py",'w')
        f.write(imp+ash+nme+" = "+pprint.pformat(new_state))
        f.close()
##    else:
##        pass
    pro+=1
