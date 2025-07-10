import os
import pyautogui
import time
import mouse
import keyboard

sleepVal = 0.02
time.sleep(9400)

#pyautogui.write('t   ',interval =sleepVal)

time.sleep(10)

keyboard.press_and_release("esc")
time.sleep(1)
mouse.move(1950,10,duration = sleepVal)
mouse.click()


os.system("C://Users//ozkan//Downloads//CraftRise.exe")


time.sleep(180)



mouse.move(1380, 670, duration=sleepVal)
time.sleep(1)
mouse.click()

time.sleep(500)

mouse.right_click()
time.sleep(3)

mouse.move(900, 480, duration=sleepVal)
time.sleep(1)
mouse.click()

keyboard.send("5")
time.sleep(3)
mouse.right_click()

time.sleep(3)

mouse.right_click()
time.sleep(3)

mouse.move(900, 480, duration=sleepVal)
time.sleep(1)
mouse.click()


