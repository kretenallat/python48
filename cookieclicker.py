from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.implicitly_wait(0.5)
cookie = driver.find_element(By.ID, "cookie")

start_time = timeout_start = time.time()
while True:
    cookie.click()
    if time.time() >= timeout_start + 9:
        timeout_start = time.time()
        driver.implicitly_wait(0.5)
        current_cookies = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        # print(current_cookies)
        best_buy = ""
        store_items = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        for item in store_items:
            if item.is_displayed():
                item_name = item.text.split(" - ")[0]
                item_price = int(item.text.split(" - ")[1].replace(",", ""))
                if item_price <= current_cookies:
                    best_buy = item_name
                    # print(best_buy)
        if best_buy is not None:
            best_action = driver.find_element(By.ID, "buy" + best_buy)
            # print(best_action.text)
            best_action.click()
    if time.time() >= start_time + 30:
        start_time = time.time()
        cps = driver.find_element(By.ID, "cps").text.split(": ")[1]
        print(f"Your cookies / second is {cps}! Good job!")

input()

