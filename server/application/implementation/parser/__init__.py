from datetime import date
from flask import request, jsonify, make_response
from application import app, db
from application.models import Publication
from application.common.templates import GET_ALL
from parsers.mainParser import getParser, parserDict
from application.common.helpers import parse_date

FIND_RESOURCE = list(parserDict.keys())


@app.route('/api/parser/insert_data/')
def insert():
    enterprises = db.session.execute(GET_ALL.format('enterprise')).fetchall()
    keywords = db.session.execute(GET_ALL.format('keyword')).fetchall()

    enterprises_keywords = []
    for enterprise in enterprises:
        enterprises_keywords.extend([(enterprise[1], keyword[1]) for keyword in keywords])

    for link in FIND_RESOURCE:
        resource_parser = getParser(link)
        if not resource_parser:
            continue

        for ek in enterprises_keywords:
            data = resource_parser([ek[1]], [ek[0]])
            new_publications = set([get_publication_obj(elem, enterprises, keywords) for elem in data])
            old_publications = set(Publication.query.filter_by(information_resource=link).all())
            publications = new_publications - old_publications
            for publication in publications:
                db.session.add(publication)
            db.session.commit()


def get_publication_obj(data, enterprises_list, keywords_list):
    title = data['news']
    date = parse_date(data['date'])
    link = data['link']
    enterprise = get_enterprise_id(data['enterprises'][0], enterprises_list)
    ir = data['resource']
    keyword = get_keyword_id(data['keywords'][0], keywords_list)
    return Publication(title, date, link, enterprise, ir, keyword)


def get_enterprise_id(elem, enterprises):
    result = list(filter(lambda x: x[1] == elem, enterprises))
    return result[0][0] if result else None


def get_keyword_id(elem, keywords):
    result = list(filter(lambda x: x[1] == elem, keywords))
    return result[0][0] if result else None
