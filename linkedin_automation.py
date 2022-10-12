from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import os

from selenium.webdriver.common.keys import Keys

firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", True)

service = FirefoxService(executable_path=GeckoDriverManager().install())
options = FirefoxOptions()
options.profile = firefox_profile
driver = webdriver.Firefox(options=options, service=service)

linkedin_id = os.environ.get("LINKEDIN_ID")
linkedin_key = os.environ.get("LINKEDIN_KEY")

url = "https://www.linkedin.com/jobs/search/?currentJobId=3305115410&f_AL=true&f_E=2%2C3&f_JT=F&f_TPR=r604800&f_WT=2%2C3&geoId=101165590&keywords=python%20engineer&location=United%20Kingdom&refresh=true&sortBy=R"

driver.get(url)

login_button = driver.find_element(By.LINK_TEXT, "Sign in")

login_button.click()

time.sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "#username")

username.send_keys(linkedin_id)

password = driver.find_element(By.CSS_SELECTOR, "#password")

password.send_keys(linkedin_key)

time.sleep(2)

password.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

