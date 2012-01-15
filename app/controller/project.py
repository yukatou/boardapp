# -*- coding: utf-8 -*-

from flask import Module,Blueprint, render_template, request, redirect, url_for, flash, session, abort
from flaskext.oauth import OAuth
from app.model.entry import EntryModel
from app.model.user import UserModel
from app.controller.forms import EntryForm, LoginForm, CreateUserForm
from app.controller.component.pagination import Pagination

PER_PAGE = 5
#app = Blueprint('board', __name__)
app = Module(__name__)

oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key='E7xMzCcx6yoONKkQMXXNQ',
    consumer_secret='sB8iO1pvFKS6eRegFBkXkP34PCoxiAhXLTB6myzf4M'
)

@twitter.tokengetter
def get_twitter_token():
    return session.get('twitter_token')

@app.route('/', defaults={'page': 1})
@app.route('/page/<int:page>')
def index(page):
    count = EntryModel.get_all_count()
    start = (page - 1) * PER_PAGE  
    end = start + PER_PAGE
    entries = EntryModel.get_entries(start, end)
    if not entries and page != 1:
      abort(404)
    pagination = Pagination(page, PER_PAGE, count)
    return render_template('index.html', entries=entries, pagination=pagination)

@app.route('/user/add', methods=['POST', 'GET'])
def add_user():
    error = None
    form = CreateUserForm()
    if form.validate_on_submit():
        try:
            UserModel.save(username=request.form['username'], password=request.form['password'])
        except Exception, e:
            error = u"そのユーザ名は登録できません"
        else:
            flash(u"登録が完了しました")
            return redirect(url_for('index'))

    elif form.is_submitted() and not error:
        error = u"入力値が正しくありません"

    return render_template('add_user.html', form=form, error=error)

@app.route('/entry/add', methods=['POST', 'GET'])
def add_entry():
    error = None
    form = EntryForm()

    if not 'screen_name' in session:
        abort(403)

    if form.validate_on_submit():
        EntryModel.save(title=request.form['title'],
                        text=request.form['text'],
                        username=session['screen_name'])

        flash(u"投稿しました")
        return redirect(url_for('index'))

    return render_template('add_entry.html', form=form, error=error)

@app.route('/login', methods=['GET'])
def login():
    return twitter.authorize(callback=url_for('oauth_authorized', next=request.args.get('next') or request.referrer or None))

@app.route('/logout')
def logout():
    session.pop('screen_name', None)
    session.pop('twitter_token', None)
    flash(u"ログアウトしました")
    return redirect(url_for('index'))


@app.route('/oauth-authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u"You denied the request sigh in.")
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )

    session['screen_name'] = resp['screen_name']
    print resp
    flash(u"You were signed in as %s" % resp['screen_name'])
    return redirect(next_url)

