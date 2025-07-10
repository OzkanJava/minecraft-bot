import os
import pyautogui
import time
import mouse
import keyboard

sleepVal = 0.02
warp = (1583, 413, (198, 198, 198))
tuccar = (1517, 337, (112, 25, 25))
tuccarilk = (1295, 529, (3, 38, 32))
tuccariki = (1625, 307, (198, 198, 198))
stokgir = (1161, 383, (255, 85, 85))
hub = (1717, 456, (236, 89, 51))
item9 = (1598,1013,(151,220,242))
tabela = (1518, 538, (78,65,38) )


def wait_for_color_for_loop(x, y, target_color, tolerance=0):

    for i in range(120):  # Toplamda 120 tur, her turda 1 saniye bekleme
        if pyautogui.pixelMatchesColor(x, y, target_color, tolerance=tolerance):
            print(f"Piksel {target_color} rengine ulaştı!")
            return True  # Renk eşleşti, fonksiyon sonlanır
        time.sleep(1)  # 1 saniye bekleme
        print(f"{i+1}. saniye, beklemeye devam ediliyor...")

    print("2 dakika (120 saniye) içinde piksel istenilen renge ulaşamadı.")
    return False  # 120 saniye sonunda renk eşleşmedi
"""
time.sleep(12300)


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


"""

"""
for i in range(999):
    mouse.right_click()
    time.sleep(1)

    mouse.move(1334, 490, duration=sleepVal)
    time.sleep(1)
    mouse.click()

    mouse.move(1334, 338)
    time.sleep(1)
    mouse.click()

    time.sleep(1)
    
    pyautogui.keyDown("shift")
    time.sleep(sleepVal)
    mouse.move(1301-36-36, 340, duration=sleepVal)
    time.sleep(1)
    pyautogui.click(button = "RIGHT")
    pyautogui.keyUp("shift")

    time.sleep(0.5)

    keyboard.write("2304")

    time.sleep(0.5)


    keyboard.send("enter")
    time.sleep(0.5)

    keyboard.send("esc")
    time.sleep(0.5)

    pyautogui.write('t  /tuccar stokekle hepsi ',interval =sleepVal)
    pyautogui.press('enter')
    time.sleep(0.5)
    
"""    
waitTime= 0.25
for i in range(999):
   
    mouse.right_click()
    wait_for_color_for_loop(*tuccarilk)
    
    mouse.move(1334,490)
    time.sleep(waitTime)
    mouse.click()
    
    wait_for_color_for_loop(*tuccariki)
    mouse.move(1334,338)
    time.sleep(waitTime)
    mouse.click()
    
    wait_for_color_for_loop(*tuccariki)
    time.sleep(1)
    
    pyautogui.keyDown("shift")
    time.sleep(sleepVal)
    mouse.move(1301-36, 340, duration=sleepVal)
    time.sleep(1)
    pyautogui.click(button = "RIGHT")
    pyautogui.keyUp("shift")

    time.sleep(0.5)

    
    wait_for_color_for_loop(*stokgir)
    
    pyautogui.write("2304", interval=0.03)
    
    time.sleep(waitTime)
    mouse.move(1294,566)
    time.sleep(waitTime)
    mouse.click()
    time.sleep(waitTime)
    wait_for_color_for_loop(*tuccariki)
    
    pyautogui.press("e") 

    pyautogui.write('t  /tuccar stokekle hepsi ',interval =sleepVal)
    pyautogui.press('enter')
    time.sleep(0.5)