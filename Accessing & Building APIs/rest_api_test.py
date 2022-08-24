from webbrowser import get
import requests

# url = "https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-7-27&to=2022-7-28&sortBy=popularity&language=en&apiKey=fe84376250a8402cbf9056123198aac7"
# req = requests.get(url)
# content = req.json()

# articles = content['articles']

# for article in articles:
#     print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])


def get_news(topic, from_date, to_date, language='en', api_key='fe84376250a8402cbf9056123198aac7'):     # api key setted to default value for now
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language=en&apiKey={api_key}'
    req = requests.get(url)
    content = req.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"'TITLE\n',{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(topic='cars', from_date='2022-07-28', to_date='2022-07-30'))



