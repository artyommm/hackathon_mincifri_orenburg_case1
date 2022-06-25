from application import db, ma


class InformationResource(db.Model):
    __tablename__ = 'informationresource'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    # отношения с другими таблицами
    publication = db.relationship('Publication', backref='informationresource')

    def __init__(self, public_id, name):
        self.public_id = public_id
        self.name = name


# класс для работы с полями в таблице InformationResource
class InformationResourceSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'name')


# объекты для отправки и приёмов запросов
informationResource_schema = InformationResourceSchema()
informationResources_schema = InformationResourceSchema(many=True)
