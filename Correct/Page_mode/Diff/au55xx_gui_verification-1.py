# -*- coding: utf-8 -*-

################################################################################
# |             Copyright (c) 2020 AURA Semiconductor Pvt.Ltd.                 #
# |                     ALL RIGHTS RESERVED                                    #
# ============================================================================ #
# | HISTORY  |                                                                 #
# +--------------------------------------------------------------------------- #
# |Who       : Harsha Vardhan Reddy A                                          #
# |When [YMD]: 20200831                                                        #
# |What      :                                                                 #
# +--------------------------------------------------------------------------- #
################################################################################

# Display setting 1080x800
import pyautogui as ptg
import subprocess
# import inputs_55 as ip55
import os
import re
import sys
# import opencv_python
ptg.PAUSE = 0.5
import time
import importlib


import importlib.util


print(ptg.position()) # To get the Position of mouse(x,y)

import importlib
import glob
import math
import copy

global inputs_covered
global outputs_covered
global plls_covered

import diff_state_json as diffjson
import diff_nvm as diffnvm

# ip55=''

# ip55 = importlib.import_module('Profile1')
# mod.HelloWorld()


# from .input.Profile1 import test




fin0_freq = "8Mhz"
i2c_add = "0x69"
fb = '4k'
nb = '100'
fout_freq = "160M"
num_ip = 4
num_op = 1
pll_names=['A','B','C','D','FT']
pll_names4out=['A','B','C','D']

clock_type_dict={'':0,'Differential':0,'Single Ended AC':1,'Single Ended DC':2}
vddo={'':0,'1.8V':-2,'2.5V':-1,'3.3V':0}
op_mode={'':0,'LVDS':0,'LVPECL':1,'CML':2,'HCSL':3,'LVPECL2':4}
ip_clock_selection={'':0,'Auto':0,'Manual':1}
lockl_delay = {'':0,'1 ms':1,'4 ms':0,'16 ms':-1,'65 ms':-2,'262 ms':-3,'1 s':-4,'4 s':-5,'16 s':-6}
# lockl_delay = {'1.02ms':0,'4.10ms':-1,'16.38ms':-2,'65.53ms':-3,'262.14ms':-4,'1.05s':-5,'4.19s':-6,'16.77s':-7}
ho_delay = {'':0,'547 ms':0,'2.188 s':-1,'8.75 s':-2,'35 s':-3,'137 ms':1,'34 ms':2,'9 ms':3,'2 ms':4}
ho_average = {'':0,'1.094 s':0,'4.375 s':-1,'17.5 s':-2,'70 s':-3,'273 ms':1,'68 ms':2,'17 ms':3,'4 ms':4}
ppm_set={'':0,'4 ppm':0,'2 ppm':-1,'0.4 ppm':-2,'0.2 ppm':-3,'1 ppb':-4,'0.5 ppb':-5,'0.1 ppb':-6,'0.05 ppb':-7,'20 ppm':1,'40 ppm':2,'200 ppm':3,'400 ppm':4,'2000 ppm':5,'4000 ppm':6}
ppm_clear={'':0,'4 ppm':1,'2 ppm':0,'0.4 ppm':-1,'0.2 ppm':-2,'1 ppb':-3,'0.5 ppb':-4,'0.1 ppb':-5,'0.05 ppb':-6,'20 ppm':2,'40 ppm':3,'200 ppm':4,'400 ppm':5,'2000 ppm':6,'4000 ppm':7}
# ppm_clear={'2':0,'0.4':-1,'0.2':-2,'200':1}
# phase_prop_slope={'Bandwidth':0,'128 us/s':1,'32 us/s':2,'8 us/s':3,'4 us/s':4,'2 us/s':5,'0.5 us/s':6,'0.25 us/s':7,'0.125 us/s':8,'62.5 ns/s':9,'31.25 ns/s':10,'15.62 ns/s':11,'7.8 ns/s':12,'4 ns/s':13,'2 ns/s':14,'1 ns/s':15}

phase_prop_slope={'Bandwidth':0,'128 us/s':1,'32 us/s':2,'8 us/s':3,'4 us/s':4,'2 us/s':5,'1 us/s':6,'0.5 us/s':7,'0.25 us/s':8,'0.125 us/s':9,'62.5 ns/s':10,'31.25 ns/s':11,'15.62 ns/s':12,'7.8 ns/s':13,'4 ns/s':14,'2 ns/s':15,'1 ns/s':16} 

freq_ramp_slope={'':0,'0.2 ppm/s':0,'2 ppm/s':1,'20 ppm/s':2,'200 ppm/s':3,'2000 ppm/s':4,'20000 ppm/s':5,'40000 ppm/s':6}
xtal_mode={'':0,'LFF CL=8pF':0,'EX TCXO (AC)':-1,'LFF CL=12pF':1,'EX TCXO (DC)':2}

trigger_edge={'':0,'5':0,'4':-1,'3':-2,'2':-3,'1':-4,'6':1,'7':2,'8':3,'9':4,'10':5,'11':6,'12':7,'13':8,'14':9,'15':10,'16':11}
Clear_edge={'':0,'4':0,'3':-1,'2':-2,'1':-3,'5':-4,'6':1,'7':2,'8':3,'9':4,'10':5,'11':6,'12':7,'13':8,'14':9,'15':10,'16':11}
val_time={'':0,'2 ms':-1,'128 ms':0,'256 ms':1,'1 s':2,'4 s':3,'32 s':4,'64 s':5,'128 s':6}

zdm_ext_feedback={'':0,'0P':0,'0N':1,'1P':2,'1N':3,'2P':4,'2N':5,'3P':6,'3N':7,'4P':8,'4N':9}
zdm_ext_output = {'':0,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'11':11}

flexio_defect_notify={'':0,'None':0,'Clock Monitoring Defect':1,'All Notify':2,'Clock Monitoring Notify':3,'PLL Notify':4,'Interrupt':5}
clock_monitoring_def_opt={'':0,'fd_fine:1':0,'fd_fine:2':1,'coarse_fd_status:1':2,'coarse_fd_status:2':3,'clock_loss_status:1':4,'clock_loss_status:2':5,'clock_loss_fd_status:1':6,'clock_loss_fd_status:2':7}

phase_lock_loss_delay={"4 ms":0,	"1 s":1,	"2 s":2,	"3 s":3,	"4 s":4,	"5 s":5,	"6 s":6,	"7 s":7,	"8 s":8,	"9 s":9,	"10 s":10,	"11 s":11,	"12 s":12,	"13 s":13,	"14 s":14,	"15 s":15,	"16 s":16,	"17 s":17,	"18 s":18,	"19 s":19,	"20 s":20,	"21 s":21,	"22 s":22,	"23 s":23,	"24 s":24,	"25 s":25,	"26 s":26,	"27 s":27,	"28 s":28,	"29 s":29,	"30 s":30,	"31 s":31,	"32 s":32,	"33 s":33,	"34 s":34,	"35 s":35,	"36 s":36,	"37 s":37,	"38 s":38,	"39 s":39,	"40 s":40,	"41 s":41,	"42 s":42,	"43 s":43,	"44 s":44,	"45 s":45,	"46 s":46,	"47 s":47,	"48 s":48,	"49 s":49,	"50 s":50,	"51 s":51,	"52 s":52,	"53 s":53,	"54 s":54,	"55 s":55,	"56 s":56,	"57 s":57,	"58 s":58,	"59 s":59,	"60 s":60,	"61 s":61,	"62 s":62,	"63 s":63,	"64 s":64,	"65 s":65,	"66 s":66,	"67 s":67,	"68 s":68,	"69 s":69,	"70 s":70,	"71 s":71,	"72 s":72,	"73 s":73,	"74 s":74,	"75 s":75,	"76 s":76,	"77 s":77,	"78 s":78,	"79 s":79,	"80 s":80,	"81 s":81,	"82 s":82,	"83 s":83,	"84 s":84,	"85 s":85,	"86 s":86,	"87 s":87,	"88 s":88,	"89 s":89,	"90 s":90,	"91 s":91,	"92 s":92,	"93 s":93,	"94 s":94,	"95 s":95,	"96 s":96,	"97 s":97,	"98 s":98,	"99 s":99,	"100 s":100,	"101 s":101,	"102 s":102,	"103 s":103,	"104 s":104,	"105 s":105,	"106 s":106,	"107 s":107,	"108 s":108,	"109 s":109,	"110 s":110,	"111 s":111,	"112 s":112,	"113 s":113,	"114 s":114,	"115 s":115,	"116 s":116,	"117 s":117,	"118 s":118,	"119 s":119,	"120 s":120,	"121 s":121,	"122 s":122,	"123 s":123,	"124 s":124,	"125 s":125,	"126 s":126,	"127 s":127,	"128 s":128,	"129 s":129,	"130 s":130,	"131 s":131,	"132 s":132,	"133 s":133,	"134 s":134,	"135 s":135,	"136 s":136,	"137 s":137,	"138 s":138,	"139 s":139,	"140 s":140,	"141 s":141,	"142 s":142,	"143 s":143,	"144 s":144,	"145 s":145,	"146 s":146,	"147 s":147,	"148 s":148,	"149 s":149,	"150 s":150,	"151 s":151,	"152 s":152,	"153 s":153,	"154 s":154,	"155 s":155,	"156 s":156,	"157 s":157,	"158 s":158,	"159 s":159,	"160 s":160,	"161 s":161,	"162 s":162,	"163 s":163,	"164 s":164,	"165 s":165,	"166 s":166,	"167 s":167,	"168 s":168,	"169 s":169,	"170 s":170,	"171 s":171,	"172 s":172,	"173 s":173,	"174 s":174,	"175 s":175,	"176 s":176,	"177 s":177,	"178 s":178,	"179 s":179,	"180 s":180,	"181 s":181,	"182 s":182,	"183 s":183,	"184 s":184,	"185 s":185,	"186 s":186,	"187 s":187,	"188 s":188,	"189 s":189,	"190 s":190,	"191 s":191,	"192 s":192,	"193 s":193,	"194 s":194,	"195 s":195,	"196 s":196,	"197 s":197,	"198 s":198,	"199 s":199,	"200 s":200,	"201 s":201,	"202 s":202,	"203 s":203,	"204 s":204,	"205 s":205,	"206 s":206,	"207 s":207,	"208 s":208,	"209 s":209,	"210 s":210,	"211 s":211,	"212 s":212,	"213 s":213,	"214 s":214,	"215 s":215,	"216 s":216,	"217 s":217,	"218 s":218,	"219 s":219,	"220 s":220,	"221 s":221,	"222 s":222,	"223 s":223,	"224 s":224,	"225 s":225,	"226 s":226,	"227 s":227,	"228 s":228,	"229 s":229,	"230 s":230,	"231 s":231,	"232 s":232,	"233 s":233,	"234 s":234,	"235 s":235,	"236 s":236,	"237 s":237,	"238 s":238,	"239 s":239,	"240 s":240,	"241 s":241,	"242 s":242,	"243 s":243,	"244 s":244,	"245 s":245,	"246 s":246,	"247 s":247,	"248 s":248,	"249 s":249,	"250 s":250,	"251 s":251,	"252 s":252,	"253 s":253,	"254 s":254,	"255 s":255
}


# swing={'':0,'0.1 V':0,'0.2 V':1,'0.3 V':2,'0.4 V':3,'0.5 V':4,'0.6 V':5,'0.7 V':6,'0.8 V':7}
# swing={'':0,'0.5 V':0,'0.54 V':1,'0.58 V':2,'0.62 V':3,'0.66 V':4,'0.68 V':5,'0.7 V':6,'0.72 V':7}
# swing={'':0,'0.05 V':0,'0.1 V':1,'0.15 V':2,'0.2 V':3,'0.25 V':4,'0.3 V':5,'0.35 V':6,'0.4 V':7}
# swing={'':0,'0.5 V':0,'0.55 V':1,'0.6 V':2,'0.64 V':3,'0.68 V':4,'0.72 V':5,'0.76 V':6,'0.8 V':7}
# swing={'':0,'0.5 V':0,'0.55 V':1,'0.6 V':2,'0.64 V':3,'0.68 V':4,'0.72 V':5,'0.76 V':6,'0.8 V':7}

swing={'LVDS':{'':0,'0.1 V':0,'0.2 V':1,'0.3 V':2,'0.4 V':3,'0.5 V':4,'0.6 V':5,'0.7 V':6,'0.8 V':7},
        'LVPECL':{'':0,'0.5 V':0,'0.54 V':1,'0.58 V':2,'0.62 V':3,'0.66 V':4,'0.68 V':5,'0.7 V':6,'0.72 V':7},
        'CML':{'':0,'0.05 V':0,'0.1 V':1,'0.15 V':2,'0.2 V':3,'0.25 V':4,'0.3 V':5,'0.35 V':6,'0.4 V':7},
        'HCSL':{'':0,'0.5 V':0,'0.55 V':1,'0.6 V':2,'0.64 V':3,'0.68 V':4,'0.72 V':5,'0.76 V':6,'0.8 V':7},
        'LVPECL2':{'':0,'0.5 V':0,'0.55 V':1,'0.6 V':2,'0.64 V':3,'0.68 V':4,'0.72 V':5,'0.76 V':6,'0.8 V':7}}

gpio_op=['0','1','2','3','4','5','9']
gpio_pll_config=['pll:A','pll:B','pll:C','pll:D']

gpio_sel={'general_purpose_inp':0,'pll_dco_sel0':1,'pll_dco_sel1':2,'pll_dco_sel2':3,
          'dco_incr':4,'dco_decr':5,'oe_b':6,'ext_clk_in_switch':7,
          'man_in_sel0':8,'man_in_sel1':9,'man_in_sel2':10,
          'man_in_sel3':11,'man_in_spare_sel_pllA':12,
          'man_in_spare_sel_pllB':13,'man_in_spare_sel_pllC':14,
          'man_in_spare_sel_pllD':15,'sysref_trigger':16,'divo_restart':17,'pll_syncb_sel0':18,
          'pll_syncb_sel1':19,'pll_syncb_sel2':20,'syncb_trigger':21,'phase_adjst_trigger':22,
          'force_exit_eeprom':23,'clk_in_disqlfy':24}

gpio_op_sel={"general_purpose_out":0,	"all_ntfy":1,	"all_pll_clkmon_ntfy":2,	"all_eeprom_ntfy":3,	"all_tdc_data_ready_ntfy":4,	"all_pll_ntfy":5,	"all_pll_ho_freeze_ntfy":6,	"all_pll_inner_ll_ntfy":7,	"all_pll_outer_ll_ntfy":8,	"all_pll_phase_ll_ntfy":9,	"all_clkmon_ntfy":10,	"all_clkmon_fine_drift_ntfy":11,	"all_clkmon_coarse_drift_ntfy":12,	"all_clkmon_clockloss_ntfy":13,	"interrupt_b_w":14,	"eeprom_read_done_ntfy":15,	"eeprom_read_done_timeout_deft_ntfy_i":16,	"start_timeout_deft_ntfy":17,	"data_deft_ntfy":18,	"stop_deft_ntfy":19,	"start_deft_ntfy":20,	"crc_deft_ntfy":21,	"arb_lost_deft_ntfy":22,	"paged_deft_ntfy":23,	"devd_deft_ntfy":24,	"eeprom_size_deft_ntfy":25,	"word_add_deft_ntfy":26,	"dev_add_deft_ntfy":27,	"eeprom_read_done_timeout_deft":28,	"start_timeout_deft":29,	"data_deft":30,	"stop_deft":31,	"start_deft":32,	"crc_deft":33,	"arb_lost_deft":34,	"paged_deft":35,	"devd_deft":36,	"eeprom_size_deft":37,	"word_add_deft":38,	"dev_add_deft":39,	"xo_loss":40,	"xo_loss_ntfy":41,	"clockloss_clk_0P_ntfy":42,	"clockloss_clk_0N_ntfy":43,	"clockloss_clk_1P_ntfy":44,	"clockloss_clk_1N_ntfy":45,	"clockloss_clk_2P_ntfy":46,	"clockloss_clk_2N_ntfy":47,	"clockloss_clk_3P_ntfy":48,	"clockloss_clk_3N_ntfy":49,	"clockloss_clk_4P_ntfy":50,	"clockloss_clk_4N_ntfy":51,	"clockloss_clk_OCXO_ntfy":52,	"clockloss_clk_INTSYNC_ntfy":53,	"clockloss_clk_0P":54,	"clockloss_clk_0N":55,	"clockloss_clk_1P":56,	"clockloss_clk_1N":57,	"clockloss_clk_2P":58,	"clockloss_clk_2N":59,	"clockloss_clk_3P":60,	"clockloss_clk_3N":61,	"clockloss_clk_4P":62,	"clockloss_clk_4N":63,	"clockloss_clk_OCXO":64,	"clockloss_clk_INTSYNC":65,	"fine_drift clk_0P_ntfy":66,	"fine_drift clk_0N_ntfy":67,	"fine_drift clk_1P_ntfy":68,	"fine_drift clk_1N_ntfy":69,	"fine_drift clk_2P_ntfy":70,	"fine_drift clk_2N_ntfy":71,	"fine_drift clk_3P_ntfy":72,	"fine_drift clk_3N_ntfy":73,	"fine_drift clk_4P_ntfy":74,	"fine_drift clk_4N_ntfy":75,	"fine_drift clk_OCXO_ntfy":76,	"fine_drift clk_INTSYNC_ntfy":77,	"coarse_drift clk_0P_ntfy":78,	"coarse_drift clk_0N_ntfy":79,	"coarse_drift clk_1P_ntfy":80,	"coarse_drift clk_1N_ntfy":81,	"coarse_drift clk_2P_ntfy":82,	"coarse_drift clk_2N_ntfy":83,	"coarse_drift clk_3P_ntfy":84,	"coarse_drift clk_3N_ntfy":85,	"coarse_drift clk_4P_ntfy":86,	"coarse_drift clk_4N_ntfy":87,	"coarse_drift clk_OCXO_ntfy":88,	"coarse_drift clk_INTSYNC_ntfy":89,	"fine_drift clk_0P":90,	"fine_drift clk_0N":91,	"fine_drift clk_1P":92,	"fine_drift clk_1N":93,	"fine_drift clk_2P":94,	"fine_drift clk_2N":95,	"fine_drift clk_3P":96,	"fine_drift clk_3N":97,	"fine_drift clk_4P":98,	"fine_drift clk_4N":99,	"fine_drift clk_OCXO":100,	"fine_drift clk_INTSYNC":101,	"coarse_drift clk_0P":102,	"coarse_drift clk_0N":103,	"coarse_drift clk_1P":104,	"coarse_drift clk_1N":105,	"coarse_drift clk_2P":106,	"coarse_drift clk_2N":107,	"coarse_drift clk_3P":108,	"coarse_drift clk_3N":109,	"coarse_drift clk_4P":110,	"coarse_drift clk_4N":111,	"coarse_drift clk_OCXO":112,	"coarse_drift clk_INTSYNC":113,	"clockloss_with_fd_deft_clk_0P":114,	"clockloss_with_fd_deft_clk_0N":115,	"clockloss_with_fd_deft_clk_1P":116,	"clockloss_with_fd_deft_clk_1N":117,	"clockloss_with_fd_deft_clk_2P":118,	"clockloss_with_fd_deft_clk_2N":119,	"clockloss_with_fd_deft_clk_3P":120,	"clockloss_with_fd_deft_clk_3N":121,	"clockloss_with_fd_deft_clk_4P":122,	"clockloss_with_fd_deft_clk_4N":123,	"clockloss_with_fd_deft_clk_OCXO":124,	"clockloss_with_fd_deft_clk_INTSYNC":125,	"cmonpll_inner_ll_ntfy_i":126,	"cmonpll_inner_ll_i":127}
itdc_edg_inp = ['0P','0N','1P','1N','2P','2N','3P','3N','4P','4N']
itdc_edg = {'Rising':0,'Falling':1}
itdc_op=['0','1','2','3','4','5','6','7','8','9']
itdc_clock = {'0N':0,'0P':1,'1N':2,'1P':3,'2N':4,'2P':5,'3N':6,'3P':7,'4N':8,'4P':9}

