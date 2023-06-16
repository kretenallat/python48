from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.implicitly_wait(0.5)

# article_count = int(driver.find_element(By.CSS_SELECTOR, "#articlecount a").text.replace(",", ""))
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()
wikinews = driver.find_element(By.LINK_TEXT, "Wikinews")
wikinews.click()

search = driver.find_element(By.ID, "searchInput")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

input()

