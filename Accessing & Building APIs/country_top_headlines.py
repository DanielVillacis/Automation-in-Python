from webbrowser import get
import requests


def get_news(country, api_key='fe84376250a8402cbf9056123198aac7'):     # api key setted to default value for now
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    req = requests.get(url)
    content = req.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"'TITLE\n',{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(country='us'))