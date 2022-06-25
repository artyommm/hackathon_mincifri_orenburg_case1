# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_data(url, kws, cmpns):
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
    # запись в файл
    with open("index.html", "w") as file:
        for article in soup.find_all("div", class_="contentheading"):
            siteUrl = resource + article.find('a')['href']
            newsDate = r = BeautifulSoup(requests.get(
                url=siteUrl, headers=headers).content, "html.parser").find("div", class_="news_date").get_text()
            print(newsDate)
            file.write(siteUrl+'\n')
            articleObject = {
                'company': cmpns,
                'resource': resource,
                'news': article.get_text(),
                'categories': kws,
                # 'date':
            }
            articles.append(siteUrl)

    return articles


def main(keywords=[], companies=[]):
    filter = '+'.join(keywords)+'+'+'+'.join(companies)  # до 20 символов
    searchUrl = "https://orensau.ru/ru/poisk?searchword=%s&ordering=&searchphrase=all&limit=0" % (
        filter)

    print(get_data(searchUrl, keywords, companies))


keywords = ['грант']
companies = []
main(keywords, companies)
