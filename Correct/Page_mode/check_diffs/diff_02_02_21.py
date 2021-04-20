# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:57:02 2021

@author: megan
"""
import diff_nvm as diffnvm
import diff_state_json as diffjson

for a in range(0,233):
    print("Profile"+str(a))
    diffjson.json_load("Profile"+str(a))
    diffnvm.get_diffs("Profile"+str(a))
    