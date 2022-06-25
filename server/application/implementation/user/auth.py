from functools import wraps
from datetime import datetime, timedelta
from pytz import timezone

import jwt
from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash

from application import app
from application.models import User, user_schema
from application.common.const import ERROR_MESSANGES, ERROR_CODES, STANDART_SESSION_TIME


def token_required(function):
    """
    Обертка для идентификации пользователя по токену
    :param function: оборачиваемая функция или метод
    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        request_get = request.headers.get('Authorization')
        token = request_get.split(' ')[1] if request_get else None
        if not token:
            return make_response(ERROR_MESSANGES['no_token'], ERROR_CODES['conflict'])

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(id=data['id'].first())
        except Exception:
            return make_response(ERROR_MESSANGES['token_timeout'], ERROR_CODES['conflict'])

        return function(current_user, *args, **kwargs)
    return wrapper


@app.route('/api/auth/auth')
def login():
    """
    Авторизация
    :return:
    """
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response(ERROR_MESSANGES['no_login_or_pass'], ERROR_CODES['unauthorized'])

    user = User.query.filter_by(mail=auth.username).first()
    if not user:
        return make_response(ERROR_MESSANGES['no_user'], ERROR_CODES['unauthorized'])

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.now(timezone('Europe/Moscow')) + timedelta(minutes=STANDART_SESSION_TIME)
        }, app.config['SECRET_KEY'])

        result = user_schema.dump(user)

        return jsonify({
            'token': token.decode('UTF-8'),
            'user': {
                'id': result.id,
                'login': result.login,
                'role': result.role
            }
        })

    return make_response(ERROR_MESSANGES['incorrect_password'], ERROR_CODES['unauthorized'])
