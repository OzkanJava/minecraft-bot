import keyboard
import pyautogui
import time


passwords = [
    
]
sleepVal = 0.01
for password in passwords:
    keyboard.press("ctrl")
    pyautogui.keyDown("a")
    pyautogui.keyUp("a")
    keyboard.release("ctrl")
    pyautogui.press("backspace")
    pyautogui.write(password, interval=sleepVal)
    time.sleep(0.01)
    pyautogui.press("enter")

    


