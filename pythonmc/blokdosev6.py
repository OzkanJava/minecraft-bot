import pyautogui
import time
import mouse
import keyboard
from os import system
from PIL import Image
from PIL import ImageGrab
import random

isBroken = False 

warp = (1583, 413, (198, 198, 198))
tuccar = (1517, 337, (112, 25, 25))
tuccarilk = (1295, 529, (3, 38, 32))
tuccariki = (1625, 307, (198, 198, 198))
stokgir = (1156, 345, (255, 85, 85))
hub = (1717, 456, (236, 89, 51))
item9 = (1598,1013,(151,220,242))
tabela = (1518, 538, (78,65,38) )
canmove = (1800, 352 ,(255, 255, 85))

def wait_for_color_for_loop(x, y, target_color, tolerance=0):
    global isBroken
    for i in range(60):  # Toplamda 120 tur, her turda 1 saniye bekleme
        if pyautogui.pixelMatchesColor(x, y, target_color, tolerance=tolerance):
            print(f"Piksel {target_color} rengine ulaştı!")
            return True  # Renk eşleşti, fonksiyon sonlanır
        time.sleep(1)  # 1 saniye bekleme
        print(f"{i+1}. saniye, beklemeye devam ediliyor...")

    print("2 dakika (120 saniye) içinde piksel istenilen renge ulaşamadı.")
    
    isBroken = True
    
    
    return False  # 120 saniye sonunda renk eşleşmedi

def checkisdisconnected():
    try:
        position = pyautogui.locateCenterOnScreen('C://Users//ozkan//Desktop//pythonmc//disconnect.PNG', confidence=0.5)
        return position
    except pyautogui.ImageNotFoundException:
        return None


def shift_ile_yuru(key, duration=1):
    keyboard.press("shift")
    keyboard.press(key)
    time.sleep(duration * 1.2)
    keyboard.release(key)
    keyboard.release("shift")

def arkaDon(a):
    for i in range(a+1):
        pyautogui.moveRel(300,0,duration=0.04)
        pyautogui.moveRel(300,0,duration=0.04)
    
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
        
def envToggle():
    keyboard.press("e")
    keyboard.release("e")
    
def asagiYukari():
    for j in range(9):
        start_x = 1293
        start_y = 551 
        step = 36
        
        mouse.move(start_x+j*step,start_y)
        time.sleep(0.10)
        
        keyboard.press_and_release(str(j%9 +1))
        time.sleep(0.10)
        
def envTemizle():
    pyautogui.keyDown("shift")
    for j in range(9):
        start_x = 1293
        start_y = 551
        step = 36
        
        mouse.move(start_x+j*step,start_y)
        time.sleep(0.10)
        mouse.click()
        
        time.sleep(0.10)
    
    
    for j in range(9):
        start_x = 1293
        start_y = 551 + 36*3
        step = 36
        
        mouse.move(start_x+j*step,start_y)
        time.sleep(0.10)
        mouse.click()
        
        time.sleep(0.10)
    
    mouse.move(1294,552)
    time.sleep(0.10)
    keyboard.press_and_release("9")
    
    time.sleep(0.10)
    pyautogui.keyUp("shift")
    
    envToggle()
    time.sleep(0.5)
    pyautogui.write("t   /tuccar stokekle hepsi ", interval=0.02)
    pyautogui.press("enter")
    
def checkWarp():
    screenshot = ImageGrab.grab()
    x1 = 1505
    y1 = 535
    
    x2 = 1543
    y2 = 534

    pixel1 = screenshot.getpixel((x1, y1))
    pixel2 = screenshot.getpixel((x2, y2))
    return pixel1 == (126,102,63) or pixel2 == (126,102,63) or pixel1 == (85,69,43) or pixel2 == (85,69,43)

def checkinhub():
    return pyautogui.pixelMatchesColor(1717, 456, (236, 89, 51))

def tuccarGit():
    global isBroken
    pyautogui.write("t   /warp  ", interval=0.02)
    pyautogui.press("enter")
    if  not wait_for_color_for_loop(*warp):
        pyautogui.write("t   /warp  ", interval=0.02)
        pyautogui.press("enter")
    mouse.move(1404,556,duration=0.02)
    mouse.click()
    if wait_for_color_for_loop(*tuccar):
        pass
    else:
        isBroken = False
    
