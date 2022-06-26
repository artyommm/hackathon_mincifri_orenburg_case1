from datetime import date
from flask import request, jsonify, make_response
from application import app, db
from application.models import Publication
from application.common.const import FIND_RESOURCE
from application.common.templates import GET_ALL
from parsers.fipsParser import fipsParser
from application.common.helpers import parse_date


@app.route('/api/parser/insert_data/')
def insert():
    enterprises = [elem[1] for elem in db.session.execute(GET_ALL.format('enterprise')).fetchall()]
    keywords = [elem[1] for elem in db.session.execute(GET_ALL.format('keyword')).fetchall()]

    enterprises_keywords = []
    for enterprise in enterprises:
        enterprises_keywords.extend([(enterprise, keyword) for keyword in keywords])

    for ek in enterprises_keywords:
        data = fipsParser([ek[0]], [ek[1]])
        publications = [get_publication_obj(elem) for elem in data]
        for publication in publications:
            db.session.add(publication)
            db.session.commit()


def get_publication_obj(data):
    title = data['news']
    date = parse_date(data['date'])
    link = data['link']
    enterprise = data['enterprises']
    ir = data['resource']
    keywords = ['keywords']

    return Publication(title, date, link, enterprise, ir)
