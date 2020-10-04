# -*- coding: utf-8 -*-
# @Author: Francesca Li

import time, os

from AppKit import NSScreen # please comment out this line if you plan to run this program on Windows
from psychopy import visual, core, event, monitors, gui, data
import pandas as pd

""" Sections of this source file
    ----------------------------
    1. Preference Settings
    2. Classes & Functions
    3. Main
    """

############################################## SETTINGS ##############################################

# EXPERIMENT DESIGN
include_practice = True

# FILEPATH & FILENAME
output_path = './outputs/'
result_log_path = output_path + 'MTT_log.csv' # you can change the file name here
exp_info_log_path = output_path + 'exp_info_log.csv'
instruction_folder = './img/instructions/' # better keep untouched
instr_path = ['{}INSTR_{}.png'.format(instruction_folder,i) for i in range(9)] # better keep untouched

# TIMING / DURATION (seconds)
display_time = 3
blank_time = 0.5
feedback_time = 0.5

# OTHER BLOCK OPTIONS
response_key = {'left':'left_key','right':'right_key'}
continue_key = ['space']
''' Specify total number of trials in each block here; 
    prac => practice; fml => formal'''
num_trial_prac = 3 
num_trial_fml = 32 # should be a multiple of 8 (8 -> number of conditions)

# MONITOR
mon_width = NSScreen.screens()[0].frame().size.width # please set the monitor width & height manually
mon_height = NSScreen.screens()[0].frame().size.height # if you plan to run this program on Windows

######################################### CLASSES & FUNCTIONS ##########################################

class Box:
    """The background box

    Attributes
    ----------
    top_box, bottom_box -> box
    top_label ('Shape'), bottom_label ('Filling') -> label

    Methods
    -------
    auto_draw, stop_draw
    """

    def __init__(self,win):
        self.top_box = visual.Rect(win,width=0.6,height=0.5,pos=(0,0.25),lineColor='yellow',lineWidth=30)
        self.bottom_box = visual.Rect(win,width=0.6,height=0.5,pos=(0,-0.25),lineColor='yellow',lineWidth=30)
        self.top_label = visual.TextStim(win,text='Shape',pos=(0.0, 0.6),color='yellow')
        self.bottom_label = visual.TextStim(win,text='Filling',pos=(0.0, -0.6),color='yellow')

    def auto_draw(self):
        self.top_box.autoDraw = True
        self.bottom_box.autoDraw = True
        self.top_label.autoDraw = True
        self.bottom_label.autoDraw = True

    def stop_draw(self):
        self.top_box.autoDraw = False
        self.bottom_box.autoDraw = False
        self.top_label.autoDraw = False
        self.bottom_label.autoDraw = False


class Drawer:
    """Draw stimulus, background box, etc.

    Attributes
    ----------
    feedback -> feedback messsage
    box, diamond, square, dots_2, dots_3 -> drawable
    shapes, fillings -> drawable collections
    shape, filling -> the shape and filling to draw

    Methods
    -------
    draw_stimuli <- set_shape_pos, set_filling_pos
    draw_feedback
    """

    def __init__(self,win):
        self.feedback = visual.TextStim(win,color='magenta')
        self.box = Box(win)
        # memo for setting the width of square & diamond: 
        # width = height * (screen.height / screen.width) <= 0.625 for MacBook Pro
        self.square = visual.Rect(win,width=0.1875,height=0.3,lineColor='yellow',lineWidth=30)
        self.diamond = visual.ShapeStim(win,vertices=((0,0.4),(0.1,0.25),(0,0.1),(-0.1,0.25)),
                                        closeShape=True,lineColor='yellow',lineWidth=30)
        self.dots_2 = visual.ImageStim(win, image='./img/dots_2.png',size=(0.18,0.18))
        self.dots_3 = visual.ImageStim(win, image='./img/dots_3.png',size=(0.18,0.18))
        # drawable collections
        self.shapes = {'square':self.square,'diamond':self.diamond}
        self.fillings = {'dots_2':self.dots_2,'dots_3':self.dots_3}
        self.shape = None
        self.filling = None

    def draw_feedback(self,msg,position):
        self.feedback.text = msg
        if position=='top':
            self.feedback.pos=(0.0, 0.25)
        else:
            self.feedback.pos=(0.0, -0.25)
        self.feedback.draw()

    def set_shape_pos(self,shape_type,position):
        if shape_type=='square':
            if position=='top':
                self.square.pos = (0,0.25)
            else:
                self.square.pos = (0,-0.25)
        else:
            if position=='top':
                self.diamond.vertices = ((0,0.4),(0.1,0.25),(0,0.1),(-0.1,0.25))
            else:
                self.diamond.vertices = ((0,-0.4),(0.1,-0.25),(0,-0.1),(-0.1,-0.25))

    def set_filling_pos(self,position):
        if position=='top':
            self.filling.pos=(0.0, 0.25)
        else:
            self.filling.pos=(0.0, -0.25)

    def draw_stimuli(self,shape_type,filling_type,position):
        self.shape = self.shapes[shape_type]
        self.filling = self.fillings[filling_type]
        self.set_shape_pos(shape_type,position)
        self.set_filling_pos(position)
        self.shape.draw()
        self.filling.draw()


