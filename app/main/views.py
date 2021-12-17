from flask.templating import render_template
from app.main import main

@main.route('/')
def index():
    return render_template('main/index.html')