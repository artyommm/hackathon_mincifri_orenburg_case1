from application import db, ma


class Publication(db.Model):
    #__table_args__ = {'extend_existing': True}
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45), nullable=False)
    date_of_publication = db.Column(db.Date, nullable=False)
    publication_url = db.Column(db.String(200), nullable=False)

    # промежуточные таблицы для создания отношений----------------------------------------------------------------

    # публикация_ключевоеслово
    publication_keyword = db.Table('publication_keyword',
                                   db.Column('publication_id', db.Integer, db.ForeignKey('publication.id')),
                                   db.Column('keyword_id', db.Integer, db.ForeignKey('keyword.id'))
                                   )
    # публикация_запрос
    publication_request = db.Table('publication_request',
                                   db.Column('publication_id', db.Integer, db.ForeignKey('publication.id')),
                                   db.Column('request_id', db.Integer, db.ForeignKey('request.id'))
                                   )
    # -------------------------------------------------------------------------------------------------------------

    # отношения с другими таблицами
    keyWord_id = db.relationship('KeyWord', secondary=publication_keyword,
                                 backref=db.backref('publication', lazy='select'))

    request_id = db.relationship('Request', secondary=publication_request,
                                 backref=db.backref('publication', lazy='select'))

    enterprise_id = db.Column(db.Integer(), db.ForeignKey('enterprise.id'))

    informationResource_id = db.Column(db.Integer(), db.ForeignKey('informationresource.id'))

    def __init__(self, public_id, title, date_of_publication, publication_url):
        self.public_id = public_id
        self.title = title
        self.date_of_publication = date_of_publication
        self.publication_url = publication_url


# класс для работы с полями в таблице User
class PublicationSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'title', 'date_of_publication', 'publication_url')


# объекты для отправки и приёмов запросов
publication_schema = PublicationSchema()
publications_schema = PublicationSchema(many=True)
