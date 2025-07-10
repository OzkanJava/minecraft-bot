import pyautogui
import time
import mouse
import keyboard

isBroken = False

def change_slot(slot):
    keyboard.press_and_release(str(slot % 9 + 1))

def place_blocks():
    pyautogui.keyDown("space")
    for _ in range(300):
        mouse.right_click()
        time.sleep(0.05)
    pyautogui.keyUp("space")

def shift_action(key, duration=1):
    keyboard.press("shift")
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)
    keyboard.release("shift")

def reconnect_if_needed():
    position = checkisdisconnected()
    if position:
        global isBroken
        isBroken = True
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(2)
        mouse.right_click()
        time.sleep(3)
        return True
    return False

def handle_reconnection():
    for attempt in range(30):
        if checkinhub():
            print("Hub'dayız.")
            break
        if attempt in [5, 10]:
            mouse.click()
            time.sleep(1)
        time.sleep(0.25)

def toggle_inventory():
    keyboard.press_and_release("e")

def dosemece(start, end):
    for i in range(start, end):
        change_slot(i)
        time.sleep(0.5)
        shift_action("s")
        time.sleep(4)
        place_blocks()

        if reconnect_if_needed():
            handle_reconnection()
            break

def main():
    for i in range(99):
        isBroken = False 
        tuccarGit()
        time.sleep(5)
        stoktanDemirAl()
        time.sleep(2)
        dosemece(0, 9)

        if isBroken:
            continue
        
        toggle_inventory()
        time.sleep(1)

        # Diğer oyun işlemleri

main()