from flask import flash, redirect, url_for, render_template, session, request, current_app, abort
from flask_login import login_user, logout_user
from flask_sqlalchemy import Pagination
# import timedelta

from project import app, db, bootstrap
from project.models import Article, User
from project.forms import ArticleInput, LoginForm, DeleteNoteForm


@app.route('/', methods=['GET', 'POST'])
def index(logged_in=False, user=None):
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.id.desc()).paginate(page=page, per_page=5, error_out = False)
    articles = pagination.items
    return render_template('index.html', bootstrap=bootstrap, pagination=pagination, articles=articles)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user, remember=True)
            # 设置session过期时间 过期时间一天
            # session.permanent = True
            # app = current_app._get_current_object()
            # app.permanent_session_lifetime = timedelta(days=1)
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    form.password.data = ''
    return render_template('login.html', form=form)


@app.route('/personalPage', methods=['GET', 'POST'])
def personalPage():
    form = DeleteNoteForm()
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.id.desc()).paginate(page=page, per_page=5, error_out=False)
    articles = pagination.items
    return render_template('personalPage.html', bootstrap=bootstrap, pagination=pagination, articles=articles, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/new_article', methods=['GET','POST'])
def new():
    form = ArticleInput()
    if form.validate_on_submit():
        title = form.title.data
        author = request.args.get('user')
        body = form.body.data
        # article = Article(title=title, author=author, body=body)
        article = Article(title=title, author='admin', body=body)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_article.html', form=form)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    form = DeleteNoteForm()
    if form.validate_on_submit():
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()
        flash('Your blog is deleted.')
    else:
        abort(400)
    return redirect(url_for('personalPage'))