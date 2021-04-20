import sys
import copy
import pprint
from fractions import Fraction
import re
import random
import json
import importlib
import os

#get working directory
working_dir=os.getcwd()

pro=0
path=working_dir+'\\json'
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
    with open(path+"\\"+files) as f:
        data = json.load(f)
    #f = open(files,"r")
    #data = json.load(f)
    new_state=data
    #new_state=copy.deepcopy(ip55.test)
############################### Made changes ###########################
    # os.rename(r''+path+'\\'+files+'',r'D:\\GUI_state_rname\\'+'Profile'+str(pro)+''+'.py')
    #print(new_state)
########################################################################
    wizard_raw={}
    wizard_raw["_appversion"]=new_state["_appversion"]
    wizard_raw["_variant"]=new_state["_variant"]
    wizard_raw["_version"]=new_state["_version"]
    wizard_raw["algorithm"]=new_state["algorithm"]
    wizard_raw["settings"]=new_state["settings"]
    # wizard_raw["birds_eye__window"] = []
    wizard_raw["user_inputs"]={}
    wizard_raw["user_inputs"]["comms"]=new_state["user_inputs"][ "comms"]
    wizard_raw["user_inputs"]["golden_clock"]=new_state["user_inputs"][ "golden_clock"]
    wizard_raw["user_inputs"]["on_the_fly"]=new_state["user_inputs"][ "on_the_fly"]
    wizard_raw["user_inputs"][ "pages"]={}
    wizard_raw["user_inputs"][ "pages"]["CRYSTAL"]={}
    wizard_raw["user_inputs"][ "pages"]["CRYSTAL"]["crystal"]=new_state["user_inputs"]["crystal"]
    # wizard_raw["user_inputs"][ "pages"]["CRYSTAL"]["image"]=[]
    wizard_raw["user_inputs"][ "pages"]["DEVICE CONFIG"]={}
    wizard_raw["user_inputs"][ "pages"][ "DEVICE CONFIG"]["acg"] = new_state["user_inputs"]["acg"]
    wizard_raw["user_inputs"][ "pages"][ "DEVICE CONFIG"]["phase_sync"] = new_state["user_inputs"]["phase_sync"]
    # wizard_raw["user_inputs"][ "pages"]["EEPROM"]={}
    # wizard_raw["user_inputs"][ "pages"]["EEPROM"] = new_state["user_inputs"]["eeprom"]
    wizard_raw["user_inputs"][ "pages"][ "GPIO"]={}
    wizard_raw["user_inputs"][ "pages"][ "GPIO"]["gpio"] = new_state["user_inputs"]["gpio"]
    wizard_raw["user_inputs"][ "pages"][ "GPIO"][ "interrupt"] = new_state["user_inputs"]["interrupt"]
    wizard_raw["user_inputs"][ "pages"][ "INPUT"]={}
    wizard_raw["user_inputs"][ "pages"][ "INPUT"][ "inputs"] = new_state["user_inputs"]["inputs"]
    wizard_raw["user_inputs"][ "pages"][ "INPUT"][ "inputs_diff"] = new_state["user_inputs"]["inputs_diff"]
    wizard_raw["user_inputs"][ "pages"][ "INPUT"][ "vdd_in"] = new_state["user_inputs"]["vdd_in"]
    wizard_raw["user_inputs"][ "pages"][ "ITDC"]= new_state["user_inputs"]["inputtdc"]
    wizard_raw["user_inputs"][ "pages"][ "OUTPUT"]= new_state["user_inputs"]["outputs"]
    wizard_raw["user_inputs"][ "pages"][ "PLL"]= new_state["user_inputs"]["plls"]
    
############################## Profile crest ###########################
    with open(working_dir+"\\json_py\\"+files,'w') as outfile: 
        json.dump(wizard_raw, outfile,indent = 2)

    
    # f = open(working_dir+"\\json_py\\"+files,'w')
    # f.write(pprint.pformat(new_state))
    # f.close()
    pro+=1
