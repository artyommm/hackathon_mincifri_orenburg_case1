from flask import jsonify
from application import app
from application.models import KeyWord, keyWord_schema


@app.route('/api/keywords/get_all')
def get_all():
    all_data = KeyWord.query.all()
    result = keyWord_schema.dump(all_data)
    return jsonify(result)
