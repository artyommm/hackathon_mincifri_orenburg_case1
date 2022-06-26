from flask import request, jsonify, make_response
from application import app, db
from application.models import Publication
from application.implementation import token_required


@app.route('/api/delete/<publication_id>', methods=['DELETE'])
@token_required
def delete(current_user, publication_id):
    publication = Publication.query.filter_by(id=publication_id).first()
    if current_user.role != 'admin':
        return make_response('Недостаточно прав!', 403)

    if not publication:
        return make_response('Произошла неизвестная ошибка', 404)

    db.session.delete(publication)
    db.session.commit()

    return make_response('Публикация успешно удалена', 200)
