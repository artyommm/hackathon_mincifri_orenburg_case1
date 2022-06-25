from application import db, ma


class Enterprise(db.Model):
    __tablename__ = 'enterprise'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    # отношения с другими таблицами
    publication = db.relationship('Publication', backref='enterprise')

    def __init__(self, public_id, name):
        self.public_id = public_id
        self.name = name


# класс для работы с полями в таблице Enterprise
class EnterpriseSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'name')


# объекты для отправки и приёмов запросов
enterprise_schema = EnterpriseSchema()
enterprises_schema = EnterpriseSchema(many=True)
