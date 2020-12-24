import pyautogui, time

time.sleep(2)

f = open("water.txt", "r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")