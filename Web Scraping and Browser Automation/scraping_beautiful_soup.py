# Beautiful soup is a library dedicated for web data scraping, 
# unlike selenium which is more used for automation.
from bs4 import BeautifulSoup
import requests

def get_currency_rate(from_currency, to_currency, amount):
    url = f"https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')  # Specify that we're looking into an html file
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])   # we only want the numbers output so we don't include the last 4 characters
    return rate



current_rate = get_currency_rate('CAD', 'EUR', '100')
print(current_rate)
