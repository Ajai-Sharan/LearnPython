import pyautogui as pg
import time

time.sleep(8)

for i in range(11):
    pg.write('Hi, ')
    pg.write('I am BAT man')
    pg.press('enter')