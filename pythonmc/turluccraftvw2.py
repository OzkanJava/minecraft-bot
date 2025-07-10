import pyautogui
import pyautogui
import time
import mouse
import keyboard

# Başlangıç koordinatları
x, y = 1339, 419
# Hareket miktarı
step = 36
durationVal = 0.01
# 3x3'lük alanı gezme
for i in range(3):
    for j in range(3):
        mouse.move(x + j*step, y + i*step)
        time.sleep(durationVal)
        pyautogui.keyDown(str(i*3 + j + 1))
        pyautogui.keyUp(str(i*3 + j + 1))
        time.sleep(durationVal)
        # Buraya tıklama veya başka işlemler ekleyebilirsiniz
        # Örneğin: pyautogui.click()


mouse.move(1528,456,duration=durationVal)
time.sleep(0.04)
keyboard.press('shift')
time.sleep(0.04)
mouse.click()
time.sleep(0.04)

keyboard.release('shift')

