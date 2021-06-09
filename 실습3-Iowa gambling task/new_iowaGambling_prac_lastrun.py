#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Wed Jun  9 23:47:03 2021
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
expName = 'new_iowaGambling_prac'  # from the Builder filename that created this script
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
    originPath='/Users/hojinjeong/Documents/GitHub/Experiment-with-Psychopy/실습3-Iowa gambling task/new_iowaGambling_prac_lastrun.py',
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

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
Instruction = visual.TextStim(win=win, name='Instruction',
    text='검사가 시작하게 되면 4개의 카드 덱 중 하나를 선택해주세요. 각 덱을 선택할때마다 일정한 금전적 이득과 손실이 발생할 수 있습니다. 이득을 최대화하는 카드 덱을 선택해주세요. 검사를 시작하려면 스페이스바를 눌러주세요.',
    font='NanumSquare',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Intro_resp = keyboard.Keyboard()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Trial_Instruction = visual.TextStim(win=win, name='Trial_Instruction',
    text='카드를 선택해주세요.',
    font='NanumSquare',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
DeckA = visual.ImageStim(
    win=win,
    name='DeckA', 
    image='images/Card.jpg', mask=None,
    ori=0.0, pos=[-0.5, 0], size=[0.25, 0.25*1.45],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
DeckB = visual.ImageStim(
    win=win,
    name='DeckB', 
    image='images/Card.jpg', mask=None,
    ori=0.0, pos=[-0.17, 0], size=[0.25, 0.25*1.45],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
DeckC = visual.ImageStim(
    win=win,
    name='DeckC', 
    image='images/Card.jpg', mask=None,
    ori=0.0, pos=[0.16, 0], size=[0.25, 0.25*1.45],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
DeckD = visual.ImageStim(
    win=win,
    name='DeckD', 
    image='images/Card.jpg', mask=None,
    ori=0.0, pos=[0.5, 0], size=[0.25, 0.25*1.45],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
border = visual.Rect(
    win=win, name='border',
    width=[0.26, 0.26*1.45][0], height=[0.26, 0.26*1.45][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor=None,
    opacity=1.0, depth=-5.0, interpolate=True)
Trial_click = event.Mouse(win=win)
x, y = [None, None]
Trial_click.mouseClock = core.Clock()
border_loc = 0
totMoney = visual.TextStim(win=win, name='totMoney',
    text='',
    font='NanumSquare',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Nchoice = visual.TextStim(win=win, name='Nchoice',
    text='',
    font='Open Sans',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
# deck list
# win or loss?
deckA_list = [1,1,1,1,1,0,0,0,0,0]
deckB_list = [1,0,0,0,0,0,0,0,0,0]
deckC_list = [1,1,1,1,1,0,0,0,0,0]
deckD_list = [1,0,0,0,0,0,0,0,0,0]
#deckA_list = [1]*deck_list[0][2]+[0]*(ncard_per_deck-deck_list[0][2])
#deckB_list = [1]*deck_list[1][2]+[0]*(ncard_per_deck-deck_list[1][2])
#deckC_list = [1]*deck_list[2][2]+[0]*(ncard_per_deck-deck_list[2][2])
#deckD_list = [1]*deck_list[3][2]+[0]*(ncard_per_deck-deck_list[3][2])

# gain per card, loss, number of loss cards in a deck(10 cards)
deckA_prop = [100, -250, deckA_list]
deckB_prop = [100, -1250, deckB_list]
deckC_prop = [50, -50, deckC_list]
deckD_prop = [50, -250, deckD_list]

# define deck_list variable
deck_list = [deckA_prop, deckB_prop, deckC_prop, deckD_prop]
random.shuffle(deck_list)

# money setting
money = 2000
net_gain = 0
gain = 0
loss = 0

# choice index
deck_choiceN = [0, 0, 0, 0]

# trial_setting
trial_tot = 0
msg_choice = " "
msg_money = " "
# Set experiment start values for variable component gain_result
gain_result = ''
gain_resultContainer = []
# Set experiment start values for variable component remained_money
remained_money = ''
remained_moneyContainer = []

# Initialize components for Routine "TaskEnd"
TaskEndClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
continueRoutine = True
# update component parameters for each repeat
Intro_resp.keys = []
Intro_resp.rt = []
_Intro_resp_allKeys = []
# keep track of which components have finished
IntroComponents = [Instruction, Intro_resp]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction* updates
    if Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction.frameNStart = frameN  # exact frame index
        Instruction.tStart = t  # local t and not account for scr refresh
        Instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction, 'tStartRefresh')  # time at next scr refresh
        Instruction.setAutoDraw(True)
    
    # *Intro_resp* updates
    waitOnFlip = False
    if Intro_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro_resp.frameNStart = frameN  # exact frame index
        Intro_resp.tStart = t  # local t and not account for scr refresh
        Intro_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro_resp, 'tStartRefresh')  # time at next scr refresh
        Intro_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Intro_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Intro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Intro_resp.status == STARTED and not waitOnFlip:
        theseKeys = Intro_resp.getKeys(keyList=['space'], waitRelease=False)
        _Intro_resp_allKeys.extend(theseKeys)
        if len(_Intro_resp_allKeys):
            Intro_resp.keys = _Intro_resp_allKeys[-1].name  # just the last key pressed
            Intro_resp.rt = _Intro_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruction.started', Instruction.tStartRefresh)
thisExp.addData('Instruction.stopped', Instruction.tStopRefresh)
# check responses
if Intro_resp.keys in ['', [], None]:  # No response was made
    Intro_resp.keys = None
thisExp.addData('Intro_resp.keys',Intro_resp.keys)
if Intro_resp.keys != None:  # we had a response
    thisExp.addData('Intro_resp.rt', Intro_resp.rt)
thisExp.addData('Intro_resp.started', Intro_resp.tStartRefresh)
thisExp.addData('Intro_resp.stopped', Intro_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=50.0, method='random', 
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
    
    # ------Prepare to start Routine "Trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    border.setOpacity(0.7)
    # setup some python lists for storing info about the Trial_click
    Trial_click.x = []
    Trial_click.y = []
    Trial_click.leftButton = []
    Trial_click.midButton = []
    Trial_click.rightButton = []
    Trial_click.time = []
    Trial_click.clicked_name = []
    gotValidClick = False  # until a click is received
    totMoney.setText(msg_money)
    Nchoice.setText(msg_choice)
    # keep track of which components have finished
    TrialComponents = [Trial_Instruction, DeckA, DeckB, DeckC, DeckD, border, Trial_click, totMoney, Nchoice]
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
        
        # *Trial_Instruction* updates
        if Trial_Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_Instruction.frameNStart = frameN  # exact frame index
            Trial_Instruction.tStart = t  # local t and not account for scr refresh
            Trial_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Instruction, 'tStartRefresh')  # time at next scr refresh
            Trial_Instruction.setAutoDraw(True)
        
        # *DeckA* updates
        if DeckA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DeckA.frameNStart = frameN  # exact frame index
            DeckA.tStart = t  # local t and not account for scr refresh
            DeckA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DeckA, 'tStartRefresh')  # time at next scr refresh
            DeckA.setAutoDraw(True)
        
        # *DeckB* updates
        if DeckB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DeckB.frameNStart = frameN  # exact frame index
            DeckB.tStart = t  # local t and not account for scr refresh
            DeckB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DeckB, 'tStartRefresh')  # time at next scr refresh
            DeckB.setAutoDraw(True)
        
        # *DeckC* updates
        if DeckC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DeckC.frameNStart = frameN  # exact frame index
            DeckC.tStart = t  # local t and not account for scr refresh
            DeckC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DeckC, 'tStartRefresh')  # time at next scr refresh
            DeckC.setAutoDraw(True)
        
        # *DeckD* updates
        if DeckD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DeckD.frameNStart = frameN  # exact frame index
            DeckD.tStart = t  # local t and not account for scr refresh
            DeckD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DeckD, 'tStartRefresh')  # time at next scr refresh
            DeckD.setAutoDraw(True)
        
        # *border* updates
        if border.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            border.frameNStart = frameN  # exact frame index
            border.tStart = t  # local t and not account for scr refresh
            border.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(border, 'tStartRefresh')  # time at next scr refresh
            border.setAutoDraw(True)
        if border.status == STARTED:  # only update if drawing
            border.setPos([border_loc, 0])
        # *Trial_click* updates
        if Trial_click.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_click.frameNStart = frameN  # exact frame index
            Trial_click.tStart = t  # local t and not account for scr refresh
            Trial_click.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_click, 'tStartRefresh')  # time at next scr refresh
            Trial_click.status = STARTED
            Trial_click.mouseClock.reset()
            prevButtonState = Trial_click.getPressed()  # if button is down already this ISN'T a new click
        if Trial_click.status == STARTED:  # only update if started and not finished!
            buttons = Trial_click.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [DeckA, DeckB, DeckC, DeckD,]:
                        if obj.contains(Trial_click):
                            gotValidClick = True
                            Trial_click.clicked_name.append(obj.name)
                    x, y = Trial_click.getPos()
                    Trial_click.x.append(x)
                    Trial_click.y.append(y)
                    buttons = Trial_click.getPressed()
                    Trial_click.leftButton.append(buttons[0])
                    Trial_click.midButton.append(buttons[1])
                    Trial_click.rightButton.append(buttons[2])
                    Trial_click.time.append(Trial_click.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        if DeckA.contains(Trial_click):
            border_loc = -0.5
        elif DeckB.contains(Trial_click):
            border_loc = -0.17
        elif DeckC.contains(Trial_click):
            border_loc = 0.16
        elif DeckD.contains(Trial_click):
            border_loc = 0.5
        
        # *totMoney* updates
        if totMoney.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            totMoney.frameNStart = frameN  # exact frame index
            totMoney.tStart = t  # local t and not account for scr refresh
            totMoney.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(totMoney, 'tStartRefresh')  # time at next scr refresh
            totMoney.setAutoDraw(True)
        
        # *Nchoice* updates
        if Nchoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Nchoice.frameNStart = frameN  # exact frame index
            Nchoice.tStart = t  # local t and not account for scr refresh
            Nchoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Nchoice, 'tStartRefresh')  # time at next scr refresh
            Nchoice.setAutoDraw(True)
        
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
    trials.addData('Trial_Instruction.started', Trial_Instruction.tStartRefresh)
    trials.addData('Trial_Instruction.stopped', Trial_Instruction.tStopRefresh)
    trials.addData('DeckA.started', DeckA.tStartRefresh)
    trials.addData('DeckA.stopped', DeckA.tStopRefresh)
    trials.addData('DeckB.started', DeckB.tStartRefresh)
    trials.addData('DeckB.stopped', DeckB.tStopRefresh)
    trials.addData('DeckC.started', DeckC.tStartRefresh)
    trials.addData('DeckC.stopped', DeckC.tStopRefresh)
    trials.addData('DeckD.started', DeckD.tStartRefresh)
    trials.addData('DeckD.stopped', DeckD.tStopRefresh)
    trials.addData('border.started', border.tStartRefresh)
    trials.addData('border.stopped', border.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(Trial_click.x): trials.addData('Trial_click.x', Trial_click.x[0])
    if len(Trial_click.y): trials.addData('Trial_click.y', Trial_click.y[0])
    if len(Trial_click.leftButton): trials.addData('Trial_click.leftButton', Trial_click.leftButton[0])
    if len(Trial_click.midButton): trials.addData('Trial_click.midButton', Trial_click.midButton[0])
    if len(Trial_click.rightButton): trials.addData('Trial_click.rightButton', Trial_click.rightButton[0])
    if len(Trial_click.time): trials.addData('Trial_click.time', Trial_click.time[0])
    if len(Trial_click.clicked_name): trials.addData('Trial_click.clicked_name', Trial_click.clicked_name[0])
    trials.addData('Trial_click.started', Trial_click.tStart)
    trials.addData('Trial_click.stopped', Trial_click.tStop)
    trials.addData('totMoney.started', totMoney.tStartRefresh)
    trials.addData('totMoney.stopped', totMoney.tStopRefresh)
    trials.addData('Nchoice.started', Nchoice.tStartRefresh)
    trials.addData('Nchoice.stopped', Nchoice.tStopRefresh)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    # gain money per card
    if Trial_click.clicked_name[0] == 'DeckA':    
        choice_idx = 0
    elif Trial_click.clicked_name[0] == 'DeckB':
        choice_idx = 1
    elif Trial_click.clicked_name[0] == 'DeckC':
        choice_idx = 2    
    elif Trial_click.clicked_name[0] == 'DeckD':
        choice_idx = 3    
    
    # increase deck choiceN
    deck_choiceN[choice_idx] += 1
    
    # shuffling result of deck choice
    if deck_choiceN[choice_idx] %10 == 1:
        card_list = deck_list[choice_idx][2]
        random.shuffle(card_list)
    
    # gain
    gain = deck_list[choice_idx][0]
    
    # loss
    loss = card_list[(deck_choiceN[choice_idx]-1) % 10]*deck_list[choice_idx][1]
    
    # calculate net gain of "this" trial
    net_gain = gain+loss
    
    # calculate money
    money += net_gain
    
    # calculate number of card choices
    trial_tot = sum(deck_choiceN)
    
    # summary
    msg_money = str(gain)+'\n'+str(loss)+'\n'+str(money)
    msg_choice = str(deck_choiceN[0])+','+str(deck_choiceN[1])+','+str(deck_choiceN[2])+','+str(deck_choiceN[3])+'\n'+str(trial_tot)
    gain_result = net_gain  # Set routine start values for gain_result
    remained_money = money  # Set routine start values for remained_money
    # keep track of which components have finished
    FeedbackComponents = []
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
    thisExp.addData('gain_result.routineEndVal', gain_result)  # Save end routine value
    thisExp.addData('remained_money.routineEndVal', remained_money)  # Save end routine value
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 50.0 repeats of 'trials'


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
