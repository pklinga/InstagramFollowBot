from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service(ChromeDriverManager().install())

INSTAGRAM_USERNAME = "" #Your Instagram account's username comes here
INSTAGRAM_PASSWORD = "" #Your Instagram account's password comes here
SIMILAR_ACCOUNT = "" #Similar Instagram page to your interest (with large number of followers) comes here

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        cookies = self.driver.find_element(by=By.CLASS_NAME, value="HoLwm")
        cookies.click()
        time.sleep(2)
        username = self.driver.find_element(by=By.NAME, value="username")
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys(INSTAGRAM_PASSWORD)
        login_button = self.driver.find_element(by=By.CLASS_NAME, value="y3zKF")
        login_button.click()
        time.sleep(10)
        not_now_button = self.driver.find_element(by=By.CLASS_NAME, value="HoLwm")
        not_now_button.click()
        time.sleep(2)

    def find_followers(self):
        search = self.driver.find_element(by=By.CLASS_NAME, value="DljaH")
        search.send_keys(SIMILAR_ACCOUNT)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        similar_account = self.driver.find_element(by=By.CLASS_NAME, value="-qQT3")
        similar_account.click()
        time.sleep(5)
        followers = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(5)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
        scrollable_popup = self.driver.find_element(By.CLASS_NAME, "isgrP")
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)


follow_accounts = InstaFollower()
follow_accounts.login()
follow_accounts.find_followers()
follow_accounts.follow()
time.sleep(600)
