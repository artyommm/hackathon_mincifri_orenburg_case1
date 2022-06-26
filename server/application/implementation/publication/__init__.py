from flask import jsonify
from application import app
from application.models import Publication, publications_schema


@app.route('/api/publications/get_all')
def get_all_publications():
    all_data = Publication.query.all()
    result = publications_schema.dump(all_data)
    return jsonify(result)
