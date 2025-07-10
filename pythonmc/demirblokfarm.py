import pyautogui
import time
import mouse
import keyboard
from os import system
from PIL import Image
from PIL import ImageGrab


def checkIsInventoryFull():
    screenshot = ImageGrab.grab()
    pixels = [(1578, 634), (1585, 636), (1598, 627), (1591, 635), (1598, 639), (1584, 640), (1583, 628)]
    return all(screenshot.getpixel(pixel) == (255, 255, 255) for pixel in pixels)


def craft():
    for i in range(4):
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

sleepVal = 0.08

while True:
    time.sleep(2)
    mouse.right_click()
    if(checkIsInventoryFull()):
        craft()
        pyautogui.press('esc')
        pyautogui.press('t')
        keyboard.write('  /tüccar ekle 1 350',delay =sleepVal)
        pyautogui.press('enter')
        pyautogui.press('t')
        keyboard.write('  /tüccar stokekle hepsi',delay =sleepVal)
        pyautogui.press('enter')
        
        