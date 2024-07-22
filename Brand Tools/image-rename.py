import pyautogui
import time


names = [
    "logo.png",
    "sec44.jpg",
    "up-arrow.png",
    "50-off.png",
]


time.sleep(1)
for i in range(len(names)):
    name = names[i]
    if i == 1:
        time.sleep(1)
    pyautogui.hotkey("ctrl", "f")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(name)
    pyautogui.hotkey("ctrl", "h")
    pyautogui.hotkey("ctrl", "a")
    file_name = name.split(".")[0]
    new = f"{file_name}.webp"
    pyautogui.write(new)
    pyautogui.hotkey("enter")
    pyautogui.hotkey("enter")
    pyautogui.hotkey("enter")
    pyautogui.hotkey("enter")
    pyautogui.hotkey("enter")
