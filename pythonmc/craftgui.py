import tkinter as tk
import pyautogui
import time
import mouse
import keyboard

sleepVal =0.02
def craft(k):
    for i in range(k):
        for j in range(9):
            currentMouseX = 1294 + j * 36.125
            currentMouseY = 553 + i * 35.5
            mouse.move(int(currentMouseX), int(currentMouseY), duration=sleepVal)
            mouse.click()
            if j <= 2:
                craftingX = 1338 + (j % 3) * 36.5
                craftingY = 419
            elif j <= 5:
                craftingX = 1338 + (j % 3) * 36.5
                craftingY = 455
            elif j <= 8:
                craftingX = 1338 + (j % 3) * 36.5
                craftingY = 491

            mouse.move(int(craftingX), int(craftingY), duration=sleepVal)
            mouse.click()

        mouse.move(1528, 456, duration=sleepVal)
        time.sleep(0.11)
        keyboard.press("shift")
        time.sleep(0.11)
        mouse.click()
        time.sleep(0.11)

        keyboard.release("shift")

def fixironblock(ilkdeger, sondeger):
    space = 36
    fixX = 1583
    fixY = 664
    for i in range(ilkdeger, sondeger):
        mouse.move(fixX - i * space, fixY, duration=sleepVal)
        mouse.click()
        mouse.move(fixX, fixY - ((i % 3) + 1) * space, duration=sleepVal)
        mouse.click()
        mouse.move(fixX - i * space, fixY, duration=sleepVal)
        mouse.click()

def fonksiyon1():
    craft(3)
    fixironblock(0,3)
    time.sleep(sleepVal)
    keyboard.press('esc')

    keyboard.release('esc')

def fonksiyon2():
    craft(3)
    fixironblock(3,6)
    time.sleep(sleepVal)
    keyboard.press('esc')

    keyboard.release('esc')

def fonksiyon3():
    craft(3)
    fixironblock(6,9)
    time.sleep(sleepVal)
    keyboard.press('esc')

    keyboard.release('esc')

def fonksiyon4():
    craft(4)

    time.sleep(sleepVal)
    keyboard.press('esc')

    keyboard.release('esc')
# Pencere oluşturma
root = tk.Tk()
root.title("4 Butonlu Arayüz")

# Butonlar
button1 = tk.Button(root, text="1", command=fonksiyon1, width=20, height=5)
button1.pack()

button2 = tk.Button(root, text="2", command=fonksiyon2, width=20, height=5)
button2.pack()

button3 = tk.Button(root, text="3", command=fonksiyon3, width=20, height=5)
button3.pack()

button4 = tk.Button(root, text="4", command=fonksiyon4, width=20, height=5)
button4.pack()

# Pencereyi gösterme döngüsü
root.mainloop()
