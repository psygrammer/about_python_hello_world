import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color='white', units='pix', size=[1000,1000], allowGUI=False, fullscr=False)#creates a window
myClock = core.Clock() #this creates and starts a clock which we can later read
    
core.wait(2)

myWin.close() #closes the window
core.quit() #quits