import pyautogui
import time

time.sleep(2)

with open("water.txt", "r") as f:
    for word in f:
        pyautogui.typewrite(word.strip())
        pyautogui.press("enter")
