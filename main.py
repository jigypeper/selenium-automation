from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)

service = FirefoxService(executable_path=GeckoDriverManager().install())
options = FirefoxOptions()
options.profile = firefox_profile
driver = webdriver.Firefox(options=options, service=service)

url = "https://www.python.org/"
driver.get(url)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {
    event_times[i].text: event_names[i].text for i in range(len(event_names))
}

print(events)

driver.quit()