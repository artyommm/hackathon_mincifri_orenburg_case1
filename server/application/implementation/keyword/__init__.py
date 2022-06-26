from flask import jsonify
from application import app
from application.models import KeyWord, keyWords_schema


@app.route('/api/keywords/get_all')
def get_all():
    all_data = KeyWord.query.all()
    result = keyWords_schema.dump(all_data)
    return jsonify(result)
