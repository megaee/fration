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
# import inputs_55 as ip55
import os
import re
# import opencv_python
ptg.PAUSE = 0.5
import time
import datetime

print(ptg.position()) # To get the Position of mouse(x,y)


global inputs_covered
global outputs_covered
global plls_covered

import diff_state_json as diffjson
import diff_nvm as diffnvm


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
        # # insert at 1, 0 is the script path (or '' in REPL)
        sys.path.insert(1, working_dir+'//'+'input')
        
        # import Profile1 as ip55
        # self.reset_dropdown(222,780,255,255) #x=192, y=779
            

        if variant == 'au5518':
            path=working_dir+'\\'+'output_pre'+'\\'+'json'
            input_files = get_only_files(path, include_str='') # Get all file names
            input_files.sort(key=natural_keys) # soting file names since I want all files to be executed in order
            inputs_covered=[]
            outputs_covered=[]
            plls_covered=[]
            
            for file in input_files:
                # TODO: Use logger
                print(file)
                # sys.path.append('input')
                a=file.replace('.json','')
                # run_config with what2run and current_state                 
                self.run_config(a,save_json=True,save_nvm=True)
                
               ######### get difference ##########
                diffjson.json_load(file)
                diffnvm.get_diffs(file)

        # print("--- %s seconds ---" % (time.time() - start_time))
        print("--- %s seconds ---" % (str(datetime.timedelta(seconds=(time.time() - start_time)))))        
        print(ptg.position())
        self._changeframe()
        sys.exit()

    def _changeframe(self):
        ptg.hotkey('alt', 'tab')
        
    def _minframe(self):
        ptg.hotkey('win', 'down')

    def _maxframe(self):
        ptg.hotkey('win', 'up')            
            
    def point_position(pself, position, clicks):
        ptg.moveTo(position)
        ptg.click(clicks=clicks)
        
    
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
        ptg.hotkey('Ctrl', 's')
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
        time.sleep(2)
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

    def reset_drop(self,init_x,init_y,existing,go_to=0):
        drop_val= go_to-existing
        self.chng_drop_values(init_x,init_y,drop_val)
            
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
        # self.point_position((init_x,init_y), 1)
        ptg.hotkey('alt', 's')
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
            # ptg.typewrite(path+'\\'+filename+'_'+dump_as)
            ptg.typewrite(path+'\\'+filename)
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
    
                
    def load_json(self,init_x,init_y,path,filename,dump_as=''):#Point(x=1850, y=1010)
        # self.point_position((init_x,init_y), 1)
        ptg.hotkey('alt', 'l')
    # def dump_ctrl(self,init_x, init_y,path,filename,dump_as='nvm'): #x=1328, y=1013
        save_user_profile= None
        timeout = time.time() + 20 # 20 seconds
        while save_user_profile is None:
            save_user_profile=ptg.locateOnScreen(working_dir+"\\"+"images\\Lode_user_profile.PNG",grayscale=True,confidence=.5)
            if save_user_profile or time.time() > timeout:
                break
        # time.sleep(2) # wait for window to respond
        if save_user_profile:
            # type name and save file
            # self.chng_drop_values(init_x-823,init_y-514,drop_val)
            # self.point_position((init_x-823,init_y-540), 3)
            print((path+'\\'+filename+dump_as))
            ptg.typewrite(path+'\\json\\'+filename+dump_as)
            ptg.press('enter')
            # ptg.press('enter')
            
            # ptg.moveTo(init_x-508,init_y)
            
            # # self.point_position((init_x-508,init_y), 1)
            
            # # self.point_position((init_x-508,init_y), 1)
            
            # replace = None
            # timeout = time.time() + 10 # 5 seconds
            # print("WWWWW")
            # while replace is None:
            #     print("HHHHH")
            #     replace=ptg.locateOnScreen(working_dir+"\\"+"images\\save_butn.PNG",grayscale=True,confidence=.5)
            #     if replace or time.time() > timeout:
            #         break
            # if replace:
            print('%s dump successful'%dump_as)
            # else:
            #     print('%s dump successful'%dump_as)
        else:
            print('%s dump failed'%dump_as)
            print('%s save window did not pop up'%dump_as)
    
            
            
    def run_config(self,filename,save_json=True,save_nvm=True,birds_eye=False,res_chip=False):       
        
        op_path=working_dir+"\\"+"output"+"\\"+variant
        json_path=working_dir+"\\"+"output"+"\\"+"json"
        nvm_path=working_dir+"\\"+"output"+"\\"+"nvm"
        uvm_path=working_dir+"\\"+"output"+"\\"+"uvm"
        input_json_path=working_dir+"\\"+"output_pre"
        print('GUI test running for %s'%(filename))
        
        
        # self.load_json(1775,1015,input_json_path,filename,dump_as='.json')#Point(x=1850, y=1010)
        # time.sleep(45)   
        self.dummy_send2chip(1872,64,filename) #x=1872, y=64 for Wizard mord#x=1746, y=74
        time.sleep(10)
        if save_json:
            self.dump_ctrl(1328, 1013,json_path,filename,dump_as='json') #x=1328, y=1013
        if save_nvm:
            self.dump_ctrl(1328, 1013,nvm_path,filename,dump_as='nvm')
        
                    
                                        
                
if __name__ == "__main__":
    RUN_GUI()
