from flask import Flask, session, g, render_template
from views import milkprofile

app = Flask(__name__)
#app.config.from_object('websiteconfig')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.before_request
def load_current_user():
    g.user = User.query.filter_by(openid=session['openid']).first() \
        if 'openid' in session else None


@app.teardown_request
def remove_db_session(exception):
    db_session.remove()


app.add_url_rule('/docs/', endpoint='docs.index', build_only=True)
app.add_url_rule('/docs/<path:page>/', endpoint='docs.show',
                 build_only=True)
app.add_url_rule('/docs/flask-docs.pdf', endpoint='docs.pdf',
                 build_only=True)
app.add_url_rule('/docs/flask-docs.zip', endpoint='docs.zip',
                 build_only=True)

from dailybasis.views import milkprofile

app.register_blueprint(milkprofile.mod)

from dailybasis.databases.database import db_session

