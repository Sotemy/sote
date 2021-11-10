from app import app, db, mail
from app.models import Post, User, Role

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Role': Role, 'Post':Post}

if __name__ == '__main__':
    app.run()