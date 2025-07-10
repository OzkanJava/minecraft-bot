import time
import pyautogui
import mouse
import os
import keyboard
import pygetwindow as gw

def checkisdisconnected():
    # Disconnect kontrolünü burada yap
    try:
        position = pyautogui.locateCenterOnScreen('C://Users//ozkan//Desktop//pythonmc//disconnect.PNG', confidence=0.5)
        return position
    except pyautogui.ImageNotFoundException:
        return None


def checkinhub():
    return pyautogui.pixelMatchesColor(1717, 456, (236, 89, 51))



def handle_disconnect():
    # Disconnect tespit edilirse yapılacak işlemler
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
        

def open_application():
    sleepVal = 0.1
    keyboard.press_and_release("esc")
    time.sleep(1)
    mouse.move(1950,10,duration = sleepVal)
    mouse.click()


    os.system("C://Users//ozkan//Desktop//CraftRise.exe")


    time.sleep(120)



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

while True:
    current_time = time.strftime("%H:%M")
    
    if current_time == "06:01":
        open_application()
        craftriseEkran = gw.getWindowsWithTitle('CraftRise')[0]

        craftriseEkran.resizeTo(958,1008)

        craftriseEkran.resize(16,39)

        craftriseEkran.moveTo(953,0)
        
        
    else:
        handle_disconnect()
        time.sleep(3)  # Belirli aralıklarla disconnect kontrolü yap
