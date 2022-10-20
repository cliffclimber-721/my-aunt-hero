import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pause

# MacOS
import hero_macro as hm
driver = webdriver.Safari()
waitFor = WebDriverWait(driver, 10)
driver.get(hm.url)

ID_show = waitFor.until(EC.element_to_be_clickable(By.ID, "userID"))
PWD_show = driver.find_element_by_id("userPW")

ID_show.send_keys(hm.my_id)
PWD_show.send_keys(hm.my_pwd)

loginNow = driver.find_element_by_id("loginBtn")
loginNow.click()

pause.until(datetime(hm.start_year, hm.start_month, hm.start_day, hm.start_hour, hm.start_min, 00))
driver.get(hm.url)

# reservation YES24
reserve = waitFor.until(EC.element_to_be_clickable((By.CLASS_NAME, "rn-bb03")))
reserve.click()

# getCalendar
driver.switch_to_window(driver.window_handles[1])

dateShow = waitFor.until(EC.element_to_be_clickable((By.ID, "2022-12-03")))
dateShow.click()