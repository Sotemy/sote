from app import app, db
from app.models import Category, Post, Tag, User, Role

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 
            'User': User, 
            'Role': Role, 
            'Post':Post, 
            'Tag':Tag, 
            'Category':Category}

context=('docs/cert.pem', 'docs/key.pem')

# ssl_context=context

if __name__ == '__main__':
    app.run()