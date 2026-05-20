from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import os
PASSWORD = os.getenv("INSTAPASS")
SIMILAR_ACCOUNT="sophieraiin"
a=webdriver.Chrome()
a.get("https://www.instagram.com/?hl=en")
sleep(2)
b=a.find_element(By.NAME,value="email")
b.send_keys("sarah_66512")
b.send_keys(Keys.ENTER)
b=a.find_element(By.NAME,value="pass")
b.send_keys(PASSWORD)
b.send_keys(Keys.ENTER)
sleep(6)
input("solve captcha")#it pauses the execution until u solve the captcha(if any),solve it and hit enter in idle
print("resuming")
d = a.find_element(By.CSS_SELECTOR, value="._aswp._aswr._aswu._asw_._asx2")
d.click()
sleep(3)
e = a.find_element(By.CSS_SELECTOR, value="._a9--._ap36._a9_1")
e.click()
a.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
sleep(3)
element = a.find_element(By.LINK_TEXT, "8.7M followers")#change it based on how many followers she has 
element.click()
sleep(2)
buttons = a.find_elements(By.CSS_SELECTOR, value="button")

for button in buttons:
    if button.text == "Follow":
        try:
            print(button.text)
            a.execute_script("arguments[0].scrollIntoView(true);", button)
            sleep(1)
            button.click()
            sleep(2)
        except ElementClickInterceptedException:
            try:
                a.execute_script("arguments[0].click();", button)
                sleep(2)
            except Exception:
                sleep(1)
                try:
                    cancel_button = a.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                except NoSuchElementException:
                    pass
