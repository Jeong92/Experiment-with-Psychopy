#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 11월 29, 2021, at 23:40
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'BreakTime'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\goran\\OneDrive\\문서\\GitHub\\Experiment-with-Psychopy\\실습7-BreakTime\\BreakTime_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_stim = visual.TextStim(win=win, name='trial_stim',
    text='+',
    font='NanumSquare',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Timer_text = visual.TextStim(win=win, name='Timer_text',
    text='',
    font='NanumSquare',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
trial_key_resp = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
rest_text = visual.TextStim(win=win, name='rest_text',
    text='잠시 과제를 쉬겠습니다.\n다음 시행을 진행하려면 스페이스바를 눌러주세요.',
    font='NanumSquare',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
rest_key_resp = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
ITI_text = visual.TextStim(win=win, name='ITI_text',
    text='+',
    font='NanumSquare',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=20.0, method='random', 
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
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    task_time = randint(100, 300)/100
    
    # set timer
    if trials.thisN == 0:
        timer = core.Clock() # core.CountdownTimer(10) 이런 식으로도 사용 가능
    trial_key_resp.keys = []
    trial_key_resp.rt = []
    _trial_key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trial_stim, Timer_text, trial_key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_stim* updates
        if trial_stim.status == NOT_STARTED and tThisFlip >= task_time-frameTolerance:
            # keep track of start time/frame for later
            trial_stim.frameNStart = frameN  # exact frame index
            trial_stim.tStart = t  # local t and not account for scr refresh
            trial_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_stim, 'tStartRefresh')  # time at next scr refresh
            trial_stim.setAutoDraw(True)
        
        # *Timer_text* updates
        if Timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Timer_text.frameNStart = frameN  # exact frame index
            Timer_text.tStart = t  # local t and not account for scr refresh
            Timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Timer_text, 'tStartRefresh')  # time at next scr refresh
            Timer_text.setAutoDraw(True)
        if Timer_text.status == STARTED:  # only update if drawing
            Timer_text.setText(round(timer.getTime(),2), log=False)
        
        # *trial_key_resp* updates
        waitOnFlip = False
        if trial_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_key_resp.frameNStart = frameN  # exact frame index
            trial_key_resp.tStart = t  # local t and not account for scr refresh
            trial_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_key_resp, 'tStartRefresh')  # time at next scr refresh
            trial_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _trial_key_resp_allKeys.extend(theseKeys)
            if len(_trial_key_resp_allKeys):
                trial_key_resp.keys = _trial_key_resp_allKeys[-1].name  # just the last key pressed
                trial_key_resp.rt = _trial_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('trial_stim.started', trial_stim.tStartRefresh)
    trials.addData('trial_stim.stopped', trial_stim.tStopRefresh)
    # check responses
    if trial_key_resp.keys in ['', [], None]:  # No response was made
        trial_key_resp.keys = None
    trials.addData('trial_key_resp.keys',trial_key_resp.keys)
    if trial_key_resp.keys != None:  # we had a response
        trials.addData('trial_key_resp.rt', trial_key_resp.rt)
    trials.addData('trial_key_resp.started', trial_key_resp.tStartRefresh)
    trials.addData('trial_key_resp.stopped', trial_key_resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    if timer.getTime() < 10:
        continueRoutine  = False
    else:
        continueRoutine  = True
    rest_key_resp.keys = []
    rest_key_resp.rt = []
    _rest_key_resp_allKeys = []
    # keep track of which components have finished
    restComponents = [rest_text, rest_key_resp]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_text* updates
        if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text.frameNStart = frameN  # exact frame index
            rest_text.tStart = t  # local t and not account for scr refresh
            rest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
            rest_text.setAutoDraw(True)
        
        # *rest_key_resp* updates
        waitOnFlip = False
        if rest_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_key_resp.frameNStart = frameN  # exact frame index
            rest_key_resp.tStart = t  # local t and not account for scr refresh
            rest_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_key_resp, 'tStartRefresh')  # time at next scr refresh
            rest_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rest_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rest_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rest_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = rest_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _rest_key_resp_allKeys.extend(theseKeys)
            if len(_rest_key_resp_allKeys):
                rest_key_resp.keys = _rest_key_resp_allKeys[-1].name  # just the last key pressed
                rest_key_resp.rt = _rest_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if timer.getTime() > 10:
        timer.reset()
    # check responses
    if rest_key_resp.keys in ['', [], None]:  # No response was made
        rest_key_resp.keys = None
    trials.addData('rest_key_resp.keys',rest_key_resp.keys)
    if rest_key_resp.keys != None:  # we had a response
        trials.addData('rest_key_resp.rt', rest_key_resp.rt)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [ITI_text]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_text* updates
        if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_text.frameNStart = frameN  # exact frame index
            ITI_text.tStart = t  # local t and not account for scr refresh
            ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
            ITI_text.setAutoDraw(True)
        if ITI_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ITI_text.tStop = t  # not accounting for scr refresh
                ITI_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI_text, 'tStopRefresh')  # time at next scr refresh
                ITI_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'trials'


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
