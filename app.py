from flask import Flask, render_template
from config import Config
from database import db






if __name__ == '__main__':
    
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app) 
    app.run(debug=True)


from routes import *