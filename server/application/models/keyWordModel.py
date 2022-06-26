from application import db, ma


class KeyWord(db.Model):
    __tablename__ = 'keyword'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    def __init__(self, name):
        self.name = name


# класс для работы с полями в таблице KeyWord
class KeyWordSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'name')


# объекты для отправки и приёмов запросов
keyWord_schema = KeyWordSchema()
keyWords_schema = KeyWordSchema(many=True)
