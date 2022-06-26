from application.common.const import KEYWORDS, ENTERPRISES
from application.models import KeyWord, Enterprise
from application import app, db

def fill():
    keyword_objects = [KeyWord(keyword) for keyword in KEYWORDS]
    if keyword_objects:
        db.session.bulk_save_objects(keyword_objects)
        db.session.commit()

    enterprises_objects = [Enterprise(enterprise) for enterprise in ENTERPRISES]
    if enterprises_objects:
        db.session.bulk_save_objects(enterprises_objects)
        db.session.commit()