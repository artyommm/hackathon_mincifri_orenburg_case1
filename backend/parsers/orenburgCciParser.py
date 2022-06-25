# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_data(url, keywords, enterprises):
    articles = []
    resource = 'https://orenburg-cci.ru/'

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
        for article in soup.find_all("h2", class_="entry-title"):
            siteUrl = article.find('a')['href']
            newsDateAttr = BeautifulSoup(requests.get(
                url=siteUrl, headers=headers).content, "html.parser").find("span", class_="news-date")
            newsDate = newsDateAttr.get_text().strip() if newsDateAttr else None
            [day, month, year] = newsDate.split(
                '.') if newsDate else ['None', 'None', 'None']

            newsDate = '.'.join([day, month, year]) if newsDate else 'None'
            articleObject = {
                'enterprises': enterprises,
                'resource': resource,
                'news': ' '.join(article.get_text().strip().split()),
                'date': newsDate,
                'link': siteUrl,
                'categories': keywords,
            }

            articles.append(articleObject)
        nextPageTag = soup.find("div", class_="nav-previous")
        soup = BeautifulSoup(requests.get(
            url=nextPageTag.find('a')['href'], headers=headers).content, "html.parser") if nextPageTag else None

    return articles


def orenburgCciParser(keywords=[], enterprises=[]):
    filter = '+'.join(keywords)+'+'+'+'.join(enterprises)  # до 20 символов
    searchUrl = "https://orenburg-cci.ru/?s=%s&ixsl=1" % (
        filter)

    articles = get_data(searchUrl, keywords, enterprises)
    return articles