class PracticeBlock:
    """Schedule and manage the timeline of the practice block.

    Attributes
    ----------
    handler, drawer, timer

    Methods
    -------
    run (data will not be saved), dismiss (a clean up method)
    """

    def __init__(self,drawer,cond):
        self.handler = data.TrialHandler(
                                trialList=cond, 
                                nReps=1, 
                                method='random')
        self.drawer = drawer
        self.timer = core.Clock()

    def run(self,win):
        self.drawer.box.auto_draw()
        # Go through the trial sequence generated by the handler
        for eachTrial in self.handler:
            # Terminate the loop if the planned number of trials have been conducted 
            if self.handler.thisN > num_trial_prac-1:
                break
            # Draw stimuli
            self.drawer.draw_stimuli(self.handler.thisTrial['Shape'],
                                    self.handler.thisTrial['Filling'],
                                    self.handler.thisTrial['Position']) 
            win.flip()
            # Wait for response
            self.timer.reset()
            self.response = 'no_response'
            self.accuracy = 'missed'
            while self.timer.getTime() < display_time:
                self.key_press = event.getKeys(keyList=list(response_key.keys()))
                if len(self.key_press) > 0:
                    self.response = self.key_press[0]
                    if response_key[self.response] == self.handler.thisTrial['Answer']:
                        self.accuracy = 'correct'
                    else:
                        self.accuracy = 'wrong'
                    break
            # Give feedback (if missed or wrong)
            if self.accuracy == 'wrong':
                self.drawer.draw_feedback('That was the\n  wrong key',self.handler.thisTrial['Position'])
            elif self.accuracy == 'missed':
                self.drawer.draw_feedback('Time is up',self.handler.thisTrial['Position'])
            win.flip()
            core.wait(feedback_time)
            # Flip the window to its blank side
            win.flip()
            core.wait(blank_time)
            event.clearEvents()
        self.drawer.box.stop_draw()
        self.dismiss()

    def dismiss(self):
        del self.drawer
        del self.handler
        del self.timer


class Block:
    """Schedule and manage the timeline of each block.

    Attributes
    ----------
    handler, drawer, timer

    Methods
    -------
    run, dismiss (a clean up method)
    """

    def __init__(self,drawer,cond,start_info):
        self.handler = data.TrialHandler(
                                trialList=cond, 
                                nReps=num_trial_fml/len(cond), 
                                method='random', 
                                dataTypes=['trial_start',
                                            'resp_time',
                                            'response',
                                            'accuracy'], 
                                extraInfo=start_info)
        self.drawer = drawer
        self.timer = core.Clock()

    def run(self,win):
        self.drawer.box.auto_draw()
        # Go through the trial sequence generated by the handler
        for eachTrial in self.handler:
            # Draw stimuli
            self.drawer.draw_stimuli(self.handler.thisTrial['Shape'],
                                    self.handler.thisTrial['Filling'],
                                    self.handler.thisTrial['Position']) 
            win.flip()
            # Track start time of each trial
            self.timer.reset()
            self.current_time = str(time.time())
            self.handler.addData('trial_start', self.current_time)
            # Wait for response
            self.response = 'no_response'
            self.resp_time = 'N/A'
            self.accuracy = 'missed'
            while self.timer.getTime() < display_time:
                self.key_press = event.getKeys(keyList=list(response_key.keys()), timeStamped=self.timer)
                if len(self.key_press) > 0:
                    (self.response,self.resp_time) = self.key_press[0]
                    if response_key[self.response] == self.handler.thisTrial['Answer']:
                        self.accuracy = 'correct'
                    else:
                        self.accuracy = 'wrong'
                    break
            # Give feedback (if missed or wrong)
            if self.accuracy == 'wrong':
                self.drawer.draw_feedback('That was the\n  wrong key',self.handler.thisTrial['Position'])
            elif self.accuracy == 'missed':
                self.drawer.draw_feedback('Time is up',self.handler.thisTrial['Position'])
            win.flip()
            core.wait(feedback_time)
            # Flip the window to its blank side
            win.flip()
            core.wait(blank_time)
            # Record response, response time, and accuracy
            self.handler.addData('resp_time', self.resp_time)
            self.handler.addData('response', self.response)
            self.handler.addData('accuracy', self.accuracy)
            event.clearEvents()
        # Save start info, stimulus, data values, etc. to log
        self.handler.saveAsWideText(result_log_path, delim=',', 
                                    matrixOnly=os.path.exists(result_log_path), 
                                    appendFile=True)
        self.drawer.box.stop_draw()
        self.dismiss()

    def dismiss(self):
        del self.drawer
        del self.handler
        del self.timer


