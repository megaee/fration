# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:02:17 2020

@author: Dell
"""

from fractions import Fraction

# nvm_list=['Profile1_nvm.nvm.py', 'Profile2_nvm.nvm.py', 'Profile3_nvm.nvm.py', 'Profile4_nvm.nvm.py', 'Profile5_nvm.nvm.py', 'Profile9_nvm.nvm.py', 'Profile10_nvm.nvm.py', 'Profile11_nvm.nvm.py', 'Profile12_nvm.nvm.py', 'Profile13_nvm.nvm.py', 'Profile14_nvm.nvm.py', 'Profile16_nvm.nvm.py', 'Profile17_nvm.nvm.py', 'Profile18_nvm.nvm.py', 'Profile19_nvm.nvm.py', 'Profile20_nvm.nvm.py', 'Profile21_nvm.nvm.py', 'Profile22_nvm.nvm.py', 'Profile23_nvm.nvm.py', 'Profile24_nvm.nvm.py', 'Profile25_nvm.nvm.py', 'Profile26_nvm.nvm.py', 'Profile27_nvm.nvm.py', 'Profile28_nvm.nvm.py', 'Profile29_nvm.nvm.py', 'Profile30_nvm.nvm.py', 'Profile31_nvm.nvm.py', 'Profile32_nvm.nvm.py', 'Profile33_nvm.nvm.py', 'Profile34_nvm.nvm.py', 'Profile35_nvm.nvm.py', 'Profile36_nvm.nvm.py', 'Profile37_nvm.nvm.py', 'Profile38_nvm.nvm.py', 'Profile39_nvm.nvm.py', 'Profile40_nvm.nvm.py', 'Profile41_nvm.nvm.py', 'Profile42_nvm.nvm.py', 'Profile43_nvm.nvm.py', 'Profile44_nvm.nvm.py', 'Profile49_nvm.nvm.py', 'Profile50_nvm.nvm.py', 'Profile51_nvm.nvm.py', 'Profile52_nvm.nvm.py', 'Profile53_nvm.nvm.py', 'Profile54_nvm.nvm.py', 'Profile55_nvm.nvm.py', 'Profile56_nvm.nvm.py', 'Profile57_nvm.nvm.py', 'Profile58_nvm.nvm.py', 'Profile59_nvm.nvm.py', 'Profile60_nvm.nvm.py', 'Profile61_nvm.nvm.py', 'Profile62_nvm.nvm.py', 'Profile63_nvm.nvm.py', 'Profile64_nvm.nvm.py', 'Profile65_nvm.nvm.py', 'Profile66_nvm.nvm.py', 'Profile67_nvm.nvm.py', 'Profile68_nvm.nvm.py', 'Profile69_nvm.nvm.py', 'Profile70_nvm.nvm.py', 'Profile72_nvm.nvm.py', 'Profile75_nvm.nvm.py', 'Profile76_nvm.nvm.py', 'Profile78_nvm.nvm.py', 'Profile79_nvm.nvm.py', 'Profile80_nvm.nvm.py', 'Profile81_nvm.nvm.py', 'Profile82_nvm.nvm.py', 'Profile83_nvm.nvm.py', 'Profile84_nvm.nvm.py', 'Profile85_nvm.nvm.py', 'Profile87_nvm.nvm.py', 'Profile88_nvm.nvm.py', 'Profile89_nvm.nvm.py', 'Profile90_nvm.nvm.py', 'Profile91_nvm.nvm.py', 'Profile92_nvm.nvm.py', 'Profile93_nvm.nvm.py', 'Profile95_nvm.nvm.py', 'Profile96_nvm.nvm.py', 'Profile97_nvm.nvm.py', 'Profile98_nvm.nvm.py', 'Profile99_nvm.nvm.py', 'Profile102_nvm.nvm.py', 'Profile103_nvm.nvm.py', 'Profile104_nvm.nvm.py', 'Profile105_nvm.nvm.py', 'Profile106_nvm.nvm.py', 'Profile107_nvm.nvm.py', 'Profile108_nvm.nvm.py', 'Profile110_nvm.nvm.py', 'Profile111_nvm.nvm.py', 'Profile112_nvm.nvm.py', 'Profile113_nvm.nvm.py', 'Profile114_nvm.nvm.py', 'Profile115_nvm.nvm.py', 'Profile116_nvm.nvm.py', 'Profile117_nvm.nvm.py', 'Profile118_nvm.nvm.py', 'Profile119_nvm.nvm.py', 'Profile120_nvm.nvm.py', 'Profile121_nvm.nvm.py', 'Profile122_nvm.nvm.py', 'Profile123_nvm.nvm.py', 'Profile124_nvm.nvm.py', 'Profile125_nvm.nvm.py', 'Profile126_nvm.nvm.py', 'Profile127_nvm.nvm.py', 'Profile128_nvm.nvm.py', 'Profile129_nvm.nvm.py', 'Profile130_nvm.nvm.py', 'Profile131_nvm.nvm.py', 'Profile132_nvm.nvm.py', 'Profile133_nvm.nvm.py', 'Profile134_nvm.nvm.py', 'Profile135_nvm.nvm.py', 'Profile136_nvm.nvm.py', 'Profile137_nvm.nvm.py', 'Profile138_nvm.nvm.py', 'Profile139_nvm.nvm.py', 'Profile140_nvm.nvm.py', 'Profile141_nvm.nvm.py', 'Profile142_nvm.nvm.py', 'Profile143_nvm.nvm.py', 'Profile144_nvm.nvm.py', 'Profile145_nvm.nvm.py', 'Profile146_nvm.nvm.py', 'Profile147_nvm.nvm.py', 'Profile148_nvm.nvm.py', 'Profile149_nvm.nvm.py', 'Profile150_nvm.nvm.py', 'Profile151_nvm.nvm.py', 'Profile152_nvm.nvm.py', 'Profile153_nvm.nvm.py', 'Profile154_nvm.nvm.py', 'Profile155_nvm.nvm.py', 'Profile156_nvm.nvm.py', 'Profile157_nvm.nvm.py', 'Profile158_nvm.nvm.py', 'Profile159_nvm.nvm.py', 'Profile160_nvm.nvm.py', 'Profile161_nvm.nvm.py', 'Profile162_nvm.nvm.py', 'Profile163_nvm.nvm.py', 'Profile164_nvm.nvm.py', 'Profile165_nvm.nvm.py', 'Profile166_nvm.nvm.py', 'Profile167_nvm.nvm.py', 'Profile168_nvm.nvm.py', 'Profile169_nvm.nvm.py', 'Profile171_nvm.nvm.py', 'Profile172_nvm.nvm.py', 'Profile173_nvm.nvm.py', 'Profile174_nvm.nvm.py', 'Profile175_nvm.nvm.py', 'Profile176_nvm.nvm.py', 'Profile184_nvm.nvm.py', 'Profile185_nvm.nvm.py', 'Profile186_nvm.nvm.py', 'Profile187_nvm.nvm.py', 'Profile188_nvm.nvm.py', 'Profile189_nvm.nvm.py', 'Profile190_nvm.nvm.py', 'Profile191_nvm.nvm.py']
# nvm_list=['Profile100_nvm.nvm.py', 'Profile101_nvm.nvm.py', 'Profile104_nvm.nvm.py', 'Profile105_nvm.nvm.py', 'Profile106_nvm.nvm.py', 'Profile107_nvm.nvm.py', 'Profile108_nvm.nvm.py', 'Profile109_nvm.nvm.py', 'Profile10_nvm.nvm.py', 'Profile110_nvm.nvm.py', 'Profile111_nvm.nvm.py', 'Profile113_nvm.nvm.py', 'Profile114_nvm.nvm.py', 'Profile115_nvm.nvm.py', 'Profile116_nvm.nvm.py', 'Profile117_nvm.nvm.py', 'Profile118_nvm.nvm.py', 'Profile119_nvm.nvm.py', 'Profile11_nvm.nvm.py', 'Profile120_nvm.nvm.py', 'Profile121_nvm.nvm.py', 'Profile122_nvm.nvm.py', 'Profile123_nvm.nvm.py', 'Profile124_nvm.nvm.py', 'Profile125_nvm.nvm.py', 'Profile126_nvm.nvm.py', 'Profile127_nvm.nvm.py', 'Profile128_nvm.nvm.py', 'Profile129_nvm.nvm.py', 'Profile12_nvm.nvm.py', 'Profile130_nvm.nvm.py', 'Profile131_nvm.nvm.py', 'Profile132_nvm.nvm.py', 'Profile133_nvm.nvm.py', 'Profile134_nvm.nvm.py', 'Profile135_nvm.nvm.py', 'Profile136_nvm.nvm.py', 'Profile137_nvm.nvm.py', 'Profile138_nvm.nvm.py', 'Profile139_nvm.nvm.py', 'Profile13_nvm.nvm.py', 'Profile140_nvm.nvm.py', 'Profile141_nvm.nvm.py', 'Profile142_nvm.nvm.py', 'Profile143_nvm.nvm.py', 'Profile144_nvm.nvm.py', 'Profile145_nvm.nvm.py', 'Profile146_nvm.nvm.py', 'Profile147_nvm.nvm.py', 'Profile148_nvm.nvm.py', 'Profile149_nvm.nvm.py', 'Profile14_nvm.nvm.py', 'Profile150_nvm.nvm.py', 'Profile151_nvm.nvm.py', 'Profile152_nvm.nvm.py', 'Profile153_nvm.nvm.py', 'Profile154_nvm.nvm.py', 'Profile155_nvm.nvm.py', 'Profile156_nvm.nvm.py', 'Profile157_nvm.nvm.py', 'Profile158_nvm.nvm.py', 'Profile159_nvm.nvm.py', 'Profile160_nvm.nvm.py', 'Profile161_nvm.nvm.py', 'Profile162_nvm.nvm.py', 'Profile163_nvm.nvm.py', 'Profile164_nvm.nvm.py', 'Profile165_nvm.nvm.py', 'Profile166_nvm.nvm.py', 'Profile169_nvm.nvm.py', 'Profile16_nvm.nvm.py', 'Profile170_nvm.nvm.py', 'Profile171_nvm.nvm.py', 'Profile172_nvm.nvm.py', 'Profile173_nvm.nvm.py', 'Profile174_nvm.nvm.py', 'Profile175_nvm.nvm.py', 'Profile177_nvm.nvm.py', 'Profile178_nvm.nvm.py', 'Profile179_nvm.nvm.py', 'Profile17_nvm.nvm.py', 'Profile180_nvm.nvm.py', 'Profile182_nvm.nvm.py', 'Profile183_nvm.nvm.py', 'Profile184_nvm.nvm.py', 'Profile185_nvm.nvm.py', 'Profile186_nvm.nvm.py', 'Profile187_nvm.nvm.py', 'Profile188_nvm.nvm.py', 'Profile189_nvm.nvm.py', 'Profile18_nvm.nvm.py', 'Profile190_nvm.nvm.py', 'Profile191_nvm.nvm.py', 'Profile192_nvm.nvm.py', 'Profile193_nvm.nvm.py', 'Profile194_nvm.nvm.py', 'Profile195_nvm.nvm.py', 'Profile196_nvm.nvm.py', 'Profile197_nvm.nvm.py', 'Profile199_nvm.nvm.py', 'Profile19_nvm.nvm.py', 'Profile1_nvm.nvm.py', 'Profile200_nvm.nvm.py', 'Profile201_nvm.nvm.py', 'Profile202_nvm.nvm.py', 'Profile203_nvm.nvm.py', 'Profile204_nvm.nvm.py', 'Profile205_nvm.nvm.py', 'Profile206_nvm.nvm.py', 'Profile207_nvm.nvm.py', 'Profile208_nvm.nvm.py', 'Profile209_nvm.nvm.py', 'Profile20_nvm.nvm.py', 'Profile214_nvm.nvm.py', 'Profile215_nvm.nvm.py', 'Profile216_nvm.nvm.py', 'Profile217_nvm.nvm.py', 'Profile218_nvm.nvm.py', 'Profile219_nvm.nvm.py', 'Profile21_nvm.nvm.py', 'Profile220_nvm.nvm.py', 'Profile221_nvm.nvm.py', 'Profile222_nvm.nvm.py', 'Profile223_nvm.nvm.py', 'Profile224_nvm.nvm.py', 'Profile225_nvm.nvm.py', 'Profile226_nvm.nvm.py', 'Profile227_nvm.nvm.py', 'Profile228_nvm.nvm.py', 'Profile22_nvm.nvm.py', 'Profile23_nvm.nvm.py', 'Profile24_nvm.nvm.py', 'Profile25_nvm.nvm.py', 'Profile26_nvm.nvm.py', 'Profile27_nvm.nvm.py', 'Profile28_nvm.nvm.py', 'Profile29_nvm.nvm.py', 'Profile2_nvm.nvm.py', 'Profile30_nvm.nvm.py', 'Profile31_nvm.nvm.py', 'Profile32_nvm.nvm.py', 'Profile33_nvm.nvm.py', 'Profile34_nvm.nvm.py', 'Profile35_nvm.nvm.py', 'Profile36_nvm.nvm.py', 'Profile37_nvm.nvm.py', 'Profile38_nvm.nvm.py', 'Profile39_nvm.nvm.py', 'Profile3_nvm.nvm.py', 'Profile40_nvm.nvm.py', 'Profile41_nvm.nvm.py', 'Profile42_nvm.nvm.py', 'Profile43_nvm.nvm.py', 'Profile44_nvm.nvm.py', 'Profile45_nvm.nvm.py', 'Profile46_nvm.nvm.py', 'Profile47_nvm.nvm.py', 'Profile48_nvm.nvm.py', 'Profile49_nvm.nvm.py', 'Profile4_nvm.nvm.py', 'Profile50_nvm.nvm.py', 'Profile51_nvm.nvm.py', 'Profile52_nvm.nvm.py', 'Profile53_nvm.nvm.py', 'Profile54_nvm.nvm.py', 'Profile55_nvm.nvm.py', 'Profile56_nvm.nvm.py', 'Profile57_nvm.nvm.py', 'Profile58_nvm.nvm.py', 'Profile59_nvm.nvm.py', 'Profile5_nvm.nvm.py', 'Profile60_nvm.nvm.py', 'Profile61_nvm.nvm.py', 'Profile62_nvm.nvm.py', 'Profile63_nvm.nvm.py', 'Profile64_nvm.nvm.py', 'Profile65_nvm.nvm.py', 'Profile66_nvm.nvm.py', 'Profile67_nvm.nvm.py', 'Profile68_nvm.nvm.py', 'Profile69_nvm.nvm.py', 'Profile70_nvm.nvm.py', 'Profile71_nvm.nvm.py', 'Profile72_nvm.nvm.py', 'Profile73_nvm.nvm.py', 'Profile75_nvm.nvm.py', 'Profile78_nvm.nvm.py', 'Profile81_nvm.nvm.py', 'Profile82_nvm.nvm.py', 'Profile83_nvm.nvm.py', 'Profile84_nvm.nvm.py', 'Profile85_nvm.nvm.py', 'Profile86_nvm.nvm.py', 'Profile87_nvm.nvm.py', 'Profile88_nvm.nvm.py', 'Profile94_nvm.nvm.py', 'Profile95_nvm.nvm.py', 'Profile96_nvm.nvm.py', 'Profile97_nvm.nvm.py', 'Profile98_nvm.nvm.py', 'Profile99_nvm.nvm.py', 'Profile9_nvm.nvm.py']

nvm_lists=['Profile1_nvm.nvm.py', 'Profile2_nvm.nvm.py', 'Profile3_nvm.nvm.py', 'Profile4_nvm.nvm.py', 'Profile5_nvm.nvm.py', 'Profile9_nvm.nvm.py', 'Profile10_nvm.nvm.py', 'Profile11_nvm.nvm.py', 'Profile12_nvm.nvm.py', 'Profile13_nvm.nvm.py', 'Profile14_nvm.nvm.py', 'Profile16_nvm.nvm.py', 'Profile17_nvm.nvm.py', 'Profile18_nvm.nvm.py', 'Profile19_nvm.nvm.py', 'Profile20_nvm.nvm.py', 'Profile21_nvm.nvm.py', 'Profile22_nvm.nvm.py', 'Profile23_nvm.nvm.py', 'Profile24_nvm.nvm.py', 'Profile25_nvm.nvm.py', 'Profile26_nvm.nvm.py', 'Profile27_nvm.nvm.py', 'Profile28_nvm.nvm.py', 'Profile29_nvm.nvm.py', 'Profile30_nvm.nvm.py', 'Profile31_nvm.nvm.py', 'Profile32_nvm.nvm.py', 'Profile33_nvm.nvm.py', 'Profile34_nvm.nvm.py', 'Profile35_nvm.nvm.py', 'Profile36_nvm.nvm.py', 'Profile37_nvm.nvm.py', 'Profile38_nvm.nvm.py', 'Profile39_nvm.nvm.py', 'Profile40_nvm.nvm.py', 'Profile41_nvm.nvm.py', 'Profile42_nvm.nvm.py', 'Profile43_nvm.nvm.py', 'Profile44_nvm.nvm.py', 'Profile45_nvm.nvm.py', 'Profile46_nvm.nvm.py', 'Profile47_nvm.nvm.py', 'Profile48_nvm.nvm.py', 'Profile49_nvm.nvm.py', 'Profile50_nvm.nvm.py', 'Profile51_nvm.nvm.py', 'Profile52_nvm.nvm.py', 'Profile53_nvm.nvm.py', 'Profile54_nvm.nvm.py', 'Profile55_nvm.nvm.py', 'Profile56_nvm.nvm.py', 'Profile57_nvm.nvm.py', 'Profile58_nvm.nvm.py', 'Profile59_nvm.nvm.py', 'Profile60_nvm.nvm.py', 'Profile61_nvm.nvm.py', 'Profile62_nvm.nvm.py', 'Profile63_nvm.nvm.py', 'Profile64_nvm.nvm.py', 'Profile65_nvm.nvm.py', 'Profile66_nvm.nvm.py', 'Profile67_nvm.nvm.py', 'Profile68_nvm.nvm.py', 'Profile69_nvm.nvm.py', 'Profile70_nvm.nvm.py', 'Profile71_nvm.nvm.py', 'Profile72_nvm.nvm.py', 'Profile73_nvm.nvm.py', 'Profile75_nvm.nvm.py', 'Profile78_nvm.nvm.py', 'Profile81_nvm.nvm.py', 'Profile82_nvm.nvm.py', 'Profile83_nvm.nvm.py', 'Profile84_nvm.nvm.py', 'Profile85_nvm.nvm.py', 'Profile86_nvm.nvm.py', 'Profile87_nvm.nvm.py', 'Profile88_nvm.nvm.py', 'Profile94_nvm.nvm.py', 'Profile95_nvm.nvm.py', 'Profile96_nvm.nvm.py', 'Profile97_nvm.nvm.py', 'Profile98_nvm.nvm.py', 'Profile99_nvm.nvm.py', 'Profile100_nvm.nvm.py', 'Profile101_nvm.nvm.py', 'Profile104_nvm.nvm.py', 'Profile105_nvm.nvm.py', 'Profile106_nvm.nvm.py', 'Profile107_nvm.nvm.py', 'Profile108_nvm.nvm.py', 'Profile109_nvm.nvm.py', 'Profile110_nvm.nvm.py', 'Profile111_nvm.nvm.py', 'Profile113_nvm.nvm.py', 'Profile114_nvm.nvm.py', 'Profile115_nvm.nvm.py', 'Profile116_nvm.nvm.py', 'Profile117_nvm.nvm.py', 'Profile118_nvm.nvm.py', 'Profile119_nvm.nvm.py', 'Profile120_nvm.nvm.py', 'Profile121_nvm.nvm.py', 'Profile122_nvm.nvm.py', 'Profile123_nvm.nvm.py', 'Profile124_nvm.nvm.py', 'Profile125_nvm.nvm.py', 'Profile126_nvm.nvm.py', 'Profile127_nvm.nvm.py', 'Profile128_nvm.nvm.py', 'Profile129_nvm.nvm.py', 'Profile130_nvm.nvm.py', 'Profile131_nvm.nvm.py', 'Profile132_nvm.nvm.py', 'Profile133_nvm.nvm.py', 'Profile134_nvm.nvm.py', 'Profile135_nvm.nvm.py', 'Profile136_nvm.nvm.py', 'Profile137_nvm.nvm.py', 'Profile138_nvm.nvm.py', 'Profile139_nvm.nvm.py', 'Profile140_nvm.nvm.py', 'Profile141_nvm.nvm.py', 'Profile142_nvm.nvm.py', 'Profile143_nvm.nvm.py', 'Profile144_nvm.nvm.py', 'Profile145_nvm.nvm.py', 'Profile146_nvm.nvm.py', 'Profile147_nvm.nvm.py', 'Profile148_nvm.nvm.py', 'Profile149_nvm.nvm.py', 'Profile150_nvm.nvm.py', 'Profile151_nvm.nvm.py', 'Profile152_nvm.nvm.py', 'Profile153_nvm.nvm.py', 'Profile154_nvm.nvm.py', 'Profile155_nvm.nvm.py', 'Profile156_nvm.nvm.py', 'Profile157_nvm.nvm.py', 'Profile158_nvm.nvm.py', 'Profile159_nvm.nvm.py', 'Profile160_nvm.nvm.py', 'Profile161_nvm.nvm.py', 'Profile162_nvm.nvm.py', 'Profile163_nvm.nvm.py', 'Profile164_nvm.nvm.py', 'Profile165_nvm.nvm.py', 'Profile166_nvm.nvm.py', 'Profile169_nvm.nvm.py', 'Profile170_nvm.nvm.py', 'Profile171_nvm.nvm.py', 'Profile172_nvm.nvm.py', 'Profile173_nvm.nvm.py', 'Profile174_nvm.nvm.py', 'Profile175_nvm.nvm.py', 'Profile177_nvm.nvm.py', 'Profile178_nvm.nvm.py', 'Profile179_nvm.nvm.py', 'Profile180_nvm.nvm.py', 'Profile182_nvm.nvm.py', 'Profile183_nvm.nvm.py', 'Profile184_nvm.nvm.py', 'Profile185_nvm.nvm.py', 'Profile186_nvm.nvm.py', 'Profile187_nvm.nvm.py', 'Profile188_nvm.nvm.py', 'Profile189_nvm.nvm.py', 'Profile190_nvm.nvm.py', 'Profile191_nvm.nvm.py', 'Profile192_nvm.nvm.py', 'Profile193_nvm.nvm.py', 'Profile194_nvm.nvm.py', 'Profile195_nvm.nvm.py', 'Profile196_nvm.nvm.py', 'Profile197_nvm.nvm.py', 'Profile199_nvm.nvm.py', 'Profile200_nvm.nvm.py', 'Profile201_nvm.nvm.py', 'Profile202_nvm.nvm.py', 'Profile203_nvm.nvm.py', 'Profile204_nvm.nvm.py', 'Profile205_nvm.nvm.py', 'Profile206_nvm.nvm.py', 'Profile207_nvm.nvm.py', 'Profile208_nvm.nvm.py', 'Profile209_nvm.nvm.py', 'Profile214_nvm.nvm.py', 'Profile215_nvm.nvm.py', 'Profile216_nvm.nvm.py', 'Profile217_nvm.nvm.py', 'Profile218_nvm.nvm.py', 'Profile219_nvm.nvm.py', 'Profile220_nvm.nvm.py', 'Profile221_nvm.nvm.py', 'Profile222_nvm.nvm.py', 'Profile223_nvm.nvm.py', 'Profile224_nvm.nvm.py', 'Profile225_nvm.nvm.py', 'Profile226_nvm.nvm.py', 'Profile227_nvm.nvm.py', 'Profile228_nvm.nvm.py']
DEBUG=2
import sys
sys.stdout = open("output_json.txt", "w")

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
        try:
            if k not in state2:
                if DEBUG>0:
                    print (rem_path, ":")
                if new_state_added:
                    if DEBUG>0:
                        print (k + " key newly added in state2", "\n")
                else:
                    if DEBUG>0:
                        print (k + " key not in state2", "\n")
                diff_output.append(k)
        except TypeError:
            pass
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
  
    input_file_path     = r'input'
    output_file_path    = r'output'
    
    input_files     = get_only_files(input_file_path)
    input_files.sort(key=natural_keys)
    output_files    = get_only_files(output_file_path)
    output_files.sort(key=natural_keys)
    
    json_needed=[]
    dummy_nvm_list=[]
    
    # same_file_list=list((input_files)&(output_files))
    # in_files=same_file_list
    # in_files.sort(key=natural_keys)
    # out_files=same_file_list
    # out_files.sort(key=natural_keys)
    in_files=input_files
    out_files=output_files
    
    for i in range(len(in_files)):
                
            # JSON file 
        print('#############################################################################################')
        print('Processing file %s vs %s'%(in_files[i],out_files[i]))
        f1 = open (input_file_path+'//'+in_files[i]) 
        f2 = open (output_file_path+'//'+out_files[i]) 
          
        # Reading from file 
        data1 = json.load(f1) 
        data2 = json.load(f2) 
        compare_state(data1, data2)
        print('#############################################################################################')
        print("\n")
        f1.close() 
        f2.close() 

json_load()        
sys.stdout.close()
   