pll_names=['A','B','C','D','FT']
pll_names4out=['A','B','C','D']
pll_names_inner=['A','B','C','D','FT','common']
interrupt_pll=["pll_outer_lol","pll_inner_lol","pll_ho_freeze","pll_phase_lol"]
interrupt_input = ['input_closs','input_fine_drift','input_coarse_drift']
interrupt_inp_sel=['0P','0N','1P','1N','2P','2N','3P','3N','4P','4N','OCXO','INTSYNC']

eeprom_type={64:0,128:1,256:2,512:3,1024:4}
block_id={'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'11':10,'12':11,'13':12,'14':13,'15':14,'16':15}
sdco_tx = ['ppath','rx1','rx2']
sdco_sl = {'0.12 ppb/s':-7,'0.98 ppb/s':-6,'7.8 ppb/s':-5,'125 ppb/s':-4,'1 ppm/s':-3,'8 ppm/s':-2,'128 ppm/s':-1,'1024 ppm/s':0}



variant ='au5518'
board_connected=False

working_dir=os.getcwd()


##### Make directories #######
output_dir=working_dir+'//'+'output'
nvm_dir=output_dir+'//'+'nvm'
json_dir=output_dir+'//'+'json'
error_images_dir=output_dir+'//'+'error_images'

try:
    os.makedirs(output_dir)
except FileExistsError:
    # directory already exists
    pass

try:
    os.makedirs(nvm_dir)
except FileExistsError:
    # directory already exists
    pass
try:
    os.makedirs(json_dir)
except FileExistsError:
    # directory already exists
    pass
try:
    os.makedirs(error_images_dir)
except FileExistsError:
    # directory already exists
    pass

###############################

def get_only_files(path, include_str=''):
    # global onlyfiles
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and include_str in f]
    return onlyfiles




def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


def reset_what2run():
    what2run= {'order_in':False,'real_time':False,'comms':False,'inputs':False,'outputs':False,  
                'plls':False,'crystal':False,'acg':False,'gpio':False,'eeprom':False,'inputtdc':False,
                'inputs_diff':False,'interrupt':False,'phase_sync':False}       
    return what2run

def  mapchange2run(what2change): #['crystal->freq->', 'golden_clock']
    # use the diff of dictionaries to create the update parameters to run
    key_changed={}
    for line in what2change:
        line_split=line.split('->')[0]
        key_changed[line_split]=True
    return key_changed

