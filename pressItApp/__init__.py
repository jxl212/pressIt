from flask import Flask
from pressItApp import config

app = Flask(__name__)
app.config.from_object(config.Config)

from pressItApp import views
