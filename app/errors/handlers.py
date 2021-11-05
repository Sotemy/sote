from flask.templating import render_template
from app.errors import error

@error.app_errorhandler(404)
def e404(error):
    return render_template('errors/404.html', error=error)

@error.app_errorhandler(500)
def e500(error):
    return render_template('errors/500.html', error=error)