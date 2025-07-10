import pyautogui
import mouse
import keyboard
import time
from PIL import Image
from PIL import ImageGrab


def checkisdisconnected():
    try:
        position = pyautogui.locateCenterOnScreen('C://Users//ozkan//Desktop//pythonmc//disconnect.PNG', confidence=0.5)
        return position
    except pyautogui.ImageNotFoundException:
        return None

def checkinhub():
    return pyautogui.pixelMatchesColor(1717, 456, (236, 89, 51))
    """
    screenshot = ImageGrab.grab()
    x = 1720
    y = 454

    pixel = screenshot.getpixel((x, y))
    return pixel == (236, 89, 51)
    """
while True:
    time.sleep(5)
    position = checkisdisconnected()
    if position is not None:
        pyautogui.moveTo(position)
        pyautogui.click()

        for a in range(30):
            if checkinhub() == True:
                print("hubssdayız")
                
                break
            print(a)
            if a == 5 or a== 10:
                mouse.click()
                time.sleep(1)
            time.sleep(0.25)
        
        
        time.sleep(2)



        mouse.right_click()
        time.sleep(3)

        mouse.move(1371, 444, duration=0.02)
        time.sleep(1)
        mouse.click()
        time.sleep(3)
        
    else:
        pass

