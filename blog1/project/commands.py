from project import app, db
from project.models import User, Article
import click

@app.cli.command()
def initdb():
    db.create_all()
    admin = User(username='admin', password='12345')
    db.session.add(admin)
    initial = Article(id=1, title='Hello', author='TuringC', body='Welcome to my blog!')
    db.session.add(initial)
    db.session.commit()
    click.echo('Initialized Database.')