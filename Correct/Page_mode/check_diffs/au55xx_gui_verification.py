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
import inputs_55 as ip55
import os
import re
# import opencv_python
ptg.PAUSE = 0.5
import time

print(ptg.position()) # To get the Position of mouse(x,y)

fin0_freq = "8Mhz"
i2c_add = "0x69"
fb = '4k'
nb = '100'
fout_freq = "160M"
num_ip = 4
num_op = 1
pll_names=['A','B','C','D','FT']
pll_names4out=['A','B','C','D']
clock_type_dict={'Differential':0,'Single Ended AC':1,'Single Ended DC':2}
vddo={'1.8V':0,'2.5V':1,'3.3V':2}
op_mode={'LVDS':0,'LVDS2':1,'LVPECL':2,'CML':3,'HCSL':4,'LVPECL2':5}
ip_clock_selection={'Auto':0,'Manual':1}
lockl_delay = {'1ms':0,'4ms':-1,'16ms':-2,'65ms':-3,'262ms':-4,'1s':-5,'4s':-6,'16s':-7}
# lockl_delay = {'1.02ms':0,'4.10ms':-1,'16.38ms':-2,'65.53ms':-3,'262.14ms':-4,'1.05s':-5,'4.19s':-6,'16.77s':-7}
ho_delay = {'547ms':0,'2.188s':-1,'8.75s':-2,'35s':-3,'137ms':1,'34ms':2,'9ms':3,'2ms':4}
ho_average = {'1.094s':0,'4.375s':-1,'17.5s':-2,'70s':-3,'273ms':1,'68ms':2,'17ms':3,'4ms':4}
ppm_set={'4ppm':0,'2ppm':-1,'0.4ppm':-2,'0.2ppm':-3,'1ppb':-4,'0.5ppb':-5,'0.1ppb':-6,'0.05ppb':-7,'20ppm':1,'40ppm':2,'200ppm':3,'400ppm':4,'2000ppm':5,'4000ppm':6}
ppm_clear={'4ppm':1,'2ppm':0,'0.4ppm':-1,'0.2ppm':-2,'1ppb':-3,'0.5ppb':-4,'0.1ppb':-5,'0.05ppb':-6,'20ppm':2,'40ppm':3,'200ppm':4,'400ppm':5,'2000ppm':6,'4000ppm':7}
# ppm_clear={'2':0,'0.4':-1,'0.2':-2,'200':1}
phase_prop_slope={'Bandwidth':0,'128us/s':1,'32us/s':2,'8us/s':3,'4us/s':4,'2us/s':5,'0.5us/s':6,'0.25us/s':7,'0.125us/s':8,'62.5ns/s':9,'31.25ns/s':10,'15.62ns/s':11,'7.8ns/s':12,'4ns/s':13,'2ns/s':14,'1ns/s':15}
freq_ramp_slope={'0.2 ppm/s':0,'2 ppm/s':1,'20 ppm/s':2,'40000 ppm/s':3}
xtal_mode={'LFF':0,'EX TCXO (AC)':-1,'OT3':-2,'HFF':-3,'EX TCXO (DC)':1}
dump_as_dict={'json':0,'nvm':1,'efuse':2}
trigger_edge={'5':0,'4':-1,'3':-2,'2':-3,'1':-4,'6':1,'7':2,'8':3,'9':4,'10':5,'11':6,'12':7,'13':8,'14':9,'15':10,'16':11}
Clear_edge={'4':0,'3':-1,'2':-2,'1':-3,'5':-4,'6':1,'7':2,'8':3,'9':4,'10':5,'11':6,'12':7,'13':8,'14':9,'15':10,'16':11}
val_time={'2ms':0,'128ms':1,'256ms':2,'1s':3,'4s':4,'32s':5,'64s':6,'128s':7}

flexio_defect_notify={'None':0,'Clock Monitoring Defect':1,'All Notify':2,'Clock Monitoring Notify':3,'PLL Notify':4,'Interrupt':5}
clock_monitoring_def_opt={'fd_fine:1':0,'fd_fine:2':1,'coarse_fd_status:1':2,'coarse_fd_status:2':3,'clock_loss_status:1':4,'clock_loss_status:2':5,'clock_loss_fd_status:1':6,'clock_loss_fd_status:2':7}


variant ='au5518'
board_connected=False

working_dir=os.getcwd()

