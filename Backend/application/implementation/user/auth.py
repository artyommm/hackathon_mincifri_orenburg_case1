from functools import wraps
from datetime import datetime, timedelta

import jwt
from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash

from application import app
from application.models import User
from common.const import ERROR_MESSANGES, ERROR_CODES


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

    # пока не работает
    # if check_password_hash(user.password, auth.password):
    #     token = jwt.encode({
    #         'public_id': user.public_id,
    #         'exp': datetime.now(pytz.timezone('Europe/Moscow')) + timedelta(minutes=60)
    #     }, app.config['SECRET_KEY'])
    #
    #     result = user_schema.dump(user)
    #     passport = Passport.query.filter_by(user_id=user.id).first()
    #     snils = Snils.query.filter_by(user_id=user.id).first()
    #     patient = Patient.query.filter_by(user_id=user.id).first()
    #
    #     if not passport:
    #         passport = Passport(None, None, None)
    #
    #     if not snils:
    #         snils = Snils(None, None)
    #
    #     if not patient:
    #         patient = Patient(None, None)
    #
    #     return jsonify({
    #         'token': token.decode('UTF-8'),
    #         'user': {
    #             'user': result,
    #             'passport': {
    #                 'series': passport.series,
    #                 'number': passport.number
    #             },
    #             'snils': snils.number,
    #             'anamnesis': patient.anamnesis
    #         }
    #     })

    return make_response(ERROR_MESSANGES['incorrect_password'], ERROR_CODES['unauthorized'])
