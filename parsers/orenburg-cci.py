# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_data(url):
    sites = []

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
        for article in soup.find_all("h2", class_="entry-title"):
            siteUrl = 'https://orensau.ru'+article.find('a')['href']
            file.write(siteUrl+'\n')
            sites.append(siteUrl)

    return sites


def main():
    filters = ['грант']  # до 20 символов
    filter = '+'.join(filters)
    searchUrl = "https://orenburg-cci.ru/?s=%s&ixsl=1" % (
        filter)

    print(get_data(searchUrl))


main()
