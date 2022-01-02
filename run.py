from app import app, db
from app.models import User, Role

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Role': Role}

context=('docs/cert.pem', 'docs/key.pem')

# ssl_context=context

if __name__ == '__main__':
    app.run()