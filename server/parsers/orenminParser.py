# https://orenmin.ru/
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
    resource = 'https://orenmin.ru'

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

    for article in soup.find_all("dt", class_="result-title"):
        articleHeader = article.find('a')
        siteUrl = resource + articleHeader['href']

        newsDateAttr = article.find_next('dd', class_="result-created")

        newsDate = newsDateAttr.get_text().strip().split() if newsDateAttr else None

        if newsDate is None:
            continue

        [day, month, year] = newsDate[1], newsDate[2], newsDate[3] if newsDate else [
            'None', 'None', 'None']

        if len(day) == 1:
            day = '0' + day  # press F

        month = months[month.upper()] if newsDate else 'None'

        newsDate = '-'.join([year, month, day]) if newsDate else 'None'
        articleObject = {
            'enterprises': enterprises,
            # 'resource': resource,
            'resource': "Оренбургские минералы",
            'news': articleHeader.get_text().strip(),
            'date': newsDate,
            'link': siteUrl,
            'keywords': keywords,
        }

        articles.append(articleObject)

    return articles


def orenminParser(keywords=[], enterprises=[]):
    filter = '+'.join(keywords)+'+'+'+'.join(enterprises)
    searchUrl = "https://orenmin.ru/component/search/?searchword=%s&ordering=newest&searchphrase=all&limit=0" % (
        filter)

    articles = get_data(searchUrl, keywords, enterprises)
    return articles
