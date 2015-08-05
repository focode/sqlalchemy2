from dailybasis.databases.database import db_session
from dailybasis.databases.models import User,Profile
from flask import Flask,render_template, request, jsonify,Blueprint,url_for,redirect,session,g,flash,abort
from flask_login import LoginManager
from flask_login import login_user , logout_user , current_user , login_required

login_manager = LoginManager()

app = Flask(__name__)
login_manager.init_app(app)

login_manager.login_view = 'login'

mod = Blueprint('auth', __name__,template_folder='templates')

@mod.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@mod.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = User.query.filter_by(username=username).first()
    if registered_user is None:
        flash('Username is invalid' , 'error')
        return redirect(url_for('login'))
    if not registered_user.check_password(password):
        flash('Password is invalid','error')
        return redirect(url_for('login'))
    login_user(registered_user, remember = remember_me)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
