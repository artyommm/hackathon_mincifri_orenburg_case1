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
        'enterprise_id': data[4],
        'informationRecource_id': data[5]
    }