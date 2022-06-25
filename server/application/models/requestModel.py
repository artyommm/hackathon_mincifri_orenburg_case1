from application import db, ma


class Request(db.Model):
    __tablename__ = 'request'
    id = db.Column(db.Integer, primary_key=True)
    request_text = db.Column(db.Text(), nullable=False)

    def __init__(self, public_id, request_text):
        self.public_id = public_id
        self.request_text = request_text


# класс для работы с полями в таблице Request
class RequestSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'request_text')


# объекты для отправки и приёмов запросов
request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)
