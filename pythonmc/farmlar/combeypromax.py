import pyautogui
import time
import mouse
import keyboard
from os import system
from PIL import Image
from PIL import ImageGrab
import random
def chestSec(i):
 
    time.sleep(0.03)

    if(i%7 == 0):
        pass
    elif(i%7 == 1):
        pass
    elif(i%7 == 2):
        pass
    elif(i%7 == 3):
        pass
    elif(i%7 == 4):
        pass
    elif(i%7 == 5):
        pass
    elif(i%7 == 6):
        pass
    time.sleep(0.03)
    
def spawnGitEnvBosalt():
    pyautogui.write('t  /is spawn ',interval =sleepVal)
    pyautogui.press('enter')
    time.sleep(5)

    

    

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
    """
    pyautogui.moveRel(0,300*-1*i,duration=0.04)
    pyautogui.moveRel(0,300*-1*i,duration=0.04)
    """
def craft(k):
    for i in range(k):
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


def checkCraftinIsOpen():
    screenshot = ImageGrab.grab()
    x = 1274
    y = 463

    pixel = screenshot.getpixel((x, y))
    return pixel == (198, 198, 198)

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
    
    time.sleep(sleepVal)

def envanterKapa():
    time.sleep(0.01)
    pyautogui.press("e")
    time.sleep(0.01)
def envDolu():
    global craftCount
    print(craftCount)
    global isCraftDone
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
            pass
        time.sleep(0.5)

    if(craftCount < 2):
        craft(3)
        fixironblock((craftCount) * 3, (craftCount) * 3 + 3)
        envanterKapa()
        lookUp(1)
        craftCount += 1
    elif(craftCount == 2):
        craft(3)
        fixironblock((craftCount) * 3, (craftCount) * 3 + 3)
        
        satircraft(3)
        
        envanterKapa()
        lookUp(1)
        craftCount += 1
    elif(craftCount < 5):
        craft(3)
        fixironblock((craftCount-2) * 3, (craftCount-2) * 3 +3)
        envanterKapa()
        lookUp(1)
        craftCount += 1
    elif(craftCount == 5):
        craft(3)
        fixironblock(0,3)
        satircraft(3)
        fixgoldblock(1,4)
        envanterKapa()
        lookUp(1)
        craftCount += 1
    elif(craftCount < 8):
        craft(3)
        fixironblock((craftCount-5) * 3, (craftCount-5) * 3 +3)
        envanterKapa()
        lookUp(1)
        craftCount += 1
    elif(craftCount == 8):
        craft(3)
        fixironblock(0,3)
        satircraft(3)
        fixgoldblock(1,4)
        envanterKapa()
        lookUp(1)
        craftCount += 1
    elif(craftCount < 11):
        craft(3)
        fixironblock((craftCount-8) * 3, (craftCount-8) * 3 +3)
        envanterKapa()
        lookUp(1)
        craftCount += 1
    elif(craftCount == 11):
        craft(3)
        fixironblock(0,3)
        satircraft(3)
        fixgoldblock(1,4)
        envanterKapa()
        craftCount += 1
        print("tur tamamlanjdi")
        isCraftDone = True
    
    
        
        




        




def checkIsInventoryFull():
    screenshot = ImageGrab.grab()
    x = 1451
    y = 975
    pixel = screenshot.getpixel((x, y))
    return pixel == (255, 85, 85)


def buyOnce(direction):
    pyautogui.keyDown(direction)
    pyautogui.click(button="right", clicks=5, duration=0.1)
    pyautogui.keyUp(direction)



def checkIsBigChestOpened():
    screenshot = ImageGrab.grab()
    x,y = 1217,396
    pixel = screenshot.getpixel((x, y))
    return pixel == (198,198,198)

sleepVal = 0.03


for i in range(1,999):
    isCraftDone = False
    craftCount = 0
    print("tur"+str(i))
    pyautogui.write("t  /is w combey   ", interval=sleepVal)
    pyautogui.press("enter")

    time.sleep(2)

    pyautogui.moveRel(0,-100,duration= sleepVal)
    pyautogui.moveRel(0,-100,duration= sleepVal)
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("w")
    time.sleep(4)  # i 0 a bölnüyorsa sola gitt  /s w combey   
    
    pyautogui.keyUp("w")
    pyautogui.keyUp("ctrl")
    keyboard.press("shift")
    pyautogui.keyDown("s")
    time.sleep(0.3)
    pyautogui.keyUp("s")
    keyboard.release("shift")

    

    pyautogui.moveRel(0,200,duration= sleepVal)
    time.sleep(0.03)
    pyautogui.moveRel(0,130,duration= sleepVal)
    time.sleep(0.03)
    if(i % 2 == 0):
        for _ in range(9):
            if isCraftDone == True:
                break
            buyOnce('d')
            if checkIsInventoryFull() == True:
                envDolu()
    else:
        for _ in range(9):
            if isCraftDone == True:
                break
            buyOnce('a')
            if checkIsInventoryFull() == True:
                envDolu()
        for _ in range(18):
            if isCraftDone == True:
                break
            buyOnce('d')
            if checkIsInventoryFull() == True:
                envDolu()
        
    while True:
        if isCraftDone == True:
            break
        for _ in range(18):
            if isCraftDone == True:
                break
            buyOnce('a')
            if checkIsInventoryFull() == True:
                envDolu()
        if isCraftDone == True:
                break
        for _ in range(18):
            if isCraftDone == True:
                break
            buyOnce('d')
            if checkIsInventoryFull() == True:
                envDolu()
        if isCraftDone == True:
                break

    spawnGitEnvBosalt()
    chestSec(i)
    time.sleep(1)
    mouse.right_click()
    for a in range(30):
        if checkIsBigChestOpened() == True:
            print("bigchesthasopened")
            break
        if a == 10 or a == 20:
            mouse.right_click()
        if a == 29:
            pass
        time.sleep(0.75)



    envanterBosalt(0)



    


    


                    









     
    
       

