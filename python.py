from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

onAdd = False

# Open the Website
browser.get('https://www.youtube.com/watch?v=lkAG1kAGzQg')

print("--------stage 0 ------")

time.sleep(5)

skip_element = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[32]/div[2]/div[1]/button"

play_button = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[26]/div[2]/div[1]/button"

print("Initital Click For video")
clickable = browser.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div')

clickable.click()

while True:
    print("Viewing Video")
    time.sleep(35)
    print("Reloading Page...")
    browser.refresh()
    print("Restarting Process")
    time.sleep(2)


