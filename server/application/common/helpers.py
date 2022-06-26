import datetime


def parse_date(string):
    data_str = string.split('-')
    data_int = [int(elem.strip()) for elem in data_str]
    return datetime.date(year=data_int[0], month=data_int[1], day=data_int[2])


def get_publication_format(data):
    return {
        'id': data[0],
        'title': data[1],
        'date_of_publication': data[2],
        'publication_url': data[3],
        'enterprise': data[4],
        'information_resource': data[5],
        'keyword': data[6]
    }


def get_all_publication_format(data):
    return {
        'id': data[0],
        'enterprise': data[1],
        'information_resource': data[2],
        'title': data[3],
        'date_of_publication': data[4],
        'publication_url': data[5],
        'keyword': data[6]
    }
