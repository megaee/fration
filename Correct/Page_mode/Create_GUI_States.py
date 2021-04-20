# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:04:06 2020

@author: mega
"""
################ GUI_States ##############

################ Get number ##############

test = {'acg': {'enabled': False,
         'value': {'clock_mode': {'parsed': None, 'valid': True, 'value': ''}}}}
        
def gui_state(state):
    #read
    fr = open("number.txt",'r')
    numb = fr.read()
    fr.close()
    #write
    fw = open("number.txt",'w')
    new_num = int(numb)+1
    fw.write(str(new_num))
    print(numb)
    fw.close()
    
    ############# create_py file ############
    num = numb
    no = "Profile"+num
    nme="test"
    ash = "\n\n############################################################# "+no+" #############################################################\n\n"
    imp = "from fractions import Fraction\n"
    f = open(no+".py",'w')
    f.write(imp+ash+nme+" = "+str(state))
    f.close()

gui_state(test)


# import pprint
# def gui_states(state):
#     #read
#     fr = open("number.txt",'r')
#     numb = fr.read()
#     fr.close()
#     #write
#     fw = open("number.txt",'w')
#     new_num = int(numb)+1
#     fw.write(str(new_num))
#     print(numb)
#     fw.close()
    
#     ############# create_py file ############
#     formate = pprint.pformat(state)
#     num = numb
#     no = "Profile"+num
#     nme="test"
#     ash = "\n\n############################################################# "+no+" #############################################################\n\n"
#     imp = "from fractions import Fraction\n"
#     f = open("D:\\inputs\\"+no+".py",'w')
#     f.write(imp+ash+nme+" = "+str(formate))
#     f.close()