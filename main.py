from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")
driver.implicitly_wait(0.5)
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# link = driver.find_elements_by_css_selector(".documentation-widget a")  # example of finding an a inside a doc widget
# bug_link = driver.find_element_by_xpath("/html/body/div[1]/div[3]/footer/div[2]/div[2]/img[4]")  # right click the element and copy xpath
#
# driver.implicitly_wait(10)


# driver.close()  # closes tab
# driver.quit()  # closes program

event_dict_list = {}
events_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
events_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
for i in range(len(events_dates)):
    event_dict_list[i] = {"time": events_dates[i].text,
                          "name": events_names[i].text}

print(event_dict_list)

