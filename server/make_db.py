from application.common.const import KEYWORDS, ENTERPRISES
from application.models import KeyWord, Enterprise
from application import app, db


def fill():
    keyword_objects = [KeyWord(keyword) for keyword in KEYWORDS]
    for keyword_object in keyword_objects:
        db.session.add(keyword_object)
        db.session.commit()

    enterprises_objects = [Enterprise(enterprise) for enterprise in ENTERPRISES]
    for enterprise_object in enterprises_objects:
        db.session.add(enterprise_object)
        db.session.commit()


def make_db():
    db.drop_all()
    db.create_all()
    fill()

