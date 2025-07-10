import pyautogui
import time
import mouse
import keyboard
from os import system
from PIL import Image
from PIL import ImageGrab
import random



for i in range(9):
    start_x = 1293
    start_y = 551 
    step = 36
    
    mouse.move(start_x+i*step,start_y)
    time.sleep(0.10)
    
    keyboard.press_and_release(str(i%9 +1))
    time.sleep(0.10)