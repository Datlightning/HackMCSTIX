import pyautogui as pg
import time
import os
import facetrack
from PyQt5.QtWidgets import QApplication
import sys
import translator
# mouseInfo = pg.position()
# print(mouseInfo)

#FUNCTIONS returns current mouse position, takes you to particular position, left and right click, keyboard input
# open app, 
pg.FAILSAFE = False
RUNNING_FACEDETECTION = False
def setup():
    global screenHeight, screenWidth, dpi
    screenWidth, screenHeight = pg.size() 
    app = QApplication(sys.argv)
    screen = app.screens()[0]
    dpi = screen.physicalDotsPerInch()
def startFaceTrack():
    RUNNING_FACEDETECTION = True
    facetrack.start()

def pauseFaceTrack():
    RUNNING_FACEDETECTION = False
    facetrack.end()

def moveToFace():
    pg.moveTo(facetrack.getMovement(screenWidth, screenHeight)[0], facetrack.getMovement(screenWidth, screenHeight)[1])
def write(string: str):
    indent: bool = False
    if "\t" in string:
        tabs = string.split("\t")
        indent = True
    elif "\n" in string:
        tabs = string.split("\n")
        indent = False
    else:
        indent = None
    if indent is None:
        pg.write(string, 0.01)
    elif indent is False:
        for s in tabs:
            pg.write(s, 0.01)
            pg.press("enter")
    elif indent is True:
        for s in tabs:
            pg.write(s, 0.01)
            pg.press("tab")
def moveMouse(inch:float):
    global dpi
    dist = inch * dpi
    x,y = pg.position()
    pg.moveTo(x+dist,y)

def copy():
    pg.hotkey("ctrl", "c")
def paste():
    pg.hotkey("ctrl", "v")
def undo():
    pg.hotkey("ctrl", "z")

def gobackhighlight():
    pg.hotkey("ctrl","shift", "left")    
def goforwardhighlight():
    pg.hotkey("ctrl","shift", "right") 
def goback():
    pg.hotkey("ctrl", "left")    
def goforward():
    pg.hotkey("ctrl","right") 
def bold():
    pg.hotkey("ctrl","b")   
def underline():
    pg.hotkey("ctrl","u")   
def ital():
    pg.hotkey("ctrl","i")  
def cut():
    pg.hotkey("ctrl", "x") 
def selectall():
    pg.hotkey("ctrl","a")   
def delete():
    pg.hotkey("ctrl", "delete")
def newtab():
    pg.hotkey("ctrl", "t")
def close():
    pg.hotkey("alt", "f4")
def leftClick():
    pg.click()
def doubleClick():
    pg.doubleClick()
def rightClick():
    pg.rightClick()

def middleClick():
    pg.middleClick()
    
def scroll(amount):
    pg.scroll(amount)
    
def goToPosition(x, y):
    pg.moveTo(x, y, duration = 0.1)

def pressKey(name):
    pg.press(name)
def openApp(name):
    pg.press("win")
    time.sleep(0.5)
    pg.write(name, 0.01)
    pg.press("enter")

def handleinstructions(instructions):
    global RUNNING_FACEDETECTION
    for dict in instructions:
        for key, value in dict.items():
            match key:
                case "click":
                    if value == "double":
                        doubleClick()
                    elif value == "left":
                        leftClick()
                    elif value == "right":
                        rightClick()
                case "write":
                    write(value)
                case "toggle_mouse_movement":
                    if value == "toggle":
                        if RUNNING_FACEDETECTION:
                            pauseFaceTrack()
                        else:
                            startFaceTrack()
                    elif value == "measure":
                        moveMouse(0)
                    RUNNING_FACEDETECTION = not RUNNING_FACEDETECTION
                case "select_command":
                    match value:
                        case "backward":
                            gobackhighlight()
                        case "forward":
                            goforwardhighlight()
                case "command":
                    match value:
                        case "new_tab":
                            newtab()
                        case "copy":
                            copy()
                        case "paste":
                            paste()
                        case "bold":
                            bold()
                        case "italicize":
                            ital()
                        case "underline":
                            underline()
                        case "forward_word":
                            goforward()
                        case "back_word":
                            goback()
                        case "all":
                            selectall()
                        case "undo":
                            undo()
                        case "close":
                            close()
                        case "cut":
                            cut()
                        
                        

def get_instructions(prompt):
        instructions = translator.generateResponse(prompt)
        print(instructions)
        print(instructions[0])
def main():
    setup()
    get_instructions("Move the mouse 3 inches to the right, then open notepad, then type out hello world, then select back.")
if __name__ == "__main__":
    main()