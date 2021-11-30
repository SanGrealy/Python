import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

#Регистрация
# driver.get("http://practice.automationtesting.in/")
#
# account = driver.find_element_by_css_selector("#menu-item-50>a")
# account.click()
#
# email = driver.find_element_by_id("reg_email")
# email.send_keys("eliza1000@mail.ru")
#
# passw = driver.find_element_by_id("reg_password")
# passw.send_keys("gfhjkmlkzfdnjvfnbpfwbb")
#
# reg = driver.find_element_by_name("register")
# reg.click()
# driver.quit()

#Логин
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")

account = driver.find_element_by_css_selector("#menu-item-50>a")
account.click()

email = driver.find_element_by_id("username")
email.send_keys("eliza1000@mail.ru")

passw = driver.find_element_by_id("password")
passw.send_keys("gfhjkmlkzfdnjvfnbpfwbb")

reg = driver.find_element_by_name("login")
reg.click()
time.sleep(3)

driver.quit()

