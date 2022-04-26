from __future__ import absolute_import, division, print_function
from psychopy import visual, core
from psychopy.hardware import keyboard

win = visual.Window(units="height")

kb = keyboard.Keyboard()

def wait_for_scanner(trigger='5'):
    kb.waitKeys(keyList=trigger)
    
def fixation():
    fix = visual.TextStim(win, 
    text=u"+",
    pos=(0, 0)) 
    
    fix.draw()
    win.flip()
    
def pulse_message(lag=1):
    pulse = visual.TextStim(win, 
    text=u"PULSE RECEIVED",
    pos=(0, 0)) 
    
    pulse.draw()
    win.flip()
    core.wait(lag)
    
def run():
    keys = kb.getKeys()
    while 'escape' not in keys:
        keys = kb.getKeys()
        fixation()
        wait_for_scanner()
        pulse_message()
    win.close()
        
run()
