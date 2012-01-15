from flask import Flask, request, url_for
from app.db import session_remove
from app.controller.project import app as project

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_module(project)

@app.after_request
def shutdown_session(response):
    session_remove()
    return response


def url_for_other_page(page):
  args = request.view_args.copy()
  args['page'] = page
  return url_for(request.endpoint, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page
