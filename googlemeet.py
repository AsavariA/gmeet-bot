from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pause
import pynput
import os
from pynput.keyboard import Key,Controller
from datetime import datetime

# for scheduled meets: arguments: year,month,day,hour,minute
# pause.until(datetime(2020,9,5,11,30))

# mail and password
username_string = 'your username'
password_string = 'your password'

meet_url = 'meet link here'

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
# options.add_argument("--window-size=800,600")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 2,
     "profile.default_content_setting_values.notifications": 2
  })

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get('https://meet.google.com/')

browser.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a').click()

browser.find_element_by_id('identifierId').send_keys(username_string, Keys.ENTER)

browser.find_element_by_name('password').send_keys(password_string)
