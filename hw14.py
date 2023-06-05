from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.demoblaze.com/")

#login process
driver.find_element(By.ID, "login2").click()
time.sleep(2)
driver.find_element(By.ID, "loginusername").send_keys("iremerd")
driver.find_element(By.XPATH, '//*[@id="loginpassword"]').send_keys("010203")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#logInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
time.sleep(2)

#assertion for Logout button
logout = driver.find_element(By.ID, "logout2").text
print(logout)
assert logout == "Log out"
time.sleep(2)

#assertion link
link = driver.current_url
print(driver.current_url)
assert "https://www.demoblaze.com/" in link
time.sleep(2)

#assertion for customer name
customerName = driver.find_element(By.ID, "nameofuser").text
print(customerName)
assert customerName == "Welcome iremerd"

#click Monitors category
driver.find_element(By.LINK_TEXT, 'Monitors').click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Apple monitor 24').click()
time.sleep(2)

#monitors assertion
link = driver.current_url
print(driver.current_url)
assert "https://www.demoblaze.com/prod.html?idp_=10" in link
time.sleep(1)

#monitors assertions for product_name and product_price
product_name = driver.find_element(By.CSS_SELECTOR, "h2.name").text
print(product_name)
assert product_name == "Apple monitor 24"

product_price = driver.find_element(By.CSS_SELECTOR, "h3.price-container").text
print(product_price)
assert product_price == "$400 *includes tax"

#click Add to chart
driver.find_element(By.LINK_TEXT, 'Add to cart').click()
time.sleep(1)

#Assertion about that product is successfully
obj = driver.switch_to.alert
message = obj.text
print(message)
obj.accept()
time.sleep(1)

#open cart
driver.find_element(By.ID, "cartur").click()
time.sleep(2)
#charts assertions for product_name and product_price
cart_page = driver.find_element(By.CSS_SELECTOR, "h2").text
print(cart_page)
assert cart_page == "Products"

cart_page_productName = driver.find_element(By.CSS_SELECTOR, "#tbodyid > tr > td:nth-child(2)").text
print(cart_page_productName)
assert cart_page_productName == "Apple monitor 24"

cart_page_productPrice = driver.find_element(By.CSS_SELECTOR, "#tbodyid > tr > td:nth-child(3)").text
print(cart_page_productPrice)
assert cart_page_productPrice == "400"
input()
