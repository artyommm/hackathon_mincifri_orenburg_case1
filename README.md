# Запуск проекта
Для запуска проекта необходимо:  
1. Создать базу данных, используя СУБД PostgreSQL.
2. Зайти в _server/application/__init__.py_ и указать в параметре  конфигурации *app.config['SQLALCHEMY_DATABASE_URI']* строку соединения с БД по формату: _[СУБД]://[Имя пользователя]:[Пароль]@[Хост]:[Порт]/[Имя БД]_
3. Зайти в папку _server_ и запустить из неё терминал. В терминале ввести следующее:
```
python
from make_db import make_db
from application.implementation import make_user
make_db()
make_user('Имя пользователя', 'Пароль', 'admin')
```
4. Запустить приложение следующей командой
```
python start.py
```
5. Дальнейшие инструкции в папке _client_