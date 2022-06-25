from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)

# убираем ошибку CORS
CORS(app)

# конфиг
# app.config['UPLOAD_FOLDER'] = 'C:/Users/mauta/Desktop/project-Tensor-main/Backend/upload'
app.config['SECRET_KEY'] = 'ORENBOOGLE'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:postgres@localhost:6432/orenboogle_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# временно не работает, т.к. моделей и роутов ещё нет
# from application import models, route