class RUN_GUI:
    def __init__(self):
        start_time = time.time()
        self._changeframe()
        time.sleep(2)
        
        
        global inputs_covered
        global outputs_covered
        global plls_covered
        import sys
        import copy
        import diff_state
        # # insert at 1, 0 is the script path (or '' in REPL)
        sys.path.insert(1, working_dir+'//'+'input')
        
        # import Profile1 as ip55
        # self.reset_dropdown(222,780,255,255) #x=192, y=779
            

        if variant == 'au5518':
            path=working_dir+'\\'+'input'
            input_files = get_only_files(path, include_str='') # Get all file names
            input_files.sort(key=natural_keys) # soting file names since I want all files to be executed in order
            current_state={}
            inputs_covered=[]
            outputs_covered=[]
            plls_covered=[]
            
            for file in input_files:
                # TODO: Use logger
                print(file)
                what2run = reset_what2run()
                import importlib
                # sys.path.append('input')
                a=file.replace('.py','')
                # import mod as ip55
                ip55 = importlib.import_module(a)
                
                # Load the new state
                new_state = copy.deepcopy(ip55.test)
                # diff current_state with new_state to get what is new from the diff state
                # compare_state(dict1, dict2, rem_path="")
                what2change = diff_state.compare_state(current_state, new_state,rem_path="")
                # Depending on what is  - use the first key in the list of key differences - to enable the corresponding what2run dictionary
                if what2change:
                    increment = mapchange2run(what2change)
                    what2run.update(increment)
                    # current_state = new_state
                    # run_config with what2run and current_state                 
                    self.run_config(new_state,current_state,a,what2run,save_json=True,save_nvm=True)
                    current_state = copy.deepcopy(new_state)
                else:
                    print("New state and current state are the same")
                    print("GUI test is not performed for %s"%file)
               ######### get difference ##########
                diffjson.json_load()
                diffnvm.get_diffs()

        print("--- %s seconds ---" % (time.time() - start_time))        
        print(ptg.position())
        self._changeframe()
        sys.exit()

    def _changeframe(self):
        ptg.hotkey('alt', 'tab')
        
    def _minframe(self):
        ptg.hotkey('win', 'down')

    def _maxframe(self):
        ptg.hotkey('win', 'up')


    # def generate_pos(self,widget_list,start_x,start_y,change_x): # This is mainly for input, output and pll page
    #     widget_list=['0N','0P','1P','1N','2P','2N','3P','3N','4P','4N','OCXO','INTSYNC']
    #     pos_dict={}
    #     for i in widget_list:
    #         pos_dict[i]['x']=
    #         pos_dict[i]['y']=start_y
            
            
    def point_position(pself, position, clicks):
        ptg.moveTo(position)
        ptg.click(clicks=clicks)
        
                     
    def otf_ctrl(self,init_x,init_y,dump_path,freq_list=['2M','3M','4M','10.2M',fout_freq],remove_freq=False,remove_all_freq=False,Shuffle_freq=False): #x=911, y=699
        self.point_position((init_x,init_y), 1)
        self.point_position((init_x+33,init_y+27), 1)
        for i in freq_list:
            self.point_position((init_x-272,init_y-157), 1)
            ptg.typewrite("%s"%i)
            self.point_position((init_x-168,init_y-157), 1)
        if remove_freq:
            self.point_position((init_x-276,init_y-374), 1)
            self.point_position((init_x-161,init_y-397), 1)
        if remove_all_freq:
            self.point_position((init_x-216,init_y-400), 1)
        if Shuffle_freq:
            self.point_position((init_x-276,init_y-374), 1)
            self.point_position((init_x-159,init_y-227), 1)
            
        # Dump Fly
        self.point_position((init_x+120,init_y+27), 1)
        ptg.typewrite(dump_path)
        ptg.press('enter')
        ptg.press('enter')
        
    
    def otf_save(self,init_x,init_y,ip_path,filename): # input and output will be dumped in the same directory
        self.load_save(ip_path,filename,init_x,init_y) #488,716
        
        # x=1326, y=911 dump fly buttom
        ptg.moveTo(init_x+563,init_y+12)
        timeout = time.time() + 30 # 30 seconds
        dump_fly = None
        while dump_fly is None:
            dump_fly=ptg.locateOnScreen(working_dir+"\\"+"images\\dump_fly.PNG",grayscale=True,confidence=.5)
            if dump_fly or time.time() > timeout:
                break
        if dump_fly:
            self.point_position((init_x+563,init_y+12), 1)
        
        timeout = time.time() + 30 # 30 seconds
        dump_folder = None
        while dump_folder is None:
            dump_folder=ptg.locateOnScreen(working_dir+"\\"+"images\\dump_folder.PNG",grayscale=True,confidence=.5)
            if dump_folder or time.time() > timeout:
                break
        if dump_folder:
            ptg.typewrite(ip_path)
            ptg.press('enter')
            time.sleep(2) # 2seconds
            ptg.press('enter')
        # incase file has to be replaced
        replace = None
        timeout = time.time() + 10 # 10 seconds
        while replace is None:
            replace=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.5)
            if replace or time.time() > timeout:
                break
        if replace:
            ptg.press('left')
            ptg.press('enter')
        
        # change fout Dyn #
        change_fout_dyn = None
        timeout = time.time() + 10 # 10 seconds
        ptg.moveTo(init_x+686,init_y+11)
        while change_fout_dyn is None:
            change_fout_dyn=ptg.locateOnScreen(working_dir+"\\"+"images\\change_fout_dyn.PNG",grayscale=True,confidence=.5)
            if change_fout_dyn or time.time() > timeout:
                break
        if change_fout_dyn:
            self.point_position((init_x+664,init_y+11), 1)
            self.point_position((init_x+71,init_y-297), 1) # Output Pin
            ptg.press('enter')
            self.point_position((init_x+193,init_y-297), 1)
            ptg.press('enter')
            self.point_position((init_x+157,init_y-264), 1)
            
    def screen_enable(self,init_x,init_y,delay,state_enabled=False):
        state_enabled=False
        ptg.moveTo(init_x,init_y)
        connection_blue= None
        timeout = time.time() + delay # 20 seconds
        while connection_blue is None:
            connection_blue=ptg.locateOnScreen(working_dir+"\\"+"images\\connection_blue.PNG",grayscale=True,confidence=.5)
            if connection_blue or time.time() > timeout:
                break
        if connection_blue:
            state_enabled=True
        else:
            state_enabled=False
        return state_enabled

    def backend_warning(self,delay,backend_warning_appear=False):
        backend_warning_appear=False
        backend_warning= None
        timeout = time.time() + delay # 20 seconds
        while backend_warning is None:
            backend_warning=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.8)
            if backend_warning or time.time() > timeout:
                break
        if backend_warning:
            backend_warning_appear=True
        else:
            backend_warning_appear=False
        return backend_warning_appear
     
    
    def err_appear(self,delay,err_state=False):
        err_state=False
        validation_err= None
        timeout = time.time() + delay # 20 seconds
        while validation_err is None:
            validation_err=ptg.locateOnScreen(working_dir+"\\"+"images\\validation_err.PNG",grayscale=True,confidence=.8)
            if validation_err or time.time() > timeout:
                break
        if validation_err:
            err_state=True
        else:
            err_state=False
        return err_state

    def save_image(self,filename):
        image = ptg.screenshot()
        image.save(working_dir+"\\"+"output"+"\\"+"error_images\\"+filename+".PNG")
        time.sleep(2)

        

    def dummy_send2chip(self,init_x,init_y,filename): #x=1872, y=64
        self.point_position((init_x,init_y), 1)
        time.sleep(3)
        
        
        if board_connected:
            programming_successful= None
            timeout = time.time() + 10 # 20 seconds
            while programming_successful is None:
                programming_successful=ptg.locateOnScreen(working_dir+"\\"+"images\\programming_successful.PNG",grayscale=True,confidence=.8)
                if programming_successful or time.time() > timeout:
                    break
            if programming_successful:
                print('------Valid state------')
                ptg.press('enter')
                
                
            else:
                validation_err= None
                timeout = time.time() + 10 # 20 seconds
                while validation_err is None:
                    validation_err=ptg.locateOnScreen(working_dir+"\\"+"images\\validation_err.PNG",grayscale=True,confidence=.8)
                    if validation_err or time.time() > timeout:
                        break
                if validation_err:
                    image = ptg.screenshot()
                    image.save(working_dir+"\\"+"output"+"\\"+"error_images\\"+filename+".PNG")
                    time.sleep(2)
                    print('------Invalid state------')
                    time.sleep(2)
                    ptg.press('enter')
                else:
                    backend_warning= None
                    timeout = time.time() + 10 # 20 seconds
                    while backend_warning is None:
                        backend_warning=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.8)
                        if backend_warning or time.time() > timeout:
                            break
                    if backend_warning:
                        print('------Warning ignored------')
                        ptg.press('left')
                        ptg.press('enter')
                    backend_warning= None
                    timeout = time.time() + 3 # 20 seconds
                    while backend_warning is None:
                        backend_warning=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.8)
                        if backend_warning or time.time() > timeout:
                            break
                    if backend_warning:
                        print('------Warning ignored------')
                        ptg.press('left')
                        ptg.press('enter')
    
                    programming_successful= None
                    timeout = time.time() + 10 # 20 seconds
                    while programming_successful is None:
                        programming_successful=ptg.locateOnScreen(working_dir+"\\"+"images\\programming_successful.PNG",grayscale=True,confidence=.8)
                        if programming_successful or time.time() > timeout:
                            break
                    if programming_successful:
                        print('------Valid state------')
                        ptg.press('enter')
                     
                    validation_err= None
                    timeout = time.time() + 5 # 20 seconds
                    while validation_err is None:
                        validation_err=ptg.locateOnScreen(working_dir+"\\"+"images\\validation_err.PNG",grayscale=True,confidence=.8)
                        if validation_err or time.time() > timeout:
                            break
                    if validation_err:
                        image = ptg.screenshot()
                        image.save(working_dir+"\\"+"output"+"\\"+"error_images\\"+filename+".PNG")
                        time.sleep(2)
    
                        print('------Invalid state------')
                        print('------Backend warning------')
                        time.sleep(2)
                        ptg.press('enter')
        # else:

        #     reset_state=self.screen_enable(init_x-1782,init_y,5,reset_enabled=False)
        #     if reset_state:
        #         print('------Valid state------')

        #     else:
        #         err_appear_state=self.err_appear(5,err_state=False)
        #         if err_appear_state:
        #             self.save_image(filename)
        #             print('------>Invalid state<------')
        #             ptg.press('enter')
        #         else:
        #             backend_warning_state=self.backend_warning(10,backend_warning_appear=False)
        #             if backend_warning_state:
        #                 print('------Warning ignored------')
        #                 ptg.press('left')
        #                 ptg.press('enter')
        #             reset_state=self.screen_enable(init_x-88,init_y,5,reset_enabled=False)
        #             if reset_state:
        #                 print('------Valid state------')
                        
        #             else:
        #                 backend_warning_state=self.backend_warning(3,backend_warning_appear=False)
        #                 if backend_warning_state:
        #                     print('------Warning ignored------')
        #                     ptg.press('left')
        #                     ptg.press('enter')
        #                 reset_state=self.screen_enable(init_x-88,init_y,5,reset_enabled=False)
        #                 if reset_state:
        #                     print('------Valid state------')
        #                 else:
        #                     err_appear_state=self.err_appear(5,err_state=False)
        #                     if err_appear_state:
        #                         self.save_image(filename)
        #                         print('------>Invalid state<------')
        #                         ptg.press('enter')
        #                     else:
        #                         print('------Valid state------')
                    
                
        else:
            self.point_position((init_x-541,init_y+949), 1)
            save_user_profile= None
            timeout = time.time() + 5 # 20 seconds
            while save_user_profile is None:
                save_user_profile=ptg.locateOnScreen(working_dir+"\\"+"images\\dump_file.PNG",grayscale=True,confidence=.8)
                if save_user_profile or time.time() > timeout:
                    break
            # time.sleep(2) # wait for window to respond
            if save_user_profile:
                ptg.press('esc')
                
            else:   
                err_appear_state=self.err_appear(3,err_state=False)
                if err_appear_state:
                    self.save_image(filename)
                    print('------>Invalid state<------')
                    ptg.press('enter')
                else:
                    backend_warning_state=self.backend_warning(3,backend_warning_appear=False)
                    if backend_warning_state:
                        self.save_image(filename)
                        print('------Warning ignored------')
                        ptg.press('left')
                        ptg.press('enter')
                    backend_warning_state=self.backend_warning(3,backend_warning_appear=False)                    
                    if backend_warning_state:
                        self.save_image(filename)
                        print('------Warning ignored------')
                        ptg.press('left')
                        ptg.press('enter')
    
                    err_appear_state=self.err_appear(3,err_state=False)
                    if err_appear_state:
                        self.save_image(filename)
                        print('------>Invalid state<------')
                        ptg.press('enter')
                    
                    
            
    def save_op(self,path,filename,init_x,init_y): #x=1872,65
        # path=r'C:\Users\Dell\Desktop\gui_test'
        
        # ptg.moveTo(init_x,init_y)
        # send2chip_blue= None
        # timeout = time.time() + 15 # 20 seconds
        # while send2chip_blue is None:
        #     send2chip_blue=ptg.locateOnScreen(working_dir+"\\"+"images\\send2chip_blue.PNG",grayscale=True,confidence=.5)
        #     if send2chip_blue or time.time() > timeout:
        #         break
        # if send2chip_blue:        
        
        self.point_position((init_x,init_y), 1)


        ###################################
        update_config_variable= None
        timeout = time.time() + 5 # 5 seconds
        while update_config_variable is None:
            update_config_variable=ptg.locateOnScreen(working_dir+"\\"+"images\\update_config_variable.PNG",grayscale=True,confidence=.5)
            if update_config_variable or time.time() > timeout:
                break
        if update_config_variable:
            self.point_position((init_x-806,init_y+131), 1)
        ###################################

        # assuming if backend warnings doesn't pop up in 10s save window will open
        backend_warn=False
        save_file= None
        timeout = time.time() + 15 # 20 seconds
        while save_file is None:
            save_file=ptg.locateOnScreen(working_dir+"\\"+"images\\save_file.PNG",grayscale=True,confidence=.5)
            if save_file or time.time() > timeout:
                break
        if save_file:
            ptg.typewrite(path+'\\'+filename)
            ptg.press('enter')
            
        else:
            backend_warn=True
        
        
        if backend_warn:
            backend_warning= None
            timeout = time.time() + 20 # 20 seconds
            while backend_warning is None:
                backend_warning=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.5)
                if backend_warning or time.time() > timeout:
                    break
            if backend_warning:
                ptg.press('left')
                ptg.press('enter')
                
                ###################################
                update_config_variable= None
                timeout = time.time() + 5 # 5 seconds
                while update_config_variable is None:
                    update_config_variable=ptg.locateOnScreen(working_dir+"\\"+"images\\update_config_variable.PNG",grayscale=True,confidence=.2)
                    if update_config_variable or time.time() > timeout:
                        break
                if update_config_variable:
                    x, y = ptg.locateCenterOnScreen(working_dir+"\\"+"images\\update_config_variable.PNG")
                    # button7point = ptg.center(working_dir+"\\"+"images\\update_config_variable.PNG")
                    # print('button7point=',button7point)
                    
                    self.point_position((init_x-806,init_y+131), 1)
                ###################################

                save_file= None
                timeout = time.time() + 20 # 20 seconds
                while save_file is None:
                    save_file=ptg.locateOnScreen(working_dir+"\\"+"images\\save_file.PNG",grayscale=True,confidence=.5)
                    if save_file or time.time() > timeout:
                        break
                if save_file:
                    ptg.typewrite(path+'\\'+filename)
                    ptg.press('enter')
            else:
                invalid_state= None
                timeout = time.time() + 20 # 20 seconds
                while invalid_state is None:
                    invalid_state=ptg.locateOnScreen(working_dir+"\\"+"images\\invalid_state.PNG",grayscale=True,confidence=.5)
                    if invalid_state or time.time() > timeout:
                        break
                if invalid_state:
                    print('Invalid state found')
                    
        

        # incase file has to be replaced
        replace = None
        timeout = time.time() + 5 # 5 seconds
        while replace is None:
            replace=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.5)
            if replace or time.time() > timeout:
                break
        if replace:
            ptg.press('left')
            ptg.press('enter')
            
            
        if board_connected:
            # wait until programming successful comes
            prg_successful = None
            timeout = time.time() + 60 # 20 seconds
            while prg_successful is None:
                prg_successful=ptg.locateOnScreen(working_dir+"\\"+"images\\programming_successful.PNG",grayscale=True,confidence=.8)
                if prg_successful or time.time() > timeout:
                    break
            if prg_successful:
                print('Programming successful')
                ptg.press('enter')
            else:
                print('Chip communication error')
                print('Could not save the output file')
                print('Programming chip was not successful')
        else: #1212,80
            ptg.moveTo(init_x,init_y+932)
            load_enabled = None
            timeout = time.time() + 60 # 20 seconds
            while load_enabled is None:
                load_enabled=ptg.locateOnScreen(working_dir+"\\"+"images\\load_enabled.PNG",grayscale=True,confidence=.8)
                if load_enabled or time.time() > timeout:
                    break
            if load_enabled:
                print('Programming successful') 
            else:
                print('Could not save the output file')
        # else:
        #     print('Send to chip button was not active/Gui took too long to respond')
            
        
            
    def load_save(self,ip_path,filename,init_x,init_y,op_path=''): #488,716
        self.point_position((init_x,init_y), 1)
        load_screen=None
        timeout = time.time() + 20 # 20 seconds
        while load_screen is None:
            load_screen=ptg.locateOnScreen(working_dir+"\\"+"images\\load_file.PNG",grayscale=True,confidence=.5)
            if load_screen or time.time() > timeout:
                break

        if load_screen:
            ptg.typewrite(ip_path+'\\'+filename)
            ptg.press('enter')
            
        send2chip= None
        timeout = time.time() + 20 # 20 seconds
        backend_warn=False
        ptg.moveTo(init_x+724,init_y-635)
        # ptg.moveTo(init_x+917,init_y-789)
        while send2chip is None:
            send2chip=ptg.locateOnScreen(working_dir+"\\"+"images\\send_to_chip_blue.PNG",grayscale=True,confidence=.9)
            if send2chip or time.time() > timeout:
                break

        if send2chip:
            # path=r'F:\Automate_GUI\output_files'
            # self.save_op(path,filename+'_op',init_x+902,init_y-796)
            if op_path:
                self.save_op(op_path,filename+'_op',init_x+724,init_y-635)
            else:
                self.save_op(ip_path,filename+'_op',init_x+724,init_y-635)
            
        else:
            backend_warn=True
            
        if backend_warn:
            backend_warning= None
            timeout = time.time() + 10 # 10 seconds
            while backend_warning is None:
                backend_warning=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.5)
                if backend_warning or time.time() > timeout:
                    break
            if backend_warning:
                ptg.press('enter')
    
                send2chip= None
                timeout = time.time() + 20 # 20 seconds
                ptg.moveTo(init_x+724,init_y-635)
                # ptg.moveTo(init_x+917,init_y-789)
                while send2chip is None:
                    send2chip=ptg.locateOnScreen(working_dir+"\\"+"images\\send_to_chip_blue.PNG",grayscale=True,confidence=.5)
                    if send2chip or time.time() > timeout:
                        break
        
                if send2chip:
                    # path=r'F:\Automate_GUI\output_files'
                    # self.save_op(path,filename+'_op',init_x+902,init_y-796)
                    if op_path:
                        self.save_op(op_path,filename+'_op',init_x+724,init_y-635)
                    else:
                        self.save_op(ip_path,filename+'_op',init_x+724,init_y-635)
                else:
                    print('Send to chip was not ready')
                    print('Output file was not saved')

        else:
            print('Send to chip was not ready')
            print('Output file was not saved')

    def reset_chip(self,init_x,init_y): #x=1776, y=62
        self.point_position((init_x,init_y), 1)
        if board_connected:
            ptg.moveTo(init_x+92,init_y+937)
            reset_chip=None
            timeout = time.time() + 30 # 20 seconds
            while reset_chip is None:
                reset_chip=ptg.locateOnScreen(working_dir+"\\"+"images\\load_enabled.PNG",grayscale=True,confidence=.8)
            if reset_chip or time.time() > timeout:
                print('reset chip')
                pass
                time.sleep(5)
        else:
            chip_not_connected=None
            timeout = time.time() + 30 # 20 seconds
            while chip_not_connected is None:
                chip_not_connected=ptg.locateOnScreen(working_dir+"\\"+"images\\chip_not_connected.PNG",grayscale=True,confidence=.5)
            if chip_not_connected or time.time() > timeout:
                ptg.press('enter')
            ptg.moveTo(init_x+92,init_y+937)
            reset_chip=None
            timeout = time.time() + 30 # 20 seconds
            while reset_chip is None:
                reset_chip=ptg.locateOnScreen(working_dir+"\\"+"images\\load_enabled.PNG",grayscale=True,confidence=.8)
            if reset_chip or time.time() > timeout:
                print('reset chip')
                pass
                time.sleep(5)
        
            
    def drop_down_ctrl(self,init_x,init_y,item_num):
        self.point_position((init_x,init_y), 1)
        [ptg.press('down') for x in range (item_num)]
        ptg.press('enter')
        
    def chng_drop_values(self,init_x,init_y,val):
        self.point_position((init_x,init_y), 1)
        time.sleep(1)
        if val <0:
            [ptg.press('up') for x in range (abs(val))]
            ptg.press('enter')
        if val >0:
            [ptg.press('down') for x in range (val)]
            ptg.press('enter')
        if val == 0:
            ptg.press('enter')
            
            
    # def scroll_values(self, init_x, init_y, val ,start_val,odd=True):
    #     self.point_position((init_x,init_y), 1) # set value
    #     val_press = (val-start_val)/1000 #val_press=0.008
    #     if val_press<0:
    #         a=str(val_press).split('.') #['0', '008']
    #         if odd:
    #             num_press = int(a[1]) #8
    #         else:
    #             mult=int('1'+('0'*(len(a[1])-1)))
    #             num_press = int(int(a[1])/2*mult) #8
                
    #         [ptg.press('up') for x in range (num_press)]
    #         # ptg.press('up')*num_press
    #         ptg.press('enter')
    #     # set value
    #     if val_press>0:
    #         a=str(val_press).split('.') #['0', '008']
    #         if odd:
    #             num_press = int(a[1]) #8
    #         else:
    #             # num_press = int(int(a[1])/2) #8
    #             mult=int('1'+('0'*(len(a[1])-1)))
    #             num_press = int(int(a[1])/2*mult) #8
                
    #         [ptg.press('down') for x in range (int(num_press))]
    #         # ptg.press('down')*val_press
    #         ptg.press('enter')
    #     if val_press==0:
    #         num_press=0
    #         ptg.press('enter')
        


    def scroll_values(self, init_x, init_y, val ,start_val,interval,odd=True):
        self.point_position((init_x,init_y), 1) # set value
        time.sleep(1)
        
        if interval<10:
            div=1
        else:
            div=int('1'+('0'*(len(str(interval))-1)))
        val_press = int((val-start_val)/div)
        a=abs(val_press)
        if odd:
            num_press = int(a) #8
        else:
            num_press = int(a/2)

        if val_press<0:
            [ptg.press('up') for x in range (num_press)]
            ptg.press('enter')
        if val_press>0:                
            [ptg.press('down') for x in range (int(num_press))]
            ptg.press('enter')
        if val_press==0:
            num_press=0
            ptg.press('enter')



    def scroll_value_numpress(self, dict,key ,start_val,interval,odd=True):

        dict_name = [ k for k,v in locals().items() if v == dict][0]
        if eval(dict_name)=={}:
            num_press=0
            return num_press
        val=int(eval(dict_name+key)) 
        if interval<10:
            div=1
        else:
            div=int('1'+('0'*(len(str(interval))-1)))
        val_press = int((val-start_val)/div)
        a=abs(val_press)
        if odd:
            num_press = int(a) #8
        else:
            num_press = int(a/2)

        if val_press==0:
            num_press=0
        return num_press

        
    def state_compare(self,old,new,keys=''):
        '''This function is to check old and new states are same/different
        The function is expected to be called before changing any widgets'''
        old_name = [ k for k,v in locals().items() if v == old][0]
        new_name = [ k for k,v in locals().items() if v == new][0]
        
        if eval(old_name)=={}:
            return True
        else:
            old_state=eval(str(old_name)+str(keys))
            new_state=eval((new_name)+str(keys))
            if old_state!=new_state:
                return True
            else:
                return False
        
    def change_drop_afterbase(self,old,new,keys,get_from_dict):
        old_name = [ k for k,v in locals().items() if v == old][0]
        new_name = [ k for k,v in locals().items() if v == new][0]
        if eval(old_name)=={}:
            existing =0
        else:
            if eval(str(old_name)+str(keys))=='':
                existing =0            
            else:
                existing=get_from_dict[eval(str(old_name)+str(keys))]
        go_to=get_from_dict[eval(new_name+str(keys))]
        return go_to-existing

    def change_drop_afterbase_swing(self,old,new,keys,get_from_dict,old_dict_swing):
        old_name = [ k for k,v in locals().items() if v == old][0]
        new_name = [ k for k,v in locals().items() if v == new][0]
        if eval(old_name)=={}:
            existing =0
        else:
            existing=old_dict_swing[eval(str(old_name)+str(keys))]
        go_to=get_from_dict[eval(new_name+str(keys))]
        return go_to-existing

    def reset_drop(self,init_x,init_y,existing,go_to=0):
        drop_val= go_to-existing
        self.chng_drop_values(init_x,init_y,drop_val)

    # def scroll_value_numpress(self, dict,key ,start_val,odd=True):
        # dict_name = [ k for k,v in locals().items() if v == dict][0]
        # if eval(dict_name)=={}:
        #     num_press=0
        #     return num_press
        # val=eval(dict_name+key)
        # val_press = (int(val)-start_val)/1000 #val_press=0.008
        # if val_press<0:
        #     a=str(val_press).split('.') #['0', '008']
        #     if odd:
        #         num_press = -(int(a[1])) #8
        #     else:
        #         # num_press = -(int(a[1]/2)) #8
        #         mult=int('1'+('0'*(len(a[1])-1)))
        #         num_press = -(int(int(a[1])/2*mult)) #8
                
        # # set value
        # if val_press>0:
        #     a=str(val_press).split('.') #['0', '008']
        #     if odd:
        #         num_press = int(a[1]) #8
        #     else:
        #         mult=int('1'+('0'*(len(a[1])-1)))
        #         num_press = int(int(a[1])/2*mult) #8
        # if val_press==0:
        #     num_press=0
        # return num_press


    def eeprom_config(self,init_x,init_y,dict1,dict2): #x=1766,y=133
        self.point_position((init_x,init_y), 1)
        time.sleep(0.5)
        ptg.hotkey('tab')

        # enter address
        keys=f"['eeprom']['addr']['value']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            time.sleep(0.5)
            ptg.typewrite(dict1['eeprom']['addr']['value'])
        # # valid_timer
        ptg.hotkey('tab')
        
        keys=f"['eeprom']['type']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            drop_val=self.change_drop_afterbase(dict2,dict1,keys,eeprom_type)
            self.chng_drop_values(init_x-743,init_y+354,drop_val)
        
        ptg.hotkey('tab')
        # self.point_position((init_x+353,init_y-332), 1)

        #block_id
        keys=f"['eeprom']['verify']['block']['value']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            drop_val=self.change_drop_afterbase(dict2,dict1,keys,block_id)
            self.chng_drop_values(init_x-815,init_y+472,drop_val)
        ptg.press('esc')
        
    # def gpio_config(self,init_x,init_y,dict1):#x=431,y=940
    #     self.point_position((init_x,init_y), 2)
    #     time.sleep(5)
    #     # ptg.hotkey('tab')
        
    #     for op in gpio_op:
                    
    #         ptg.hotkey('ctrl','tab')
    #         if dict1['gpio']['gpio']['value'][op]['inversion']:
    #             #ptg.hotkey('tab')
    #             # ptg.hotkey('space')
    #              ptg.click(init_x+534,init_y-669)
    #         #input
    #         if dict1['gpio']['gpio']['value'][op]['input']['state']=='input':
    #             self.point_position((init_x+387,init_y-643), 1)
    #             self.point_position((init_x+412,init_y-558), 2)
    #             for pll in pll_names4out:
    #                 if dict1['gpio']['gpio']['value'][op]['input']['value']['pll'][pll]:
    #                     ptg.hotkey('space')
    #                 ptg.hotkey('tab')
    #             #drop_doun
    #             self.point_position((init_x+538,init_y-326), 1)
    #             drop_val=gpio_sel[dict1['gpio']['gpio']['value'][op]['configuration']['value']['parsed']]
    #             self.chng_drop_values(init_x+538,init_y-326,drop_val)
    #         #output    
    #         elif dict1['gpio']['gpio']['value'][op]['output']['state']=='output':  
    #             # self.point_position((init_x+552,init_y-637), 1)
    #             self.point_position((init_x+387,init_y-643), 1)
    #             ptg.hotkey('tab')
    #             ptg.hotkey('space')
    #             if dict1['gpio']['gpio']['value'][op]['output']['value']["open_drain"]:
    #                 self.point_position((init_x+622,init_y-611), 1)
    #             if not dict1['gpio']['gpio']['value'][op]['output']['value']["configuration"]["general"]:
    #                 self.point_position((init_x+632,init_y-557), 1)
    #             if not dict1['gpio']['gpio']['value'][op]['output']['value']["configuration"]["eeprom"]:
    #                 self.point_position((init_x+614,init_y-505), 1)
    #             if not dict1['gpio']['gpio']['value'][op]['output']['value']["configuration"]["clkmon"]:
    #                 self.point_position((init_x+700,init_y-504), 1)
    #             self.point_position((init_x+613,init_y-449), 2)
    #             for pll in gpio_pll_config:
    #                 if dict1['gpio']['gpio']['value'][op]['output']['value']["configuration"][pll]:
    #                     ptg.hotkey('space')
    #                 ptg.hotkey('tab')
    #     ptg.press('esc')
                            
    def gpio_config(self,init_x,init_y,dict1,dict2):#x=413, y=974
        self.point_position((init_x,init_y), 1)    
        time.sleep(5)
        # num_tabs=0
        for k in dict1['gpio']['gpio']['value']:
            ptg.hotkey('ctrl','tab')
            keys=f"['gpio']['gpio']['value']['{k}']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                # for i in range(num_tabs):
                #     ptg.hotkey('ctrl','tab')
                keys=f"['gpio']['gpio']['value']['{k}']['inversion']"
                if_change=self.state_compare(dict2,dict1,keys)
                if if_change:
                    if dict2!={}:
                        self.point_position((init_x+563,init_y-704), 1)
                    else:
                        if dict1['gpio']['gpio']['value'][k]['inversion']:
                            self.point_position((init_x+563,init_y-704), 1)
                            
                if dict1['gpio']['gpio']['value'][k]['input']['state']=='input':
                    self.point_position((init_x+437,init_y-671), 1)
                    j=0
                    change_y=0
                    change_x=0
                    for ip in dict1['gpio']['gpio']['value'][k]['input']['value']['pll']['value']:
                        if dict2!={}:
                            keys=f"['gpio']['gpio']['value']['{k}']['input']['value']['pll']['value']['{ip}']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                self.point_position((init_x+431+change_x,init_y-584+change_y), 1)
                        else:
                            if dict1['gpio']['gpio']['value'][k]['input']['value']['pll']['value'][ip]:
                                self.point_position((init_x+431+change_x,init_y-584+change_y), 1)                    
                        change_y+=64
                        j+=1
                        if j==2:
                            change_y=0
                            change_x+=64
                            j=0
                    # dropdown
                    keys=f"['gpio']['gpio']['value']['{k}']['configuration']['value']['parsed']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:                        
                        drop_val=self.change_drop_afterbase(dict2,dict1,keys,gpio_sel)
                        self.chng_drop_values(init_x+568,init_y-362,drop_val)
                    
                            
                if dict1['gpio']['gpio']['value'][k]['output']['state']=='output':
                    self.point_position((init_x+602,init_y-671), 1)
                    keys=f"['gpio']['gpio']['value']['{k}']['output']['value']['open_drain']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+646,init_y-642), 1)
                        else:
                            if dict1['gpio']['gpio']['value'][k]['output']['value']['open_drain']:
                                self.point_position((init_x+646,init_y-642), 1)
                    
                    keys=f"['gpio']['gpio']['value']['{k}']['output']['value']['configuration']['general']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+680,init_y-589), 1)
                        else:
                            if not(dict1['gpio']['gpio']['value'][k]['output']['value']['configuration']['general']):
                                self.point_position((init_x+680,init_y-589), 1)
                    
                    keys=f"['gpio']['gpio']['value']['{k}']['output']['value']['configuration']['eeprom']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+634,init_y-562), 1)
                        else:
                            if not(dict1['gpio']['gpio']['value'][k]['output']['value']['configuration']['eeprom']):
                                self.point_position((init_x+634,init_y-562), 1)
                    
                    keys=f"['gpio']['gpio']['value']['{k}']['output']['value']['configuration']['clkmon']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+719,init_y-562), 1)
                        else:
                            if not(dict1['gpio']['gpio']['value'][k]['output']['value']['configuration']['clkmon']):
                                self.point_position((init_x+719,init_y-562), 1)
                
                    keys=f"['gpio']['gpio']['value']['{k}']['output']['value']['configuration']['pll:A']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+646,init_y-506), 1)
                        else:
                            if dict1['gpio']['gpio']['value'][k]['output']['value']['configuration']['pll:A']:
                                self.point_position((init_x+646,init_y-506), 1)

                    keys=f"['gpio']['gpio']['value']['{k}']['output']['value']['configuration']['pll:B']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+720,init_y-506), 1)
                        else:
                            if dict1['gpio']['gpio']['value'][k]['output']['value']['configuration']['pll:B']:
                                self.point_position((init_x+720,init_y-506), 1)
    
                    keys=f"['gpio']['gpio']['value']['{k}']['output']['value']['configuration']['pll:C']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+646,init_y-451), 1)
                        else:
                            if dict1['gpio']['gpio']['value'][k]['output']['value']['configuration']['pll:C']:
                                self.point_position((init_x+646,init_y-451), 1)

                    keys=f"['gpio']['gpio']['value']['{k}']['output']['value']['configuration']['pll:D']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+720,init_y-451), 1)
                        else:
                            if dict1['gpio']['gpio']['value'][k]['output']['value']['configuration']['pll:D']:
                                self.point_position((init_x+720,init_y-451), 1)
                                
                    # dropdown
                    keys=f"['gpio']['gpio']['value']['{k}']['configuration']['value']['parsed']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:                        
                        drop_val=self.change_drop_afterbase(dict2,dict1,keys,gpio_op_sel)
                        self.chng_drop_values(init_x+568,init_y-362,drop_val)
            # num_tabs+=1
        ptg.press('esc')


    def inputtdc(self,init_x,init_y,dict1,dict2):#x=1855, y=135
    # x=1855, y=135
        self.point_position((init_x,init_y), 1)
        time.sleep(2)
        edge_selection_clock=[]
        itdc_clock_dict1={}
        # Get all inputs that are enabled in itdc_edg_inp order
        # itdc_edg = {'Rising':0,'Falling':1}

        k=0
        for i in itdc_edg_inp:
            if dict1['inputs'][i]['enabled']:
                edge_selection_clock.append(i)
                itdc_clock_dict1[i]=k
                k+=1

        change_y=0
        change_x=0
        row=0
        col=0
        cntrl_tab_num=0
        for k in dict1['inputtdc']['edge']:    
            row+=1
            col+=1
            keys=f"['inputtdc']['edge']['{k}']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                drop_val=self.change_drop_afterbase(dict2,dict1,keys,itdc_edg)
                self.chng_drop_values(init_x+change_x-1055,init_y+change_y+357,drop_val)
                    
            change_y+=55
            if row==2:
                row=0
                change_y=0
                change_x+=80

        self.point_position((init_x-1084,init_y+446), 1)
        for op in itdc_op:
            keys=f"['inputtdc']['tdcs']['{op}']['enabled']"
            if dict2!={}:
                if_change=self.state_compare(dict2,dict1,keys)
                if if_change:
                    time.sleep(1)
                    self.point_position((init_x-1034,init_y+467), 1)
            else:
                if dict1['inputtdc']['tdcs'][op]['enabled']:
                    time.sleep(1)
                    self.point_position((init_x-1034,init_y+467), 1)
                    
            
            if dict1['inputtdc']['tdcs'][op]['enabled']:
                for j in range(cntrl_tab_num):
                    ptg.hotkey('cntrl','tab')
                keys=f"['inputtdc']['tdcs']['{op}']['enabled']"
                if not dict1['inputtdc']['tdcs'][op]['value']['clk1']['value']=='':            
                    # drop_val = itdc_clock[dict1['inputtdc']['tdcs'][op]['value']['clk1']['value']]
                    keys=f"['inputtdc']['tdcs']['{op}']['value']['clk1']['value']"

                    existing=12
                    # existing=self.scroll_value_numpress(dict2,keys ,4,1)
                    self.reset_drop(init_x-972,init_y+493,existing,go_to=0)
                    # drop_val=self.change_drop_afterbase(dict2,dict1,keys,itdc_clock)
                    drop_val = itdc_clock_dict1[dict1['inputtdc']['tdcs'][op]['value']['clk1']['value']]
                    self.chng_drop_values(init_x-972,init_y+493,drop_val)
                if not dict1['inputtdc']['tdcs'][op]['value']['clk2']['value']=='':
                    keys=f"['inputtdc']['tdcs']['{op}']['value']['clk2']['value']"
                    existing=12
                    # existing=self.scroll_value_numpress(dict2,keys ,4,1)
                    self.reset_drop(init_x-763,init_y+493,existing,go_to=0)
                    drop_val = itdc_clock_dict1[dict1['inputtdc']['tdcs'][op]['value']['clk2']['value']]    
                    # drop_val=self.change_drop_afterbase(dict2,dict1,keys,itdc_clock)
                    self.chng_drop_values(init_x-763,init_y+493,drop_val)
                self.point_position((init_x-839,init_y+531), 3)
                ptg.typewrite(dict1['inputtdc']['tdcs'][op]['value']['nsamples']['value'])
            ptg.hotkey('ctrl','tab')
            
            cntrl_tab_num+=1
        ptg.press('esc')
            
        
        
    def smartdco(self,init_x,init_y,pll,dict1,dict2):#644, 168
        # self.point_position((init_x+145,init_y+773), 1)
        
        keys=f"['plls']['{pll}']['value']['smartdco']['transmitter']['tx1']['enabled']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict2!={}:
                self.point_position((init_x+147,init_y+286), 1)
            else:
               if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx1']['enabled']:
                   self.point_position((init_x+147,init_y+286), 1)
               
        if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx1']['enabled']:
            keys=f"['plls']['{pll}']['value']['smartdco']['transmitter']['tx1']['value']['ppath']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict2!={}:
                    self.point_position((init_x+314,init_y+324), 1)
                else:
                   if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx1']['value']['ppath']:
                       self.point_position((init_x+314,init_y+324), 1)
                
            keys=f"['plls']['{pll}']['value']['smartdco']['transmitter']['tx1']['value']['rx1']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict2!={}:
                    self.point_position((init_x+176,init_y+371), 1)
                else:
                   if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx1']['value']['rx1']:
                       self.point_position((init_x+176,init_y+371), 1)

            keys=f"['plls']['{pll}']['value']['smartdco']['transmitter']['tx1']['value']['rx2']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict2!={}:
                    self.point_position((init_x+314,init_y+371), 1)
                else:
                   if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx1']['value']['rx2']:
                       self.point_position((init_x+314,init_y+371), 1)
            
        keys=f"['plls']['{pll}']['value']['smartdco']['transmitter']['tx2']['enabled']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict2!={}:
                self.point_position((init_x+147,init_y+418), 1)
            else:
               if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx2']['enabled']:
                   self.point_position((init_x+147,init_y+418), 1)
               
        if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx2']['enabled']:
            keys=f"['plls']['{pll}']['value']['smartdco']['transmitter']['tx2']['value']['ppath']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict2!={}:
                    self.point_position((init_x+314,init_y+453), 1)
                else:
                   if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx2']['value']['ppath']:
                       self.point_position((init_x+314,init_y+453), 1)
                
            keys=f"['plls']['{pll}']['value']['smartdco']['transmitter']['tx2']['value']['rx1']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict2!={}:
                    self.point_position((init_x+176,init_y+502), 1)
                else:
                   if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx2']['value']['rx1']:
                       self.point_position((init_x+176,init_y+502), 1)

            keys=f"['plls']['{pll}']['value']['smartdco']['transmitter']['tx2']['value']['rx2']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict2!={}:
                    self.point_position((init_x+314,init_y+502), 1)
                else:
                   if dict1['plls'][pll]['value']['smartdco']['transmitter']['tx2']['value']['rx2']:
                       self.point_position((init_x+314,init_y+502), 1)
            

        keys=f"['plls']['{pll}']['value']['smartdco']['receiver']['value']['sl']['enabled']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict2!={}:
                self.point_position((init_x+467,init_y+288), 1)
            else:
               if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['sl']['enabled']:
                   self.point_position((init_x+467,init_y+288), 1)
        if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['sl']['enabled']:
            keys=f"['plls']['{pll}']['value']['smartdco']['receiver']['value']['sl']['value']['value']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                drop_val=self.change_drop_afterbase(dict2,dict1,keys,sdco_sl)
                self.chng_drop_values(init_x+462,init_y+314,drop_val)
            
        keys=f"['plls']['{pll}']['value']['smartdco']['receiver']['value']['rx1']['enabled']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict2!={}:
                self.point_position((init_x+442,init_y+354), 1)
            else:
               if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx1']['enabled']:
                   self.point_position((init_x+442,init_y+354), 1)
        if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx1']['enabled']:
            keys=f"['plls']['{pll}']['value']['smartdco']['receiver']['value']['rx1']['value']['tx']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx1']['value']['tx']=='tx1':
                    self.point_position((init_x+519,init_y+384), 1)
                if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx1']['value']['tx']=='tx2':
                    self.point_position((init_x+519,init_y+413), 1)

            pll_temp=list(pll_names)
            pll_temp.remove(pll)
            existing=4
            self.reset_drop(init_x,init_y,existing,go_to=0)
            
            # keys=f"['plls']['{pll}']['value']['smartdco']['receiver']['value']['rx1']['value']['pll']['parsed']"
            # if_change=self.state_compare(dict2,dict1,keys)
            # if if_change:
            pll_rx1=dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx1']['value']['pll']['value'].replace('PLL ','')
            if dict2!={}:
                if dict2['plls'][pll]['value']['smartdco']['receiver']['value']['rx1']['value']['pll']['value']=='':
                    pll_rx2=pll_temp[0]
                else:
                    pll_rx2=dict2['plls'][pll]['value']['smartdco']['receiver']['value']['rx1']['value']['pll']['value'].replace('PLL ','')
            else:
                pll_rx2=pll_rx1
            drop_val=pll_temp.index(pll_rx1)-pll_temp.index(pll_rx2)
            self.chng_drop_values(init_x+441,init_y+408,drop_val)
                
        keys=f"['plls']['{pll}']['value']['smartdco']['receiver']['value']['rx2']['enabled']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict2!={}:
                self.point_position((init_x+442,init_y+451), 1)
            else:
               if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx2']['enabled']:
                   self.point_position((init_x+442,init_y+451), 1)
            
        if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx2']['enabled']:
            keys=f"['plls']['{pll}']['value']['smartdco']['receiver']['value']['rx2']['value']['tx']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx2']['value']['tx']=='tx1':
                    self.point_position((init_x+519,init_y+479), 1)
                if dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx2']['value']['tx']=='tx2':
                    self.point_position((init_x+519,init_y+507), 1)

            pll_temp=list(pll_names)
            pll_temp.remove(pll)
            existing=4
            self.reset_drop(init_x,init_y,existing,go_to=0)
            
            # keys=f"['plls']['{pll}']['value']['smartdco']['receiver']['value']['rx2']['value']['pll']['parsed']"
            # if_change=self.state_compare(dict2,dict1,keys)
            # if if_change:
            pll_rx1=dict1['plls'][pll]['value']['smartdco']['receiver']['value']['rx2']['value']['pll']['parsed'].replace('PLL ','')
            if dict2!={}:
                if dict2['plls'][pll]['value']['smartdco']['receiver']['value']['rx2']['value']['pll']['parsed']=='':
                    pll_rx2=pll_temp[0]
                else:
                    pll_rx2=dict2['plls'][pll]['value']['smartdco']['receiver']['value']['rx2']['value']['pll']['parsed'].replace('PLL ','')
            else:
                pll_rx2=pll_rx1
            drop_val=pll_temp.index(pll_rx1)-pll_temp.index(pll_rx2)
            self.chng_drop_values(init_x+439,init_y+504,drop_val)
        ptg.press('esc')
            
                
                
                   
                          # 'smartdco': {'receiver': {'valid': True,
                          #                           'value': {'rx1': {'enabled': False,
                          #                                             'value': {'pll': '',
                          #                                                       'tx': 'tx1'}},
                          #                                     'rx2': {'enabled': False,
                          #                                             'value': {'pll': '',
                          #                                                       'tx': 'tx1'}},
                          #                                     'sl': {'enabled': False,
                          #                                            'parsed': Fraction(16, 15625),
                          #                                            'valid': True,
                          #                                            'value': '1024 '
                          #                                                     'ppm/s'}}},
                          #              'transmitter': {'tx1': {'enabled': False,
                          #                                      'value': {'ipath': True,
                          #                                                'ppath': False,
                          #                                                'rx1': True,
                          #                                                'rx2': True}},
                          #                              'tx2': {'enabled': False,
                          #                                      'value': {'ipath': True,
                          #                                                'ppath': False,
                          #                                                'rx1': True,
                          #                                                'rx2': True}}}}}},

    def interrupt(self,init_x,init_y,dict1,dict2): #x=580, y=974
        self.point_position((init_x,init_y), 2)
        time.sleep(2)
        pll_loop=['pll_outer_lol','pll_inner_lol','pll_ho_freeze','pll_phase_lol']
        for p_loop in pll_loop:
            if p_loop=='pll_inner_lol':
                plls_int=['A','B','C','D','FT','common']
            else:
                plls_int=['A','B','C','D','FT']
            ptg.hotkey('tab')
            ptg.hotkey('tab')
            for p in plls_int:
                keys=f"['interrupt']['{p_loop}']['{p}']"
                if dict2!={}:
                    ptg.hotkey('tab')
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:   
                        ptg.hotkey('space')
                else:
                    ptg.hotkey('tab')
                    if dict1['interrupt'][p_loop][p]:
                        ptg.hotkey('space')                        
                        
        ip_loop=['input_closs','input_coarse_drift','input_fine_drift']
        ip_list=['0P','0N','1P','1N','2P','2N','3P','3N','4P','4N','OCXO','INTSYNC']
        
        for k in ip_loop:
            ptg.hotkey('tab')
            ptg.hotkey('tab')
            for ip in ip_list:
                keys=f"['interrupt']['{k}']['{ip}']"
                if dict2!={}:
                    ptg.hotkey('tab')
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:   
                        ptg.hotkey('space')
                else:
                    ptg.hotkey('tab')
                    if dict1['interrupt'][k][ip]:
                        ptg.hotkey('space')                        
                
        ptg.press('esc')
                
            
        
 # 'interrupt': {'eeprom': {'defect_interrupt': False},
 #               'input_closs': {'0N': False,
 #                               '0P': False,
 #                               '1N': False,
 #                               '1P': False,
 #                               '2N': False,
 #                               '2P': False,
 #                               '3N': False,
 #                               '3P': False,
 #                               '4N': False,
 #                               '4P': False,
 #                               'INTSYNC': False,
 #                               'OCXO': False},
 #               'input_coarse_drift': {'0N': False,
 #                                      '0P': False,
 #                                      '1N': False,
 #                                      '1P': False,
 #                                      '2N': False,
 #                                      '2P': False,
 #                                      '3N': False,
 #                                      '3P': False,
 #                                      '4N': False,
 #                                      '4P': False,
 #                                      'INTSYNC': False,
 #                                      'OCXO': False},
 #               'input_fine_drift': {'0N': False,
 #                                    '0P': False,
 #                                    '1N': False,
 #                                    '1P': False,
 #                                    '2N': False,
 #                                    '2P': False,
 #                                    '3N': False,
 #                                    '3P': False,
 #                                    '4N': False,
 #                                    '4P': False,
 #                                    'INTSYNC': False,
 #                                    'OCXO': False},
 #               'pll_ho_freeze': {'A': False,
 #                                 'B': False,
 #                                 'C': False,
 #                                 'D': False,
 #                                 'FT': False},
 #               'pll_inner_lol': {'A': False,
 #                                 'B': False,
 #                                 'C': False,
 #                                 'D': False,
 #                                 'FT': False,
 #                                 'common': False},
 #               'pll_outer_lol': {'A': False,
 #                                 'B': False,
 #                                 'C': False,
 #                                 'D': False,
 #                                 'FT': False},
 #               'pll_phase_lol': {'A': False,
 #                                 'B': False,
 #                                 'C': False,
 #                                 'D': False,
 #                                 'FT': False},

                           
    # def interrupt(self,init_x,init_y,dict1): #x=1767, y=134
    #     self.point_position((init_x,init_y), 2)
    #     time.sleep(2)
    #     ptg.hotkey('tab')
    #     #pll
    #     for int_pll in interrupt_pll:
    #         ptg.hotkey('tab')
    #         ptg.hotkey('tab')
    #         for pll in pll_names:
    #             if dict1["interrupt"][int_pll][pll]:
    #                 ptg.hotkey('space')
    #             ptg.hotkey('tab')
    #         if int_pll=='pll_inner_lol':
    #             if dict1["interrupt"][int_pll]['common']:
    #                 ptg.hotkey('space')
    #             ptg.hotkey('tab')
    #     #inputs
    #     for int_inp in interrupt_input:
    #         ptg.hotkey('tab')
    #         ptg.hotkey('tab')
    #         for sel in interrupt_inp_sel:
    #             if dict1["interrupt"][int_inp][sel]:
    #                 ptg.hotkey('space')
    #             ptg.hotkey('tab')
    #     #eeprom
    #     if dict1["interrupt"]['eeprom']['defect_interrupt']:
    #         ptg.hotkey('space')
    #     #TDC
    #     ptg.hotkey('tab')
    #     ptg.hotkey('tab')
    #     ptg.hotkey('tab')
    #     for pll in pll_names4out:
    #         if dict1["interrupt"]['tdc'][pll]:
    #             ptg.hotkey('space')
    #         ptg.hotkey('tab')
            
    # def hold_W (self,hold_time):
    #     start = time.time()
    #     while time.time() - start < hold_time:
    #         ptg.press('up')

    def phase_sync(self, init_x, init_y,dict1,dict2): #x=1236, y=48
        keys=f"['phase_sync']['enabled']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict2!={}:
                self.point_position((init_x,init_y), 1)                
            else:
                if dict1['phase_sync']['enabled']:
                    self.point_position((init_x,init_y), 1)
                    
        k=0
        change_y=0
        change_x=0
        for key in dict1['phase_sync']['value']:
            if dict2!={}:
                keys=f"['phase_sync']['value']['{key}']"
                if_change=self.state_compare(dict2,dict1,keys)
                if if_change:
                    self.point_position((init_x-39+change_x,init_y+34+change_y), 1)
            else:
                if not(dict1['phase_sync']['value'][key]):
                    self.point_position((init_x-39+change_x,init_y+34+change_y), 1)                    
            change_y+=45
            k+=1
            if k==2:
                change_y=0
                change_x+=55
                k=0
                
    
        
 # 'phase_sync': {'enabled': False,
 #                'value': {'A': False, 'B': False, 'C': False, 'D': False}},
        
                
            
        
    def change_ip_config(self, init_x, init_y,dict1,dict2): # x=32, y=249
        '''
        Function to change input page configuration
        Settings are given by the user in the form of dictionary
        This is same as gui state
        '''
        # self.point_position((init_x,init_y), 1)
         # 'inputs_diff': {'0P': True, '1P': True, '2P': False, '3P': False, '4P': False},
         
        # Don't run anytests for diff_pair N-type inputs
        diff_pair={'0P': '0N', '1P': '1N', '2P': '2N', '3P': '3N', '4P': '4N'}
        diff_ip=[]
        clock_loss_te={"1":-2,	"2":-1,	"3":0,	"4":1,	"5":2,	"6":3,	"7":4,	"8":5,	"9":6,	"10":7,	"11":8,	"12":9,	"13":10,	"14":11,	"15":12,	"16":13}
        clock_loss_ce={"1":-1,	"2":0,	"3":1,	"4":2,	"5":3,	"6":4,	"7":5,	"8":6,	"9":7,	"10":8,	"11":9,	"12":10,	"13":11,	"14":12,	"15":13,	"16":14}
        coarse_drift_set={"100":-4,"200":-3,"300":-2,"400":-1,"500":0,"600":1,"700":2,"800":3,"900":4,"1000":5,"1100":6,"1200":7,"1300":8,"1400":9,"1500":10,"1600":11}
        coarse_drift_clear={"100":-3,"200":-2,"300":-1,"400":0,"500":1,"600":2,"700":3,"800":4,"900":5,"1000":6,"1100":7,"1200":8,"1300":9,"1400":10,"1500":11,"1600":12}

        fine_drift_set={"2":-4,	"4":-3,	"6":-2,	"8":-1,	"10":0,	"12":1,	"14":2,	"16":3,	"18":4,	"20":5,	"22":6,	"24":7,	"26":8,	"28":9,	"30":10,	"32":11,	"34":12,	"36":13,	"38":14,	"40":15,	"42":16,	"44":17,	"46":18,	"48":19,	"50":20,	"52":21,	"54":22,	"56":23,	"58":24,	"60":25,	"62":26,	"64":27,	"66":28,	"68":29,	"70":30,	"72":31,	"74":32,	"76":33,	"78":34,	"80":35,	"82":36,	"84":37,	"86":38,	"88":39,	"90":40,	"92":41,	"94":42,	"96":43,	"98":44,	"100":45,	"102":46,	"104":47,	"106":48,	"108":49,	"110":50,	"112":51,	"114":52,	"116":53,	"118":54,	"120":55,	"122":56,	"124":57,	"126":58,	"128":59,	"130":60,	"132":61,	"134":62,	"136":63,	"138":64,	"140":65,	"142":66,	"144":67,	"146":68,	"148":69,	"150":70,	"152":71,	"154":72,	"156":73,	"158":74,	"160":75,	"162":76,	"164":77,	"166":78,	"168":79,	"170":80,	"172":81,	"174":82,	"176":83,	"178":84,	"180":85,	"182":86,	"184":87,	"186":88,	"188":89,	"190":90,	"192":91,	"194":92,	"196":93,	"198":94,	"200":95,	"202":96,	"204":97,	"206":98,	"208":99,	"210":100,	"212":101,	"214":102,	"216":103,	"218":104,	"220":105,	"222":106,	"224":107,	"226":108,	"228":109,	"230":110,	"232":111,	"234":112,	"236":113,	"238":114,	"240":115,	"242":116,	"244":117,	"246":118,	"248":119,	"250":120,	"252":121,	"254":122,	"256":123,	"258":124,	"260":125,	"262":126,	"264":127,	"266":128,	"268":129,	"270":130,	"272":131,	"274":132,	"276":133,	"278":134,	"280":135,	"282":136,	"284":137,	"286":138,	"288":139,	"290":140,	"292":141,	"294":142,	"296":143,	"298":144,	"300":145,	"302":146,	"304":147,	"306":148,	"308":149,	"310":150,	"312":151,	"314":152,	"316":153,	"318":154,	"320":155,	"322":156,	"324":157,	"326":158,	"328":159,	"330":160,	"332":161,	"334":162,	"336":163,	"338":164,	"340":165,	"342":166,	"344":167,	"346":168,	"348":169,	"350":170,	"352":171,	"354":172,	"356":173,	"358":174,	"360":175,	"362":176,	"364":177,	"366":178,	"368":179,	"370":180,	"372":181,	"374":182,	"376":183,	"378":184,	"380":185,	"382":186,	"384":187,	"386":188,	"388":189,	"390":190,	"392":191,	"394":192,	"396":193,	"398":194,	"400":195,	"402":196,	"404":197,	"406":198,	"408":199,	"410":200,	"412":201,	"414":202,	"416":203,	"418":204,	"420":205,	"422":206,	"424":207,	"426":208,	"428":209,	"430":210,	"432":211,	"434":212,	"436":213,	"438":214,	"440":215,	"442":216,	"444":217,	"446":218,	"448":219,	"450":220,	"452":221,	"454":222,	"456":223,	"458":224,	"460":225,	"462":226,	"464":227,	"466":228,	"468":229,	"470":230,	"472":231,	"474":232,	"476":233,	"478":234,	"480":235,	"482":236,	"484":237,	"486":238,	"488":239,	"490":240,	"492":241,	"494":242,	"496":243,	"498":244,	"500":245,	"502":246,	"504":247,	"506":248,	"508":249,	"510":250}
        
        fine_drift_clear={"2":-3,	"4":-2,	"6":-1,	"8":0,	"10":1,	"12":2,	"14":3,	"16":4,	"18":5,	"20":6,	"22":7,	"24":8,	"26":9,	"28":10,	"30":11,	"32":12,	"34":13,	"36":14,	"38":15,	"40":16,	"42":17,	"44":18,	"46":19,	"48":20,	"50":21,	"52":22,	"54":23,	"56":24,	"58":25,	"60":26,	"62":27,	"64":28,	"66":29,	"68":30,	"70":31,	"72":32,	"74":33,	"76":34,	"78":35,	"80":36,	"82":37,	"84":38,	"86":39,	"88":40,	"90":41,	"92":42,	"94":43,	"96":44,	"98":45,	"100":46,	"102":47,	"104":48,	"106":49,	"108":50,	"110":51,	"112":52,	"114":53,	"116":54,	"118":55,	"120":56,	"122":57,	"124":58,	"126":59,	"128":60,	"130":61,	"132":62,	"134":63,	"136":64,	"138":65,	"140":66,	"142":67,	"144":68,	"146":69,	"148":70,	"150":71,	"152":72,	"154":73,	"156":74,	"158":75,	"160":76,	"162":77,	"164":78,	"166":79,	"168":80,	"170":81,	"172":82,	"174":83,	"176":84,	"178":85,	"180":86,	"182":87,	"184":88,	"186":89,	"188":90,	"190":91,	"192":92,	"194":93,	"196":94,	"198":95,	"200":96,	"202":97,	"204":98,	"206":99,	"208":100,	"210":101,	"212":102,	"214":103,	"216":104,	"218":105,	"220":106,	"222":107,	"224":108,	"226":109,	"228":110,	"230":111,	"232":112,	"234":113,	"236":114,	"238":115,	"240":116,	"242":117,	"244":118,	"246":119,	"248":120,	"250":121,	"252":122,	"254":123,	"256":124,	"258":125,	"260":126,	"262":127,	"264":128,	"266":129,	"268":130,	"270":131,	"272":132,	"274":133,	"276":134,	"278":135,	"280":136,	"282":137,	"284":138,	"286":139,	"288":140,	"290":141,	"292":142,	"294":143,	"296":144,	"298":145,	"300":146,	"302":147,	"304":148,	"306":149,	"308":150,	"310":151,	"312":152,	"314":153,	"316":154,	"318":155,	"320":156,	"322":157,	"324":158,	"326":159,	"328":160,	"330":161,	"332":162,	"334":163,	"336":164,	"338":165,	"340":166,	"342":167,	"344":168,	"346":169,	"348":170,	"350":171,	"352":172,	"354":173,	"356":174,	"358":175,	"360":176,	"362":177,	"364":178,	"366":179,	"368":180,	"370":181,	"372":182,	"374":183,	"376":184,	"378":185,	"380":186,	"382":187,	"384":188,	"386":189,	"388":190,	"390":191,	"392":192,	"394":193,	"396":194,	"398":195,	"400":196,	"402":197,	"404":198,	"406":199,	"408":200,	"410":201,	"412":202,	"414":203,	"416":204,	"418":205,	"420":206,	"422":207,	"424":208,	"426":209,	"428":210,	"430":211,	"432":212,	"434":213,	"436":214,	"438":215,	"440":216,	"442":217,	"444":218,	"446":219,	"448":220,	"450":221,	"452":222,	"454":223,	"456":224,	"458":225,	"460":226,	"462":227,	"464":228,	"466":229,	"468":230,	"470":231,	"472":232,	"474":233,	"476":234,	"478":235,	"480":236,	"482":237,	"484":238,	"486":239,	"488":240,	"490":241,	"492":242,	"494":243,	"496":244,	"498":245,	"500":246,	"502":247,	"504":248,	"506":249,	"508":250,	"510":251}
        
         
        for key,value in dict1['inputs_diff'].items():
            if value:
                diff_ip.append(diff_pair[key])

        global inputs_covered
        in_change_x={'0P':0,'0N':1,'1P':2,'1N':3,'2P':4,'2N':5,'3P':6,'3N':7,'4P':8,'4N':9,'OCXO':10,'INTSYNC':11}
        

        for key in dict1['inputs']:
            
            old_state = copy.deepcopy(dict2)
            change_x=24
            delta_x=0
            if key=='OCXO' or key=='INTSYNC':
                delta_x=15
                
            ## Only go to inputs that have differences##
            IP_CHANGE=False
            if dict2=={}:
                IP_CHANGE=True
            else:
                if dict1['inputs'][key]!=dict2['inputs'][key]:
                    IP_CHANGE=True
            if IP_CHANGE:
            ## Only go to inputs that have differences##

                if dict2!={}:
                    ##########################################################
                    keys=f"['inputs']['{key}']['enabled']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        self.point_position((init_x+(change_x*in_change_x[key])+delta_x,init_y), 1)
                        time.sleep(1)
                        # enable input
                        self.point_position((init_x+44,init_y+26), 1)
                else:
                    if dict1['inputs'][key]['enabled']:
                        self.point_position((init_x+(change_x*in_change_x[key])+delta_x,init_y), 1)
                        time.sleep(1)
                        # enable input
                        self.point_position((init_x+44,init_y+26), 1)
                        
    
    
                if dict1['inputs'][key]['enabled']:
                    if key not in diff_ip:
                        #inputs covered
                        
                        if key not in inputs_covered:
                            dict2={}
                        inputs_covered.append(key)
        
                        if key!='INTSYNC':
        
                            self.point_position((init_x+(change_x*in_change_x[key])+delta_x,init_y), 1)
                            time.sleep(1)
                            #golden clock
                            ##########################################################
                            keys="['golden_clock']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict1['golden_clock']==key:
                                    self.point_position((init_x+135,init_y+59), 1)
                            #enter freq
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['freq']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                self.point_position((init_x+419,init_y+80), 3) # Triple Click to select the text and replace it
                                ptg.typewrite(dict1['inputs'][key]['value']['freq']['value'])
                            # Coupling
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_couple']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict1['inputs'][key]['value']['clock_couple']=='ac':
                                    self.point_position((init_x+150,init_y+139), 1)
                                else:
                                    self.point_position((init_x+435,init_y+139), 1)
                            # Clock inversion
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_inversion']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict2!={}:
                                    self.point_position((init_x+99,init_y+204), 1)    
                                else:
                                    if dict1['inputs'][key]['value']['clock_inversion']:
                                        self.point_position((init_x+99,init_y+204), 1)    
                                        
                            #Clock Gap
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_gap']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict2!={}:
                                    self.point_position((init_x+291,init_y+204), 1)
                                else:                            
                                    if dict1['inputs'][key]['value']['clock_gap']:
                                        self.point_position((init_x+291,init_y+204), 1)
                            # valid timer
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['valid_timer']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                drop_val=self.change_drop_afterbase(dict2,dict1,keys,val_time)
                                self.chng_drop_values(init_x+476,init_y+226,drop_val)
                          
            
                            keys=f"['inputs']['{key}']['value']['clock_loss']['value']['edge_trigger']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                drop_val=self.change_drop_afterbase(dict2,dict1,keys,clock_loss_te)
                                self.chng_drop_values(init_x+175,init_y+287,drop_val)
                                # existing=self.scroll_value_numpress(dict2,keys ,3,1)
                                # self.reset_drop(init_x+175,init_y+287,existing,go_to=0)
                                # self.scroll_values(init_x+175,init_y+287, int(dict1['inputs'][key]['value']['clock_loss']['value']['edge_trigger']['value']) ,3,1)# set value
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_loss']['value']['edge_clear']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                drop_val=self.change_drop_afterbase(dict2,dict1,keys,clock_loss_ce)
                                self.chng_drop_values(init_x+457,init_y+287,drop_val)
                                # existing=self.scroll_valuse_numpress(dict2,keys ,2,1)
                                # self.reset_drop(init_x+457,init_y+287,existing,go_to=0)
                                # self.scroll_values(init_x+457,init_y+287, int(dict1['inputs'][key]['value']['clock_loss']['value']['edge_clear']['value']) ,2,1)# clr value
                           
                            # Clock Switch
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_switch']['clock_loss']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                if dict2!={}:
                                    self.point_position((init_x+79,init_y+361), 1)
                                else:                            
                                    if not(dict1['inputs'][key]['value']['clock_switch']['clock_loss']): # enabled by default
                                        self.point_position((init_x+79,init_y+361), 1)
                                  
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_switch']['fd_coarse']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                if dict2!={}:
                                    self.point_position((init_x+270,init_y+361), 1)                 
                                else:
                                    if dict1['inputs'][key]['value']['clock_switch']['fd_coarse']:
                                        self.point_position((init_x+270,init_y+361), 1)                 
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_switch']['fd_fine']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                if dict2!={}:
                                    self.point_position((init_x+471,init_y+361), 1)                 
                                else:                            
                                    if dict1['inputs'][key]['value']['clock_switch']['fd_fine']:
                                        self.point_position((init_x+471,init_y+361), 1)                 
                                
                            # coarse drift
                            ##########################################################
                            if dict1['golden_clock']=='xtal':
                                keys=f"['inputs']['{key}']['value']['drift_coarse']['enabled']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    if dict2!={}:
                                        self.point_position((init_x+57,init_y+443), 1)
                                    else:
                                        if dict1['inputs'][key]['value']['drift_coarse']['enabled']:
                                            self.point_position((init_x+57,init_y+443), 1)
                                        
                                if dict1['inputs'][key]['value']['drift_coarse']['enabled']:
            
                                    ##########################################################
                                    keys=f"['inputs']['{key}']['value']['drift_coarse']['value']['set']"
                                    if_change=self.state_compare(dict2,dict1,keys)
                                    if if_change:
                                        time.sleep(1)
                                        drop_val=self.change_drop_afterbase(dict2,dict1,keys,coarse_drift_set)
                                        self.chng_drop_values(init_x+163,init_y+483,drop_val)

                                        # existing=self.scroll_value_numpress(dict2,keys ,500,100)
                                        # self.reset_drop(init_x+163,init_y+483,existing,go_to=0)
                                        # self.scroll_values(init_x+163,init_y+483, int(dict1['inputs'][key]['value']['drift_coarse']['value']['set']) ,500,100)# set value
                                    ##########################################################
                                    keys=f"['inputs']['{key}']['value']['drift_coarse']['value']['clr']"
                                    if_change=self.state_compare(dict2,dict1,keys)
                                    if if_change:
                                        time.sleep(1)
                                        drop_val=self.change_drop_afterbase(dict2,dict1,keys,coarse_drift_clear)
                                        self.chng_drop_values(init_x+457,init_y+483,drop_val)

                                        # existing=self.scroll_value_numpress(dict2,keys ,400,100)
                                        # self.reset_drop(init_x+457,init_y+483,existing,go_to=0)
                                        # self.scroll_values(init_x+457,init_y+483, int(dict1['inputs'][key]['value']['drift_coarse']['value']['clr']) ,400,100)# clr value
                                  
                                # Fine drift
                                ##########################################################
                                keys=f"['inputs']['{key}']['value']['drift_fine']['enabled']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    if dict2!={}:
                                        self.point_position((init_x+57,init_y+519), 1)
                                    else:
                                        if dict1['inputs'][key]['value']['drift_fine']['enabled']:
                                            self.point_position((init_x+57,init_y+519), 1)
            
                                if dict1['inputs'][key]['value']['drift_fine']['enabled']:
                                    ##########################################################
                                    keys=f"['inputs']['{key}']['value']['drift_fine']['value']['set']"
                                    if_change=self.state_compare(dict2,dict1,keys)
                                    if if_change:
                                        time.sleep(1)
                                        drop_val=self.change_drop_afterbase(dict2,dict1,keys,fine_drift_set)
                                        self.chng_drop_values(init_x+163,init_y+554,drop_val)
                                        # existing=self.scroll_value_numpress(dict2,keys ,10,2,odd=False)
                                        # self.reset_drop(init_x+163,init_y+554,existing,go_to=0)
                                        # self.scroll_values(init_x+163,init_y+554, int(dict1['inputs'][key]['value']['drift_fine']['value']['set']) ,10,2,odd=False)# set value
                                    ##########################################################
                                    keys=f"['inputs']['{key}']['value']['drift_fine']['value']['clr']"
                                    if_change=self.state_compare(dict2,dict1,keys)
                                    if if_change:
                                        time.sleep(1)
                                        drop_val=self.change_drop_afterbase(dict2,dict1,keys,fine_drift_clear)
                                        self.chng_drop_values(init_x+457,init_y+554,drop_val)
                                        # existing=self.scroll_value_numpress(dict2,keys ,8,2,odd=False)
                                        # self.reset_drop(init_x+457,init_y+554,existing,go_to=0)
                                        # self.scroll_values(init_x+457,init_y+554, int(dict1['inputs'][key]['value']['drift_fine']['value']['clr']) ,8,2,odd=False)# clr value
               
                            change_x=0
                            for pll in pll_names:
                                keys=f"['inputs']['{key}']['value']['plls']['{pll}']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    if dict2!={}:
                                        if dict1['inputs'][key]['value']['plls'][pll] and not(dict2['inputs'][key]['value']['plls'][pll]):
                                            self.point_position((init_x+52+change_x,init_y+649), 1) # check box
                                        if not(dict1['inputs'][key]['value']['plls'][pll]) and dict2['inputs'][key]['value']['plls'][pll]:
                                            self.point_position((init_x+52+change_x,init_y+649), 1) # check box
                                    else:
                                        if dict1['inputs'][key]['value']['plls'][pll]:
                                            self.point_position((init_x+52+change_x,init_y+649), 1) # check box
                                change_x+=114
                        else:
                            self.point_position((init_x+(change_x*in_change_x[key])+delta_x,init_y), 1)
                            time.sleep(1)
                            #golden clock
                            ##########################################################
                            keys="['golden_clock']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict1['golden_clock']==key:
                                    self.point_position((init_x+137,init_y+92), 1)
                            #enter freq
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['freq']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                self.point_position((init_x+430,init_y+92), 3) # Triple Click to select the text and replace it
                                ptg.typewrite(dict1['inputs'][key]['value']['freq']['value'])
             
                            # valid timer
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['valid_timer']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                drop_val=self.change_drop_afterbase(dict2,dict1,keys,val_time)
                                self.chng_drop_values(init_x+280,init_y+177,drop_val)
                           
                            #Clock Loss
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_loss']['value']['edge_trigger']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                drop_val=self.change_drop_afterbase(dict2,dict1,keys,clock_loss_te)
                                self.chng_drop_values(init_x+177,init_y+255,drop_val)
                                # existing=self.scroll_value_numpress(dict2,keys ,5,1)
                                # self.reset_drop(init_x+177,init_y+255,existing,go_to=0)
                                # self.scroll_values(init_x+177,init_y+255, int(dict1['inputs'][key]['value']['clock_loss']['value']['edge_trigger']['value']) ,5,1)# set value
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_loss']['value']['edge_clear']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                drop_val=self.change_drop_afterbase(dict2,dict1,keys,clock_loss_ce)
                                self.chng_drop_values(init_x+456,init_y+255,drop_val)
                                # existing=self.scroll_value_numpress(dict2,keys ,4,1)
                                # self.reset_drop(init_x+456,init_y+255,existing,go_to=0)
                                # self.scroll_values(init_x+456,init_y+255, int(dict1['inputs'][key]['value']['clock_loss']['value']['edge_clear']['value']) ,4,1)# clr value
                           
                            # Clock Switch
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_switch']['clock_loss']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                if dict2!={}:
                                    self.point_position((init_x+82,init_y+356), 1)                 
                                else:                            
                                    if not(dict1['inputs'][key]['value']['clock_switch']['clock_loss']): # enabled by default
                                        self.point_position((init_x+82,init_y+356), 1)                 
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_switch']['fd_coarse']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                if dict2!={}:
                                    self.point_position((init_x+269,init_y+356), 1)                 
                                else:                            
                                    if dict1['inputs'][key]['value']['clock_switch']['fd_coarse']:
                                        self.point_position((init_x+269,init_y+356), 1)                 
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['clock_switch']['fd_fine']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                if dict2!={}:
                                    self.point_position((init_x+468,init_y+356), 1)       
                                else:
                                    if dict1['inputs'][key]['value']['clock_switch']['fd_fine']:
                                        self.point_position((init_x+468,init_y+356), 1)                 
                                
                            # coarse drift
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['drift_coarse']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                if dict2!={}:
                                    self.point_position((init_x+63,init_y+422), 1)
                                else:
                                    if dict1['inputs'][key]['value']['drift_fine']['enabled']:
                                        self.point_position((init_x+63,init_y+422), 1)
                                    # self.point_position((init_x+63,init_y+402), 1)
                            ##########################################################
                            if dict1['inputs'][key]['value']['drift_coarse']:
                                keys=f"['inputs']['{key}']['value']['drift_coarse']['value']['set']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,coarse_drift_set)
                                    self.chng_drop_values(init_x+161,init_y+454,drop_val)
                                   # existing=self.scroll_value_numpress(dict2,keys ,500,100)
                                    # self.reset_drop(init_x+161,init_y+454,existing,go_to=0)
                                    # self.scroll_values(init_x+161,init_y+454, int(dict1['inputs'][key]['value']['drift_coarse']['value']['set']) ,500,100)# set value
                                ##########################################################
                                keys=f"['inputs']['{key}']['value']['drift_coarse']['value']['clr']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,coarse_drift_clear)
                                    self.chng_drop_values(init_x+455,init_y+454,drop_val)
                                    # existing=self.scroll_value_numpress(dict2,keys ,400,100)
                                    # self.reset_drop(init_x+455,init_y+454,existing,go_to=0)
                                    # self.scroll_values(init_x+455,init_y+454, int(dict1['inputs'][key]['value']['drift_coarse']['value']['clr']) ,400,100)# clr value
                              
                            # Fine drift
                            ##########################################################
                            keys=f"['inputs']['{key}']['value']['drift_fine']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                # self.point_position((init_x+52,init_y+483), 1) # check box
                                if dict2!={}:
                                    self.point_position((init_x+57,init_y+504), 1)
                                else:
                                    if dict1['inputs'][key]['value']['drift_fine']['enabled']:
                                        self.point_position((init_x+57,init_y+504), 1)
        
                            if dict1['inputs'][key]['value']['drift_fine']:
                                ##########################################################
                                keys=f"['inputs']['{key}']['value']['drift_fine']['value']['set']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,fine_drift_set)
                                    self.chng_drop_values(init_x+166,init_y+544,drop_val)
                                    # existing=self.scroll_value_numpress(dict2,keys ,10,2,odd=False)
                                    # self.reset_drop(init_x+166,init_y+544,existing,go_to=0)
                                    # self.scroll_values(init_x+166,init_y+544, int(dict1['inputs'][key]['value']['drift_fine']['value']['set']) ,10,2,odd=False)# set value
                                ##########################################################
                                keys=f"['inputs']['{key}']['value']['drift_fine']['value']['clr']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,fine_drift_clear)
                                    self.chng_drop_values(init_x+166,init_y+544,drop_val)
                                    # existing=self.scroll_value_numpress(dict2,keys ,8,2,odd=False)
                                    # self.reset_drop(init_x+455,init_y+544,existing,go_to=0)
                                    # self.scroll_values(init_x+455,init_y+544, int(dict1['inputs'][key]['value']['drift_fine']['value']['clr']) ,8,2,odd=False)# clr value
        
        
                            change_x=0                    
                            for pll in pll_names:
                                keys=f"['inputs']['{key}']['value']['plls']['{pll}']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    if dict2!={}:
                                        if dict1['inputs'][key]['value']['plls'][pll] and not(dict2['inputs'][key]['value']['plls'][pll]):
                                            self.point_position((init_x+52+change_x,init_y+644), 1) # check box
                                        if not(dict1['inputs'][key]['value']['plls'][pll]) and dict2['inputs'][key]['value']['plls'][pll]:
                                            self.point_position((init_x+52+change_x,init_y+644), 1) # check box
                                    else:
                                        if dict1['inputs'][key]['value']['plls'][pll]:
                                            self.point_position((init_x+52+change_x,init_y+644), 1) # check box
                                        
                                change_x+=114
            dict2=old_state
                    
        
    def change_op_config(self, init_x, init_y,dict1,dict2): #x=1319, y=170
        '''
        Function to change output page configuration
        Settings are given by the user in the form of dictionary
        This is same as gui state
        '''
        
        # self.point_position((init_x,init_y), 1)
        # num_tabs=0
        global outputs_covered
        out_change_x={'11':0,'10':1,'9':2,'8':3,'7':4,'6':5,'5':6,'4':7,'3':8,'2':9,'1':10,'0':11}
        for key in dict1['outputs']['value']:
            old_state = copy.deepcopy(dict2)
                # if key not in inputs_covered:
                #     dict2={}
                # outputs_covered.append(key)
            
            change_x=27
            if key!='10' or key!='11':
                delta_x=0
            else:
                delta_x=0

            ## Only go to Outputs that have differences##            
            OP_CHANGE=False
            if dict2=={}:
                OP_CHANGE=True
            else:
                if dict1['outputs']['value'][key]!=dict2['outputs']['value'][key]:
                    OP_CHANGE=True
            ## Only go to Outputs that have differences##            
            if OP_CHANGE:
                if dict2!={}:
                    ##########################################################
                    keys=f"['outputs']['value']['{key}']['enabled']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        ##########################################################
                        # keys=f"['outputs']['value']['{key}']['enabled']"
                        # if_change=self.state_compare(dict2,dict1,keys)
                        # if if_change:
                        self.point_position((init_x+(change_x*out_change_x[key])+delta_x,init_y), 1)
                        time.sleep(1)
                        # enable output
                        self.point_position((init_x+42,init_y+23), 1)
                else:
                    if dict1['outputs']['value'][key]['enabled']:
                        self.point_position((init_x+(change_x*out_change_x[key])+delta_x,init_y), 1)
                        time.sleep(1)
                        # enable output
                        self.point_position((init_x+42,init_y+23), 1)
                    
                
                if dict1['outputs']['value'][key]['enabled']:
    
                    if key not in outputs_covered:
                        dict2={}
                    outputs_covered.append(key)
    
                    self.point_position((init_x+(change_x*out_change_x[key])+delta_x,init_y), 1)
                    time.sleep(1)
    
                    #enter freq
                    ##########################################################
                    keys=f"['outputs']['value']['{key}']['value']['freq']['value']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        self.point_position((init_x+138,init_y+100), 3) # Triple Click to select the text and replace it
                        ptg.typewrite(dict1['outputs']['value'][key]['value']['freq']['value'])
                    # VDD
                    ##########################################################
                    keys=f"['outputs']['value']['{key}']['value']['vddo']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        drop_val=self.change_drop_afterbase(dict2,dict1,keys,vddo)
                        # num_down=vddo[dict1['outputs']['value'][key]['value']['vddo']]
                        self.chng_drop_values(init_x+429,init_y+100,drop_val)
    
                    # PLL configuration
                    change_x_pll=0
                    for i in range (len(pll_names4out)):
                        ##########################################################
                        keys=f"['outputs']['value']['{key}']['value']['pll']['value']"
                        if_change=self.state_compare(dict2,dict1,keys)
                        if if_change:
                            if dict1['outputs']['value'][key]['value']['pll']['value']==pll_names4out[i]:
                                time.sleep(1)
                                self.point_position((init_x+62+change_x_pll,init_y+233), 1) # radio button
                        change_x_pll+=143
                        
                    # Sys ref
                    ##########################################################
                    keys=f"['outputs']['value']['{key}']['value']['sys_ref']['enabled']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+46,init_y+301), 1)
                        else:
                            if dict1['outputs']['value'][key]['value']['sys_ref']['enabled']:
                                self.point_position((init_x+46,init_y+301), 1)
                                
                    if dict1['outputs']['value'][key]['value']['sys_ref']['enabled']:
                        ##########################################################
                        keys=f"['outputs']['value']['{key}']['value']['sys_ref']['value']['pulser']['state']"
                        if_change=self.state_compare(dict2,dict1,keys)
                        if if_change:
                            time.sleep(1)
                            if dict1['outputs']['value'][key]['value']['sys_ref']['value']['pulser']['state']=='pulsar':
                                self.point_position((init_x+299,init_y+324), 1)
                                self.point_position((init_x+438,init_y+383), 3) # Triple Click to select the text and replace it
                                ptg.typewrite(dict1['outputs']['value'][key]['value']['freq']['value'])                                          
    
                    #delay
                    ##########################################################
                    keys=f"['outputs']['value']['{key}']['value']['delay']['value']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        time.sleep(1)
                        if dict1['outputs']['value'][key]['value']['delay']['value']:
                            self.point_position((init_x+102,init_y+512), 3)
                            ptg.typewrite(dict1['outputs']['value'][key]['value']['delay']['value'])
                    #Sync B
                    ##########################################################
                    keys=f"['outputs']['value']['{key}']['value']['syncb']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+296,init_y+512), 1)
                        else:                        
                            if dict1['outputs']['value'][key]['value']['syncb']:
                                self.point_position((init_x+296,init_y+512), 1)
                    #Phase hopping
                    ##########################################################
                    keys=f"['outputs']['value']['{key}']['value']['phfl']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        if dict2!={}:
                            self.point_position((init_x+471,init_y+512), 1)
                        else:
                            if dict1['outputs']['value'][key]['value']['phfl']:
                                self.point_position((init_x+471,init_y+512), 1)
                    # Single Ended
                    ##########################################################
                    keys=f"['outputs']['value']['{key}']['value']['m_se']['state']"
                    if_change=self.state_compare(dict2,dict1,keys)
                    if if_change:
                        # if dict2!={}:
                        self.point_position((init_x+58,init_y+579), 1) # single ended radio button
    
                    if dict1['outputs']['value'][key]['value']['m_se']['state']=='se':
                        ##########################################################
                        keys=f"['outputs']['value']['{key}']['value']['m_se']['value']['on']['enabled']"
                        if_change=self.state_compare(dict2,dict1,keys)
                        if if_change:
                            # if dict1['outputs']['value'][key]['value']['m_se']['value']['on']['enabled']:
                            self.point_position((init_x+44,init_y+604), 1) # ON
                            
                            ##########################################################
                            keys=f"['outputs']['value']['{key}']['value']['m_se']['value']['on']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:                                   
                                type1 = dict1['outputs']['value'][key]['value']['m_se']['value']['on']['value']
                                if type1=='clkp':
                                    self.point_position((init_x+69,init_y+670), 1)
                                if type1=='clkn':
                                    self.point_position((init_x+211,init_y+670), 1)
                            ##########################################################
                            keys=f"['outputs']['value']['{key}']['value']['m_se']['value']['op']['enabled']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                # if dict1['outputs']['value'][key]['value']['m_se']['value']['op']['enabled']:
                                    self.point_position((init_x+44,init_y+719), 1) # OP
                                ##########################################################
                                    keys=f"['outputs']['value']['{key}']['value']['m_se']['value']['op']['value']"
                                    if_change=self.state_compare(dict2,dict1,keys)
                                    if if_change:                                   
                                        type1 = dict1['outputs']['value'][key]['value']['m_se']['value']['op']['value']
                                        if type1=='clkp':
                                            self.point_position((init_x+69,init_y+776), 1)
                                        if type1=='clkn':
                                            self.point_position((init_x+211,init_y+776), 1)
                                            
                    else:
                                
                    
    
                        ##########################################################
                        keys=f"['outputs']['value']['{key}']['value']['m_de']['state']"
                        if_change=self.state_compare(dict2,dict1,keys)
                        if if_change:
                            self.point_position((init_x+365,init_y+580), 1)
        
                        if dict1['outputs']['value'][key]['value']['m_de']['state']=='de':
                            ##########################################################
                            keys=f"['outputs']['value']['{key}']['value']['m_de']['value']['submode']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict1['outputs']['value'][key]['value']['m_de']['value']['submode']!='':
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,op_mode)
                                    # num_down=op_mode[dict1['outputs']['value'][key]['value']['m_de']['value']['submode']]
                                    self.chng_drop_values(init_x+432,init_y+641,drop_val)
        
        ##################################################################################    
                                # ##########################################################
                            # if_change=self.state_compare(dict2,dict1,keys)

