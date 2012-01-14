# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from app.model.entry import EntryModel
from app.model.user import UserModel

app = Blueprint('board', __name__)

@app.route('/')
def index():
    entries = EntryModel().get_entries()
    return render_template('index.html', entries=entries)

@app.route('/user/add', methods=['POST', 'GET'])
def add_user():
    return "add"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return redirect(url_for('.index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash(u"ログアウトしました")
    return redirect(url_for('.index'))
