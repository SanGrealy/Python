#Отображение страницы товара
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
#
# account = driver.find_element_by_css_selector("#menu-item-50>a")
# account.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("eliza1000@mail.ru")
#
# passw = driver.find_element_by_id("password")
# passw.send_keys("gfhjkmlkzfdnjvfnbpfwbb")
#
# reg = driver.find_element_by_name("login")
# reg.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
#
# html = driver.find_element_by_css_selector(".products.masonry-done>li:nth-child(3)>a>h3")
# html_text = html.text
# assert "HTML5 Forms" in html_text
# html.click()
# time.sleep(3)
#
# driver.quit()

#Количество товаров в категории
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
#
# account = driver.find_element_by_css_selector("#menu-item-50>a")
# account.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("eliza1000@mail.ru")
#
# passw = driver.find_element_by_id("password")
# passw.send_keys("gfhjkmlkzfdnjvfnbpfwbb")
#
# reg = driver.find_element_by_name("login")
# reg.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
#
# html = driver.find_element_by_css_selector(".cat-item.cat-item-19>a")
# html.click()
#
# items_count = driver.find_elements_by_css_selector(".products.masonry-done>li")
# print(items_count)
# if len(items_count) ==3:
#     print("Три товара")
#
# driver.quit()

#сортировка товаров

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
#
# account = driver.find_element_by_css_selector("#menu-item-50>a")
# account.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("eliza1000@mail.ru")
#
# passw = driver.find_element_by_id("password")
# passw.send_keys("gfhjkmlkzfdnjvfnbpfwbb")
#
# reg = driver.find_element_by_name("login")
# reg.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
#
# sorting = driver.find_element_by_css_selector(".orderby>[selected='selected']")
# sorting_checked = sorting.get_attribute('value')
# assert "menu_order" in sorting_checked
#
# sortingselect = driver.find_element_by_class_name("orderby")
# select=Select(sortingselect)
# select.select_by_value("price-desc")
# time.sleep(2)
#
# sorting = driver.find_element_by_css_selector(".orderby>[selected='selected']")
# sorting_checked = sorting.get_attribute('value')
# assert "price-desc" in sorting_checked
#
# driver.quit()

#отображение, скидка товара

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
#
# account = driver.find_element_by_css_selector("#menu-item-50>a")
# account.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("eliza1000@mail.ru")
#
# passw = driver.find_element_by_id("password")
# passw.send_keys("gfhjkmlkzfdnjvfnbpfwbb")
#
# reg = driver.find_element_by_name("login")
# reg.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# time.sleep(1)
#
# android = driver.find_element_by_css_selector('.products.masonry-done>li:nth-child(1)>a>h3')
# android.click()
#
# price1 = driver.find_element_by_css_selector('.price>del>span')
# price1_text = price1.text
# assert '600' in price1_text
#
# price2 = driver.find_element_by_css_selector('.price>ins>span')
# price2_text = price2.text
# assert '450' in price2_text
#
# pic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images>a>img")))
# pic.click()
#
# pic1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# pic1.click()
#
# driver.quit()

# проверка цены в корзине

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
#
# account = driver.find_element_by_css_selector("#menu-item-50>a")
# account.click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("eliza1000@mail.ru")
#
# passw = driver.find_element_by_id("password")
# passw.send_keys("gfhjkmlkzfdnjvfnbpfwbb")
#
# reg = driver.find_element_by_name("login")
# reg.click()
#
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
#
# add = driver.find_element_by_css_selector('.products.masonry-done>li:nth-child(4)>a:nth-child(2)')
# add.click()
# time.sleep(2)
# item_count = driver.find_element_by_class_name('cartcontents')
# item_count_text = item_count.text
# print(item_count_text)
# assert '1 Item' in item_count_text
#
# price = driver.find_element_by_css_selector('.wpmenucart-contents .amount')
# price_text = price.text
# assert '₹180.00' in price_text
#
# item_count.click()
#
# subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '.cart-subtotal>td>span'),'180.00'))

# работа в корзине
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://practice.automationtesting.in/")
#
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
#
# add = driver.find_element_by_css_selector('.products.masonry-done>li:nth-child(4)>a:nth-child(2)')
# add.click()
# time.sleep(2)
#
# add2 = driver.find_element_by_css_selector('.products.masonry-done>li:nth-child(5)>a:nth-child(2)')
# add2.click()
# time.sleep(2)
#
# item_count = driver.find_element_by_class_name('cartcontents')
# item_count.click()
# time.sleep(1)
#
# remove = driver.find_element_by_css_selector('.cart_item:nth-child(1)>.product-remove>a')
# remove.click()
# time.sleep(3)
#
# undo = driver.find_element_by_css_selector('.woocommerce-message>a')
# undo.click()
#
# quan = driver.find_element_by_css_selector('.quantity>input')
# quan.clear()
# quan.send_keys('3')
#
# update = driver.find_element_by_name('update_cart')
# update.click()
# time.sleep(5)
#
# quan = driver.find_element_by_css_selector('.quantity>input')
# quan_1 = quan.get_attribute('value')
# assert '3' in quan_1
#
# apply = driver.find_element_by_name('apply_coupon')
# apply.click()
# time.sleep(20)
#
# coupon = driver.find_element_by_css_selector('.woocommerce-error>li')
# coupon_text = coupon.text
# assert 'Please enter a coupon code' in coupon_text
# driver.quit()

#покупка товара

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_css_selector("#menu-item-40>a")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")

add = driver.find_element_by_css_selector('.products.masonry-done>li:nth-child(4)>a:nth-child(2)')
add.click()
time.sleep(2)

item_count = driver.find_element_by_class_name('cartcontents')
item_count.click()
time.sleep(1)

checkout = driver.find_element_by_css_selector('.wc-proceed-to-checkout>a')
checkout.click()

name = driver.find_element_by_id('billing_first_name')
name.send_keys('Lisa')

last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Syrkina')

phone = driver.find_element_by_id('billing_phone')
phone.send_keys('89999999999')

email = driver.find_element_by_id('billing_email')
email.send_keys('eliza1000@mail.ru')

adress = driver.find_element_by_id('billing_address_1')
adress.send_keys('Valovaya 15')

town = driver.find_element_by_id('billing_city')
town.send_keys('Saratov')

country = driver.find_element_by_id('billing_state')
country.send_keys('Russia')

postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('611033')

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)

check = driver.find_element_by_id('payment_method_cheque')
check.click()
time.sleep(2)

order = driver.find_element_by_id('place_order')
order.click()

time.sleep(3)

text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
text1 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)>td"), "Check Payments"))
driver.quit