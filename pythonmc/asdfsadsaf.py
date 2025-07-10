import pyautogui
import time
import mouse
import keyboard
from os import system
from PIL import Image
from PIL import ImageGrab
import random
import os

def satircraft(i):
    durationVal = 0.06
    for j in range(9):
        currentMouseX = 1294 + j * 36.125
        currentMouseY = 553 + i * 35.5
        mouse.move(int(currentMouseX), int(currentMouseY), duration=durationVal)
        time.sleep(0.01)
        mouse.click()
        if j <= 2:
            craftingX = 1338 + (j % 3) * 36.5
            craftingY = 419
        elif j <= 5:
            craftingX = 1338 + (j % 3) * 36.5
            craftingY = 455
        elif j <= 8:
            craftingX = 1338 + (j % 3) * 36.5
            craftingY = 491

        mouse.move(int(craftingX), int(craftingY), duration=durationVal)
        time.sleep(0.01)
        mouse.click()
    
    mouse.move(1528, 456, duration=durationVal)
    time.sleep(0.3)
    keyboard.press("shift")
    time.sleep(0.11)
    mouse.click()
    time.sleep(0.11)

    keyboard.release("shift")
def chestSec():
    global chestqueue
    chestqueue += 1
    
    i = chestqueue
    if(i%7 == 0):
        pyautogui.moveRel(180,0,duration=0.04)
    elif(i%7 == 1):
        pyautogui.moveRel(180,0,duration=0.04)
        pyautogui.moveRel(180,0,duration=0.04)
    elif(i%7 == 2):
        pyautogui.moveRel(180,0,duration=0.04)
        pyautogui.moveRel(180,0,duration=0.04)
        pyautogui.moveRel(50,0,duration=0.04)
    elif(i%7 == 3):
        pyautogui.moveRel(-180,0,duration=0.04)
    elif(i%7 == 4):
        pyautogui.moveRel(-180,0,duration=0.04)
        pyautogui.moveRel(-180,0,duration=0.04)
    elif(i%7 == 5):
        pyautogui.moveRel(-180,0,duration=0.04)
        pyautogui.moveRel(-180,0,duration=0.04)
        pyautogui.moveRel(-50,0,duration=0.04)
    elif(i%7 == 6):
        pass
def spawnGitEnvBosalt():
    pyautogui.write('t  /is spawn ',interval =sleepVal)
    pyautogui.press('enter')
    time.sleep(2)

    chestSec()

    envanterBosalt(1)

def envanterBosalt(a):
    mouse.right_click()
    time.sleep(1)
    mouse.move(1584,756-a*36)                         #mouse.move(1584,756) büyük sandık
    time.sleep(0.05)                          #time.sleep(0.05)
    pyautogui.click()                            #mouse.click()
    pyautogui.moveTo(1584-72,756-a*36)                           #mouse.move(1584-72,756)
    pyautogui.keyDown('shift')                           #keyboard.press('shift')                           #
    time.sleep(0.1)                           #time.sleep(0.1)
    pyautogui.click(clicks=2)                           #mouse.double_click()
    pyautogui.keyUp('shift')                           # keyboard.release('shift')
    time.sleep(0.1)                           #time.sleep(0.1)
    pyautogui.click()                           #mouse.click()
    pyautogui.keyDown('shift')                           #keyboard.press('shift')
    time.sleep(0.1)                           #time.sleep(0.1)
    pyautogui.click()                            #mouse.click()
    pyautogui.keyUp('shift')                             #keyboard.release('shift')
    pyautogui.press('e')  
def lookUp(i):
    pyautogui.moveRel(0,130*-1*i,duration=0.04)
    pyautogui.moveRel(0,130*-1*i,duration=0.04)
def craft():
    for i in range(3):
        for j in range(9):
            currentMouseX = 1294 + j * 36.125
            currentMouseY = 553 + i * 35.5
            mouse.move(int(currentMouseX), int(currentMouseY), duration=sleepVal)
            mouse.click()
            if j <= 2:
                craftingX = 1338 + (j % 3) * 36.5
                craftingY = 419
            elif j <= 5:
                craftingX = 1338 + (j % 3) * 36.5
                craftingY = 455
            elif j <= 8:
                craftingX = 1338 + (j % 3) * 36.5
                craftingY = 491

            mouse.move(int(craftingX), int(craftingY), duration=sleepVal)
            mouse.click()

        mouse.move(1528, 456, duration=sleepVal)
        time.sleep(0.11)
        keyboard.press("shift")
        time.sleep(0.11)
        mouse.click()
        time.sleep(0.11)

        keyboard.release("shift")


