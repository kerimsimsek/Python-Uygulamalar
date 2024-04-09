import pyautogui
import time

time.sleep(10)

def mesaj():
    pyautogui.write("Bu mesaj python ile gonderilmektedir.")
    pyautogui.press('enter')

i = 0

while i < 2:
    i += 1
    mesaj()
    time.sleep(0)

#Mesajı kime göndereceksen fare imlecini oraya koy