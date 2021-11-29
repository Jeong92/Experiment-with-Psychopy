#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Thu Jul 15 00:15:34 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import random


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'ReactionTime'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/hojinjeong/Google 드라이브/PsychoPy/Human Benchmark/1. Reaction Time/ReactionTime_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='SteelBlue', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Introduction"
IntroductionClock = core.Clock()
stim_inst = visual.TextStim(win=win, name='stim_inst',
    text='빨간색 사각형이 초록색으로 바뀌었을 때, 최대한 빠르게 버튼을 눌러주세요.\n\n마우스를 클릭하면 검사가 시작됩니다.',
    font='NanumSquare',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stim_resp = event.Mouse(win=win)
x, y = [None, None]
stim_resp.mouseClock = core.Clock()

# Initialize components for Routine "Cue"
CueClock = core.Clock()
stim_cue = visual.Rect(
    win=win, name='stim_cue',units='height', 
    width=(2, 1)[0], height=(2, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
stim_message = visual.TextStim(win=win, name='stim_message',
    text='',
    font='NanumSquare',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
stim_mouse = event.Mouse(win=win)
x, y = [None, None]
stim_mouse.mouseClock = core.Clock()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
rt_recorded = []
rt_sum = 0
feedback_message = visual.TextStim(win=win, name='feedback_message',
    text='',
    font='NanumSquare',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedback_mouse = event.Mouse(win=win)
x, y = [None, None]
feedback_mouse.mouseClock = core.Clock()

# Initialize components for Routine "TaskEnd"
TaskEndClock = core.Clock()
TaskEnd_message = visual.TextStim(win=win, name='TaskEnd_message',
    text='',
    font='NanumSquare',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
TaskEnd_mouse = event.Mouse(win=win)
x, y = [None, None]
TaskEnd_mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Introduction"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the stim_resp
gotValidClick = False  # until a click is received
# keep track of which components have finished
IntroductionComponents = [stim_inst, stim_resp]
for thisComponent in IntroductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Introduction"-------
while continueRoutine:
    # get current time
    t = IntroductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stim_inst* updates
    if stim_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stim_inst.frameNStart = frameN  # exact frame index
        stim_inst.tStart = t  # local t and not account for scr refresh
        stim_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stim_inst, 'tStartRefresh')  # time at next scr refresh
        stim_inst.setAutoDraw(True)
    # *stim_resp* updates
    if stim_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stim_resp.frameNStart = frameN  # exact frame index
        stim_resp.tStart = t  # local t and not account for scr refresh
        stim_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stim_resp, 'tStartRefresh')  # time at next scr refresh
        stim_resp.status = STARTED
        stim_resp.mouseClock.reset()
        prevButtonState = stim_resp.getPressed()  # if button is down already this ISN'T a new click
    if stim_resp.status == STARTED:  # only update if started and not finished!
        buttons = stim_resp.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction"-------
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stim_inst.started', stim_inst.tStartRefresh)
thisExp.addData('stim_inst.stopped', stim_inst.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = stim_resp.getPos()
buttons = stim_resp.getPressed()
thisExp.addData('stim_resp.x', x)
thisExp.addData('stim_resp.y', y)
thisExp.addData('stim_resp.leftButton', buttons[0])
thisExp.addData('stim_resp.midButton', buttons[1])
thisExp.addData('stim_resp.rightButton', buttons[2])
thisExp.addData('stim_resp.started', stim_resp.tStart)
thisExp.addData('stim_resp.stopped', stim_resp.tStop)
thisExp.nextEntry()
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Cue"-------
    continueRoutine = True
    # update component parameters for each repeat
    time_change = random.randint(101,500)/100
    
    stim_color = 'DarkRed'
    stim_msg = '사각형 색생이 초록색으로 바뀔 때까지 기다려주세요.'
    
    
    timer = core.Clock()
    stim_cue.setLineColor(stim_color)
    # setup some python lists for storing info about the stim_mouse
    stim_mouse.x = []
    stim_mouse.y = []
    stim_mouse.leftButton = []
    stim_mouse.midButton = []
    stim_mouse.rightButton = []
    stim_mouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    CueComponents = [stim_cue, stim_message, stim_mouse]
    for thisComponent in CueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Cue"-------
    while continueRoutine:
        # get current time
        t = CueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if timer.getTime() > time_change:
            stim_color = 'MediumSeaGreen'
            stim_msg = '마우스를 클릭해 주세요!'
        
        # *stim_cue* updates
        if stim_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_cue.frameNStart = frameN  # exact frame index
            stim_cue.tStart = t  # local t and not account for scr refresh
            stim_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_cue, 'tStartRefresh')  # time at next scr refresh
            stim_cue.setAutoDraw(True)
        if stim_cue.status == STARTED:  # only update if drawing
            stim_cue.setFillColor(stim_color)
        
        # *stim_message* updates
        if stim_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_message.frameNStart = frameN  # exact frame index
            stim_message.tStart = t  # local t and not account for scr refresh
            stim_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_message, 'tStartRefresh')  # time at next scr refresh
            stim_message.setAutoDraw(True)
        if stim_message.status == STARTED:  # only update if drawing
            stim_message.setText(stim_msg)
        # *stim_mouse* updates
        if stim_mouse.status == NOT_STARTED and t >= time_change-frameTolerance:
            # keep track of start time/frame for later
            stim_mouse.frameNStart = frameN  # exact frame index
            stim_mouse.tStart = t  # local t and not account for scr refresh
            stim_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_mouse, 'tStartRefresh')  # time at next scr refresh
            stim_mouse.status = STARTED
            stim_mouse.mouseClock.reset()
            prevButtonState = stim_mouse.getPressed()  # if button is down already this ISN'T a new click
        if stim_mouse.status == STARTED:  # only update if started and not finished!
            buttons = stim_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = stim_mouse.getPos()
                    stim_mouse.x.append(x)
                    stim_mouse.y.append(y)
                    buttons = stim_mouse.getPressed()
                    stim_mouse.leftButton.append(buttons[0])
                    stim_mouse.midButton.append(buttons[1])
                    stim_mouse.rightButton.append(buttons[2])
                    stim_mouse.time.append(stim_mouse.mouseClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cue"-------
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('stim_cue.started', stim_cue.tStartRefresh)
    trials.addData('stim_cue.stopped', stim_cue.tStopRefresh)
    trials.addData('stim_message.started', stim_message.tStartRefresh)
    trials.addData('stim_message.stopped', stim_message.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(stim_mouse.x): trials.addData('stim_mouse.x', stim_mouse.x[0])
    if len(stim_mouse.y): trials.addData('stim_mouse.y', stim_mouse.y[0])
    if len(stim_mouse.leftButton): trials.addData('stim_mouse.leftButton', stim_mouse.leftButton[0])
    if len(stim_mouse.midButton): trials.addData('stim_mouse.midButton', stim_mouse.midButton[0])
    if len(stim_mouse.rightButton): trials.addData('stim_mouse.rightButton', stim_mouse.rightButton[0])
    if len(stim_mouse.time): trials.addData('stim_mouse.time', stim_mouse.time[0])
    trials.addData('stim_mouse.started', stim_mouse.tStart)
    trials.addData('stim_mouse.stopped', stim_mouse.tStop)
    # the Routine "Cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    mouse_rt = stim_mouse.time[-1]*1000
    rt_recorded.append(round(mouse_rt, 2))
    rt_sum += round(mouse_rt, 2)
    
    feedback_msg = str(round(mouse_rt, 2))+" ms"+"\n"+"클릭하면 다음 시행으로 넘어갑니다."
    feedback_message.setText(feedback_msg)
    # setup some python lists for storing info about the feedback_mouse
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    FeedbackComponents = [feedback_message, feedback_mouse]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_message* updates
        if feedback_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_message.frameNStart = frameN  # exact frame index
            feedback_message.tStart = t  # local t and not account for scr refresh
            feedback_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_message, 'tStartRefresh')  # time at next scr refresh
            feedback_message.setAutoDraw(True)
        # *feedback_mouse* updates
        if feedback_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_mouse.frameNStart = frameN  # exact frame index
            feedback_mouse.tStart = t  # local t and not account for scr refresh
            feedback_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_mouse, 'tStartRefresh')  # time at next scr refresh
            feedback_mouse.status = STARTED
            feedback_mouse.mouseClock.reset()
            prevButtonState = feedback_mouse.getPressed()  # if button is down already this ISN'T a new click
        if feedback_mouse.status == STARTED:  # only update if started and not finished!
            buttons = feedback_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedback_message.started', feedback_message.tStartRefresh)
    trials.addData('feedback_message.stopped', feedback_message.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = feedback_mouse.getPos()
    buttons = feedback_mouse.getPressed()
    trials.addData('feedback_mouse.x', x)
    trials.addData('feedback_mouse.y', y)
    trials.addData('feedback_mouse.leftButton', buttons[0])
    trials.addData('feedback_mouse.midButton', buttons[1])
    trials.addData('feedback_mouse.rightButton', buttons[2])
    trials.addData('feedback_mouse.started', feedback_mouse.tStart)
    trials.addData('feedback_mouse.stopped', feedback_mouse.tStop)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'trials'


# ------Prepare to start Routine "TaskEnd"-------
continueRoutine = True
# update component parameters for each repeat
meanRT = rt_sum/len(rt_recorded)
TaskEnd_message.setText("평균 반응 속도: "+"\n"+str(meanRT)+"ms")
# setup some python lists for storing info about the TaskEnd_mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
TaskEndComponents = [TaskEnd_message, TaskEnd_mouse]
for thisComponent in TaskEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TaskEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TaskEnd"-------
while continueRoutine:
    # get current time
    t = TaskEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TaskEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TaskEnd_message* updates
    if TaskEnd_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TaskEnd_message.frameNStart = frameN  # exact frame index
        TaskEnd_message.tStart = t  # local t and not account for scr refresh
        TaskEnd_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TaskEnd_message, 'tStartRefresh')  # time at next scr refresh
        TaskEnd_message.setAutoDraw(True)
    # *TaskEnd_mouse* updates
    if TaskEnd_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TaskEnd_mouse.frameNStart = frameN  # exact frame index
        TaskEnd_mouse.tStart = t  # local t and not account for scr refresh
        TaskEnd_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TaskEnd_mouse, 'tStartRefresh')  # time at next scr refresh
        TaskEnd_mouse.status = STARTED
        TaskEnd_mouse.mouseClock.reset()
        prevButtonState = TaskEnd_mouse.getPressed()  # if button is down already this ISN'T a new click
    if TaskEnd_mouse.status == STARTED:  # only update if started and not finished!
        buttons = TaskEnd_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TaskEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TaskEnd"-------
for thisComponent in TaskEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TaskEnd_message.started', TaskEnd_message.tStartRefresh)
thisExp.addData('TaskEnd_message.stopped', TaskEnd_message.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = TaskEnd_mouse.getPos()
buttons = TaskEnd_mouse.getPressed()
thisExp.addData('TaskEnd_mouse.x', x)
thisExp.addData('TaskEnd_mouse.y', y)
thisExp.addData('TaskEnd_mouse.leftButton', buttons[0])
thisExp.addData('TaskEnd_mouse.midButton', buttons[1])
thisExp.addData('TaskEnd_mouse.rightButton', buttons[2])
thisExp.addData('TaskEnd_mouse.started', TaskEnd_mouse.tStart)
thisExp.addData('TaskEnd_mouse.stopped', TaskEnd_mouse.tStop)
thisExp.nextEntry()
# the Routine "TaskEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
