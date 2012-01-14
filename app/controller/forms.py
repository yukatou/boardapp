# -*- coding: utf-8 -*-

from flaskext.wtf import Form, TextField, TextAreaField, PasswordField, validators

class EntryForm(Form):
    title = TextField(u'タイトル', [validators.required(), validators.Length(max=255)])
    text = TextAreaField(u'内容', [validators.required()])

class LoginForm(Form):
    username = TextField(u'ユーザ名', [validators.required()])
    password = PasswordField(u'パスワード', [validators.required()])

class CreateUserForm(Form):
    username = TextField(u'ユーザ名', [validators.required()])
    password = PasswordField(u'パスワード', [validators.required()])
    repassword = PasswordField(u'パスワード(確認)', [
        validators.required(),
        validators.EqualTo('password', message=u"パスワードが一致しません")
    ])


