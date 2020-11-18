import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Todo: from dicepy.lib.middleware.auth_middleware import login_required
from dicepy.lib.database.create_db import *

# Load environment variables
load_dotenv()

def create_app(test_config=None):
    
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY')
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    create_all_tables()
    
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html', title='DicePy - Index')
    
    return app