from datetime import date
from flask import request, jsonify, make_response
from application import app, db
from application.models import Publication


@app.route('/api/parser/insert_data')
def insert(link):
    data = parser(link)
    publications = []


def parser(link):
    pass


def get_publication_obj(data):
    title = data['news']
    date = data['date']
    link = data['link']
    enterprise = data['enterprise']
