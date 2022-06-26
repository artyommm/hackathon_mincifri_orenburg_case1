from flask import request, jsonify, make_response
from application import app, db
from application.common.helpers import get_all_publication_format
from application.common.templates import SEARCH_ALL_PUBLICATIONS


@app.route('/api/publications/get_all', methods=['GET'])
def get_all_publications():
    all_data = db.session.execute(SEARCH_ALL_PUBLICATIONS)
    return jsonify([get_all_publication_format(elem) for elem in all_data])


