import pyautogui
import time

def nav_to_image(image, clicks, off_x = 0, off_y = 0):
    position = pyautogui.locateCenterOnScreen(image, confidence = 0.76)
    
    if position is None:
        print(f'{image} not found..')
        return 0
    else:
        pyautogui.moveTo(position, duration = 0.1)
        pyautogui.moveRel(off_x,off_y)
        pyautogui.click(clicks=clicks,interval = 0.1)
        
    
#position = pyautogui.locateCenterOnScreen('C://Users//ozkan//Desktop//pythonmc//disconnect.PNG' , confidence= 0.5)

for i in range(959):
    #time.sleep(0.5)
    try:
        position = pyautogui.locateCenterOnScreen('C://Users//ozkan//Desktop//pythonmc//disconnect.PNG' , confidence= 0.5)
        print("ekranda var\n")
    except :
        print("ekranda yok\n")
    
  
#print(pyautogui.pixelMatchesColor(1561, 689, (251, 144, 102)))
