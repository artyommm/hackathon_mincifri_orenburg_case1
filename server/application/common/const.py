APPLICATION_NAME = 'OrenBoogle'
STANDART_SESSION_TIME = 120

ERROR_MESSANGES = {
    'no_token': 'Ошибка авторизации. Токен не найден!',
    'token_timeout': 'Ошибка авторизации. Время сеанса истекло!',
    'no_login_or_pass': 'Ошибка авторизации. Не введёны имя пользователя или пароль!',
    'no_user': 'Ошибка авторизации. Такой пользователь не найден!',
    'incorrect_password': 'Ошибка авторизации. Введённый пароль не верен!',
    'bad_params': 'Ошибка запроса. Были переданы неправильные параметры фильтра!'
}

RESPONSE_CODES = {
    'conflict': 409,
    'unauthorized': 401,
    'bad_request': 400
}
