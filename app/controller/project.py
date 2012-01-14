# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from app.model.entry import EntryModel
from app.model.user import UserModel
from app.controller.forms import EntryForm, LoginForm, CreateUserForm

app = Blueprint('board', __name__)

@app.route('/')
def index():
    entries = EntryModel().get_entries()
    return render_template('index.html', entries=entries)

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
            return redirect(url_for('.index'))

    elif form.is_submitted() and not error:
        error = u"入力値が正しくありません"

    return render_template('add_user.html', form=form, error=error)

@app.route('/entry/add', methods=['POST', 'GET'])
def add_entry():
    error = None
    form = EntryForm()

    if not 'user' in session:
        abort(403)

    if form.validate_on_submit():
        EntryModel.save(title=request.form['title'],
                        text=request.form['text'],
                        user_id=session['user'].id)

        flash(u"投稿しました")
        return redirect(url_for('.index'))

    return render_template('add_entry.html', form=form, error=error)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = UserModel.get(username=username, password=password)
    if user:
        session['user'] = user
        flash(u"ログイン完了しました")
    else:
        flash(u"ログイン失敗しました")

    return redirect(url_for('.index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash(u"ログアウトしました")
    return redirect(url_for('.index'))
