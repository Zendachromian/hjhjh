from flask import Flask, render_template
from models import *
app = Flask(__name__)

import config


import api

import routes


if __name__ == '__main__':
    app.run(debug=True)