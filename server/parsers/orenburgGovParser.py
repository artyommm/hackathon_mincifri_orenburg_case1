# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

months = {
    'ЯНВ.': '01',
    'ФЕВ.': '02',
    'МАР.': '03',
    'АПР.': '04',
    'МАЯ': '05',
    'ИЮН.': '06',
    'ИЮЛ.': '07',
    'АВГ.': '08',
    'СЕН.': '09',
    'ОКТ.': '10',
    'НОЯ.': '11',
    'ДЕК.': '12',
}


def get_data(url, keywords, enterprises):
    articles = []
    resource = 'https://orenburg-gov.ru'

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
        for article in soup.find_all("div", class_="list__item"):
            articleHeader = article.find('a', class_="list__item-link")
            siteUrl = resource + \
                articleHeader['href']
            newsDateAttrArray = article.find(
                'div', class_="list__item-footer").find_all('div')
            newsDateAttr = None
            if len(newsDateAttrArray) == 2:
                newsDateAttr = newsDateAttrArray[1]
            else:
                newsDateAttr = newsDateAttrArray[0]

            newsDate = newsDateAttr.get_text().strip().split() if newsDateAttr else None

            if newsDate is None:
                continue

            [day, month, year] = newsDate[2], newsDate[3], newsDate[4] if newsDate else [
                'None', 'None', 'None']

            if len(day) == 1:
                day = '0' + day  # press F

            month = months[month.upper()] if newsDate else 'None'

            newsDate = '-'.join([year, month, day]) if newsDate else 'None'
            articleObject = {
                'enterprises': enterprises,
                'resource': resource,
                'news': ' '.join(articleHeader.get_text().strip().split()),
                'date': newsDate,
                'link': siteUrl,
                'keywords': keywords,
            }

            articles.append(articleObject)
        nextPageTag = soup.find(
            "a", class_="pagenav__page pagenav__page--next")

        soup = BeautifulSoup(requests.get(
            url=resource + nextPageTag['href'], headers=headers).content, "html.parser") if nextPageTag else None

    return articles


def orenburGovParser(keywords=[], enterprises=[]):
    filter = '+'.join(keywords)+'+'+'+'.join(enterprises)
    searchUrl = "https://orenburg-gov.ru/search/?q=%s" % (
        filter)

    articles = get_data(searchUrl, keywords, enterprises)
    return articles
