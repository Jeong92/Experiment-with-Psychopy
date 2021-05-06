#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on 5월 06, 2021, at 14:24
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
    originPath='D:\\Google Drive\\PsychoPy\\Cued GoNogo Task\\Cued GoNogo Task.py',
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
    text='+',
    font='NanumSquare',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
grating = visual.GratingStim(
    win=win, name='grating',
    tex=None, mask=None,
    ori=0.0, pos=(0, 0), size=1.0, sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=0.0)
env_grating = visual.EnvelopeGrating(
    win=win, name='env_grating',
    carrier='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.3),
    sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
     opacity=None, contrast=0.5,
    texRes=128.0, envelope='sin',
    envori=0.0, envsf=1.0,
    envphase=0.0, power=1.0,
    moddepth=1.0, blendmode='avg', beat=False, interpolate=True, depth=-1.0)
if sys.version[0]=='3' and np.min(win.gamma) == None:
    logging.warning('Envelope grating in use with no gamma set. Unless you have hardware gamma correction the image will be distorted.')
elif np.min(win.gamma) < 1.01:
    logging.warning('Envelope grating in use with window gamma <= 1.0 or no gamma set at all. Unless you have hardware gamma correction the image will be distorted.')

# Initialize components for Routine "TaskEnd"
TaskEndClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "TaskIntro"-------
continueRoutine = True
routineTimer.add(0.700000)
# update component parameters for each repeat
# keep track of which components have finished
TaskIntroComponents = [fixation]
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation.tStartRefresh + 0.7-frameTolerance:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
            fixation.setAutoDraw(False)
    
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
        grating.setSize([Stim_Width, Stim_Height])
        # keep track of which components have finished
        TrialComponents = [grating, env_grating]
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
            
            # *grating* updates
            if grating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grating.frameNStart = frameN  # exact frame index
                grating.tStart = t  # local t and not account for scr refresh
                grating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
                grating.setAutoDraw(True)
            if grating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grating.tStartRefresh + CueTime-frameTolerance:
                    # keep track of stop time/frame for later
                    grating.tStop = t  # not accounting for scr refresh
                    grating.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(grating, 'tStopRefresh')  # time at next scr refresh
                    grating.setAutoDraw(False)
            
            # *env_grating* updates
            if env_grating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                env_grating.frameNStart = frameN  # exact frame index
                env_grating.tStart = t  # local t and not account for scr refresh
                env_grating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(env_grating, 'tStartRefresh')  # time at next scr refresh
                env_grating.setAutoDraw(True)
            if env_grating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > env_grating.tStartRefresh + CueTime-frameTolerance:
                    # keep track of stop time/frame for later
                    env_grating.tStop = t  # not accounting for scr refresh
                    env_grating.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(env_grating, 'tStopRefresh')  # time at next scr refresh
                    env_grating.setAutoDraw(False)
            
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
        Trials.addData('grating.started', grating.tStartRefresh)
        Trials.addData('grating.stopped', grating.tStopRefresh)
        Trials.addData('env_grating.started', env_grating.tStartRefresh)
        Trials.addData('env_grating.stopped', env_grating.tStopRefresh)
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