def stoktanDemirAl():
    waitTime= 0.25
    mouse.right_click()
    wait_for_color_for_loop(*tuccarilk)
    
    mouse.move(1581,528)
    time.sleep(waitTime)
    mouse.click()
    
    wait_for_color_for_loop(*tuccariki)
    mouse.move(1266,339)
    time.sleep(waitTime)
    mouse.click()
    
    wait_for_color_for_loop(*stokgir)
    
    pyautogui.write("2286", interval=0.03)
    
    time.sleep(waitTime)
    mouse.move(1294,566)
    time.sleep(waitTime)
    mouse.click()
    time.sleep(4)
    wait_for_color_for_loop(*tuccarilk)
    
    pyautogui.press("e") 
    
def dosemece(a,b): # 0. tur da ilk ogeyi alır
    for i in range(a,b):
        keyboard.press_and_release(str(i%9 +1))
        time.sleep(0.5)
        keyboard.press("shift")
        keyboard.press("s")
        time.sleep(1)
        keyboard.release("s")

        keyboard.release("shift")

        time.sleep(4.5)

        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")

        time.sleep(0.5)
        
        pyautogui.keyDown("space")

        for _ in range(300):
            mouse.right_click()
            time.sleep(0.05)
            
        pyautogui.keyUp("space")
        
        
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        time.sleep(2.5)
        
        position = checkisdisconnected()
        if position is not None:
            global isBroken
            isBroken = True
            print("disconnected")
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
            time.sleep(8)

            mouse.move(1371, 444, duration=0.02)
            time.sleep(1)
            mouse.click()
            time.sleep(10) 
            
            if pyautogui.pixelMatchesColor(*item9) :
                print(" 9. slotitem geldi satir 250")
                pyautogui.write('t  /is w fusi ',interval =0.2)
                pyautogui.press('enter')

                time.sleep(1)
                keyboard.press_and_release(str(9))
                mouse.click()
                time.sleep(1)
                envToggle()
                envTemizle()
                time.sleep(10)
                print("dongu kirildi satir 261")
                break
            else:
                print("9.slot tespit edilmedi satir 264")
                time.sleep(5)
                isBroken = False
                pyautogui.write("t   /fly ", interval=0.02)
                pyautogui.press("enter")
                time.sleep(4)
                pyautogui.keyDown("space")
                pyautogui.keyUp("space")
                pyautogui.keyDown("space")
                pyautogui.keyUp("space")
                time.sleep(1)
                
                pyautogui.keyDown("space")

                for _ in range(300):
                    mouse.right_click()
                    time.sleep(0.05)
                    
                pyautogui.keyUp("space")
                
                print("satir 283")
                
                
    




for i in range(99999):
    
    if pyautogui.pixelMatchesColor(*canmove) == True:
        print("hareket edebiliyoruz devam")
        pass
    else:
        print("bilinmeyen menü açıldı esc basılıyor")
        pyautogui.press("esc")
        time.sleep(1)
    
    
    
    
    isBroken = False 
    tuccarGit()
    if isBroken:
        continue
    
    keyboard.press("w")
    time.sleep(1.15)
    keyboard.release("w")
    
    stoktanDemirAl()
    if isBroken:
        continue
    
    print(f"{i+1}. tur")
    pyautogui.write("t   /is w fow ", interval=0.02)
    pyautogui.press("enter")
    
    wait_for_color_for_loop(*tabela)
    if isBroken == True:
        continue
    
    pyautogui.write("t   /fly ", interval=0.02)
    pyautogui.press("enter")
    
    
    
    pyautogui.moveRel(0,300,duration=0.04)

    pyautogui.moveRel(0,300,duration=0.04)

    pyautogui.moveRel(0,-60,duration=0.04)    
    arkaDon(1)
    
    shift_ile_yuru("s", i + 3)
    keyboard.press("shift")
    keyboard.press("w")
    time.sleep(0.25)
    keyboard.release("w")
    keyboard.release("shift")
    
    dosemece(0,1)
    
    if isBroken == True:
        continue
    
    arkaDon(0)
    
    dosemece(1,9)
    
    if isBroken == True:
        continue
    
    envToggle()
    time.sleep(1)
    asagiYukari()
    envToggle()
    time.sleep(1)
    dosemece(0,9)  
    
    if isBroken == True:
        continue 
    time.sleep(0.25)
    
    
    envToggle()
    
    envTemizle()
    
    time.sleep(12)
    