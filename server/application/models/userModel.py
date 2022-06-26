from application import db, ma


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(45), nullable=False)

    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role


# класс для работы с полями в таблице User
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'login', 'password', 'role')


# объекты для отправки и приёмов запросов
user_schema = UserSchema()
users_schema = UserSchema(many=True)
