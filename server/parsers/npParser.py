import requests
from bs4 import BeautifulSoup


def get_data(url, keywords, enterprises):
    articles = []
    resource = 'https://56np.ru'

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip',
        'Accept-Charset': 'utf-8',
        'content-Type': 'charset=utf-8',
        'cache-control': 'max-age=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'
    }

    r = requests.get(
        url=url, headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")

    while soup is not None:
        for article in soup.find_all(
                'a', class_='search-link'):

            articleHeader = article
            siteUrl = articleHeader['href']

            newsDateAttr = BeautifulSoup(requests.get(
                url=siteUrl, headers=headers).content, "html.parser").find('time')

            newsDateAttr = newsDateAttr['datetime'] if newsDateAttr else None

            if newsDateAttr is None:
                continue

            newsDate = newsDateAttr.strip().split(
                'T')[0] if newsDateAttr else None

            articleObject = {
                'enterprises': enterprises,
                # 'resource': resource,
                'resource': "Оренбургская область. Национальные проекты",
                'news': articleHeader.get_text().strip(),
                'date': newsDate,
                'link': siteUrl,
                'keywords': keywords,
            }

            articles.append(articleObject)
        nextPageTag = soup.find(
            "span", class_='page-numbers current')

        nextPageTag = nextPageTag.find_next('a', class_='page-numbers')

        soup = BeautifulSoup(requests.get(
            url=nextPageTag['href'], headers=headers).content, "html.parser") if nextPageTag else None

    return articles


def npParser(keywords=[], enterprises=[]):
    filter = '+'.join(keywords)+'+'+'+'.join(enterprises)
    searchUrl = "https://56np.ru/?s=%s" % (
        filter)

    articles = get_data(searchUrl, keywords, enterprises)
    return articles
