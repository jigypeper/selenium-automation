from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

from selenium.webdriver.common.keys import Keys

firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", True)

service = FirefoxService(executable_path=GeckoDriverManager().install())
options = FirefoxOptions()
options.profile = firefox_profile
driver = webdriver.Firefox(options=options, service=service)

url = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(url)

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

i = 0

while i < 100000:

    cookie.click()

    money = int(driver.find_element(By.CSS_SELECTOR, "#money").text)

    store_items = [item.text.split(" - ")[0] for item in driver.find_elements(By.CSS_SELECTOR, "#store b") if item.text != ""]

    store_costs = [int(cost.text.split("- ")[1].replace(",", "")) for cost in driver.find_elements(By.CSS_SELECTOR, "#store b") if cost.text != ""]

    store = {
        store_items[i]: store_costs[i] for i in range(len(store_items))
    }

    time.sleep(0.01)
    i += 1

    while i % 5 == 0:
        for key in store:
            if money > store[key]:
                buy = driver.find_element(By.CSS_SELECTOR, f"#buy{key}")
                buy.click()
        i += 1

    print(store)





