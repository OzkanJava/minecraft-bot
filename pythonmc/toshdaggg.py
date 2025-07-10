import time
import keyboard
import mouse
import  pyautogui

from PIL import Image
from PIL import ImageGrab

sleepVal= 0.02

def domates():
    x,y = pyautogui.position()
    #x,y = 1505,535
    screenshot = ImageGrab.grab()
    pixel = screenshot.getpixel((x,y))
    print(x,y)
    print(pixel)
    return 0


def checkIsInventoryFull():
    screenshot = ImageGrab.grab()
    pixels = [(1578, 634), (1585, 636), (1598, 627), (1591, 635), (1598, 639), (1584, 640), (1583, 628)]
    return all(screenshot.getpixel(pixel) == (255, 255, 255) for pixel in pixels)

def checkIsGoldBlock():

    screenshot = ImageGrab.grab()
    x = 1598
    y = 1013
    
    pixel = screenshot.getpixel((x, y))
    return pixel == (151,220,242)
import pyautogui
import time

warp = (1583, 413, (198, 198, 198))
tuccar = (1517, 337, (112, 25, 25))
tuccarilk = (1295, 529, (3, 38, 32))
tuccariki = (1625, 307, (198, 198, 198))
stokgir = (1156, 345, (255, 85, 85))
item9 = (1598,1013,(151,220,242))
canmove = (1800, 352 ,(255, 255, 85))

"""
while True:
    time.sleep(0.5)
    
    # Her bir konumun pixelMatchesColor sonucunu alıyoruz
    warp_result = pyautogui.pixelMatchesColor(*warp)
    tuccar_result = pyautogui.pixelMatchesColor(*tuccar)
    tuccarilk_result = pyautogui.pixelMatchesColor(*tuccarilk)
    tuccariki_result = pyautogui.pixelMatchesColor(*tuccariki)
    stokgir_result = pyautogui.pixelMatchesColor(*stokgir)
    item9_result = pyautogui.pixelMatchesColor(*item9)
    canmove_result = pyautogui.pixelMatchesColor(*canmove)
    # Sonuçları yan yana yazdırıyoruz
    print(f"Warp: {warp_result}, Tuccar: {tuccar_result}, Tuccar İlk: {tuccarilk_result}, Tuccar İki: {tuccariki_result}, \n Stok Gir: {stokgir_result}, item9: {item9_result}, canmove: {canmove_result}")
"""
def wait_for_color_for_loop(x, y, target_color, tolerance=0):

    for i in range(120):  # Toplamda 120 tur, her turda 1 saniye bekleme
        if pyautogui.pixelMatchesColor(x, y, target_color, tolerance=tolerance):
            print(f"Piksel {target_color} rengine ulaştı!")
            return True  # Renk eşleşti, fonksiyon sonlanır
        time.sleep(1)  # 1 saniye bekleme
        print(f"{i+1}. saniye, beklemeye devam ediliyor...")

    print("2 dakika (120 saniye) içinde piksel istenilen renge ulaşamadı.")
    return False  # 120 saniye sonunda renk eşleşmedi

# Örnek kullanım:
# (500, 400) pozisyonundaki pikselin kırmızıya (255, 0, 0) ulaşmasını bekler.

while True:
    time.sleep(0.5) #1800 352 255 255 85
    domates()