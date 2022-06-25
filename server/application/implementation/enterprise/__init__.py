from flask import jsonify
from application import app
from application.models import Enterprise, enterprise_schema

@app.route('/api/enterprises/get_all')
def get_all_enterprises():
    all_data = Enterprise.query.all()
    result = enterprise_schema.dump(all_data)
    return jsonify(result)
