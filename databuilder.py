from GoogleNews import GoogleNews
import datetime
from newspaper import Article
from newspaper import Config
import pandas as pd
import concurrent.futures

MAX_THREADS = 30

tickers = ['AMC', 'AAPL', 'GME', 'AMZN', 'GOOG', 'TSLA', 'MSFT', 'ABT', 'SNDL', 'NAKD', 'T', 'GE', 'XOM', 'SNAP', 'MSFT', 'NVDA']

def download(title, url, description):
    url = 'https://' + url
    try:
        a = Article(url)
        a.download()
        a.parse()
        a.nlp()
        return title, url, description, a.text
    except Exception:
        return title, url, description, None

def download_articles(titles, article_urls, descriptions):
    
    threads = min(MAX_THREADS, len(article_urls))

    data = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
       for title, url, description, text in executor.map(download, titles, article_urls, descriptions):
           data.append((title, url, description, text))
    return data

def setup():

    # grab date from a year ago
    end = datetime.datetime.now()
    days = datetime.timedelta(days = 365)
    start = end - days
    end = end.date()
    start = start.date()

    # setup GoogleNews
    googlenews = GoogleNews(lang='en')
    googlenews.set_time_range(start, end)
    googlenews.set_encode('utf-8')

    for ticker in tickers:
        googlenews.get_news(ticker)
    
    # grab results
    results = googlenews.results()
    
    titles = []
    links = []
    desc = []

    for result in results:
        titles.append(result['title'])
        links.append(result['link'])
        desc.append(result['desc'])

    data = download_articles(titles, links, desc)

    # create DataFrame
    df = pd.DataFrame(data, columns=['title', 'url', 'desc', 'text']) 

    print(df.head())

    df.to_csv('dataset.csv', index=False)

if __name__ == "__main__":
    setup()

    