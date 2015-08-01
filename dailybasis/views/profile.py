from dailybasis.databases.database import db_session,Base
from dailybasis.databases.models import User,Profile
from flask import Flask,render_template, request, jsonify,Blueprint,url_for,redirect,session,g,flash,abort

mod = Blueprint('profiles', __name__,template_folder='templates')

@mod.route('/allprofiles')
def allprofiles():
    profiles = Profile.query.all()
    print profiles
    val2 = db_session.query(Profile).all()
    print val2

    return render_template('/forms/allprofiles.html')


