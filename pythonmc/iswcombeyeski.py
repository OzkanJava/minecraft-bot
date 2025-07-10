import pyautogui
import time
import mouse
import keyboard
from os import system
from PIL import Image
from PIL import ImageGrab
import random
chestqueue = 0
craftCount = 0
sleepVal = 0.02
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
    pyautogui.moveRel(0,70*-1*i,duration=0.04)
    pyautogui.moveRel(0,70*-1*i,duration=0.04)
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


def buyOnce(direction):
    pyautogui.keyDown(direction)
    time.sleep(0.05)
    mouse.right_click()
    time.sleep(0.05)
    mouse.right_click()
    pyautogui.keyUp(direction)
    if checkIsInventoryFull() == True:
        envDolu()


def tur():
    global craftCount
    craftCount = 0
    # Pozisyon alış
    pyautogui.write("t  /is w combey   ", interval=sleepVal)
    pyautogui.press("enter")

    time.sleep(2)

    pyautogui.moveRel(0,-100,duration= sleepVal)
    pyautogui.moveRel(0,-100,duration= sleepVal)
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("w")
    time.sleep(2)  # i 0 a bölnüyorsa sola git
    pyautogui.keyUp("w")
    pyautogui.keyUp("ctrl")
    pyautogui.moveRel(0,200,duration= sleepVal)
    time.sleep(0.03)
    pyautogui.moveRel(0,200,duration= sleepVal)
    time.sleep(0.03)
    pyautogui.moveRel(0,60,duration= sleepVal)
    time.sleep(0.03)


    keyboard.press("shift")
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    keyboard.release("shift")
    if (chestqueue % 2) == 0 :
        for i in range(10):
                buyOnce('a')
        while True:
            for i in range(19):
                buyOnce('d')
            for i in range(19):
                buyOnce('a')
    else:
        for i in range(10):
            buyOnce('d')
        while True:
            for i in range(19):
                buyOnce('a')
            for i in range(19):
                buyOnce('d')

    

     
    
       


def main():
    tur()


if __name__ == "__main__":
    main()
