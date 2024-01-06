import pyautogui
from functions import click, scan

X, Y, W, H = 1587, 188, 326, 327

sh = pyautogui.screenshot(region=(X, Y, W, H))

sh.save('screenshot.png')

if pyautogui.locate('pics/1.png', 'screenshot.png'):
    print("felfele mutat (fekete)")
elif pyautogui.locate('pics/2.png', 'screenshot.png'):
    print(f"lefele mutat (fekete) found at {pyautogui.locate('pics/2.png', 'screenshot.png')}")
elif pyautogui.locate('third_image_to_find.png', 'screenshot.png'):
    print("Third image found")
elif pyautogui.locate('fourth_image_to_find.png', 'screenshot.png'):
    print("Fourth image found")
else:
    print("No image found")