# swing={'LVDS':{'':0,'0.1 V':0,'0.2 V':1,'0.3 V':2,'0.4 V':3,'0.5 V':4,'0.6 V':5,'0.7 V':6,'0.8 V':7},
#         'LVPECL':{'':0,'0.5 V':0,'0.54 V':1,'0.58 V':2,'0.62 V':3,'0.66 V':4,'0.68 V':5,'0.7 V':6,'0.72 V':7},
#         'CML':{'':0,'0.05 V':0,'0.1 V':1,'0.15 V':2,'0.2 V':3,'0.25 V':4,'0.3 V':5,'0.35 V':6,'0.4 V':7},
#         'HCSL':{'':0,'0.5 V':0,'0.55 V':1,'0.6 V':2,'0.64 V':3,'0.68 V':4,'0.72 V':5,'0.76 V':6,'0.8 V':7},
#         'LVPECL2':{'':0,'0.5 V':0,'0.55 V':1,'0.6 V':2,'0.64 V':3,'0.68 V':4,'0.72 V':5,'0.76 V':6,'0.8 V':7}}

        
                                keys=f"['outputs']['value']['{key}']['value']['m_de']['value']['swing']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    # self.point_position((init_x+365,init_y+552), 1)
                                    keys=f"['outputs']['value']['{key}']['value']['m_de']['value']['swing']['value']"
                                    if dict1['outputs']['value'][key]['value']['m_de']['value']['swing']['value']!='':
                                        if dict2!={}:
                                            sub_mode=dict2['outputs']['value'][key]['value']['m_de']['value']['submode']
                                            if sub_mode=='':
                                                existing=0
                                            else:
                                                # existing=swing[sub_mode][dict2['outputs']['value'][key]['value']['m_de']['value']['swing']['value']]
                                                existing=7
                                        else:
                                            existing=0
                                        self.reset_drop(init_x+430,init_y+717,existing,go_to=0)
                                        sub_mode=dict1['outputs']['value'][key]['value']['m_de']['value']['submode']
                                        drop_val=swing[sub_mode][dict1['outputs']['value'][key]['value']['m_de']['value']['swing']['value']]
                                        # drop_val=swing[dict1['outputs']['value'][key]['value']['m_de']['value']['swing']['value']]
                                        self.chng_drop_values(init_x+430,init_y+717,drop_val)
                                    
                                    
                                    
                            else:
                                keys=f"['outputs']['value']['{key}']['value']['m_de']['value']['swing']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    # self.point_position((init_x+365,init_y+552), 1)
                                    if dict1['outputs']['value'][key]['value']['m_de']['value']['swing']['value']!='':
                                        if dict2!={}:
                                            sub_mode=dict2['outputs']['value'][key]['value']['m_de']['value']['submode']
                                            if sub_mode=='':
                                                existing=0
                                            else:
                                                existing=swing[sub_mode][dict2['outputs']['value'][key]['value']['m_de']['value']['swing']['value']]
                                        else:
                                            existing=0
                                        self.reset_drop(init_x+430,init_y+717,existing,go_to=0)
                                        sub_mode=dict1['outputs']['value'][key]['value']['m_de']['value']['submode']
                                        drop_val=swing[sub_mode][dict1['outputs']['value'][key]['value']['m_de']['value']['swing']['value']]
                                        # drop_val=swing[dict1['outputs']['value'][key]['value']['m_de']['value']['swing']['value']]
                                        self.chng_drop_values(init_x+430,init_y+717,drop_val)
            dict2=old_state
                                
                                
                                
                                # if dict2!={}:
                                #     swing_dict = swing[dict1['outputs']['value'][key]['value']['m_de']['value']['submode']]
                                #     old_dict = swing[dict2['outputs']['value'][key]['value']['m_de']['value']['submode']]
                                #     drop_val=self.change_drop_afterbase_swing(dict2,dict1,keys,swing_dict,old_dict)
                                # else:
                                #     sub_mode=dict1['outputs']['value'][key]['value']['m_de']['value']['submode']
                                #     drop_val=swing[sub_mode][dict1['outputs']['value'][key]['value']['m_de']['value']['swing']['value']]
                                # # num_down=swing[dict1['outputs']['value'][key]['value']['m_de']['value']['swing']['value']]
                                # self.drop_down_ctrl(init_x+430,init_y+686,drop_val)