class RUN_GUI:
    def __init__(self):
        start_time = time.time()
        self._changeframe()
        time.sleep(2)

        if variant == 'au5518':        
            # self.run_config(ip29.profile1,"profile1")
            # self.run_config(ip29.profile2,"profile2")
            # self.run_config(ip29.profile3,"profile3")
            # self.run_config(ip29.profile4,"profile4")
            # self.run_config(ip29.profile5,"profile5")
            # self.run_config(ip29.profile6,"profile6")
            # self.run_config(ip29.profile7,"profile7")
            # self.run_config(ip29.profile8,"profile8")
            # self.run_config(ip29.profile9,"profile9")
            # self.run_config(ip29.profile10,"profile10")
            # self.run_config(ip29.profile11,"profile11")
            # self.run_config(ip29.profile12,"profile12")
            # self.run_config(ip29.profile13,"profile13")
            # self.run_config(ip29.profile14,"profile14")
            # self.run_config(ip29.profile15,"profile15")
            # self.run_config(ip29.profile16,"profile16")
            # self.run_config(ip29.profile17,"profile17")
            # self.run_config(ip29.profile18,"profile18")
            # self.run_config(ip29.profile19,"profile19")
            # self.run_config(ip29.profile20,"profile20")
            # self.run_config(ip29.profile21,"profile21")
            # self.run_config(ip29.profile22,"profile22")
            # self.run_config(ip29.profile23,"profile23")
            # self.run_config(ip29.profile24,"profile24")
            # self.run_config(ip29.profile25,"profile25")
            # self.run_config(ip29.profile26,"profile26")
            # self.run_config(ip29.profile27,"profile27")
            # self.run_config(ip29.profile28,"profile28")
            # self.run_config(ip29.profile29,"profile29")
            # self.run_config(ip29.profile30,"profile30")
            # self.run_config(ip29.profile31,"profile31")
            # self.run_config(ip29.profile32,"profile32")
            # self.run_config(ip29.profile33,"profile33")
            # self.run_config(ip29.profile34,"profile34")
            # self.run_config(ip29.profile35,"profile35")
            # self.run_config(ip29.profile36,"profile36")
            # self.run_config(ip29.profile37,"profile37")
            # self.run_config(ip29.profile38,"profile38")
            # self.run_config(ip29.profile39,"profile39")
            # self.run_config(ip29.profile40,"profile40")
            # self.run_config(ip29.profile41,"profile41")
            # self.run_config(ip29.profile42,"profile42")
            # self.run_config(ip29.profile43,"profile43")
            # self.run_config(ip29.profile44,"profile44")
            # self.run_config(ip29.profile45,"profile45")
            # self.run_config(ip29.profile46,"profile46")
            # self.run_config(ip29.profile47,"profile47")
            # self.run_config(ip29.profile48,"profile48")
            # self.run_config(ip29.profile49,"profile49")
            # self.run_config(ip29.profile50,"profile50")
            # self.run_config(ip29.profile51,"profile51")
            # self.run_config(ip29.profile52,"profile52")
            # self.run_config(ip29.profile53,"profile53")
            # self.run_config(ip29.profile54,"profile54")
            # self.run_config(ip29.profile55,"profile55")
            # self.run_config(ip29.profile56,"profile56",ip_order=True)
            # self.run_config(ip29.profile57,"profile57")
            # self.run_config(ip29.profile58,"profile58")
            # self.run_config(ip29.profile59,"profile59")
            # self.run_config(ip29.profile60,"profile60")
            # self.run_config(ip29.profile61,"profile61")
            # self.run_config(ip29.profile62,"profile62",chng_interrupt=True)
            # self.run_config(ip29.profile63,"profile63",chng_interrupt=False,chng_flexio=True)
            # self.run_config(ip29.profile64,"profile64",chng_interrupt=False,chng_flexio=True)
            # self.run_config(ip29.profile65,"profile65",chng_interrupt=False,chng_flexio=True)
            # self.run_config(ip29.profile66,"profile66",chng_interrupt=False,chng_flexio=True)
            # self.run_config(ip29.profile67,"profile67",chng_interrupt=False,chng_flexio=True)
            # self.run_config(ip29.profile68,"profile68",chng_interrupt=False,chng_flexio=True)
            # self.run_config(ip29.profile69,"profile69",chng_interrupt=False,chng_flexio=True)
            # self.run_config(ip29.profile70,"profile70",chng_interrupt=False,chng_flexio=True)
            # self.run_config(ip29.profile71,"profile71",chng_interrupt=False,chng_flexio=True,birds_eye=True,real_time=True,res_chip=False, load_nvm_test=True, verify_efuse_test=True,nvm_filename='profile71_nvm.nvm')
            # self.run_config(ip29.profile71,"profile71",chng_interrupt=False,chng_flexio=False,birds_eye=False,real_time=False,res_chip=False, load_nvm_test=True, verify_efuse_test=True,nvm_filename='profile71_nvm.nvm')

            # self.birds_eye_ctrl(427,721)
            # self.realtime_ctrl(106,721) #x=106, y=721
            # self.load_nvm(640,722,op_path,nvm_filename) #640, y=722 #F:\Automate_GUI\output_files filename = profile17_nvm.nvm
            # self.verify_efuse(1232,111,op_path,nvm_filename) #x=1232, y=111
            

            self.change_ip_config(32, 229,ip55.profile1) # x=32, y=229
            self.change_op_config(1319, 154,ip55.profile1) #x=1319, y=154
            self.change_pll_config(644, 152,ip55.profile1) #644, 152

        print("--- %s seconds ---" % (time.time() - start_time))        
        print(ptg.position())
        exit()

    def _changeframe(self):
        ptg.hotkey('alt', 'tab')


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
        

            
    def save_op(self,path,filename,init_x,init_y): #x=1212,80
        # path=r'C:\Users\Dell\Desktop\gui_test'
        
        self.point_position((init_x,init_y), 1)
        # time.sleep(10)

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
                ptg.press('enter')
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
            ptg.moveTo(init_x-673,init_y+645)
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

    def reset_chip(self,init_x,init_y): ##1125,83
        self.point_position((init_x,init_y), 1)
        if board_connected:
            ptg.moveTo(init_x-593,init_y+643)
            reset_chip=None
            timeout = time.time() + 30 # 20 seconds
            while reset_chip is None:
                reset_chip=ptg.locateOnScreen(working_dir+"\\"+"images\\load_enabled.PNG",grayscale=True,confidence=.8)
            if reset_chip or time.time() > timeout:
                pass
                time.sleep(5)
        else:
            chip_not_connected=None
            timeout = time.time() + 30 # 20 seconds
            while chip_not_connected is None:
                chip_not_connected=ptg.locateOnScreen(working_dir+"\\"+"images\\chip_not_connected.PNG",grayscale=True,confidence=.5)
            if chip_not_connected or time.time() > timeout:
                ptg.press('enter')
                time.sleep(5)
        
            
    def drop_down_ctrl(self,init_x,init_y,item_num):
        self.point_position((init_x,init_y), 1)
        [ptg.press('down') for x in range (item_num)]
        ptg.press('enter')
        
    def chng_drop_values(self,init_x,init_y,val):
        self.point_position((init_x,init_y), 1)
        if val <0:
            [ptg.press('up') for x in range (abs(val))]
            ptg.press('enter')
        if val >0:
            [ptg.press('down') for x in range (val)]
            ptg.press('enter')
        if val == 0:
            ptg.press('enter')
            
            
    def scroll_values(self, init_x, init_y, val ,start_val):
        self.point_position((init_x,init_y), 1) # set value
        val_press = (val-start_val)/1000 #val_press=0.008
        if val_press<0:
            a=str(val_press).split('.') #['0', '008']
            num_press = int(a[1]) #8
            [ptg.press('up') for x in range (num_press)]
            # ptg.press('up')*num_press
            ptg.press('enter')
        # set value
        if val_press>0:
            [ptg.press('down') for x in range (int(val_press))]
            # ptg.press('down')*val_press
            ptg.press('enter')
        if val_press==0:
            ptg.press('enter')
                           
            
    def change_ip_config(self, init_x, init_y,dict1): # x=32, y=229
        '''
        Function to change input page configuration
        Settings are given by the user in the form of dictionary
        This is same as gui state
        '''
    # 'inputs': {'0P': {'enabled': False,
    #                   'value': {'clock_couple': 'dc',
    #                             'clock_gap': False,
    #                             'clock_inversion': False,
    #                             'clock_loss': {'enabled': True,
    #                                            'value': {'edge_clr': '4',
    #                                                      'edge_trig': '5',
    #                                                      'time_val': {'parsed': Fraction(1, 500),
    #                                                                   'valid': True,
    #                                                                   'value': '2ms'}},
    #                                            'warn': True},
    #                             'clock_switch': {'clock_loss': True,
    #                                              'fd_coarse': False,
    #                                              'fd_fine': False},
    #                             'drift_coarse': {'enabled': False,
    #                                              'value': {'clr': '800',
    #                                                        'set': '1000'},
    #                                              'warn': True},
    #                             'drift_fine': {'enabled': False,
    #                                            'value': {'clr': '8', 'set': '10'},
    #                                            'warn': True},
    #                             'freq': {'parsed': None,
    #                                      'valid': True,
    #                                      'value': ''},
    #                             'plls': {'A': False,
    #                                      'B': False,
    #                                      'C': False,
    #                                      'D': False,
    #                                      'FT': False}}},
        self.point_position((init_x,init_y), 1)
        num_tabs=0
        for key in dict1['inputs']:
            if dict1['inputs'][key]['enabled']:
                for i in range(num_tabs):
                    ptg.hotkey('ctrl','tab') # This is needed to go to the correct widget
                time.sleep(1)
                # enable input
                self.point_position((init_x+44,init_y+26), 1)
                #golden clock
                if dict1['golden_clock']==key:
                    self.point_position((init_x+123,init_y+61), 1)
                #enter freq
                self.point_position((init_x+414,init_y+81), 3) # Triple Click to select the text and replace it
                ptg.typewrite(dict1['inputs'][key]['value']['freq']['value'])
                # Coupling
                if dict1['inputs'][key]['value']['clock_couple']=='ac':
                    self.point_position((init_x+150,init_y+144), 1)
                else:
                    self.point_position((init_x+437,init_y+144), 1)
                # Clock inversion
                if dict1['inputs'][key]['value']['clock_inversion']:
                    self.point_position((init_x+135,init_y+191), 1)                 
                #Clock Gap
                if dict1['inputs'][key]['value']['clock_gap']:
                    self.point_position((init_x+423,init_y+191), 1)
                #Clock Loss
                drop_val=trigger_edge[dict1['inputs'][key]['value']['clock_loss']['value']['edge_trig']]
                self.chng_drop_values(init_x+92,init_y+283,drop_val)
                drop_val=Clear_edge[dict1['inputs'][key]['value']['clock_loss']['value']['edge_clr']]
                self.chng_drop_values(init_x+284,init_y+283,drop_val)
                drop_val=val_time[dict1['inputs'][key]['value']['clock_loss']['value']['time_val']['value']]
                self.chng_drop_values(init_x+474,init_y+283,drop_val)
                
                # Clock Switch
                if not(dict1['inputs'][key]['value']['clock_switch']['clock_loss']): # enabled by default
                    self.point_position((init_x+81,init_y+463), 1)                 
                if dict1['inputs'][key]['value']['clock_switch']['fd_coarse']:
                    self.point_position((init_x+267,init_y+463), 1)                 
                if dict1['inputs'][key]['value']['clock_switch']['fd_fine']:
                    self.point_position((init_x+468,init_y+463), 1)                 
                     
                # coarse drift
                if dict1['inputs'][key]['value']['drift_coarse']:
                    self.point_position((init_x+57,init_y+433), 1)
                    self.scroll_values(init_x+163,init_y+464, int(dict1['inputs'][key]['value']['drift_coarse']['value']['set']) ,1000)# set value
                    self.scroll_values(init_x+457,init_y+464, int(dict1['inputs'][key]['value']['drift_coarse']['value']['clr']) ,800)# clr value
                    
                # Fine drift
                if dict1['inputs'][key]['value']['drift_fine']:
                    self.point_position((init_x+57,init_y+508), 1) # check box
                    self.scroll_values(init_x+163,init_y+538, int(dict1['inputs'][key]['value']['drift_fine']['value']['set']) ,10)# set value
                    self.scroll_values(init_x+457,init_y+538, int(dict1['inputs'][key]['value']['drift_fine']['value']['clr']) ,8)# clr value

                change_x=0
                for i in range (len(pll_names)):
                    if dict1['inputs'][key]['value']['plls'][pll_names[i]]:
                        self.point_position((init_x+52+change_x,init_y+634), 1) # check box
                    change_x+=114
            num_tabs+=1
                    
        
    def change_op_config(self, init_x, init_y,dict1): #x=1319, y=154
        '''
        Function to change output page configuration
        Settings are given by the user in the form of dictionary
        This is same as gui state
        # '''
        
    # 'outputs': {'valid': True,
    #             'value': {'0': {'enabled': False,
    #                             'valid': True,
    #                             'value': {'delay': {'parsed': None,
    #                                                 'valid': True,
    #                                                 'value': ''},
    #                                       'freq': {'parsed': None,
    #                                                'valid': True,
    #                                                'value': ''},
    #                                       'm_de': {'state': '',
    #                                                'value': {'it': False,
    #                                                          'submode': '',
    #                                                          'swing': {'parsed': None,
    #                                                                    'valid': True,
    #                                                                    'value': ''}}},
    #                                       'm_se': {'state': '',
    #                                                'value': {'on': {'enabled': False,
    #                                                                 'value': ''},
    #                                                          'op': {'enabled': False,
    #                                                                 'value': ''}}},
    #                                       'phfl': False,
    #                                       'pll': {'enabled': False, 'value': ''},
    #                                       'syncb': False,
    #                                       'sys_ref': {'enabled': False,
    #                                                   'value': {'continuous': '',
    #                                                             'pulsar': {'state': '',
    #                                                                        'value': {'count': {'parsed': None,
    #                                                                                            'valid': True,
    #                                                                                            'value': ''}}}}},
    #                                       'vddo': ''}},

        self.point_position((init_x,init_y), 1)
        num_tabs=0
        for key in dict1['outputs']['value']:
            if dict1['outputs']['value'][key]['enabled']:
                for i in range(num_tabs):
                    ptg.hotkey('ctrl','tab') # This is needed to go to the correct widget
                time.sleep(1)
                # enable output
                self.point_position((init_x+42,init_y+23), 1)
                #enter freq
                self.point_position((init_x+138,init_y+100), 3) # Triple Click to select the text and replace it
                ptg.typewrite(dict1['outputs']['value'][key]['value']['freq']['value'])
                # VDD
                num_down=vddo[dict1['outputs']['value'][key]['value']['vddo']]
                self.drop_down_ctrl(init_x+429,init_y+100,num_down)

                # PLL configuration
                change_x_pll=0
                for i in range (len(pll_names4out)):
                    if dict1['outputs']['value'][key]['value']['pll']['value']==pll_names4out[i]:
                        self.point_position((init_x+62+change_x_pll,init_y+228), 1) # radio button
                    change_x_pll+=143
                    
                # Sys ref
                if dict1['outputs']['value'][key]['value']['sys_ref']['enabled']:
                    self.point_position((init_x+46,init_y+291), 1)
                    if dict1['outputs']['value'][key]['value']['sys_ref']['value']['pulsar']['state']=='pulsar':
                        self.point_position((init_x+299,init_y+319), 1)
                        self.point_position((init_x+438,init_y+373), 3) # Triple Click to select the text and replace it
                        ptg.typewrite(dict1['outputs']['value'][key]['value']['freq']['value'])                                          

                #delay
                if dict1['outputs']['value'][key]['value']['delay']['value']:
                    self.point_position((init_x+102,init_y+476), 3)
                    ptg.typewrite(dict1['outputs']['value'][key]['value']['delay']['value'])
                #Sync B
                if dict1['outputs']['value'][key]['value']['syncb']:
                    self.point_position((init_x+296,init_y+476), 1)
                #Phase hopping
                if dict1['outputs']['value'][key]['value']['phfl']:
                    self.point_position((init_x+471,init_y+476), 1)
                # Single Ended
                if dict1['outputs']['value'][key]['value']['m_se']['state']=='se':
                    self.point_position((init_x+58,init_y+563), 1) # single ended radio button
                    if dict1['outputs']['value'][key]['value']['m_se']['value']['on']['enabled']:
                        self.point_position((init_x+44,init_y+588), 1) # ON
                        type1 = dict1['outputs']['value'][key]['value']['m_se']['value']['on']['value']
                        if type1=='clkp':
                            self.point_position((init_x+69,init_y+628), 1)
                        if type1=='clkn':
                            self.point_position((init_x+211,init_y+628), 1)
                    if dict1['outputs']['value'][key]['value']['m_se']['value']['op']['enabled']:
                        self.point_position((init_x+44,init_y+698), 1) # OP
                        type1 = dict1['outputs']['value'][key]['value']['m_se']['value']['op']['value']
                        if type1=='clkp':
                            self.point_position((init_x+69,init_y+739), 1)
                        if type1=='clkn':
                            self.point_position((init_x+211,init_y+739), 1)
                            
            #     # Differential
                
                if dict1['outputs']['value'][key]['value']['m_de']['state']=='de':
                    self.point_position((init_x+365,init_y+563), 1)
                    num_down=op_mode[dict1['outputs']['value'][key]['value']['m_de']['value']['submode']]
                    self.drop_down_ctrl(init_x+432,init_y+623,num_down)
            num_tabs+=1
                
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
                
    def change_pll_config(self, init_x, init_y,dict1,ip_order=False): #644, 152
        '''
        Function to change pll page configuration
        Settings are given by the user in the form of dictionary
        This is same as gui state
        '''                
        active_plls=[]
        # for pll in pll_names:
        for key in dict1['outputs']['value']:
            pll=dict1['outputs']['value'][key]['value']['pll']['value']
            if pll!='' and pll not in active_plls:
                active_plls.append(pll)
                        
    # 'plls': {'A': {'enabled': False,
    #                'value': {'clock_switch': {'frequency_ramp': {'enabled': False,
    #                                                              'value': {'slope': {'parsed': None,
    #                                                                                  'valid': True,
    #                                                                                  'value': ''}}},
    #                                           'hitless': {'ph_bout': '',
    #                                                       'ph_prop': {'state': '',
    #                                                                   'value': {'slope': {'parsed': None,
    #                                                                                       'valid': True,
    #                                                                                       'value': ''}}}},
    #                                           'in3_sync': False},
    #                          'free_running': {'enabled': False,
    #                                           'value': {'dco': True,
    #                                                     'fast_lock_ho': False,
    #                                                     'holdover': {'average': '1.094s',
    #                                                                  'delay': '547ms'},
    #                                                     'ip_clock': {'revertive': True,
    #                                                                  'select': 'Auto'},
    #                                                     'll': {'lock_loss': {'enabled': False,
    #                                                                          'value': {'delay': {'parsed': Fraction(1, 1000),
    #                                                                                              'valid': True,
    #                                                                                              'value': '1 '
    #                                                                                                       'ms'},
    #                                                                                    'ppm': {'valid': True,
    #                                                                                            'value': {'clr': {'parsed': Fraction(1, 500000),
    #                                                                                                              'value': '2 '
    #                                                                                                                       'ppm'},
    #                                                                                                      'set': {'parsed': Fraction(1, 250000),
    #                                                                                                              'value': '4 '
    #                                                                                                                       'ppm'}}},
    #                                                                                    'timer': True}},
    #                                                            'phase_lock_loss': {'enabled': True,
    #                                                                                'value': {'delay': {'parsed': Fraction(1, 250),
    #                                                                                                    'valid': True,
    #                                                                                                    'value': '4 '
    #                                                                                                             'ms'},
    #                                                                                          'phase_threshold': {'parsed': None,
    #                                                                                                              'valid': True,
    #                                                                                                              'value': ''},
    #                                                                                          'timer': True}}}}},
    #                          'fuse_lock': {'enabled': False,
    #                                        'value': {'fvco': {'parsed': None,
    #                                                           'valid': True,
    #                                                           'value': ''}}},
    #                          'lwm': False,
    #                          'mode': {'o:phfl': {'state': '', ---sys_ref,syncb,''
    #                                              'value': {'threshold': {'parsed': None,
    #                                                                      'valid': True,
    #                                                                      'value': ''}}},
    #                                   'value': ''},
    #                          'order_in': [],
    #                          'ptp': {'enabled': False,
    #                                  'value': {'bw': {'parsed': None,
    #                                                   'valid': False,
    #                                                   'value': ''},
    #                                            'ipath': False,
    #                                            'phase_sl': {'parsed': None,
    #                                                         'valid': True,
    #                                                         'value': ''},
    #                                            'phase_ur': {'parsed': None,
    #                                                         'valid': False,
    #                                                         'value': ''},
    #                                            'ppath': False}},
    #                          'smartdco': {'receiver': {'valid': True,
    #                                                    'value': {'rx1': {'enabled': False,
    #                                                                      'value': {'pll': '',
    #                                                                                'tx': 'tx1'}},
    #                                                              'rx2': {'enabled': False,
    #                                                                      'value': {'pll': '',
    #                                                                                'tx': 'tx1'}},
    #                                                              'sl': {'parsed': Fraction(1, 10000000000),
    #                                                                     'valid': True,
    #                                                                     'value': '0.1 '
    #                                                                              'ppb/s'}}},
    #                                       'transmitter': {'tx1': {'enabled': False,
    #                                                               'value': {'ipath': True,
    #                                                                         'ppath': False,
    #                                                                         'rx1': True,
    #                                                                         'rx2': True}},
    #                                                       'tx2': {'enabled': False,
    #                                                               'value': {'ipath': True,
    #                                                                         'ppath': False,
    #                                                                         'rx1': True,
    #                                                                         'rx2': True}}}},
    #                          'sw_ext': {'state': 'oc',
    #                                     'value': {'decimation': {'parsed': None,
    #                                                              'valid': True,
    #                                                              'value': ''}}},
    #                          'sw_oc': {'state': 'oc',
    #                                    'value': {'fast': {'parsed': None,
    #                                                       'value': '',
    #                                                       'warn': True},
    #                                              'normal': {'parsed': None,
    #                                                         'value': '',
    #                                                         'warn': True}}},
    #                          'zdm': {'external': {'input': {'parsed': None,
    #                                                         'valid': True,
    #                                                         'value': ''}},
    #                                  'state': ''}}},
