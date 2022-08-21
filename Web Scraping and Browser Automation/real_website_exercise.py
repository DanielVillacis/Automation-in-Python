from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
    url = "https://www.bestbuy.ca/identity/en-ca/signin?tid=dbwmIiycoNHY%252BW9EK96oJy4i9uNzsIissMdOI5k7Wr5sGNzUJJpQ4ryLSG1Gr9%252B9aEIH0eFwnZJVtgE2F30MYHWrJnkSF%252BG3gPw0ObIkVYehgXMmtVIqYH7hGpvyVcmtFVQ%252FYNr8lDh5XG1no442k%252FUQBCjRI7Iy0LRilzBTPwQ0z0f%252BCFxrRGcy8v5gDEKM07TrZpSXCunNU4kqcGqmMOmdxJEn0VUeHtWf9UUwkUT6%252B3r266%252F3oBtZMMW3TUQlCPTQwElO6f%252BpMOwcaK2H7Ht6Q3jANxaaCnfe6ClM9shcWW7cXsC35pRsGAEXH1wX"
    driver.get(url)
    return driver


def clean_text(text):
    """Extract only the temperature from the text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_chrome_driver()
    driver.find_element(by="id", value="username").send_keys("daniel1997v@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="password").send_keys("drve1997" + Keys.RETURN) # Keys.RETURN = pressing the enter key on the keyboard
    time.sleep(2)
    #driver.find_element(by="xpath", value="").click()
    #time.sleep(2)
    #element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")


print(main())