# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:21:19 2021

@author: megan
"""
import pprint
import json
with open("Position_pages.json") as file:
    new_state = json.load(file)
    
wizard_raw={}
wizard_raw["birds_eye__window"] = []
wizard_raw["comms"]=new_state[ "comms"]
wizard_raw["golden_clock"]=new_state[ "golden_clock"]
wizard_raw["on_the_fly"]=new_state[ "on_the_fly"]
wizard_raw[ "pages"]={}
wizard_raw[ "pages"]["CRYSTAL"]={}
wizard_raw[ "pages"]["CRYSTAL"]["crystal"]=new_state["crystal"]
wizard_raw[ "pages"]["CRYSTAL"]["image"]=[]
wizard_raw[ "pages"]["DEVICE CONFIG"]={}
wizard_raw[ "pages"][ "DEVICE CONFIG"]["acg"] = new_state["acg"]
wizard_raw[ "pages"][ "DEVICE CONFIG"]["phase_sync"] = new_state["phase_sync"]
wizard_raw[ "pages"]["EEPROM"]={}
wizard_raw[ "pages"]["EEPROM"] = new_state["eeprom"]
wizard_raw[ "pages"][ "GPIO"]={}
######################################################################
new_state["gpio"]["vdd"]={'parsed': 1.8,
                             'valid': True,
                             'value': new_state["gpio"]["vdd"]}
wizard_raw[ "pages"][ "GPIO"]["gpio"] = new_state["gpio"]

wizard_raw[ "pages"][ "GPIO"][ "interrupt"] = new_state["interrupt"]
wizard_raw[ "pages"][ "INPUT"]={}
######################################################################
for inp in ['0N', '0P', '1N', '1P', '2N', '2P', '3N', '3P', '4N', '4P', 'INTSYNC', 'OCXO']:
    for sc in ['set', 'clr']:
        for cf in ['drift_coarse', 'drift_fine']:
            new_state['inputs'][inp]['value'][cf]['value'][sc] = {'parsed': new_state['inputs'][inp]['value'][cf]['value'][sc],
                                                                  'valid': True,
                                                                  'value': new_state['inputs'][inp]['value'][cf]['value'][sc]}
wizard_raw[ "pages"][ "INPUT"][ "inputs"] = new_state["inputs"]
wizard_raw[ "pages"][ "INPUT"][ "inputs_diff"] = new_state["inputs_diff"]
wizard_raw[ "pages"][ "INPUT"][ "vdd_in"] = new_state["vdd_in"]
wizard_raw[ "pages"][ "ITDC"]= new_state["inputtdc"]
for inp in ['0N', '0P', '1N', '1P', '2N', '2P', '3N', '3P', '4N', '4P', 'INTSYNC', 'OCXO']:
    pop_valid_timer = wizard_raw[ "pages"][ "INPUT"][ "inputs"][inp]["value"].pop("valid_timer")
    wizard_raw[ "pages"][ "INPUT"][ "inputs"][inp]["value"]["clock_switch"]["valid_timer"] = pop_valid_timer

######################################################################
for oup in ['0', '1', '10', '11', '2', '3', '4', '5', '6', '7', '8', '9']:        
    new_state['outputs']['value'][oup]['value']['vddo'] = {'parsed': 1.8,
                                                           'valid': True,
                                                           'value': new_state['outputs']['value'][oup]['value']['vddo']}
wizard_raw[ "pages"][ "OUTPUT"]= new_state["outputs"]
wizard_raw[ "pages"][ "PLL"]= new_state["plls"]
# create_new(wizard_raw,pro)

no = "Position"

f = open("D:\\zeus\\Correct\\positions\\"+no+".json",'w')
f.write(pprint.pformat(wizard_raw))
f.close()
