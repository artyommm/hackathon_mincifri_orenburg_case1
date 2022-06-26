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

FIND_RESOURCE = [
    r'https://orenburg-cci.ru/',
    r'https://orenburg-gov.ru/',
    r'https://mineconomy.orb.ru/',
    r'https://orenmin.ru/',
    r'https://orensau.ru/',
    r'https://fips.ru/'
]

KEYWORDS = [
    'технологии', 'импортозамещение', 'инновации', 'научные разработки',
    'патенты', 'гранты', 'исследования', 'технология', 'импортозамещение',
    'инновация', 'научная разработка', 'патенты', 'грант', 'исследование'
]

ENTERPRISES = [
    'Газпром'
]