# 
        self.point_position((init_x,init_y), 1)
        num_tabs=0
        for pll in pll_names:
            if pll in active_plls:
                for i in range(num_tabs):
                    ptg.hotkey('ctrl','tab') # This is needed to go to the correct widget
                time.sleep(1)
                ptg.hotkey('alt',pll)
                # Mode selection and configuration
                if dict1['plls'][pll]['value']['mode']['o:phfl']['state']=='':
                    self.point_position((init_x+106,init_y+76), 1)
                if dict1['plls'][pll]['value']['mode']['o:phfl']['state']=='sys_ref':
                    self.point_position((init_x+318,init_y+76), 1)
                if dict1['plls'][pll]['value']['mode']['o:phfl']['state']=='syncb':
                    self.point_position((init_x+536,init_y+76), 1)
                if dict1['plls'][pll]['value']['mode']['o:phfl']['state']=='phfl':
                    self.point_position((init_x+96,init_y+104), 1)
                    self.point_position((init_x+377,init_y+134), 3)
                    ptg.typewrite(dict1['plls'][pll]['value']['mode']['o:phfl']['value']['threshold']['value'])
                    
                # OnChip Filter bandwidth
                if dict1['plls'][pll]['value']['sw_oc']['state']=='oc':
                    self.point_position((init_x+81,init_y+179), 1)
                    self.point_position((init_x+81,init_y+231), 3)
                    #enter freq
                    ptg.typewrite(dict1['plls'][pll]['bw']['fast']['value'])
                    # enter normal bw
                    self.point_position((init_x+270,init_y+231), 3)
                    #enter freq
                    ptg.typewrite(dict1['plls'][pll]['bw']['normal']['value'])
                if dict1['plls'][pll]['value']['sw_ext']['state']=='ext':
                    self.point_position((init_x+448,init_y+179), 1)
                    self.point_position((init_x+509,init_y+231), 3)
                    #enter freq
                    ptg.typewrite(dict1['plls'][pll]['value']['sw_ext']['value']['decimation']['value'])
                    
                # Free running select
                if not(dict1['plls'][pll]['value']['free_running']['enabled']):
                    num_down=ip_clock_selection[dict1['plls'][pll]['value']['free_running']['value']['ip_clock']['select']]
                    self.drop_down_ctrl(init_x+119,init_y+322,num_down)
                    if not(dict1['pll'][pll]['free_running']['value']['ip_clock']['revertive']): # revertive enabled by default
                        self.point_position((init_x+283,init_y+322), 1)

                    ########## Lock loss widget#########
                     
                    if dict1['pll'][pll]['free_running']['value']['ll']['lock_loss']['enabled']:
                        self.point_position((init_x+40,init_y+382), 1)
                        self.point_position((init_x+60,init_y+404), 1)
                        drop_val=lockl_delay[dict1['plls'][pll]['free_running']['value']['ll']['lock_loss']['value']['delay']]                
                        self.chng_drop_values(init_x+60,init_y+457,drop_val)
                        if not(dict1['plls'][pll]['free_running']['value']['ll']['lock_loss']['value']['timer']): # timer enabled by default
                            self.point_position((init_x+158,init_y+457), 1)
                        
                        ########## PPM widget#########
                        # PPM Set Clear
                        drop_val=ppm_set[dict1['plls'][pll]['free_running']['value']['ll']['lock_loss']['value']['ppm']['value']['set']['value']]
                        self.chng_drop_values(init_x+60,init_y+532,drop_val)
                        drop_val=ppm_clear[dict1['plls'][pll]['free_running']['value']['ll']['lock_loss']['value']['ppm']['value']['clr']['value']]
                        self.chng_drop_values(init_x+149,init_y+532,drop_val)
                    if dict1['pll'][pll]['free_running']['value']['ll']['phase_lock_loss']['enabled']:
                        self.point_position((init_x+116,init_y+382), 1)
                        self.point_position((init_x+88,init_y+403), 1)
                        drop_val=dict1['pll'][pll]['free_running']['value']['ll']['phase_lock_loss']['value']['delay']['value']
                        a=re.findall('\d+', drop_val)              
                        self.chng_drop_values(init_x+63,init_y+465,int(a[0]))
                        if not(dict1['pll'][pll]['free_running']['value']['ll']['phase_lock_loss']['value']['timer']):
                            self.point_position((init_x+158,init_y+463), 1)
                            
                        self.point_position((init_x+107,init_y+534), 3)
                        ptg.typewrite(dict1['pll'][pll]['free_running']['value']['ll']['phase_lock_loss']['value']['phase_threshold']['value'])
                                            
                    ########## HoldOver #############
                    drop_val=ho_delay[dict1['plls'][pll]['free_running']['value']['holdover']['delay']]
                    self.chng_drop_values(init_x+292,init_y+410,drop_val)
                    drop_val=ho_average[dict1['plls'][pll]['free_running']['value']['holdover']['average']]
                    self.chng_drop_values(init_x+292,init_y+471,drop_val)
    
                    ########## DCO Mode #############
                    
                    if not(dict1['plls'][pll]['free_running']['value']['dco']): # dco enabled by default
                        self.point_position((init_x+292,init_y+512), 1)
                    ########### Fast Lock HoldOver ###########
                    if dict1['plls'][pll]['free_running']['value']['fast_lock_ho']:
                        self.point_position((init_x+292,init_y+559), 1)
                # else:
                #     if dict1['pll'][pll]['free_running']['enabled']:
                #         self.point_position((init_x-20,init_y+43), 1)
                        

                if dict1['plls'][pll]['clock_switch']['hitless']['ph_bout']=='buildout':
                    self.point_position((init_x+450,init_y+320), 1)
                if dict1['plls'][pll]['clock_switch']['hitless']['ph_prop']['state']=='propagation':
                    self.point_position((init_x+450,init_y+363), 1)
                    drop_val=phase_prop_slope[dict1['plls'][pll]['clock_switch']['hitless']['ph_prop']['value']['slope']['value']]
                    self.chng_drop_values(init_x+507,init_y+420,drop_val)
                
                ############## Frequency Ramp #########
                if dict1['pll'][pll]['clock_switch']['frequency_ramp']['enabled']:
                    self.point_position((init_x+451,init_y+472), 1)
                    drop_val = freq_ramp_slope[dict1['pll'][pll]['clock_switch']['frequency_ramp']['value']['slope']]
                    self.chng_drop_values(init_x+507,init_y+531,drop_val)
                if dict1['pll'][pll]['clock_switch']['in3_sync']:
                    self.point_position((init_x+507,init_y+567), 1)
                    
            if ip_order: #576, 231
                self.point_position((init_x+11,init_y+422), 1)
                self.point_position((init_x+40,init_y+446), 1)
            num_tabs+=1
        
    def chip_communication(self,init_x,init_y,dict1): # x=212, y=70
    #     'comms': {'address': 105, 'type': 'i2c'},
        if dict1['comms']['type']=='i2c':
            self.point_position((init_x,init_y), 1)
            self.point_position((init_x+64,init_y+26), 3)
            ptg.typewrite(str(dict1['comms']['address']))
        if dict1['comms']['type']=='spi':
            self.point_position((init_x-48,init_y+26), 1)
        
    def xtal_ctrl(self, init_x, init_y,dict1): #x=482, y=100

