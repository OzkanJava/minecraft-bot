import tkinter as tk
import pyautogui
import time
import mouse
import keyboard
from os import system
from PIL import Image
from PIL import ImageGrab
import random

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

        

sleepVal = 0.02







def buton1():
    label.config(text="Son basılan buton: 1")
    craft(3)
    fixironblock((0) * 3, (0) * 3 + 3)
    envanterKapa()


def buton2():
    label.config(text="Son basılan buton: 2")
    craft(3)
    fixironblock((1) * 3, (1) * 3 + 3)
    envanterKapa()
def buton3():
    label.config(text="Son basılan buton: 3")
    craft(3)
    fixironblock((2) * 3, (2) * 3 + 3)
    
    satircraft(3)
    
    envanterKapa()

def buton4():
    label.config(text="Son basılan buton: 4")
    craft(3)
    fixironblock((1) * 3, (1) * 3 +3)
    envanterKapa()

def buton5():
    label.config(text="Son basılan buton: 5")
    craft(3)
    fixironblock((2) * 3, (2) * 3 +3)
    envanterKapa()

def buton6():
    label.config(text="Son basılan buton: 6")
    craft(3)
    fixironblock(0,3)
    satircraft(3)
    fixgoldblock(1,4)
    envanterKapa()

def buton7():
    label.config(text="Son basılan buton: 7")
    craft(3)
    fixironblock((1) * 3, (1) * 3 +3)
    envanterKapa()

def buton8():
    label.config(text="Son basılan buton: 8")
    craft(3)
    fixironblock((2) * 3, (2) * 3 +3)
    envanterKapa()

def buton9():
    label.config(text="Son basılan buton: 9")
    craft(3)
    fixironblock(0,3)
    satircraft(3)
    fixgoldblock(1,4)
    envanterKapa()

def buton10():
    label.config(text="Son basılan buton: 10")
    craft(3)
    fixironblock((1) * 3, (1) * 3 +3)
    envanterKapa()

def buton11():
    label.config(text="Son basılan buton: 11")
    craft(3)
    fixironblock((2) * 3, (2) * 3 +3)
    envanterKapa()

def buton12():
    label.config(text="Son basılan buton: 12")
    craft(3)
    fixironblock(0,3)
    satircraft(3)
    fixgoldblock(1,4)
    envanterKapa()

root = tk.Tk()
root.title("12 Butonlu Arayüz")

# Grid layout için sayısal parametreler
rows, cols = 3, 4

# Etiket, en son basılan buton numarasını gösterecek
label = tk.Label(root, text="Son basılan buton: Yok", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=cols, pady=10)

# Butonları oluştur ve yerleştir
buttons = [
    ("1", buton1),
    ("2", buton2),
    ("3", buton3),
    ("4", buton4),
    ("5", buton5),
    ("6", buton6),
    ("7", buton7),
    ("8", buton8),
    ("9", buton9),
    ("10", buton10),
    ("11", buton11),
    ("12", buton12),
]

for i, (text, command) in enumerate(buttons):
    button = tk.Button(root, text=text, command=command, width=10, height=3, font=("Arial", 12))
    button.grid(row=(i)//cols + 1, column=(i)%cols, padx=5, pady=5)

root.mainloop()