def present_instruction(win,instruction,i):
    instruction.image = instr_path[i]
    instruction.draw()
    win.flip()
    event.waitKeys(keyList=continue_key)
    event.clearEvents()


def import_conditions():
    """Prepare condition settings for each task"""

    dual_task = pd.read_excel('./conditions.xlsx')
    shape_task = dual_task[dual_task.Target=='shape']
    filling_task = dual_task[dual_task.Target=='filling']
    return dual_task.to_dict('records'),shape_task.to_dict('records'),filling_task.to_dict('records')


def obtain_start_info():
    """Obtain subject ID and session No. via GUI"""

    myDlg = gui.Dlg(title='Multi-tasking Test')
    myDlg.addField('Subject ID: ')
    myDlg.addField('Session No: ')
    myDlg.show()
    if myDlg.OK and myDlg.data[0] and myDlg.data[1]:
        print("🕐 Setting experiment info ...")
        return {'subject_id': myDlg.data[0],'session_no': myDlg.data[1]}
    else:
        print("😵 Test cancelled or required start info (i.e., subject ID or session No) is missing.")
        core.quit()


def double_check():
    """Double-check of required materials & validity of preference setting"""

    print("🕐 Double-checking required materials & validity of preference setting ...")
    required_materials = [
        './img/dots_2.png',
        './img/dots_3.png',
        './conditions.xlsx',
        output_path
    ] + instr_path
    for path in required_materials:
        if not os.path.exists(path):
            if path == output_path:
                os.mkdir(output_path)
            else:
                print("😵 Required material not found: {}".format(path))

    if num_trial_fml % 8 != 0:
        print("😵 The number of trials in each block should be a multiple of 8")


def conduct_fml_block(win,instruction,instr_no,drawer,cond,start_info):
    present_instruction(win,instruction,instr_no)
    block = Block(drawer,cond,start_info)
    block.run(win)


def conduct_prac_block(win,instruction,instr_no,drawer,cond):
    present_instruction(win,instruction,instr_no)
    prac_block = PracticeBlock(drawer,cond)
    prac_block.run(win)
    

################################################# MAIN #################################################

def main():
    """ Summary of workflow:

    Preparation
    -----------
    1. Double-check of required materials & the validity of preference setting
    2. Setup experiment info
    3. Setup the window and begin the session
    4. Introduce task

    Conduct Experiment
    ------------------
    5. Schedule and run each block
    6. End the session and write experiment info (start info + preference + runtime info) to log
    7. clean up
    """

# Double-check of required materials & the validity of preference setting
    double_check()

# Setup experiment info
    start_info = obtain_start_info() # Subject ID & session No
    dual_task_cond,shape_task_cond,filling_task_cond = import_conditions()
    runtime_info = {}
    runtime_info['session_start'] = time.time()

# Setup the window and begin the session
    exp_mon = monitors.Monitor(name='testMonitor',width=mon_width)
    win = visual.Window(
                        size=(mon_width,mon_height),
                        fullscr=True,
                        color='black',
                        monitor=exp_mon,
                        units='norm')
    drawer = Drawer(win)

# Introduce task (task overview)
    instruction = visual.ImageStim(win,size=(1.5,1.5))
    for i in range(3):
        present_instruction(win,instruction,i)

# Schedule and run each block
    # Practice session
    if include_practice:
        present_instruction(win,instruction,7) # start message of practice session
        conduct_prac_block(win,instruction,3,drawer,shape_task_cond)
        conduct_prac_block(win,instruction,4,drawer,filling_task_cond)
        conduct_prac_block(win,instruction,5,drawer,dual_task_cond)
        present_instruction(win,instruction,8) # end message of practice session
    # Formal session
    conduct_fml_block(win,instruction,3,drawer,shape_task_cond,{**start_info,**{'block':'shape_task'}})
    conduct_fml_block(win,instruction,4,drawer,filling_task_cond,{**start_info,**{'block':'filling_task'}})
    conduct_fml_block(win,instruction,5,drawer,dual_task_cond,{**start_info,**{'block':'dual_task'}})
    present_instruction(win,instruction,6) # end message of the whole session
    
# End the session and write experiment info to log
    runtime_info['session_end'] = time.time()
    preferences = {
        'include_practice': include_practice,
        'display_time': display_time,
        'blank_time': blank_time,
        'feedback_time': feedback_time,
        'left_key': list(response_key.keys())[0],
        'right_key': list(response_key.keys())[1],
        'num_trial_prac': num_trial_prac,
        'num_trial_fml': num_trial_fml
    }
    exp_info = {**start_info, **preferences, **runtime_info}
    exp_record = pd.DataFrame([exp_info],columns=exp_info.keys())
    need_header = not os.path.exists(exp_info_log_path)
    with open(exp_info_log_path,'a') as f:
        exp_record.to_csv(f,header=need_header,index=False)

# cleanup
    win.close()
    core.quit()


if __name__ == '__main__':
    main()