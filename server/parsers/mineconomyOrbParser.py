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
    resource = 'https://mineconomy.orb.ru'

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
        for article in soup.find_all("div", class_="news__item"):
            articleHeader = article.find('h2', class_="news__title").find('a')
            siteUrl = resource + articleHeader['href']

            newsDateAttr = BeautifulSoup(requests.get(
                url=siteUrl, headers=headers).content, "html.parser").find('span', class_="news__info-value")

            newsDate = newsDateAttr.get_text().strip().split() if newsDateAttr else None
            [day, month, year] = newsDate if newsDate else [
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
            "a", class_="modern-page-next")
        soup = BeautifulSoup(requests.get(
            url=resource + nextPageTag['href'], headers=headers).content, "html.parser") if nextPageTag else None

    return articles


def mineconomyOrbParser(keywords=[], enterprises=[]):
    filter = '+'.join(keywords)+'+'+'+'.join(enterprises)
    searchUrl = "https://mineconomy.orb.ru/search/?q=%s" % (
        filter)

    articles = get_data(searchUrl, keywords, enterprises)
    return articles
