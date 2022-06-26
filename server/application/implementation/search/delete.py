from flask import request, jsonify, make_response
from application import app, db
from application.models import Publication


@app.route('/api/delete/<publication_id>', methods=['DELETE'])
def delete(current_user, publication_id):
    publication = Publication.query.filter_by(id=publication_id).first()
    if current_user.role != 'admin':
        return make_response('Недостаточно прав!', 403)

    db.session.delete(publication)
    db.session.commit()

    return make_response('Статья успешно удалена', 403)
