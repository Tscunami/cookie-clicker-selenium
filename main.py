from selenium import webdriver
import time

chrome_driver_path = "C:\Shortcuts\Applications/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")

waiting_time = 5

x_end = time.time() + 60
while time.time() < x_end:

    t_end = time.time() + waiting_time
    while time.time() < t_end:
        cookie.click()

    waiting_time += 8

    store_upgrades = driver.find_element_by_id("store")

    enabled_upgrades = driver.find_elements_by_class_name("enabled")
    best_upgrade = enabled_upgrades[len(enabled_upgrades) - 1]

    best_upgrade.click()




