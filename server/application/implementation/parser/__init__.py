from datetime import date
from flask import request, jsonify, make_response
from application import app, db
from application.models import Publication


@app.route('/api/parser/insert_data')
def insert(link):
    data = parser(link)
    publications = [get_publication_obj(elem) for elem in data]
    db.session.add(publications)
    db.session.commit()


def parser(link):
    return []


def get_publication_obj(data):
    title = data['news']
    date = data['date']
    link = data['link']
    enterprise = data['enterprises']
    ir = data['resource']
    keywords = ['keywords']
    return Publication(title, date, link, enterprise, ir)
