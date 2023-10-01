import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a WebDriver instance (in this case, Chrome)
driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()


# Locate the search input field and enter "ABC"
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("ABC")
search_input.send_keys(Keys.ENTER)

driver.find_element(By.XPATH,"//h3[contains(text(),'ABC Network - ABC.com')]").click()
assert "https://abc.com/" in driver.current_url
print(driver.current_url)
driver.quit()