def checkCraftinIsOpen():
    screenshot = ImageGrab.grab()
    x = 1274
    y = 463

    pixel = screenshot.getpixel((x, y))
    return pixel == (198, 198, 198)



def fixironblock(ilkdeger, sondeger):
    space = 36
    fixX = 1583
    fixY = 664
    for i in range(ilkdeger, sondeger):
        mouse.move(fixX - i * space, fixY, duration=sleepVal)
        mouse.click()
        mouse.move(fixX, fixY - ((i % 3) + 1) * space, duration=sleepVal)
        mouse.click()
        mouse.move(fixX - i * space, fixY, duration=sleepVal)
        mouse.click()
        
def fixgoldblock(ilkdeger,sondeger):
    space = 36
    fixX = 1583
    fixY = 664
    sabit = 1
    for i in range(ilkdeger, sondeger):
        mouse.move(fixX, fixY - (sabit) * space, duration=sleepVal)
        mouse.click()
        mouse.move(fixX - i * space, fixY, duration=sleepVal)
        mouse.click()
        sabit+=1
        
        


def envDolu():
    global craftCount
    print(craftCount)
    time.sleep(sleepVal)
    lookUp(-1)
    time.sleep(0.5)
    mouse.right_click()
    for a in range(30):
        if checkCraftinIsOpen() == True:
            break
        if a == 10 or a == 20:
            mouse.right_click()
        if a == 29:
            spawnGitEnvBosalt(i)
            main()
        time.sleep(0.5)

    craft()
    craftCount += 1
    if(craftCount == 4):
        time.sleep(0.5)
                        
        keyboard.press('esc')

        keyboard.release('esc')
        time.sleep(1)
        spawnGitEnvBosalt()
        tur()


    fixironblock((craftCount-1) * 3, (craftCount-1) * 3 + 3)

    time.sleep(0.5)
    pyautogui.press("e")
    time.sleep(1)
    lookUp(1)
    time.sleep(1)


def checkIsInventoryFull():
    screenshot = ImageGrab.grab()
    x = 1451
    y = 975
    pixel = screenshot.getpixel((x, y))
    return pixel == (255, 85, 85)




def satircraft(i):
    for j in range(9):
        currentMouseX = 1294 + j * 36.125
        currentMouseY = 553 + i * 35.5
        mouse.move(int(currentMouseX), int(currentMouseY), duration=sleepVal)
        mouse.click()
        if j <= 2:
            craftingX = 1338 + (j % 3) * 36.5
            craftingY = 419
        elif j <= 5:
            craftingX = 1338 + (j % 3) * 36.5
            craftingY = 455
        elif j <= 8:
            craftingX = 1338 + (j % 3) * 36.5
            craftingY = 491

        mouse.move(int(craftingX), int(craftingY), duration=sleepVal)
        mouse.click()
    
    mouse.move(1528, 456, duration=sleepVal)
    time.sleep(0.11)
    keyboard.press("shift")
    time.sleep(0.11)
    mouse.click()
    time.sleep(0.11)

    keyboard.release("shift")
sleepVal = 0.02

def buyOnce(direction):
    keyboard.press(direction)
    for _ in range(4):
        mouse.right_click()
        time.sleep(0.05)
    keyboard.release(direction)
    
def checkinhub():
    return pyautogui.pixelMatchesColor(1717, 456, (236, 89, 51))
    """
    screenshot = ImageGrab.grab()
    x = 1720
    y = 454

    pixel = screenshot.getpixel((x, y))
    return pixel == (236, 89, 51)
    """
"""
keyboard.press("shift")
pyautogui.keyDown("s")
time.sleep(0.6)
pyautogui.keyUp("s")
keyboard.release("shift")

keyboard.press("ctrl")
pyautogui.keyDown("a")

pyautogui.keyUp("a")
keyboard.release("ctrl")

"""
"""
keyboard.press('a')

for _ in range(8):
    
    mouse.right_click()
    time.sleep(0.05)
    
keyboard.release('a')
"""
def checkIsGoldBlock():

    screenshot = ImageGrab.grab()
    x = 1511
    y = 748

    pixel = screenshot.getpixel((x, y))
    return pixel == (255,216,62) 

"""
pyautogui.moveRel(300,0,duration=0.04)
pyautogui.moveRel(300,0,duration=0.04)
"""
os.system("C://Users//ozkan//Desktop//CraftRise.exe")


    



