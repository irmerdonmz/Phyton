
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

# open site (https://www.saucedemo.com/)
driver.get("https://www.saucedemo.com/")

#paste correct name into Username field (info below)
driver.find_element(By.ID, "user-name").send_keys("standard_user")

#paste correct password into Password field (info below also)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")

#click to Login button
driver.find_element(By.ID, "login-button").click()

#get current URL
link = driver.current_url
print(driver.current_url)

#check that current URL and expected URL (https://www.saucedemo.com/inventory.html, for example) are the same
assert "https://www.saucedemo.com/inventory.html" in link
if "https://www.saucedemo.com/inventory.html" in link:
    print("Pass")
else:
    print("Fail")
input()
