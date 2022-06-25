# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

months = {
    'ЯНВАРЯ': '01',
    'ФЕВРАЛЯ': '02',
    'МАРТА': '03',
    'АПРЕЛЯ': '04',
    'МАЯ': '05',
    'ИЮНЯ': '06',
    'ИЮЛЯ': '07',
    'АВГУСТА': '08',
    'СЕНТЯБРЯ': '09',
    'ОКТЯБРЯ': '10',
    'НОЯБРЯ': '11',
    'ДЕКАБРЯ': '12',
}


def get_data(url, keywords, enterprises):
    articles = []
    resource = 'https://orensau.ru'

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

    for article in soup.find_all("div", class_="contentheading"):
        siteUrl = resource + article.find('a')['href']

        newsDateAttr = BeautifulSoup(requests.get(
            url=siteUrl, headers=headers).content, "html.parser").find("div", class_="news_date")
        newsDate = newsDateAttr.get_text().strip() if newsDateAttr else None

        [day, month, year] = newsDate.split(
            ' ') if newsDate else ['None', 'None', 'None']

        month = months[month.upper()] if newsDate else 'None'

        newsDate = '.'.join([day, month, year]) if newsDate else 'None'
        articleObject = {
            'enterprises': enterprises,
            'resource': resource,
            'news': ' '.join(article.get_text().strip().split()),
            'date': newsDate,
            'link': siteUrl,
            'keywords': keywords,
        }

        articles.append(articleObject)

    return articles


def orensauParser(keywords=[], enterprises=[]):
    filter = '+'.join(keywords)+'+'+'+'.join(enterprises)  # до 20 символов
    searchUrl = "https://orensau.ru/ru/poisk?searchword=%s&ordering=&searchphrase=all&limit=0" % (
        filter)

    articles = get_data(searchUrl, keywords, enterprises)
    return articles
