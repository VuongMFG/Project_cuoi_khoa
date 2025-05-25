from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from bs4 import BeautifulSoup
import time
import pyautogui
import keyboard
import random
import string
from datetime import datetime
import sys
import ctypes

# Creat license
due_date = "30/06/2025"
due_date1 = datetime.strptime(due_date, "%d/%m/%Y")
now = datetime.now()
if due_date1 >= now:

    edge_driver_path = "msedgedriver.exe"  

    # Open Edge browser
    service = EdgeService(executable_path=edge_driver_path)
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(service=service, options=options)

    # Wait "backspace"
    keyboard.wait("backspace")

    # Get "words" list
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    spans = soup.select("div.content-display span")
    span_list = [span.get_text(strip=True) for span in spans]
    time.sleep(2)
    a = [0, 0, 0, 0]
    for i in range(len(a)):
        a[i]= random.randint(1,70)
    for i in range(len(a)):
        span_list[a[i]] = random.choice(string.ascii_letters)

    # Simulate physical keyboard
    pyautogui.FAILSAFE = False
    for i in range(100):
        if keyboard.is_pressed("enter"):
            break
        for j in range(len(span_list[i])):
            pyautogui.press(span_list[i][j])
        pyautogui.press('space')
        time.sleep(0.2)
    pyautogui.FAILSAFE = True
else:
    ctypes.windll.user32.MessageBoxW(0, "Chương trình hết hạn.", "Thông báo", 0)
    sys.exit()
