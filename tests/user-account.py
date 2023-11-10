import random
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker

fake = Faker()
driver = webdriver.Chrome()
driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')
driver.maximize_window()

#filling in the form
first_name = driver.find_element(By.ID, "input-firstname")
first_name.send_keys(fake.first_name())

last_name = driver.find_element(By.ID, "input-lastname")
last_name.send_keys(fake.last_name())

email = driver.find_element(By.ID, "input-email")
email.send_keys(fake.email())


phone = driver.find_element(By.ID, "input-telephone")
phone.send_keys(fake.phone_number())

fakePassword = fake.password()
password = driver.find_element(By.ID, "input-password")
password.send_keys(fakePassword)

password_confirmation = driver.find_element(By.ID, "input-confirm")
password_confirmation.send_keys(fakePassword)

newsletter = driver.find_element(By.XPATH, "//label[@for='input-newsletter-yes']").click()
driver.find_element(By.XPATH, "//label[@for='input-agree']").click()
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

time.sleep(3)

try:
    assert driver.title == "Your Account Has Been Created!"
except AssertionError:
    print("Our title its different from expected.Current title is:",driver.title)

time.sleep(3)
print("register test has passed successfully")
driver.quit()
