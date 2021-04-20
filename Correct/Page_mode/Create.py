# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:51:33 2020

@author: mega
"""
#profile_create
import pprint
import random
#profile={}

widgt = ['acg', 'comms', 'crystal', 'eeprom', 'golden_clock', '!gpio', '!inputs', 'inputs_diff', 'inputtdc', 'interrupt', 'on_the_fly', '!outputs', 'phase_sync', '!plls']

inputs_names=['0P','0N','1P','1N','2P','2N','3P','3N','4P','4N','OCXO','INTSYNC']
inputs_names4out=['0P','0N','1P','1N','2P','2N','3P','3N','4P','4N']
pll_names=['A','B','C','D','FT']
pll_names4out=['A','B','C','D']

enabled = [False,True]
valid = True
#acg
agc_value = ['00','01','10','11']
#comms
comms_type = ['i2c','spi']
address = '0x5B'
spi_wires = [3,4]
#crystal
crystal_mode=['EX TCXO (AC)','LFF CL=8pF','LFF CL=12pF','EX TCXO (DC)']
#eeprom
eeprom_addr = ['0','1','2','3','4','5','6','7']
eeprom_type=[64,128,256,512,1024]

################## #ACG_8 ###################
# for enable in enabled:
#     for value in agc_value:
#         if not enable:
#             value = ''
#         profile = {'acg':{'enabled': enable,
#             'value': {'clock_mode': {'value': value}}}}
#         pprint.pprint(profile)


################ #comms_4 ###################
# for typ in comms_type:
#     for wires in spi_wires:
#         profile = {'i2c': {'address': {'value': '0x5B'}},
#                   'spi': {'wires': wires},
#                   'type': typ}
#         pprint.pprint(profile)

################ #crystal_25 ################
# for enable in enabled:
#     for mode in crystal_mode:
#         for freq in [25,250,random.randrange(25,250)]:
#             if enable:
#                 freq = freq//2
#             else:
#                 freq = freq
#             profile = {'doubler': enable,
#                         'freq': {'value': str(freq)+'MHz'},
#                         'mode': mode}
#             pprint.pprint(profile)

############## # eeprom_249 ################
# for addr in eeprom_addr:
#     for typ in eeprom_type:
#         for block_id in range(1,typ//64+1):
#             profile = {'addr': {'value': addr},
#                         'ibus': None,
#                         'type': typ,
#                         'verify': {'block': {'value': str(block_id)}}}
#             pprint.pprint(profile)

############ #golden_clock ################
#golden_clock = 'xtal'

########### #inputs_diff_10 ###############
#profile = {'0P': False,'1P': False,'2P': False,'3P': False,'4P': False}
#for enable in enabled:
#    for diff in ['0P','1P','2P','3P','4P']:
#        profile[diff] = enable
#        pprint.pprint(profile)

############## #on_the_fly ###############
#profile = {'enabled': False, 'value': {'multi': [], 'single': []}}

############# #phase_sync_16 ################
#profile = {'enabled': False,
#            'value': {'A': False, 'B': False, 'C': False, 'D': False}}
#for enable in enabled:
#    profile['enabled']=enable
#    for enab in enabled:
#        for pll in ['A','B','C','D']:
#            profile['value'][pll] = enab
#            print(profile)


########################## #interrupt ##############################

#interrupt: ['eeprom','input_closs','input_coarse_drift','input_fine_drift','pll_ho_freeze','pll_inner_lol','pll_outer_lol','pll_phase_lol','tdc']
##inputs_names=['0P','0N','1P','1N','2P','2N','3P','3N','4P','4N','OCXO','INTSYNC']
##pll_names=['A','B','C','D','FT']
##pll_names4out=['A','B','C','D']

####### input_closs ######

#eeprom = {'defect_interrupt': False}
#for enable in enabled:
#    eeprom['defect_interrupt'] = enable
#    print(eeprom)

############### input_closs#input_coarse_drift#input_coarse_drift#input_fine_drift ###############
#input_closs = {'0N': False,'0P': False,'1N': False,'1P': False,'2N': False,'2P': False,'3N': False,'3P': False,'4N': False,'4P': False,'INTSYNC': False,'OCXO': False}      
#input_coarse_drift = {'0N': False,'0P': False,'1N': False,'1P': False,'2N': False,'2P': False,'3N': False,'3P': False,'4N': False,'4P': False,'INTSYNC': False,'OCXO': False}
#input_fine_drift = {'0N': False,'0P': False,'1N': False,'1P': False,'2N': False,'2P': False,'3N': False,'3P': False,'4N': False,'4P': False,'INTSYNC': False,'OCXO': False}

#for enable in enabled:
#    for inp in inputs_names:
#        input_closs[inp] = enable
#        input_coarse_drift[inp] = enable
#        input_fine_drift[inp] = enable
#        print(input_closs)
#        print(input_coarse_drift)
#        print(input_fine_drift)

#pll_ho_freeze = {'A': False,'B': False,'C': False,'D': False,'FT': False}
#pll_inner_lol = {'A': False,'B': False,'C': False,'D': False,'FT': False,'common': False}
#pll_outer_lol = {'A': False,'B': False,'C': False,'D': False,'FT': False}
#pll_phase_lol = {'A': False,'B': False,'C': False,'D': False,'FT': False}

#for enable in enabled:
#    for pll in pll_names:
#        pll_ho_freeze[pll] = enable
#        pll_outer_lol[pll] = enable
#        pll_phase_lol[pll] = enable
#        print(pll_ho_freeze)
#        print(pll_outer_lol)
#        print(pll_phase_lol)

#for enable in enabled:
#    for pll in ['A','B','C','D','FT','common']:
#        pll_inner_lol[pll] = enable
#        print(pll_inner_lol)

#tdc = {'A': False, 'B': False, 'C': False, 'D': False}
#for enable in enabled:
#    for pll in pll_names4out:
#        tdc[pll] = enable
#        print(tdc)
    
######################## #inputtdc ##############################

inputs_names4out=['0P','0N','1P','1N','2P','2N','3P','3N','4P','4N']
output_names9out = ['0','1','2','3','4','5','6','7','8','9']
nsamples = [0,1,2,3,4,5,6,7,8,9,10,11]
edges = []
#inputtdc = ['edge','tdcs']
################ #edge ###########
#edges = []
edge = {'0N': 'Rising',
        '0P': 'Rising',
        '1N': 'Rising',
        '1P': 'Rising',
        '2N': 'Rising',
        '2P': 'Rising',
        '3N': 'Rising',
        '3P': 'Rising',
        '4N': 'Rising',
        '4P': 'Rising'}
for edg in ['Rising', 'Falling']:
    for inp in inputs_names4out:
        edge[inp] = edg
        print(edge)
print(set(edges))

########## #tdcs ################
        
#inp_tdc = {'enabled': False,
#            'value': {'clk1': {'parsed': None,
#                                'value': ''},
#                      'clk2': {'parsed': None,
#                                'value': ''},
#                      'nsamples': {'parsed': 11,
#                                    'value': '11'}}}
#for enable in enabled:
#    if not enable:
#        print(inp_tdc)
#    if enable:
#        for clk1 in inputs_names4out:
#            for clk2 in inputs_names4out:
#                for ns in nsamples:
#                    inp_tdcs = {'enabled': enable,
#                            'value': {'clk1': {'parsed': clk1,
#                                                'value': clk1},
#                                      'clk2': {'parsed': clk2,
#                                                'value': clk2},
#                                      'nsamples': {'parsed': ns,
#                                                    'value': str(ns)}}}
#                    print(inp_tdcs)

########################## #inputs ###############################

