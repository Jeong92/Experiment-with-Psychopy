#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on 5월 06, 2021, at 15:04
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
psychopyVersion = '2021.1.4'
expName = 'Cued GoNogo Task'  # from the Builder filename that created this script
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
    originPath='D:\\Google Drive\\PsychoPy\\Cued GoNogo Task\\Cued GoNogo Task_lastrun.py',
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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "TaskIntro"
TaskIntroClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='안녕하세요. 검사에 참여해주셔서 감사합니다. 스페이스바를 누르면 검사가 시작됩니다.',
    font='NanumSquare',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
FixationPhase = visual.TextStim(win=win, name='FixationPhase',
    text='+',
    font='NanumSquare',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Blank = visual.TextStim(win=win, name='Blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Cue = visual.Rect(
    win=win, name='Cue',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
GoNogo_Stim = visual.Rect(
    win=win, name='GoNogo_Stim',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.5,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
Key_Resp = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Feedback_Present = visual.TextStim(win=win, name='Feedback_Present',
    text='',
    font='NanumSquare',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "TaskEnd"
TaskEndClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "TaskIntro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
TaskIntroComponents = [fixation, key_resp]
for thisComponent in TaskIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TaskIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TaskIntro"-------
while continueRoutine:
    # get current time
    t = TaskIntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TaskIntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation* updates
    if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation.frameNStart = frameN  # exact frame index
        fixation.tStart = t  # local t and not account for scr refresh
        fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
        fixation.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TaskIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TaskIntro"-------
for thisComponent in TaskIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation.started', fixation.tStartRefresh)
thisExp.addData('fixation.stopped', fixation.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "TaskIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BlockList.xlsx'),
    seed=None, name='Blocks')
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in Blocks:
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(Block),
        seed=None, name='Trials')
    thisExp.addLoop(Trials)  # add the loop to the experiment
    thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in Trials:
        currentLoop = Trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Fixation"-------
        continueRoutine = True
        routineTimer.add(1.200000)
        # update component parameters for each repeat
        # keep track of which components have finished
        FixationComponents = [FixationPhase, Blank]
        for thisComponent in FixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixationPhase* updates
            if FixationPhase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixationPhase.frameNStart = frameN  # exact frame index
                FixationPhase.tStart = t  # local t and not account for scr refresh
                FixationPhase.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixationPhase, 'tStartRefresh')  # time at next scr refresh
                FixationPhase.setAutoDraw(True)
            if FixationPhase.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixationPhase.tStartRefresh + 0.7-frameTolerance:
                    # keep track of stop time/frame for later
                    FixationPhase.tStop = t  # not accounting for scr refresh
                    FixationPhase.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixationPhase, 'tStopRefresh')  # time at next scr refresh
                    FixationPhase.setAutoDraw(False)
            
            # *Blank* updates
            if Blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Blank.frameNStart = frameN  # exact frame index
                Blank.tStart = t  # local t and not account for scr refresh
                Blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Blank, 'tStartRefresh')  # time at next scr refresh
                Blank.setAutoDraw(True)
            if Blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Blank.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Blank.tStop = t  # not accounting for scr refresh
                    Blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Blank, 'tStopRefresh')  # time at next scr refresh
                    Blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Fixation"-------
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Trials.addData('FixationPhase.started', FixationPhase.tStartRefresh)
        Trials.addData('FixationPhase.stopped', FixationPhase.tStopRefresh)
        Trials.addData('Blank.started', Blank.tStartRefresh)
        Trials.addData('Blank.stopped', Blank.tStopRefresh)
        
        # ------Prepare to start Routine "Trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Cue.setSize([Stim_Width, Stim_Height])
        if StimType == 'Go':
            StimColor = 'green'
        elif StimType == 'NoGo':
            StimColor = 'blue'
        GoNogo_Stim.setFillColor(StimColor)
        GoNogo_Stim.setSize([Stim_Width, Stim_Height])
        Key_Resp.keys = []
        Key_Resp.rt = []
        _Key_Resp_allKeys = []
        # keep track of which components have finished
        TrialComponents = [Cue, GoNogo_Stim, Key_Resp]
        for thisComponent in TrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Trial"-------
        while continueRoutine:
            # get current time
            t = TrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Cue* updates
            if Cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Cue.frameNStart = frameN  # exact frame index
                Cue.tStart = t  # local t and not account for scr refresh
                Cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cue, 'tStartRefresh')  # time at next scr refresh
                Cue.setAutoDraw(True)
            if Cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Cue.tStartRefresh + CueTime-frameTolerance:
                    # keep track of stop time/frame for later
                    Cue.tStop = t  # not accounting for scr refresh
                    Cue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Cue, 'tStopRefresh')  # time at next scr refresh
                    Cue.setAutoDraw(False)
            
            # *GoNogo_Stim* updates
            if GoNogo_Stim.status == NOT_STARTED and tThisFlip >= CueTime+0.2-frameTolerance:
                # keep track of start time/frame for later
                GoNogo_Stim.frameNStart = frameN  # exact frame index
                GoNogo_Stim.tStart = t  # local t and not account for scr refresh
                GoNogo_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GoNogo_Stim, 'tStartRefresh')  # time at next scr refresh
                GoNogo_Stim.setAutoDraw(True)
            if GoNogo_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GoNogo_Stim.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    GoNogo_Stim.tStop = t  # not accounting for scr refresh
                    GoNogo_Stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GoNogo_Stim, 'tStopRefresh')  # time at next scr refresh
                    GoNogo_Stim.setAutoDraw(False)
            
            # *Key_Resp* updates
            waitOnFlip = False
            if Key_Resp.status == NOT_STARTED and tThisFlip >= CueTime+0.2-frameTolerance:
                # keep track of start time/frame for later
                Key_Resp.frameNStart = frameN  # exact frame index
                Key_Resp.tStart = t  # local t and not account for scr refresh
                Key_Resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Key_Resp, 'tStartRefresh')  # time at next scr refresh
                Key_Resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Key_Resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Key_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Key_Resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Key_Resp.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Key_Resp.tStop = t  # not accounting for scr refresh
                    Key_Resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Key_Resp, 'tStopRefresh')  # time at next scr refresh
                    Key_Resp.status = FINISHED
            if Key_Resp.status == STARTED and not waitOnFlip:
                theseKeys = Key_Resp.getKeys(keyList=['space'], waitRelease=False)
                _Key_Resp_allKeys.extend(theseKeys)
                if len(_Key_Resp_allKeys):
                    Key_Resp.keys = _Key_Resp_allKeys[-1].name  # just the last key pressed
                    Key_Resp.rt = _Key_Resp_allKeys[-1].rt
                    # was this correct?
                    if (Key_Resp.keys == str(CRESP)) or (Key_Resp.keys == CRESP):
                        Key_Resp.corr = 1
                    else:
                        Key_Resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial"-------
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Trials.addData('Cue.started', Cue.tStartRefresh)
        Trials.addData('Cue.stopped', Cue.tStopRefresh)
        Trials.addData('GoNogo_Stim.started', GoNogo_Stim.tStartRefresh)
        Trials.addData('GoNogo_Stim.stopped', GoNogo_Stim.tStopRefresh)
        # check responses
        if Key_Resp.keys in ['', [], None]:  # No response was made
            Key_Resp.keys = None
            # was no response the correct answer?!
            if str(CRESP).lower() == 'none':
               Key_Resp.corr = 1;  # correct non-response
            else:
               Key_Resp.corr = 0;  # failed to respond (incorrectly)
        # store data for Trials (TrialHandler)
        Trials.addData('Key_Resp.keys',Key_Resp.keys)
        Trials.addData('Key_Resp.corr', Key_Resp.corr)
        if Key_Resp.keys != None:  # we had a response
            Trials.addData('Key_Resp.rt', Key_Resp.rt)
        Trials.addData('Key_Resp.started', Key_Resp.tStartRefresh)
        Trials.addData('Key_Resp.stopped', Key_Resp.tStopRefresh)
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        if StimType == 'Go': # go cue 제시 조건에서 
            if Key_Resp.corr == 1: # 정답을 맞췄으면,
                fb_color = 'Maroon'
                fb_msg = "정확합니다"+"\n"+"반응속도: "+str(int(Key_Resp.rt*1000))+"ms"
            else: # 틀린 경우에
                fb_color = 'MediumBlue'
                fb_msg = "틀렸습니다"
        elif StimType == 'NoGo': # Nogo cue 제시 조건에서 
            if Key_Resp.corr == 1: # 정답을 맞췄으면,
                fb_color = 'Maroon'
                fb_msg = "정확합니다"
            else: # 틀린 경우에
                fb_color = 'MediumBlue'
                fb_msg = "틀렸습니다. 버튼을 누르면 안 됩니다."    
        Feedback_Present.setColor(fb_color, colorSpace='rgb')
        Feedback_Present.setText(fb_msg)
        # keep track of which components have finished
        FeedbackComponents = [Feedback_Present]
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
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Feedback_Present* updates
            if Feedback_Present.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback_Present.frameNStart = frameN  # exact frame index
                Feedback_Present.tStart = t  # local t and not account for scr refresh
                Feedback_Present.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback_Present, 'tStartRefresh')  # time at next scr refresh
                Feedback_Present.setAutoDraw(True)
            if Feedback_Present.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback_Present.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback_Present.tStop = t  # not accounting for scr refresh
                    Feedback_Present.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Feedback_Present, 'tStopRefresh')  # time at next scr refresh
                    Feedback_Present.setAutoDraw(False)
            
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
        Trials.addData('Feedback_Present.started', Feedback_Present.tStartRefresh)
        Trials.addData('Feedback_Present.stopped', Feedback_Present.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Trials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Blocks'


# ------Prepare to start Routine "TaskEnd"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
TaskEndComponents = []
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
