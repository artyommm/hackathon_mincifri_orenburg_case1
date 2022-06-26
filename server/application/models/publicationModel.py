from application import db, ma


class Publication(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    date_of_publication = db.Column(db.Date, nullable=False)
    publication_url = db.Column(db.Text, nullable=False)
    information_resource = db.Column(db.Text, nullable=False)

    # отношения с другими таблицами
    enterprise_id = db.Column(db.Integer(), db.ForeignKey('enterprise.id'))
    keyWord_id = db.Column(db.Integer(), db.ForeignKey('keyword.id'))

    def __init__(self, title, date_of_publication, publication_url, enterprise_id, information_resource,keyWord_id):
        self.title = title
        self.date_of_publication = date_of_publication
        self.publication_url = publication_url
        self.enterprise_id = enterprise_id
        self.information_resource = information_resource
        self.keyWord_id = keyWord_id

    def __eq__(self, other):
        return self.title == other.title


# класс для работы с полями в таблице User
class PublicationSchema(ma.Schema):
    class Meta:
        fields = (
            'title', 'date_of_publication', 'publication_url', 'enterprise_id', 'information_resource', 'keyWord_id')


# объекты для отправки и приёмов запросов
publication_schema = PublicationSchema()
publications_schema = PublicationSchema(many=True)