#     'crystal': {'doubler': True,
#                 'freq': {'parsed': None, 'valid': False, 'value': ''},
#                 'mode': 'LFF'},
        if dict1['golden_clock']=='xtal':
            self.point_position((init_x-136,init_y+7), 1)
            
        self.point_position((init_x,init_y), 3)
        ptg.typewrite(dict1['crystal']['freq']['value'])
        # choose mode
        drop_val = xtal_mode[dict1['crystal']['mode']]
        self.chng_drop_values(init_x+206,init_y,drop_val)
        if not(dict1['crystal']['doubler']):
            self.point_position((init_x+368,init_y), 1)

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
        
    def dump_ctrl(self,init_x, init_y,path,filename,dump_as='nvm'): #904, 725
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
            self.chng_drop_values(init_x-412,init_y-240,drop_val)
            self.point_position((init_x-537,init_y-267), 3)
            ptg.typewrite(path+'\\'+filename+'_'+dump_as)
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
                print('nvm dump successful')
            else:
                print('nvm dump successful')
        else:
            print('nvm dump failed')
            print('nvm save window did not pop up')
            

            
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
            
            
            
    def run_config(self,profile,filename,chng_chip_communication=True,chng_ip_config=True,chng_op_config=True,chng_pll_config=True,chng_xtal=True,chng_vddio=False,chng_interrupt=False,chng_flexio=False,save_json=False,save_nvm=True,save_efuse=False,birds_eye=False,real_time=False,res_chip=True, load_nvm_test=False, verify_efuse_test=False,nvm_filename='',ip_order=False):
        op_path=working_dir+"\\"+"output_files"+"\\"+variant
        nvm_path=working_dir+"\\"+"output_files"+"\\"+variant+"_nvm"
        print('GUI test running for %s'%(filename))
        if chng_chip_communication:
            self.chip_communication(212,70,profile)
        if chng_ip_config:
            self.change_ip_config(37, 160,profile)
        if chng_op_config:
            self.change_op_config(954, 162,profile) #912,166
        if chng_pll_config:
            self.change_pll_config(576, 231,profile,ip_order)
        if chng_xtal:
            self.xtal_ctrl(482, 100,profile)
        if chng_vddio:
            self.vddio_ctrl(83, 618,profile)
        if chng_interrupt:
            self.interrupt_ctrl(1004,73,profile)
        if chng_flexio:
            self.flexio_ctrl(420, 587,profile)
        self.save_op(op_path,filename,1212,80)#1212,80
        if save_json:
            self.dump_ctrl(904, 725,op_path,filename,dump_as='json')
        if save_nvm:
            self.dump_ctrl(904, 725,nvm_path,filename,dump_as='nvm')
        if save_efuse:
            self.dump_ctrl(904, 725,op_path,filename,dump_as='efuse')
        if birds_eye:
            self.birds_eye_ctrl(427,721)
        if real_time:
            self.realtime_ctrl(106,721) #x=106, y=721
        if load_nvm_test:
            if board_connected:
                self.load_nvm(640,722,op_path,nvm_filename) #640, y=722 #F:\Automate_GUI\output_files filename = profile17_nvm.nvm
        if verify_efuse_test:
            if board_connected:
                self.verify_efuse(1232,111,op_path,nvm_filename) #x=1232, y=111
        if res_chip:
            self.reset_chip(1125,83) #1125,83 #profile17_nvm.nvm
                    
            # self.change_ip_config(37, 160,ip29.profile1)
            # self.change_op_config(954, 162,ip29.profile1) #954,162
            # self.change_pll_config(576, 231,ip29.profile1) #(576, 231)
            # self.chip_communication(212,70,ip29.profile1) # x=212, y=70
            # self.xtal_ctrl(482, 100,ip29.profile1) #x=482, y=100
            # self.vddio_ctrl(104, 771,ip29.profile1) #x=104, y=771
            # self.interrupt_ctrl(1258,90,ip29.profile1) # x=1258, y=90
            # self.flexio_ctrl(405, 210,ip29.profile70) #405,210
                    
                
if __name__ == "__main__":
    RUN_GUI()

