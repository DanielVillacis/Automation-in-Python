from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
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
    url = "http://automated.pythonanywhere.com"
    driver.get(url)
    return driver


def clean_text(text):
    """Extract only the temperature from the text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_chrome_driver()
    time.sleep(2)
    #element1 = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    element2 = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    #print(element1.text)
    return clean_text(element2.text)
    
print(main())