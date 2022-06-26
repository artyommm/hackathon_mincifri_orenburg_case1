from application import db, ma


class Publication(db.Model):
    # __table_args__ = {'extend_existing': True}
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45), nullable=False)
    date_of_publication = db.Column(db.Date, nullable=False)
    publication_url = db.Column(db.String(200), nullable=False)
    information_resource = db.Column(db.Text, nullable=False)

    # промежуточные таблицы для создания отношений----------------------------------------------------------------

    # публикация_ключевоеслово
    publication_keyword = db.Table('publication_keyword',
                                   db.Column('publication_id', db.Integer, db.ForeignKey('publication.id')),
                                   db.Column('keyword_id', db.Integer, db.ForeignKey('keyword.id'))
                                   )
    # -------------------------------------------------------------------------------------------------------------

    # отношения с другими таблицами
    keyWord_id = db.relationship('KeyWord', secondary=publication_keyword,
                                 backref=db.backref('publication', lazy='select'))

    enterprise_id = db.Column(db.Integer(), db.ForeignKey('enterprise.id'))

    def __init__(self, title, date_of_publication, publication_url, enterprise_id, information_resource):
        self.title = title
        self.date_of_publication = date_of_publication
        self.publication_url = publication_url
        self.enterprise_id = enterprise_id
        self.information_resource = information_resource


    def __eq__(self, other):
        return self.title == other.title


# класс для работы с полями в таблице User
class PublicationSchema(ma.Schema):
    class Meta:
        fields = (
            'title', 'date_of_publication', 'publication_url', 'enterprise_id', 'information_resource')


# объекты для отправки и приёмов запросов
publication_schema = PublicationSchema()
publications_schema = PublicationSchema(many=True)
