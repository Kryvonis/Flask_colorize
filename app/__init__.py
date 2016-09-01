from flask import Flask,Blueprint

app = Flask(__name__)
app.config.from_object('config')

from .views import main_view
