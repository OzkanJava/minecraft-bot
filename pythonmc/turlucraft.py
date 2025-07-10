import mouse as bot
import time
import keyboard
durationVal = 0.02
sleepVal =0.11

while True:
    kactur = int(input("Kactur donelim:"))

    for i in range(kactur):
        for j in range(9):
            currentMouseX = 1294 + j*36.125;
            currentMouseY = 553 + i*35.5;
            bot.move(int(currentMouseX),int(currentMouseY))
            time.sleep(durationVal)
            bot.click()
            if(j <= 2):
                craftingX = 1338 + (j%3) * 36.5
                craftingY = 419
            elif(j <= 5):
                craftingX = 1338 + (j%3) * 36.5
                craftingY = 455
            elif(j <= 8):
                craftingX = 1338 + (j%3) * 36.5
                craftingY = 491
        
            bot.move(int(craftingX),int(craftingY),duration=durationVal)
            time.sleep(durationVal)
            bot.click()


        bot.move(1528,456,duration=durationVal)
        time.sleep(durationVal*10)
        keyboard.press('shift')
        time.sleep(durationVal*10)
        bot.click()
        time.sleep(durationVal*10)
    
        keyboard.release('shift')
    
