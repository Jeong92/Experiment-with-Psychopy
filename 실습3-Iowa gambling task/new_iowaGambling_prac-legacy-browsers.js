/****************************** 
 * New_Iowagambling_Prac Test *
 ******************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'new_iowaGambling_prac';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'

function sum(arr) {
   var num = 0;
   for (var i = 0; i < arr.length; i++) {
       num += (typeof arr[i] == 'number') ? arr[i] : 0;
   }
   return num;
};
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(IntroRoutineBegin());
flowScheduler.add(IntroRoutineEachFrame());
flowScheduler.add(IntroRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(TaskEndRoutineBegin());
flowScheduler.add(TaskEndRoutineEachFrame());
flowScheduler.add(TaskEndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'images/Card.jpg', 'path': 'images/Card.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var IntroClock;
var Instruction;
var Intro_resp;
var TrialClock;
var Trial_Instruction;
var DeckA;
var DeckB;
var DeckC;
var DeckD;
var border;
var Trial_click;
var border_loc;
var totMoney;
var Nchoice;
var FeedbackClock;
var deckA_list;
var deckB_list;
var deckC_list;
var deckD_list;
var deckA_prop;
var deckB_prop;
var deckC_prop;
var deckD_prop;
var deck_list;
var money;
var net_gain;
var gain;
var loss;
var deck_choiceN;
var trial_tot;
var msg_choice;
var msg_money;
var TaskEndClock;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Intro"
  IntroClock = new util.Clock();
  Instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruction',
    text: '검사가 시작하게 되면 4개의 카드 덱 중 하나를 선택해주세요. 각 덱을 선택할때마다 일정한 금전적 이득과 손실이 발생할 수 있습니다. 이득을 최대화하는 카드 덱을 선택해주세요. 검사를 시작하려면 스페이스바를 눌러주세요.',
    font: 'NanumSquare',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  Intro_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trial"
  TrialClock = new util.Clock();
  Trial_Instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'Trial_Instruction',
    text: '카드를 선택해주세요.',
    font: 'NanumSquare',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  DeckA = new visual.ImageStim({
    win : psychoJS.window,
    name : 'DeckA', units : undefined, 
    image : 'images/Card.jpg', mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0], size : [0.25, (0.25 * 1.45)],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  DeckB = new visual.ImageStim({
    win : psychoJS.window,
    name : 'DeckB', units : undefined, 
    image : 'images/Card.jpg', mask : undefined,
    ori : 0.0, pos : [(- 0.17), 0], size : [0.25, (0.25 * 1.45)],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  DeckC = new visual.ImageStim({
    win : psychoJS.window,
    name : 'DeckC', units : undefined, 
    image : 'images/Card.jpg', mask : undefined,
    ori : 0.0, pos : [0.16, 0], size : [0.25, (0.25 * 1.45)],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  DeckD = new visual.ImageStim({
    win : psychoJS.window,
    name : 'DeckD', units : undefined, 
    image : 'images/Card.jpg', mask : undefined,
    ori : 0.0, pos : [0.5, 0], size : [0.25, (0.25 * 1.45)],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  border = new visual.Rect ({
    win: psychoJS.window, name: 'border', 
    width: [0.26, (0.26 * 1.45)][0], height: [0.26, (0.26 * 1.45)][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('blue'),
    fillColor: new util.Color(undefined),
    opacity: 1.0, depth: -5, interpolate: true,
  });
  
  Trial_click = new core.Mouse({
    win: psychoJS.window,
  });
  Trial_click.mouseClock = new util.Clock();
  border_loc = 0;
  
  totMoney = new visual.TextStim({
    win: psychoJS.window,
    name: 'totMoney',
    text: '',
    font: 'NanumSquare',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  Nchoice = new visual.TextStim({
    win: psychoJS.window,
    name: 'Nchoice',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  deckA_list = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0];
  deckB_list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  deckC_list = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0];
  deckD_list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  deckA_prop = [100, (- 250), deckA_list];
  deckB_prop = [100, (- 1250), deckB_list];
  deckC_prop = [50, (- 50), deckC_list];
  deckD_prop = [50, (- 250), deckD_list];
  deck_list = [deckA_prop, deckB_prop, deckC_prop, deckD_prop];
  util.shuffle(deck_list);
  money = 2000;
  net_gain = 0;
  gain = 0;
  loss = 0;
  deck_choiceN = [0, 0, 0, 0];
  trial_tot = 0;
  msg_choice = " ";
  msg_money = " ";
  
  // Initialize components for Routine "TaskEnd"
  TaskEndClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _Intro_resp_allKeys;
var IntroComponents;
function IntroRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Intro'-------
    t = 0;
    IntroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Intro_resp.keys = undefined;
    Intro_resp.rt = undefined;
    _Intro_resp_allKeys = [];
    // keep track of which components have finished
    IntroComponents = [];
    IntroComponents.push(Instruction);
    IntroComponents.push(Intro_resp);
    
    IntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function IntroRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Intro'-------
    // get current time
    t = IntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruction* updates
    if (t >= 0.0 && Instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruction.tStart = t;  // (not accounting for frame time here)
      Instruction.frameNStart = frameN;  // exact frame index
      
      Instruction.setAutoDraw(true);
    }

    
    // *Intro_resp* updates
    if (t >= 0.0 && Intro_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Intro_resp.tStart = t;  // (not accounting for frame time here)
      Intro_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Intro_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Intro_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Intro_resp.clearEvents(); });
    }

    if (Intro_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Intro_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Intro_resp_allKeys = _Intro_resp_allKeys.concat(theseKeys);
      if (_Intro_resp_allKeys.length > 0) {
        Intro_resp.keys = _Intro_resp_allKeys[_Intro_resp_allKeys.length - 1].name;  // just the last key pressed
        Intro_resp.rt = _Intro_resp_allKeys[_Intro_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    IntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function IntroRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Intro'-------
    IntroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Intro_resp.keys', Intro_resp.keys);
    if (typeof Intro_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Intro_resp.rt', Intro_resp.rt);
        routineTimer.reset();
        }
    
    Intro_resp.stop();
    // the Routine "Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 50, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(TrialRoutineBegin(snapshot));
    trialsLoopScheduler.add(TrialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(TrialRoutineEnd(snapshot));
    trialsLoopScheduler.add(FeedbackRoutineBegin(snapshot));
    trialsLoopScheduler.add(FeedbackRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(FeedbackRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var gotValidClick;
var TrialComponents;
function TrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Trial'-------
    t = 0;
    TrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    border.setOpacity(0.7);
    // setup some python lists for storing info about the Trial_click
    // current position of the mouse:
    Trial_click.x = [];
    Trial_click.y = [];
    Trial_click.leftButton = [];
    Trial_click.midButton = [];
    Trial_click.rightButton = [];
    Trial_click.time = [];
    Trial_click.clicked_name = [];
    gotValidClick = false; // until a click is received
    totMoney.setText(msg_money);
    Nchoice.setText(msg_choice);
    // keep track of which components have finished
    TrialComponents = [];
    TrialComponents.push(Trial_Instruction);
    TrialComponents.push(DeckA);
    TrialComponents.push(DeckB);
    TrialComponents.push(DeckC);
    TrialComponents.push(DeckD);
    TrialComponents.push(border);
    TrialComponents.push(Trial_click);
    TrialComponents.push(totMoney);
    TrialComponents.push(Nchoice);
    
    TrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function TrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Trial'-------
    // get current time
    t = TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Trial_Instruction* updates
    if (t >= 0.0 && Trial_Instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Trial_Instruction.tStart = t;  // (not accounting for frame time here)
      Trial_Instruction.frameNStart = frameN;  // exact frame index
      
      Trial_Instruction.setAutoDraw(true);
    }

    
    // *DeckA* updates
    if (t >= 0.0 && DeckA.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      DeckA.tStart = t;  // (not accounting for frame time here)
      DeckA.frameNStart = frameN;  // exact frame index
      
      DeckA.setAutoDraw(true);
    }

    
    // *DeckB* updates
    if (t >= 0.0 && DeckB.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      DeckB.tStart = t;  // (not accounting for frame time here)
      DeckB.frameNStart = frameN;  // exact frame index
      
      DeckB.setAutoDraw(true);
    }

    
    // *DeckC* updates
    if (t >= 0.0 && DeckC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      DeckC.tStart = t;  // (not accounting for frame time here)
      DeckC.frameNStart = frameN;  // exact frame index
      
      DeckC.setAutoDraw(true);
    }

    
    // *DeckD* updates
    if (t >= 0.0 && DeckD.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      DeckD.tStart = t;  // (not accounting for frame time here)
      DeckD.frameNStart = frameN;  // exact frame index
      
      DeckD.setAutoDraw(true);
    }

    
    // *border* updates
    if (t >= 0.0 && border.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      border.tStart = t;  // (not accounting for frame time here)
      border.frameNStart = frameN;  // exact frame index
      
      border.setAutoDraw(true);
    }

    
    if (border.status === PsychoJS.Status.STARTED){ // only update if being drawn
      border.setPos([border_loc, 0], false);
    }
    // *Trial_click* updates
    if (t >= 0.0 && Trial_click.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Trial_click.tStart = t;  // (not accounting for frame time here)
      Trial_click.frameNStart = frameN;  // exact frame index
      
      Trial_click.status = PsychoJS.Status.STARTED;
      Trial_click.mouseClock.reset();
      prevButtonState = Trial_click.getPressed();  // if button is down already this ISN'T a new click
      }
    if (Trial_click.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = Trial_click.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = Trial_click.getPos();
          Trial_click.x.push(_mouseXYs[0]);
          Trial_click.y.push(_mouseXYs[1]);
          Trial_click.leftButton.push(_mouseButtons[0]);
          Trial_click.midButton.push(_mouseButtons[1]);
          Trial_click.rightButton.push(_mouseButtons[2]);
          Trial_click.time.push(Trial_click.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [DeckA, DeckB, DeckC, DeckD,]) {
            if (obj.contains(Trial_click)) {
              gotValidClick = true;
              Trial_click.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    if (DeckA.contains(Trial_click)) {
        border_loc = (- 0.5);
    } else {
        if (DeckB.contains(Trial_click)) {
            border_loc = (- 0.17);
        } else {
            if (DeckC.contains(Trial_click)) {
                border_loc = 0.16;
            } else {
                if (DeckD.contains(Trial_click)) {
                    border_loc = 0.5;
                }
            }
        }
    }
    
    
    // *totMoney* updates
    if (t >= 0.0 && totMoney.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      totMoney.tStart = t;  // (not accounting for frame time here)
      totMoney.frameNStart = frameN;  // exact frame index
      
      totMoney.setAutoDraw(true);
    }

    
    // *Nchoice* updates
    if (t >= 0.0 && Nchoice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Nchoice.tStart = t;  // (not accounting for frame time here)
      Nchoice.frameNStart = frameN;  // exact frame index
      
      Nchoice.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Trial'-------
    TrialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    if (Trial_click.x) {  psychoJS.experiment.addData('Trial_click.x', Trial_click.x[0])};
    if (Trial_click.y) {  psychoJS.experiment.addData('Trial_click.y', Trial_click.y[0])};
    if (Trial_click.leftButton) {  psychoJS.experiment.addData('Trial_click.leftButton', Trial_click.leftButton[0])};
    if (Trial_click.midButton) {  psychoJS.experiment.addData('Trial_click.midButton', Trial_click.midButton[0])};
    if (Trial_click.rightButton) {  psychoJS.experiment.addData('Trial_click.rightButton', Trial_click.rightButton[0])};
    if (Trial_click.time) {  psychoJS.experiment.addData('Trial_click.time', Trial_click.time[0])};
    if (Trial_click.clicked_name) {  psychoJS.experiment.addData('Trial_click.clicked_name', Trial_click.clicked_name[0])};
    
    // the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var choice_idx;
var card_list;
var FeedbackComponents;
function FeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Feedback'-------
    t = 0;
    FeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((Trial_click.clicked_name[0] === "DeckA")) {
        choice_idx = 0;
    } else {
        if ((Trial_click.clicked_name[0] === "DeckB")) {
            choice_idx = 1;
        } else {
            if ((Trial_click.clicked_name[0] === "DeckC")) {
                choice_idx = 2;
            } else {
                if ((Trial_click.clicked_name[0] === "DeckD")) {
                    choice_idx = 3;
                }
            }
        }
    }
    deck_choiceN[choice_idx] += 1;
    if (((deck_choiceN[choice_idx] % 10) === 1)) {
        card_list = deck_list[choice_idx][2];
        util.shuffle(card_list);
    }
    gain = deck_list[choice_idx][0];
    loss = (card_list[((deck_choiceN[choice_idx] - 1) % 10)] * deck_list[choice_idx][1]);
    net_gain = (gain + loss);
    money += net_gain;
    trial_tot = sum(deck_choiceN);
    msg_money = ((((gain.toString() + "\n") + loss.toString()) + "\n") + money.toString());
    msg_choice = ((((((((deck_choiceN[0].toString() + ",") + deck_choiceN[1].toString()) + ",") + deck_choiceN[2].toString()) + ",") + deck_choiceN[3].toString()) + "\n") + trial_tot.toString());
    
    // keep track of which components have finished
    FeedbackComponents = [];
    
    FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function FeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Feedback'-------
    // get current time
    t = FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Feedback'-------
    FeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var TaskEndComponents;
function TaskEndRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TaskEnd'-------
    t = 0;
    TaskEndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    TaskEndComponents = [];
    
    TaskEndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TaskEndRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TaskEnd'-------
    // get current time
    t = TaskEndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TaskEndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TaskEndRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TaskEnd'-------
    TaskEndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "TaskEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
