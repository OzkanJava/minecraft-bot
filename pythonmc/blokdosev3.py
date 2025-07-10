import pyautogui
import time
import mouse
import keyboard
from os import system
from PIL import Image
from PIL import ImageGrab
import random


def arkaDon(a):
    for i in range(a+1):
        pyautogui.moveRel(300,0,duration=0.04)
        pyautogui.moveRel(300,0,duration=0.04)

    
    
def envToggle():
    keyboard.press("e")
    keyboard.release("e")
    
def dosemece(a,b): # 0. tur da ilk ogeyi alır
    for i in range(a,b):
        keyboard.press_and_release(str(i%9 +1))
        time.sleep(0.5)
        keyboard.press("shift")
        keyboard.press("s")
        time.sleep(1)
        keyboard.release("s")

        keyboard.release("shift")

        time.sleep(4)

        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")

        time.sleep(0.5)
        pyautogui.keyDown("space")

        for _ in range(300):
            mouse.right_click()
            time.sleep(0.05)
        pyautogui.keyUp("space")
        
        
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        time.sleep(1)      

def asagiYukari():
    for j in range(9):
        start_x = 1293
        start_y = 551 
        step = 36
        
        mouse.move(start_x+j*step,start_y)
        time.sleep(0.10)
        
        keyboard.press_and_release(str(j%9 +1))
        time.sleep(0.10)
        
def envTemizle():
    pyautogui.keyDown("shift")
    for j in range(9):
        start_x = 1293
        start_y = 551
        step = 36
        
        mouse.move(start_x+j*step,start_y)
        time.sleep(0.10)
        mouse.click()
        
        time.sleep(0.10)
    
    
    for j in range(9):
        start_x = 1293
        start_y = 551 + 36*3
        step = 36
        
        mouse.move(start_x+j*step,start_y)
        time.sleep(0.10)
        mouse.click()
        
        time.sleep(0.10)
    
    mouse.move(1294,552)
    time.sleep(0.10)
    keyboard.press_and_release("9")
    
    time.sleep(0.10)
    pyautogui.keyUp("shift")
    
    envToggle()
    time.sleep(0.5)
    pyautogui.write("t   /tuccar stokekle hepsi ", interval=0.02)
    pyautogui.press("enter")
def checkWarp():
    screenshot = ImageGrab.grab()
    x1 = 1505
    y1 = 535
    
    x2 = 1543
    y2 = 534

    pixel1 = screenshot.getpixel((x1, y1))
    pixel2 = screenshot.getpixel((x2, y2))
    return pixel1 == (126,102,63) or pixel2 == (126,102,63) or pixel1 == (85,69,43) or pixel2 == (85,69,43)       

def blokCinsindenYolAl(i):
    keyboard.press("shift")
    keyboard.press("s")
    time.sleep(i*0.75)
    keyboard.release("s")
    keyboard.release("shift")

def tuccarGit():
    pyautogui.write("t   /warp  ", interval=0.02)
    pyautogui.press("enter")
    time.sleep(2)
    mouse.move(1404,556,duration=0.02)
    mouse.click()
    time.sleep(1)
    
def stoktanDemirAl():
    waitTime= 0.25
    mouse.right_click()
    time.sleep(waitTime*2)
    mouse.move(1581,528)
    time.sleep(waitTime)
    mouse.click()
    time.sleep(waitTime)
    mouse.move(1266,339)
    time.sleep(waitTime)
    mouse.click()
    time.sleep(waitTime*3)
    pyautogui.write("2286", interval=0.03)
    time.sleep(waitTime*2)
    
    mouse.move(1294,566)
    time.sleep(waitTime)
    mouse.click()
    time.sleep(waitTime)
    
    time.sleep(waitTime*2)
    pyautogui.press("esc") 
print(time.localtime()[3], ":",time.localtime()[4])
for i in range(20):
    pyautogui.write("t   /is w fow ", interval=0.02)
    pyautogui.press("enter")
    
    for a in range(30):
        if checkWarp() == True:
            print("warpaulasildi")
            break
        if a == 15:
            pyautogui.write("t         /is w fow   ", interval=0.02)
            pyautogui.press("enter")
          
        time.sleep(0.75)
    pyautogui.write("t   /fly ", interval=0.02)
    pyautogui.press("enter")
    pyautogui.moveRel(0,300,duration=0.04)

    pyautogui.moveRel(0,300,duration=0.04)

    pyautogui.moveRel(0,-60,duration=0.04)    
    arkaDon(1)
    
    blokCinsindenYolAl(i+3)
    keyboard.press("shift")
    keyboard.press("w")
    time.sleep(0.25)
    keyboard.release("w")
    keyboard.release("shift")
    
    
    dosemece(0,1)
    
    arkaDon(0)
    
    dosemece(1,9)
    
    envToggle()
    time.sleep(1)
    asagiYukari()
    envToggle()
    time.sleep(1)
    dosemece(0,9)   
    time.sleep(0.25)
    
    envToggle()
    
    envTemizle()
    
    time.sleep(0.25)
    
    tuccarGit()
    time.sleep(5)
    
    keyboard.press("w")
    time.sleep(1)
    keyboard.release("w")
    
    stoktanDemirAl()
    
    time.sleep(2)
    
    
    
    
    
    
    
