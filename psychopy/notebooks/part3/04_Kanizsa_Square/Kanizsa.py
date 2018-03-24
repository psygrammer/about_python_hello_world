import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color='white', units='pix', size=[1000,1000], allowGUI=False, fullscr=False)#creates a window
myClock = core.Clock() #this creates and starts a clock which we can later read

#these lines are very powerful, they create all stimuli using psychopy
disk = visual.Circle(myWin, radius=80, fillColor='black', lineColor=None)
line =visual.Rect(myWin, width=2, height=400, fillColor='black', lineColor=None)
square =visual.Rect(myWin, width=200, height=200, fillColor='white', lineColor=None)

myScale = visual.RatingScale(myWin, pos=[0, -280], low=10, high=100,  textSize=0.5, lineColor='black',  tickHeight=False, scale=None, showAccept=False, singleClick=True)
information=visual.TextStim(myWin, pos=[0,-325], text='', height=18, color='black') 

finished = False
while not finished:
    
    disk.setPos([-100,-100])
    disk.draw()
    disk.setPos([-100,100])
    disk.draw()
    disk.setPos([100,100])
    disk.draw()
    disk.setPos([100,-100])
    disk.draw()

    line.draw()
    square.draw()
    information.draw()
    myScale.draw()
    myWin.flip()
    
    if myScale.noResponse ==False: #some new value has been selected with the mouse
        radius = myScale.getRating()
        disk.setRadius(radius)
        information.setText(str(radius))
        myScale.reset()

    if event.getKeys(keyList=['escape']): #pressing ESC quits the program
        finished =True
    
myWin.close() #closes the window
core.quit() #quits





