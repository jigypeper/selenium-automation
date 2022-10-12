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

twitter_id = os.environ.get("TWITTER_ID")
twitter_key = os.environ.get("TWITTER_KEY")


class InternetSpeedTwitterBot:

    def __init__(self):
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("javascript.enabled", True)

        service = FirefoxService(executable_path=GeckoDriverManager().install())
        options = FirefoxOptions()
        options.profile = firefox_profile
        self.driver = webdriver.Firefox(options=options, service=service)

        self.down = 455
        self.actual_speed = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        time.sleep(5)
        privacy = self.driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
        privacy.click()
        time.sleep(5)
        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        time.sleep(30)
        self.actual_speed = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        time.sleep(5)
        return self.actual_speed

    def tweet_at_provider(self):
        url = "https://twitter.com/login"
        self.driver.get(url)
        time.sleep(3)
        username = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        username.send_keys(twitter_id)
        next_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_button.click()
        time.sleep(3)
        password = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        time.sleep(3)
        password.send_keys(twitter_key)
        password.send_keys(Keys.ENTER)
        tweet = f"@VodafoneUK, why is my internet running slow? {self.actual_speed}MB, I'm paying for 900MB."
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        time.sleep(5)
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        tweet_button.click()
        time.sleep(3)


if __name__ == "__main__":

    twitter = InternetSpeedTwitterBot()
    speed = twitter.get_internet_speed()
    print(speed)
    if speed <= twitter.down:
        twitter.tweet_at_provider()
        twitter.driver.quit()

