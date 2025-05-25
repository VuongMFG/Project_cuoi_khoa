from PIL import Image
import pytesseract
import pyautogui
import mouse
import keyboard
import time
from datetime import datetime
import ctypes
import sys
import random
import string

# Creat license
due_date = "23/07/2025"
due_date1 = datetime.strptime(due_date, "%d/%m/%Y")
now = datetime.now()
while True:
    if due_date1 >= now:
        # wait "ctrl"
        keyboard.wait("ctrl")

        # detect text region
        mouse.wait("left")
        x1, y1 = pyautogui.position()
        time.sleep(2)
        mouse.wait("left")
        x2, y2 = pyautogui.position()
        time.sleep(1)
        left = min(x1, x2)
        top = min(y1, y2)
        width = abs(x2 - x1)
        height = abs(y2 - y1)
    
        # capture image and save .png file

        region = (left, top, width, height)
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save("image.png")


        # open image
        img = Image.open('image.png')

        # Covert image to texts
        text = pytesseract.image_to_string(img, lang='eng')  # 'eng' là ngôn ngữ tiếng Anh
        text = text.replace('\n',' ')
        words = text.split(" ")
        a = [0, 0, 0, 0]
        for i in range(len(a)):
            a[i]= random.randint(1,70)
        for i in range(len(a)):
            words[a[i]] = random.choice(string.ascii_letters)

        # Simulate physical keyboard
        keyboard.wait("backspace")
        pyautogui.FAILSAFE = False
        for i in range(100):
            if keyboard.is_pressed("enter"):
                break
            for j in range(len(words[i])):
                pyautogui.press(words[i][j])
            pyautogui.press('space')
            time.sleep(0.1)
        pyautogui.FAILSAFE = True
    else:
        ctypes.windll.user32.MessageBoxW(0, "Chương trình hết hạn.", "Thông báo", 0)
        sys.exit()
