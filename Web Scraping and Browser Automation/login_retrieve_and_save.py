from asyncore import write
from itertools import count
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt
service = Service('/Users/danielvillacis/Documents/chromedriver')

# Options to make browsing chrome easier
def get_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")      # to get greater privileges
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    url = "http://automated.pythonanywhere.com/login/"
    driver.get(url)
    return driver


def clean_text(text):
    """Extract only the temperature from the text"""
    output = float(text.split(": ")[1])
    return output


def write_file(text):
    file_name = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(file_name, 'w') as file:
        file.write(text)


def main():
    driver = get_chrome_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN) # Keys.RETURN = pressing the enter key on the keyboard
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    #element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    while True:
        time.sleep(3)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)

print(main())