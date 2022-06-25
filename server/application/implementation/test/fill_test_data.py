from flask import make_response
from application import app, db
from application.models import KeyWord, InformationResource, Enterprise


@app.route('/api/fill_test_data/')
def make_envinronment():
    """
    Заполнить БД вспомогательными тестовыми сущностями
    :return:
    """
    keywords_amount, ir_amount, enterprises_amount = 10, 10, 10
    keywords = [get_keyword(i) for i in range(1, keywords_amount+1)]
    information_resources = [get_information_resource(i) for i in range(1, ir_amount)]
    enterprises = [get_enterprises(i) for i in range(1, enterprises_amount)]

    for keyword in keywords:
        obj = KeyWord(keyword['id'], keyword['name'])
        db.session.add(obj)

    for ir in information_resources:
        obj = InformationResource(ir['id'], ir['name'])
        db.session.add(obj)

    for enterprise in enterprises:
        obj = Enterprise(enterprise['id'], enterprise['name'])
        db.session.add(obj)
    db.session.commit()
    return make_response('Записи успешно добавлены', 200)


def get_publications():
    return {

    }


def get_keyword(number):
    return {
        'id': number,
        'name': f'keyword_{number}'
    }


def get_information_resource(number):
    return {
        'id': number,
        'name': f'information_resource_{number}'
    }


def get_enterprises(number):
    return {
        'id': number,
        'name': f'enterprises_{number}'
    }
