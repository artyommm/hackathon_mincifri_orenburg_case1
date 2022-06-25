from flask import request, jsonify
from application import app


@app.route('/api/search/', methods=['GET'])
def search():
    data = request.json
    keywords = data.get('keywords')
    companies = data.get('companies')
    date = data.get('date')
    