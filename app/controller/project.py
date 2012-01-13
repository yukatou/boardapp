from flask import Module, render_template
from app.model.entry import EntryModel

project = Module(__name__)

@project.route('/')
def index():
    entry = EntryModel()
    return render_template('project.html', entry=entry)

