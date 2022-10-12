from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from selenium.webdriver.common.keys import Keys

firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)

service = FirefoxService(executable_path=GeckoDriverManager().install())
options = FirefoxOptions()
options.profile = firefox_profile
driver = webdriver.Firefox(options=options, service=service)

url = "http://secure-retreat-92358.herokuapp.com/"

driver.get(url)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Ahaaa")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Ahahaaa")
email = driver.find_element(By.NAME, "email")
email.send_keys("ahaaa.ahahaaa@email.com")

button = driver.find_element(By.CSS_SELECTOR, "form button")

button.click()