##################################################################################    
                    
                    
            # num_tabs+=1
                
            #     change_x_pll=0
            #     for i in range (len(pll_names)):
            #         if dict1['outputs']['value'][key]['value']['pll']['value']==pll_names[i]:
            #             self.point_position((init_x+65+change_x_pll,init_y+503), 1) # radio button
            #         change_x_pll+=152
            #         # if dict1['outputs']['value'][key]['value']['pll']['enabled']:
            #         #     if dict1['outputs']['value'][key]['value']['pll']['value']==pll_names[i]:
            #         #         self.point_position((init_x+32+change_x_pll,init_y+482), 1) # radio button
            #         # change_x_pll+=85
            # change_x+=27
                
    def change_pll_config(self, init_x, init_y,dict1,dict2,ip_order=False): #644, 168
        '''
        Function to change pll page configuration
        Settings are given by the user in the form of dictionary
        This is same as gui state
        '''                
        global plls_covered
        

        self.point_position((init_x,init_y), 1)
        
        

        for pll in dict1['plls']:
            # self.point_position((init_x+145,init_y+773), 1)                        
            # self.smartdco(init_x,init_y,pll,dict1,dict2)#x=796, y=819
            old_state = copy.deepcopy(dict2)
            PLL_CHANGE=False
            if dict1['plls'][pll]['enabled']:
                ## Only go to Plls that have differences##            
                if dict2=={}:
                    PLL_CHANGE=True
                else:
                    if dict2['plls'][pll]!=dict1['plls'][pll]:
                        PLL_CHANGE=True
                ## Only go to Plls that have differences##            
                if pll not in plls_covered:
                    dict2={}
                plls_covered.append(pll)
                if PLL_CHANGE:
                    self.point_position((init_x,init_y), 1)
                    time.sleep(1)
                    ptg.hotkey('alt',pll[:1])
                    
                    ################## Minimize and maximize ##################s
                    self._minframe()
                    time.sleep(3)
                    self._maxframe()
                    time.sleep(6)
                    ###########################################################
    
                    if pll!='FT':
                        self.point_position((init_x+641,init_y+502), 1)
                        ptg.dragTo(init_x+641,init_y+ 349, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
                        # Free running select
                        if dict1['plls'][pll]['value']['free_running']['enabled']:
                            ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['mode']['o:phfl']['state']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict1['plls'][pll]['value']['free_running']['value']['mode']['o:phfl']['state']=='':   # Mode selection and configuration       
                                    self.point_position((init_x+47,init_y+102), 1)                                
                                if dict1['plls'][pll]['value']['free_running']['value']['mode']['o:phfl']['state']=='sys_ref':
                                    self.point_position((init_x+47,init_y+132), 1)
                                if dict1['plls'][pll]['value']['free_running']['value']['mode']['o:phfl']['state']=='syncb':
                                    self.point_position((init_x+47,init_y+162), 1)
                                if dict1['plls'][pll]['value']['free_running']['value']['mode']['o:phfl']['state']=='phfl':
                                    self.point_position((init_x+348,init_y+102), 1)
                                    time.sleep(1)
                                    self.point_position((init_x+437,init_y+157), 3)
                                    ptg.typewrite(dict1['plls'][pll]['value']['free_running']['value']['mode']['o:phfl']['value']['delta']['value'])
    
                                # OnChip Filter bandwidth
                              ##########################################################
                            if dict1['plls'][pll]['value']['free_running']['value']['sw_oc']['state']=='oc':
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['sw_oc']['state']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:                                    
                                    self.point_position((init_x+81,init_y+204), 1)
                                #enter freq
                                ##########################################################
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['sw_oc']['value']['fast']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    self.point_position((init_x+81,init_y+252), 3)
                                    ptg.typewrite(dict1['plls'][pll]['value']['free_running']['value']['sw_oc']['value']['fast']['value'])
                                    # enter normal bw
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['sw_oc']['value']['normal']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    self.point_position((init_x+270,init_y+252), 3)
                                    #enter freq
                                    ptg.typewrite(dict1['plls'][pll]['value']['free_running']['value']['sw_oc']['value']['normal']['value'])
                                  ##########################################################
                            if dict1['plls'][pll]['value']['free_running']['value']['sw_ext']['state']=='ext':
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['sw_ext']['state']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                      self.point_position((init_x+399,init_y+204), 1)
                                ##########################################################
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['sw_ext']['value']['decimation']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    time.sleep(1)
                                    self.point_position((init_x+470,init_y+255), 3)
                                    #enter freq
                                    ptg.typewrite(dict1['plls'][pll]['value']['free_running']['value']['sw_ext']['value']['decimation']['value'])
                              # Clock Switch
                              #                                         'hitless': {'ph_bout': 'propagation',
                              #                                                     'ph_prop': {'state': 'propagation',
                              #                                                                 'value': {'slope': {'parsed': None,
                              #                                                                                     'valid': True,
                              #                                                                                     'value': 'Bandwidth'}}}}},
                              # ##########################################################
                            if dict1['plls'][pll]['value']['free_running']['value']['clock_switch']['hitless']['ph_bout']=='buildout':
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['clock_switch']['hitless']['ph_bout']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    self.point_position((init_x+85,init_y+337), 1)
                            if dict1['plls'][pll]['value']['free_running']['value']['clock_switch']['hitless']['ph_prop']['state']=='propagation':
                                ##########################################################
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['clock_switch']['hitless']['ph_prop']['value']['slope']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    self.point_position((init_x+85,init_y+367), 1)
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,phase_prop_slope)
                                    # drop_val=phase_prop_slope[dict1['plls'][pll]['value']['free_running']['value']['clock_switch']['hitless']['ph_prop']['value']['slope']['value']]
                                    self.chng_drop_values(init_x+154,init_y+418,drop_val)
    
                              ############## Frequency Ramp #########
                              ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['clock_switch']['frequency_ramp']['enabled']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  if dict2!={}:
                                      self.point_position((init_x+399,init_y+317), 1)
                                  else:
                                      if dict1['plls'][pll]['value']['free_running']['value']['clock_switch']['frequency_ramp']['enabled']:
                                          self.point_position((init_x+399,init_y+317), 1)
                                        
    
                            if dict1['plls'][pll]['value']['free_running']['value']['clock_switch']['frequency_ramp']['enabled']:
                                  ##########################################################
                                  keys=f"['plls']['{pll}']['value']['free_running']['value']['clock_switch']['frequency_ramp']['value']['slope']['value']"
                                  if_change=self.state_compare(dict2,dict1,keys)
                                  if if_change:                                    
                                      drop_val=self.change_drop_afterbase(dict2,dict1,keys,freq_ramp_slope)
                                      self.chng_drop_values(init_x+466,init_y+396,drop_val)
                
                
                              ############## Frequency Lock Loss #############
                              
                              ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['enabled']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  if dict2!={}:
                                    self.point_position((init_x+95,init_y+472), 1)                                        
                                  else:
                                      if not (dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['enabled']):
                                          self.point_position((init_x+95,init_y+472), 1)
                                    
    
                            if dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['enabled']:
                                  # self.point_position((init_x+95,init_y+472), 1)
                                  ##########################################################
                                  keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['value']['delay']['value']"
                                  if_change=self.state_compare(dict2,dict1,keys)
                                  if if_change:
                                      # drop_val=lockl_delay[dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['value']['delay']['value']]                
                                      drop_val=self.change_drop_afterbase(dict2,dict1,keys,lockl_delay)
                                      self.chng_drop_values(init_x+95,init_y+501,drop_val)
                                  ##########################################################
                                  keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['value']['timer']"
                                  if_change=self.state_compare(dict2,dict1,keys)
                                  if if_change:
                                      if dict2!={}:
                                          self.point_position((init_x+258,init_y+498), 1)
                                      else:
                                          if not(dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['value']['timer']): # timer enabled by default
                                              self.point_position((init_x+258,init_y+498), 1)
            
                                  ########## PPM widget#########
                                  # PPM Set Clear
                                  ##########################################################
                                  keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['value']['ppm']['value']['set']['value']"
                                  if_change=self.state_compare(dict2,dict1,keys)
                                  if if_change:
                                      # drop_val=ppm_set[dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['value']['ppm']['value']['set']['value']]
                                      drop_val=self.change_drop_afterbase(dict2,dict1,keys,ppm_set)
                                      self.chng_drop_values(init_x+78,init_y+575,drop_val)
                                  ##########################################################
                                  keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['value']['ppm']['value']['clr']['value']"
                                  if_change=self.state_compare(dict2,dict1,keys)
                                  if if_change:
                                      # drop_val=ppm_clear[dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['value']['ppm']['value']['clr']['value']]
                                      drop_val=self.change_drop_afterbase(dict2,dict1,keys,ppm_clear)
                                      self.chng_drop_values(init_x+236,init_y+575,drop_val)
                                  # else:
                                  #     self.point_position((init_x+95,init_y+472), 1)
                                
                                  
                              
                              ############## IP Clock Selection ##############
                              ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['ip_clock']['select']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  # num_down=ip_clock_selection[dict1['plls'][pll]['value']['free_running']['value']['ip_clock']['select']]
                                  drop_val=self.change_drop_afterbase(dict2,dict1,keys,ip_clock_selection)
                                  self.chng_drop_values(init_x+470,init_y+522,drop_val)
                            ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['ip_clock']['revertive']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict2!={} and dict1['plls'][pll]['value']['free_running']['value']['ip_clock']['select']=='Auto':
                                    self.point_position((init_x+470,init_y+579), 1)
                                else:
                                      if not(dict1['plls'][pll]['value']['free_running']['value']['ip_clock']['revertive']) and dict1['plls'][pll]['value']['free_running']['value']['ip_clock']['select']=='Auto': # revertive enabled by default
                                          self.point_position((init_x+470,init_y+579), 1)

                    
                            ############## Phase Lock Loss ###################     
                            ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['phase_lock_loss']['enabled']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  if dict2!={}:
                                    self.point_position((init_x+95,init_y+624), 1)                                        
                                  else:
                                      if not (dict1['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['enabled']):
                                          self.point_position((init_x+95,init_y+624), 1)
                                
                            if dict1['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['enabled']:
                                  # self.point_position((init_x+116,init_y+382), 1)
                                  # self.point_position((init_x+88,init_y+403), 1)
                                  ##########################################################
                                  keys=f"['plls']['{pll}']['value']['free_running']['value']['phase_lock_loss']['value']['delay']['value']"
                                  if_change=self.state_compare(dict2,dict1,keys)
                                  if if_change:
                                      # phase_lock_loss_delay
                                      drop_val=self.change_drop_afterbase(dict2,dict1,keys,phase_lock_loss_delay)
                                      self.chng_drop_values(init_x+47,init_y+673,drop_val)
                                    
                                  ##########################################################
                                  keys=f"['plls']['{pll}']['value']['free_running']['value']['phase_lock_loss']['value']['timer']"
                                  if_change=self.state_compare(dict2,dict1,keys)
                                  if if_change:
                                      if dict2!={}:
                                          self.point_position((init_x+147,init_y+671), 1)
                                      else:
                                          if not(dict1['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['value']['timer']):
                                              self.point_position((init_x+147,init_y+671), 1)
                                          
                                  ##########################################################
                                  keys=f"['plls']['{pll}']['value']['free_running']['value']['phase_lock_loss']['value']['phase_delta']['value']"
                                  if_change=self.state_compare(dict2,dict1,keys)
                                  if if_change:
                                      time.sleep(2)
                                      self.point_position((init_x+97,init_y+730), 3)
                                      ptg.typewrite(dict1['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['value']['phase_delta']['value'])
                                                                              
                              ########## HoldOver #############
                              ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['holdover']['delay']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  # drop_val=ho_delay[dict1['plls'][pll]['value']['free_running']['value']['holdover']['delay']['value']]
                                  drop_val=self.change_drop_afterbase(dict2,dict1,keys,ho_delay)
                                  self.chng_drop_values(init_x+532,init_y+671,drop_val)
                            ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['holdover']['average']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  # drop_val=ho_average[dict1['plls'][pll]['value']['free_running']['value']['holdover']['average']['value']]
                                  drop_val=self.change_drop_afterbase(dict2,dict1,keys,ho_average)
                                  self.chng_drop_values(init_x+532,init_y+725,drop_val)
                              
                            ######### ZDM ###################
                
                            ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['zdm']['state']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  if dict1['plls'][pll]['value']['free_running']['value']['zdm']['state']=='':
                                      self.point_position((init_x+229,init_y+648), 1)
                                  if dict1['plls'][pll]['value']['free_running']['value']['zdm']['state']=='internal':
                                      self.point_position((init_x+229,init_y+704), 1)
                                  if dict1['plls'][pll]['value']['free_running']['value']['zdm']['state']=='external':
                                      self.point_position((init_x+314,init_y+643), 1)
                                      ##########################################################
                                      keys=f"['plls']['{pll}']['value']['free_running']['value']['zdm']['external']['feedback']['value']"
                                      if_change=self.state_compare(dict2,dict1,keys)
                                      if if_change:
                                          drop_val=self.change_drop_afterbase(dict2,dict1,keys,zdm_ext_feedback)
                                          self.chng_drop_values(init_x+393,init_y+674,drop_val)
                                      ##########################################################
                                      keys=f"['plls']['{pll}']['value']['free_running']['value']['zdm']['external']['output']['value']"
                                      if_change=self.state_compare(dict2,dict1,keys)
                                      if if_change:
                                          drop_val=self.change_drop_afterbase(dict2,dict1,keys,zdm_ext_output)
                                          self.chng_drop_values(init_x+393,init_y+719,drop_val)
                                  
                  
                                ########## DCO Mode #############
                              
                            ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['dco']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  # if dict1['plls'][pll]['value']['free_running']['value']['dco']: # dco enabled by default
                                  if dict2!={}:
                                      self.point_position((init_x+162,init_y+763), 1)
                                  else:
                                      if dict1['plls'][pll]['value']['free_running']['value']['dco']:
                                          self.point_position((init_x+162,init_y+763), 1)
                                        
                                      ########### Fast Lock HoldOver ###########
                            ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['fast_lock_ho']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                  if dict2!={}:
                                      self.point_position((init_x+488,init_y+763), 1)
                                  else:                                
                                      if not(dict1['plls'][pll]['value']['free_running']['value']['fast_lock_ho']):
                                          self.point_position((init_x+488,init_y+763), 1)
                              
                        #### End of free running widgets #######
                        self.point_position((init_x+641,init_y+422), 1)
                        ptg.dragTo(init_x+641,init_y+ 465, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
                #                                            'ppath': True}},
               
                        ############# Smart DCO ###########
                        # if dict2!={}:
                        #     if dict1['plls'][pll]['value']['smartdco']!=dict2['plls'][pll]['value']['smartdco']:
                        #         self.point_position((init_x+145,init_y+773), 1)                        
                        #         self.smartdco(init_x,init_y,pll,dict1,dict2)#x=796, y=819
                        # else:
                        #     self.point_position((init_x+145,init_y+773), 1)                        
                        #     self.smartdco(init_x,init_y,pll,dict1,dict2)#x=796, y=819
                            
              
                        ##########################################################
                        keys=f"['plls']['{pll}']['value']['ptp']['enabled']"
                        if_change=self.state_compare(dict2,dict1,keys)
                        if if_change:
                              if dict2!={}:
                                  self.point_position((init_x+359,init_y+743), 1)
                              else:
                                  if dict1['plls'][pll]['value']['ptp']['enabled']:
                                      self.point_position((init_x+359,init_y+743), 1)                                
                                
                        if dict1['plls'][pll]['value']['ptp']['enabled']:
                              self.point_position((init_x+468,init_y+767), 1)
                              ##########################################################
                              ptg.hotkey('tab')
                              time.sleep(1)
                              # self.point_position((917,544), 1)
                              keys=f"['plls']['{pll}']['value']['ptp']['value']['bw']['value']"
                              if_change=self.state_compare(dict2,dict1,keys)
                              if if_change:
                                  ptg.typewrite(dict1['plls'][pll]['value']['ptp']['value']['bw']['value'])
                              ##########################################################
                              ptg.hotkey('tab')
                              keys=f"['plls']['{pll}']['value']['ptp']['value']['ipath']"
                              if_change=self.state_compare(dict2,dict1,keys)
                              if if_change:
                                  if dict2!={}:
                                      ptg.hotkey('space')
                                  else:
                                      if not(dict1['plls'][pll]['value']['ptp']['value']['ipath']):
                                          ptg.hotkey('space')
                              ##########################################################
                              ptg.hotkey('tab')
                              # self.point_position((911,600), 1)
                              time.sleep(1)
                              keys=f"['plls']['{pll}']['value']['ptp']['value']['phase_ur']['value']"
                              if_change=self.state_compare(dict2,dict1,keys)
                              if if_change:
                                  ptg.typewrite(dict1['plls'][pll]['value']['ptp']['value']['phase_ur']['value'])
                              ##########################################################
                              keys=f"['plls']['{pll}']['value']['ptp']['value']['phase_sl']['value']"
                              if_change=self.state_compare(dict2,dict1,keys)
                              if if_change:
                                  # drop_val=phase_prop_slope[dict1['plls'][pll]['value']['ptp']['value']['phase_sl']['value']]
                                  drop_val=self.change_drop_afterbase(dict2,dict1,keys,phase_prop_slope)
                                  self.chng_drop_values(init_x+385,init_y+433,drop_val)
                              ptg.hotkey('esc')
                              time.sleep(1)
                            
                                                       
                        ##########################################################
                        keys=f"['plls']['{pll}']['value']['in3_sync']"
                        if_change=self.state_compare(dict2,dict1,keys)
                        if if_change:
                            if dict2!={}:
                                if pll=='A':
                                    self.point_position((init_x+312,init_y+808), 1)
                                else:
                                    self.point_position((init_x+152,init_y+808), 1)
                            else:
                                if dict1['plls'][pll]['value']['in3_sync']:
                                    if pll=='A':
                                        self.point_position((init_x+312,init_y+808), 1)
                                    else:
                                        self.point_position((init_x+152,init_y+808), 1)

                        ##########################################################
                        keys=f"['plls']['{pll}']['value']['lwm']"
                        if_change=self.state_compare(dict2,dict1,keys)
                        if if_change:
                              if dict2!={}:
                                  self.point_position((init_x+482,init_y+808), 1)        
                              else:
                                  if dict1['plls'][pll]['value']['lwm']:
                                      self.point_position((init_x+482,init_y+808), 1)
                                                          # 
                    else: # FT PLL
                        
                          # OnChip Filter bandwidth
                          ##########################################################
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['sw_oc']['state']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                              if dict1['plls'][pll]['value']['free_running']['value']['sw_oc']['state']=='oc':
                                  self.point_position((init_x+81,init_y+89), 1)
                          ##########################################################
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['sw_oc']['value']['fast']['value']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                            time.sleep(1)
                            self.point_position((init_x+159,init_y+148), 3)
                            #enter freq
                            ptg.typewrite(dict1['plls'][pll]['value']['free_running']['value']['sw_oc']['value']['fast']['value'])
                            # enter normal bw
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['sw_oc']['value']['normal']['value']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                            time.sleep(1)
                            self.point_position((init_x+470,init_y+148), 3)
                            #enter freq
                            ptg.typewrite(dict1['plls'][pll]['value']['free_running']['value']['sw_oc']['value']['normal']['value'])
                            
                              ############## Frequency Lock Loss #############
                              
                          ##########################################################
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['enabled']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                              if dict2!={}:
                                  self.point_position((init_x+78,init_y+201), 1)
                              else:
                                  if not(dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['enabled']):
                                      self.point_position((init_x+78,init_y+201), 1)
                          
                          if dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['enabled']:
                                # self.point_position((init_x+95,init_y+472), 1)
                                ##########################################################
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['value']['delay']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    # drop_val=lockl_delay[dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['value']['delay']['value']]                
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,lockl_delay)
                                    self.chng_drop_values(init_x+105,init_y+230,drop_val)
                                ##########################################################
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['value']['timer']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    if dict2!={}:
                                        self.point_position((init_x+266,init_y+230), 1)
                                    else:                                    
                                        if not(dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['value']['timer']): # timer enabled by default
                                            self.point_position((init_x+266,init_y+230), 1)
                   
                                    ########## PPM widget#########
                                    # PPM Set Clear
                                ##########################################################
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['value']['ppm']['value']['set']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    # drop_val=ppm_set[dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['value']['ppm']['value']['set']['value']]
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,ppm_set)
                                    self.chng_drop_values(init_x+81,init_y+314,drop_val)
                                ##########################################################
                                keys=f"['plls']['{pll}']['value']['free_running']['value']['freq_lock_loss']['value']['ppm']['value']['clr']['value']"
                                if_change=self.state_compare(dict2,dict1,keys)
                                if if_change:
                                    # drop_val=ppm_clear[dict1['plls'][pll]['value']['free_running']['value']['freq_lock_loss']['value']['ppm']['value']['clr']['value']]
                                    drop_val=self.change_drop_afterbase(dict2,dict1,keys,ppm_clear)
                                    self.chng_drop_values(init_x+243,init_y+314,drop_val)
                          # else:
                          #    self.point_position((init_x+78,init_y+201), 1)
                                
                                  
                              
                          ############## IP Clock Selection ##############
                          ##########################################################
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['ip_clock']['select']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                            # num_down=ip_clock_selection[dict1['plls'][pll]['value']['free_running']['value']['ip_clock']['select']]
                            drop_val=self.change_drop_afterbase(dict2,dict1,keys,ip_clock_selection)
                            self.chng_drop_values(init_x+487,init_y+250,drop_val)
                          ##########################################################
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['ip_clock']['revertive']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                            if dict2!={}:
                                self.point_position((init_x+487,init_y+315), 1)
                            else:
                                if not(dict1['plls'][pll]['value']['free_running']['value']['ip_clock']['revertive']): # revertive enabled by default
                                    self.point_position((init_x+487,init_y+315), 1)
                  
                          ############## Phase Lock Loss ###################     
                          ##########################################################
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['phase_lock_loss']['enabled']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                              if dict2!={}:
                                  self.point_position((init_x+71,init_y+367), 1)
                              else:
                                  if not(dict1['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['enabled']):
                                      self.point_position((init_x+71,init_y+367), 1)
                                 
                          if dict1['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['enabled']:
                            # self.point_position((init_x+116,init_y+382), 1)
                            # self.point_position((init_x+88,init_y+403), 1)
                            ##########################################################
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['phase_lock_loss']['value']['delay']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                # phase_lock_loss_delay
                                drop_val=self.change_drop_afterbase(dict2,dict1,keys,phase_lock_loss_delay)
                                self.chng_drop_values(init_x+154,init_y+414,drop_val)

                            keys=f"['plls']['{pll}']['value']['free_running']['value']['phase_lock_loss']['value']['timer']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                if dict2!={}:
                                    self.point_position((init_x+473,init_y+414), 1)
                                else:
                                    if not(dict1['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['value']['timer']):
                                        self.point_position((init_x+473,init_y+414), 1)
                                
                            keys=f"['plls']['{pll}']['value']['free_running']['value']['phase_lock_loss']['value']['phase_delta']['value']"
                            if_change=self.state_compare(dict2,dict1,keys)
                            if if_change:
                                time.sleep(1)
                                self.point_position((init_x+316,init_y+475), 3)
                                ptg.typewrite(dict1['plls'][pll]['value']['free_running']['value']['phase_lock_loss']['value']['phase_delta']['value'])
                               
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['dco']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                              if dict2!={}:
                                  self.point_position((init_x+491,init_y+527), 1)
                              else:
                                  if dict1['plls'][pll]['value']['free_running']['value']['dco']:
                                      self.point_position((init_x+491,init_y+527), 1)
                                     
                          keys=f"['plls']['{pll}']['value']['free_running']['value']['fast_lock_ho']"
                          if_change=self.state_compare(dict2,dict1,keys)
                          if if_change:
                              if dict2!={}:
                                  self.point_position((init_x+502,init_y+527), 1)
                              else:
                                  if not(dict1['plls'][pll]['value']['free_running']['value']['fast_lock_ho']):
                                      self.point_position((init_x+502,init_y+527), 1)
                         
                          ############# Smart DCO ###########
                          # if dict2!={}:
                          #      if dict1['plls'][pll]['value']['smartdco']!=dict2['plls'][pll]['value']['smartdco']:
                          #          self.point_position((init_x+312,init_y+624), 1)
                          #          self.smartdco(init_x,init_y,pll,dict1,dict2)#x=796, y=819
                          # else:
                          #      self.point_position((init_x+312,init_y+624), 1)
                          #      self.smartdco(init_x,init_y,pll,dict1,dict2)#x=796, y=819                             
    
    
                    if ip_order: #696, 896
                          self.point_position((init_x+52,init_y+728), 1)
                          self.point_position((init_x+85,init_y+754), 1)
                    
                    
            dict2=old_state
            # num_tabs+=1
        
    def chip_communication(self,init_x,init_y,dict1,dict2): # x=155, y=64
     # 'comms': {'i2c': {'address': {'parsed': 91, 'valid': True, 'value': '0x5B'}},
     #       'spi': {'wires': 4},
     #       'type': 'i2c'},

        time.sleep(2)
        keys="['comms']['type']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict1['comms']['type']=='spi':               
                self.point_position((init_x,init_y), 1)
                
        keys="['comms']['spi']['wires']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict1['comms']['spi']['wires']==3:
                self.point_position((init_x+15,init_y+62), 1)
            if dict1['comms']['spi']['wires']==4:
                self.point_position((init_x+149,init_y+62), 1)

        keys="['comms']['type']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict1['comms']['type']=='i2c':
                # keys="['comms']['i2c']['address']['value']"
                self.point_position((init_x+271,init_y), 1)
                time.sleep(1)
                self.point_position((init_x+344,init_y+63), 3)
                ptg.typewrite(str(dict1['comms']['i2c']['address']['value']))
        
    def xtal_ctrl(self, init_x, init_y,dict1,dict2): #x=772, y=112

 # 'crystal': {'doubler': True,
 #             'freq': {'parsed': Fraction(54000000, 1),
 #                      'valid': True,
 #                      'value': '54 MHz'},
             # 'mode': 'LFF CL=8pF'},

        ##########################################################
        keys="['golden_clock']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict1['golden_clock']=='xtal':
                self.point_position((init_x-120,init_y-10), 1)
            
        keys="['crystal']['freq']['value']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            time.sleep(1)
            self.point_position((init_x,init_y), 3)
            ptg.typewrite(dict1['crystal']['freq']['value'])
        # choose mode
        keys="['crystal']['mode']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            drop_val=self.change_drop_afterbase(dict2,dict1,keys,xtal_mode)
            # drop_val = xtal_mode[dict1['crystal']['mode']]
            self.chng_drop_values(init_x+174,init_y,drop_val)
        keys="['crystal']['doubler']"
        if_change=self.state_compare(dict2,dict1,keys)
        if dict2!={}:
            if if_change:
                # if not(dict1['crystal']['doubler']):
                self.point_position((init_x+331,init_y), 1)
        else:
            if not(dict1['crystal']['doubler']):
                self.point_position((init_x+331,init_y), 1)

    def vddio_ctrl(self, init_x, init_y,dict1): #x=104, y=771
        if dict1['vddio']=='vdd':
            self.point_position((init_x,init_y), 1)
        if dict1['vddio']=='vddin':
            self.point_position((init_x,init_y+65), 1)
        else:
            pass
            
    def birds_eye_ctrl(self,init_x, init_y): #427,721
        self.point_position((init_x,init_y), 1)
        be=None
        while be is None:
            be=ptg.locateOnScreen(working_dir+"\\"+"images\\birds_eye.PNG",grayscale=True,confidence=.8)
        if be:
            self.point_position((init_x+3,init_y-211), 1)
            
        be_popup=None
        timeout = time.time() + 20 # 20 seconds
        while be_popup is None:
            be_popup=ptg.locateOnScreen(working_dir+"\\"+"images\\birds_eye_popup_"+variant+".PNG",grayscale=True,confidence=.8)
            if be_popup or time.time() > timeout:
                break
        if be_popup:
            # self.point_position((init_x+710,init_y-604), 1)
            print('Birds eye view test passed')
            self.point_position((init_x+649,init_y-609), 1)
        else:
            print('Birds eye view window did not match')
            print('Birds eye view test failed')
            
    def realtime_ctrl(self,init_x, init_y): #79,716
        self.point_position((init_x,init_y), 1)
        realtime_if_popup=None
        timeout = time.time() + 30 # 20 seconds
        while realtime_if_popup is None:
            realtime_if_popup=ptg.locateOnScreen(working_dir+"\\"+"images\\realtime_if_popup.PNG",grayscale=True,confidence=.8)
            if realtime_if_popup or time.time() > timeout:
                break
        if realtime_if_popup:            
            realtime_window=None
            timeout = time.time() + 20 # 20 seconds
            while realtime_window is None:
                realtime_window=ptg.locateOnScreen(working_dir+"\\"+"images\\realtime_window_"+variant+".PNG",grayscale=True,confidence=.8)
                if realtime_window or time.time() > timeout:
                    break
            if realtime_window:
                # self.point_position((init_x+1044,init_y-706), 1)
                print('realtime window test passed')
                ptg.press('esc')
            else:
                print('realtime window did not match')
                print('realtime window popup test failed')
        else:
            print('realtime window did not popup or took too long to pop up')        
            print('realtime window popup test failed')
            
    def verify_efuse_ctrl(self,init_x, init_y): #1223,115
        self.point_position((init_x,init_y), 1)
        
    def dump_ctrl(self,init_x, init_y,path,filename,dump_as='nvm'): #x=1328, y=1013
        dump_as_dict={'json':1,'nvm':2,'uvm':3}
        self.point_position((init_x,init_y), 1)
        # time.sleep(5) # wait for window to respond
        save_user_profile= None
        timeout = time.time() + 20 # 20 seconds
        while save_user_profile is None:
            save_user_profile=ptg.locateOnScreen(working_dir+"\\"+"images\\dump_file.PNG",grayscale=True,confidence=.5)
            if save_user_profile or time.time() > timeout:
                break
        # time.sleep(2) # wait for window to respond
        if save_user_profile:
            drop_val=dump_as_dict[dump_as]
            # type name and save file
            # self.chng_drop_values(init_x-823,init_y-514,drop_val)
            # self.point_position((init_x-823,init_y-540), 3)
            ptg.typewrite(path+'\\'+filename+'_'+dump_as)
            ptg.press('tab')
            [ptg.press('down') for x in range(0,drop_val)]
            ptg.press('enter')
            ptg.press('enter')
                
            replace = None
            timeout = time.time() + 10 # 5 seconds
            while replace is None:
                replace=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.5)
                if replace or time.time() > timeout:
                    break
            if replace:
                ptg.press('left')
                ptg.press('enter')
                print('%s dump successful'%dump_as)
            else:
                print('%s dump successful'%dump_as)
        else:
            print('%s dump failed'%dump_as)
            print('%s save window did not pop up'%dump_as)
            

            
    def load_nvm(self, init_x, init_y,path,filename): #x=640, y=722 #F:\Automate_GUI\output_files filename = profile17_nvm.nvm
        ptg.moveTo(init_x,init_y)
        # self.point_position((init_x,init_y), 1)
        load_nvm= None
        timeout = time.time() + 20 # 20 seconds
        while load_nvm is None:
            load_nvm=ptg.locateOnScreen(working_dir+"\\"+"images\\load_nvm.PNG",grayscale=True,confidence=.5)
            if load_nvm or time.time() > timeout:
                break
        if load_nvm:
            self.point_position((init_x,init_y), 1)
            load_nvm_profile= None
            timeout = time.time() + 20 # 20 seconds
            while load_nvm_profile is None:
                load_nvm_profile=ptg.locateOnScreen(working_dir+"\\"+"images\\load_nvm_profile.PNG",grayscale=True,confidence=.5)
                if load_nvm_profile or time.time() > timeout:
                    break
            if load_nvm_profile:
                
                # ptg.typewrite(working_dir+\\"+'\\'+filename)
                ptg.typewrite(path+'_nvm'+'\\'+filename)
                ptg.press('enter')
                
                nvm_load_successful= None
                timeout = time.time() + 60 # 30 seconds
                while nvm_load_successful is None:
                    nvm_load_successful=ptg.locateOnScreen(working_dir+"\\"+"images\\nvm_load_successful.PNG",grayscale=True,confidence=.5)
                    if nvm_load_successful or time.time() > timeout:
                        break
                if nvm_load_successful:
                    ptg.press('enter')
                    nvm_load_window= None
                    timeout = time.time() + 30 # 30 seconds
                    while nvm_load_window is None:
                        nvm_load_window=ptg.locateOnScreen(working_dir+"\\"+"images\\nvm_load_window_"+variant+".PNG",grayscale=True,confidence=.5)
                        if nvm_load_window or time.time() > timeout:
                            break
                    if nvm_load_window:
                        # incase file has to be replaced
                        print('load nvm test successful')
                        ptg.press('esc')
                    else:
                        print('load nvm test failed')
                        print('nvm not loaded correctly')
                else:
                    print('load nvm test failed')
                    print('nvm was not loaded successfully in the chip')
            else:
                print('load nvm test failed')
                print('load nvm window was not loaded. Hence the nvm name could not be entered for loading')
                
        else:
            print('load nvm test failed')
            print('load nvm button was not ready for loading nvm file')
            
    def verify_efuse(self,init_x, init_y,path,filename): #x=1232, y=111 #profile17_nvm.nvm
        if '.efuse' in filename:
            print('Your file seems to be an efuse file')
            print('It is not recommonded to load an efuse file hence we are stopping efuse verify test')
        else:
            self.point_position((init_x,init_y), 1)
            load_efuse_file= None
            timeout = time.time() + 20 # 20 seconds
            while load_efuse_file is None:
                load_efuse_file=ptg.locateOnScreen(working_dir+"\\"+"images\\load_efuse_file.PNG",grayscale=True,confidence=.5)
                if load_efuse_file or time.time() > timeout:
                    break
            if load_efuse_file:
                ptg.typewrite(path+'\\'+filename)
                ptg.press('enter')
                not_efuse_file= None
                timeout = time.time() + 20 # 20 seconds
                while not_efuse_file is None:
                    not_efuse_file=ptg.locateOnScreen(working_dir+"\\"+"images\\not_efuse_file.PNG",grayscale=True,confidence=.5)
                    if not_efuse_file or time.time() > timeout:
                        break
                if not_efuse_file:
                    ptg.press('enter')
                else:
                    print('verify efuse test failed')
                    print('This is not a EFUSE file. confirm? window did not pop up')
                
                efuse_verify_successful= None
                timeout = time.time() + 20 # 20 seconds
                while efuse_verify_successful is None:
                    efuse_verify_successful=ptg.locateOnScreen(working_dir+"\\"+"images\\efuse_verify_successful_ok.PNG",grayscale=True,confidence=.5)
                    if efuse_verify_successful or time.time() > timeout:
                        break
                if efuse_verify_successful:
                    ptg.press('enter')
                    print('verify efuse test successful')
                else:
                    mismatch_found= None
                    timeout = time.time() + 20 # 20 seconds
                    while mismatch_found is None:
                        mismatch_found=ptg.locateOnScreen(working_dir+"\\"+"images\\mismatch_found.PNG",grayscale=True,confidence=.5)
                        if mismatch_found or time.time() > timeout:
                            break
                    if mismatch_found:
                        print('verify efuse test failed')
                        print('Mismatch found')
                        ptg.press('enter')
                    else:
                        print('efuse verify test failed')
                        print('Loading took too long')
            else:
                print('efuse verify window was not loaded. Hence the nvm name could not be entered for loading')
                
                        
    def json_load(self,init_x, init_y,path,filename): #497,716  profile17_json.variants.json
        self.reset_chip(init_x+620,init_y-639) #1117,77
        ptg.moveTo(init_x,init_y)
        load_enabled= None
        timeout = time.time() + 20 # 20 seconds
        while load_enabled is None:
            load_enabled=ptg.locateOnScreen(working_dir+"\\"+"images\\load_enabled.PNG",grayscale=True,confidence=.8)
            if load_enabled or time.time() > timeout:
                break
        if load_enabled:
            self.point_position((init_x,init_y), 1)
            
            load_screen=None
            timeout = time.time() + 20 # 20 seconds
            while load_screen is None:
                load_screen=ptg.locateOnScreen(working_dir+"\\"+"images\\load_file.PNG",grayscale=True,confidence=.5)
                if load_screen or time.time() > timeout:
                    break
    
            if load_screen:
                ptg.typewrite(path+'\\'+filename)
                ptg.press('enter')
                time.sleep(15)
    
                json_load=None
                timeout = time.time() + 20 # 20 seconds
                while json_load is None:
                    json_load=ptg.locateOnScreen(working_dir+"\\"+"images\\json_load.PNG",grayscale=True,confidence=0.5)
                    if json_load or time.time() > timeout:
                        break
                if json_load:
                    ptg.press('enter') # json loads but if warnings is there it pops up and stays. This is to avaoid that
                    print('json file loaded successfully')
                    print('json file load test passed')
                else:
                    # checking for backend warnings if exists
                    backend_warning= None
                    timeout = time.time() + 10 # 10 seconds
                    while backend_warning is None:
                        backend_warning=ptg.locateOnScreen(working_dir+"\\"+"images\\backend_warning.PNG",grayscale=True,confidence=.5)
                        if backend_warning or time.time() > timeout:
                            break
                    if backend_warning:
                        ptg.press('enter')
                        json_load=None
                        timeout = time.time() + 20 # 20 seconds        
                        while json_load is None:
                            json_load=ptg.locateOnScreen(working_dir+"\\"+"images\\json_load.PNG",grayscale=True,confidence=0.5)
                            if json_load or time.time() > timeout:
                                break
                        if json_load:
                            print('json file loaded successfully')
                            print('json file load test passed')

                        else:
                            print('json load test failed')
                            print('json file did not get loaded or took too long to get loaded')                    
            else:
                print('json load test failed')
                print('json load window took too long to load')
        else:
            print('json load test failed')
            print('load button took too long to get enabled')
        
    def flexio_dropdown_ctrl(self,init_x, init_y,num_dropdown):
        
        for x in range (num_dropdown):
            self.point_position((init_x,init_y), 1)
            if x>0:
                ptg.press('down')
                ptg.press('enter')
            else:
                ptg.press('enter')
    
    def select_bw_boxes(self,init_x, init_y,change_x,change_y,total_rows,total_cols): #359,235 To select between boxes in clock Monitoring Defect, Clock Monitoring Notify and PLL Notify options
        rem_change_y=change_y
        rem_change_x=change_x
        for x in range(total_rows):
            if x==0:
                change_y=0
            for i in range(total_cols):
                if i==0:
                    change_x=0
                self.point_position((init_x+change_x,init_y+change_y), 1)
                change_x+=rem_change_x
            change_y+=rem_change_y
                
            
      
    #flexio_defect_notify
    def flexio_select(self,init_x,init_y,dict1,flexio_num):
        self.point_position((init_x,init_y), 1)
        drop_val=flexio_defect_notify[dict1['flexio']['value']['flexio'][flexio_num]['value']]
        delta_y=50
        if flexio_num=='15':
            delta_y= 100
        self.chng_drop_values(init_x+95,init_y+delta_y,drop_val)
        
    def fexio_clock_mon(self,init_x,init_y,dict1): #425,327
        k=0
        change_y=0
        change_x=0
        val=clock_monitoring_def_opt[dict1['flexio']['value']['clkmon_def']]
        for i in range (len(clock_monitoring_def_opt)):
            k+=1
            if i==val:
                self.point_position((init_x+change_x,init_y+change_y), 1)
            change_y+=30
            if k==2:
                k=0
                change_x+=149
                change_y=0
            
    def fexio_clock_nty(self,init_x,init_y,dict1): #459,453
                # 'value': {'clkmon_def': 'fd_fine:1',
                #           'clkmon_not': {'clock_loss': {'1': True, '2': True},
                #                         'fd_coarse': {'1': True, '2': True},
                #                         'fd_fine': {'1': True, '2': True}},
                #           'flexio': {'14': {'enabled': True, 'value': 'Clock Monitoring Defect'},
                #                     '15': {'enabled': True, 'value': 'Clock Monitoring Defect'}},
                #           'pll_not': {'ho_freeze': {'B': True, 'D': True},
                #                       'loss_lock': {'B': True, 'D': True}}}},
     
        change_x=0
        for key in dict1['flexio']['value']['clkmon_not']:
            change_y=0
            for opt in dict1['flexio']['value']['clkmon_not'][key]:
                if not(dict1['flexio']['value']['clkmon_not'][key][opt]):
                    self.point_position((init_x+change_x,init_y+change_y), 1)
                change_y+=30
            change_x+=202
                    
    def pll_nty(self,init_x,init_y,dict1): #520, 590
        change_x=0
        for key in dict1['flexio']['value']['pll_not']:
            change_y=0
            for opt in dict1['flexio']['value']['pll_not'][key]:
                if not(dict1['flexio']['value']['pll_not'][key][opt]):
                    self.point_position((init_x+change_x,init_y+change_y), 1)
                change_y+=30
            change_x+=288

        
    def flexio_ctrl(self,init_x, init_y,dict1,summary=False): #x=424, y=585
        self.point_position((init_x,init_y), 1)
        flexio_init= None
        timeout = time.time() + 20 # 20 seconds
        while flexio_init is None:
            flexio_init=ptg.locateOnScreen(working_dir+"\\"+"images\\flexio_init_"+variant+".PNG",grayscale=True,confidence=.8)
            if flexio_init or time.time() > timeout:
                break
        if flexio_init:
            if dict1['flexio']['value']['flexio']['3']['enabled']:
                self.flexio_select(init_x-27,init_y-463,dict1,'3')
            if dict1['flexio']['value']['flexio']['14']['enabled']:
                self.flexio_select(init_x+285,init_y-463,dict1,'14')
            if dict1['flexio']['value']['flexio']['8']['enabled']:
                self.flexio_select(init_x-27,init_y-374,dict1,'8')
            if dict1['flexio']['value']['flexio']['13']['enabled']:
                self.flexio_select(init_x-27,init_y-283,dict1,'13')
            if dict1['flexio']['value']['flexio']['15']['enabled']:
                self.flexio_select(init_x+285,init_y-374,dict1,'15')
            self.fexio_clock_mon(init_x+3,init_y-167,dict1) #425,327
            self.fexio_clock_nty(init_x+30,init_y-43,dict1) #459,453
            self.pll_nty(init_x+89,init_y+95,dict1) #520, 590
            ptg.press('esc')
            if summary:
                flexio_summary= None
                timeout = time.time() + 20 # 20 seconds
                while flexio_summary is None:
                    flexio_summary=ptg.locateOnScreen(working_dir+"\\"+"images\\flexio_summary_"+variant+".PNG",grayscale=True,confidence=.8)
                    if flexio_summary or time.time() > timeout:
                        break
                if flexio_summary:
                    print('flexio test passed')
                else:
                    print('flexio test failed')
                    print('flexio summary was not correct')            
        else:
            print('flexio test failed')
            print('flexio window did not pop up')
        
            
        
            
    def interrupt_ctrl(self,init_x,init_y,dict1): # x=1005, y=74
            # 'intrb': {'CLOSS_CLKIN1': True,
            #   'CLOSS_CLKIN2': True,
            #   'DRIFT_CLKIN1': True,
            #   'DRIFT_CLKIN2': True,
            #   'PLLB_HO_FREEZE': True,
            #   'PLLB_LOL': True,
            #   'PLLD_HO_FREEZE': True,
            #   'PLLD_LOL': True},
        self.point_position((init_x,init_y), 1)
        interrupt_edit_all= None
        timeout = time.time() + 20 # 20 seconds
        while interrupt_edit_all is None:
            interrupt_edit_all=ptg.locateOnScreen(working_dir+"\\"+"images\\interrupt_edit_all_"+variant+".PNG",grayscale=True,confidence=.8)
            if interrupt_edit_all or time.time() > timeout:
                break
        if interrupt_edit_all:
            change_x=0
            change_y=0
            num_col=0
            for key in dict1['intrb']:
                num_col+=1
                if not dict1['intrb'][key]:
                    self.point_position((init_x+change_x-414,init_y+change_y+303), 1)
                change_x+=124
                if num_col==2:
                    num_col=0
                    change_x=0
                    change_y+=30
            ptg.press('esc')
        else:
            print('Interrupt edit test failed')
            print('Interrupt edit window did not pop up')

            
    def diff_input(self,init_x,init_y,dict1,dict2): # x=93, y=202
        change_x=0
        for key,value in dict1['inputs_diff'].items():
            ##########################################################
            keys=f"['inputs_diff']['{key}']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                if dict2!={}:
                    if dict2['inputs_diff'][key]!=dict1['inputs_diff'][key]:
                        self.point_position((init_x+change_x,init_y), 1)
                else:                        
                    if value:
                        self.point_position((init_x+change_x,init_y), 1)    
            change_x += 118
        
    def acg(self,init_x,init_y,dict1,dict2): #x=1368, y=65
# test = {'acg': {'enabled': False,
#          'value': {'clock_mode': {'parsed': None, 'valid': True, 'value': ''}}},
        acg_clockmode={'00':0,'01':1,'10':2,'11':3}

        keys=f"['acg']['enabled']"
        if_change=self.state_compare(dict2,dict1,keys)
        if if_change:
            if dict2!={}:
                self.point_position((init_x,init_y), 1)  
            else:
                if not(dict1['acg']['enabled']):
                    self.point_position((init_x,init_y), 1)  
                
        if dict1['acg']['enabled']:            
            keys=f"['acg']['value']['clock_mode']['value']"
            if_change=self.state_compare(dict2,dict1,keys)
            if if_change:
                drop_val=self.change_drop_afterbase(dict2,dict1,keys,acg_clockmode)
                self.chng_drop_values(init_x+130,init_y+64,drop_val)
            
            
    def run_config(self,new_state,old_state,filename,what2run=
                   {'order_in':False,'real_time':False,'comms':False,'inputs':False,'outputs':False,  
                'plls':False,'crystal':False,'acg':False,'gpio':False,'eeprom':False,'inputtdc':False,
                'inputs_diff':False,'interrupt':False,'phase_sync':False},save_json=True,save_nvm=True,birds_eye=False,res_chip=False):       
        
        op_path=working_dir+"\\"+"output"+"\\"+variant
        json_path=working_dir+"\\"+"output"+"\\"+"json"
        nvm_path=working_dir+"\\"+"output"+"\\"+"nvm"
        uvm_path=working_dir+"\\"+"output"+"\\"+"uvm"
        print('GUI test running for %s'%(filename))
        time.sleep(3)
        if what2run['comms']:
            self.chip_communication(155,64,new_state,old_state)  #x=155, y=64
        if what2run['inputs_diff']:
            self.diff_input(93,202,new_state,old_state) # x=93, y=202
        if what2run['inputs']:
            self.change_ip_config(32, 249,new_state,old_state) # x=32, y=229
        if what2run['outputs']:
            self.change_op_config(1319, 170,new_state,old_state) #x=1319, y=170
        if what2run['plls']:
            self.change_pll_config(644, 168,new_state,old_state,ip_order=False) #644, 168
        if what2run['crystal']:
            self.xtal_ctrl(772, 112,new_state,old_state) #x=772, y=112
        if what2run['acg']:
            self.acg(1368, 65,new_state,old_state) #x=1368, y=65
        
        if what2run['interrupt']:  #x=580, y=974
            self.interrupt(580,974,new_state,old_state)
        if what2run['phase_sync']:  #x=1236, y=48
            self.phase_sync(1236,48,new_state,old_state)
        if what2run['eeprom']:
            self.eeprom_config(1766,133,new_state,old_state) #x=1766,y=133
        if what2run['inputtdc']:
            self.inputtdc(1855,135,new_state,old_state) #x=1855, y=135
        if what2run['gpio']:
            self.gpio_config(413,974,new_state,old_state) #x=413, y=974
            

        self.dummy_send2chip(1872,64,filename) #x=1872, y=64
        time.sleep(5)
        if save_json:
            self.dump_ctrl(1328, 1013,json_path,filename,dump_as='json') #x=1328, y=1013
        if save_nvm:
            self.dump_ctrl(1328, 1013,nvm_path,filename,dump_as='nvm')
        # if save_uvm:
        #     self.dump_ctrl(1328, 998,uvm_path,filename,dump_as='uvm')
        # if birds_eye:
        #     self.birds_eye_ctrl(427,721)
        # if real_time:
        #     self.realtime_ctrl(106,721) #x=106, y=721
        # if load_nvm_test:
        #     if board_connected:
        #         self.load_nvm(640,722,op_path,nvm_filename) #640, y=722 #F:\Automate_GUI\output_files filename = profile17_nvm.nvm
        # if verify_efuse_test:
        #     if board_connected:
        #         self.verify_efuse(1232,111,op_path,nvm_filename) #x=1232, y=111
        # if res_chip:
        #     self.reset_chip(1776,62) #x=1776, y=62
                    
                                        
                
if __name__ == "__main__":
    RUN_GUI()

