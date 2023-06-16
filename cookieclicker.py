from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.implicitly_wait(0.5)

cookie = driver.find_element(By.ID, "cookie")
store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
for item in store_items:
    print(item.id)
# for i in range(100):
#     cookie.click()

input()

