import requests
from bs4 import BeautifulSoup


def get_data(url, keywords, enterprises):
    articles = []
    resource = 'https://fips.ru'

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

    soup = BeautifulSoup(r.content, "html.parser").find(
        'div', class_='search-page')

    while soup is not None:
        for article in soup.find_all("a"):
            if article.parent.name == 'small' or\
                article.find('div') or \
                article.get_text().strip() in ['Главная', 'О ФИПС', 'Всероссийская патентно-техническая библиотека',
                                               'Новости', 'Архив новостей', 'Сортировать по дате', 'След.', 'Конец',
                                               'fips@rupto.ru', 'Новости', 'Документы', 'Вакансии', 'Глоссарий',
                                               'Ссылки', 'Ответы на вопросы', 'О сайте', 'Карта сайта', 'Как проехать',
                                               'Сообщить о ошибке', 'Начало', 'Пред.', 'Правила приема заявок',
                                               '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                               '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']:
                continue
            articleHeader = article
            siteUrl = resource + articleHeader['href']

            newsDateAttr = article.find_next('small')

            newsDate = newsDateAttr.get_text().strip().split(' ')[
                1] if newsDateAttr else None

            if newsDate is None:
                continue

            [day, month, year] = newsDate.split('.') if newsDate else [
                'None', 'None', 'None']

            newsDate = '-'.join([year, month, day]) if newsDate else 'None'
            articleObject = {
                'enterprises': enterprises,
                'resource': resource,
                'news': articleHeader.get_text().strip(),
                'date': newsDate,
                'link': siteUrl,
                'keywords': keywords,
            }

            articles.append(articleObject)
        nextPageTag = soup.find(
            "a", text="След.")
        print(nextPageTag)
        soup = BeautifulSoup(requests.get(
            url=resource + nextPageTag['href'], headers=headers).content, "html.parser").find(
            'div', class_='search-page') if nextPageTag else None

    return articles


def fipsParser(keywords=[], enterprises=[]):
    filter = '+'.join(keywords)+'+'+'+'.join(enterprises)
    searchUrl = "https://fips.ru/search/?q=%s" % (
        filter)

    articles = get_data(searchUrl, keywords, enterprises)
    return articles
