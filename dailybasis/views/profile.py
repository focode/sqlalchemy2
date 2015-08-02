from dailybasis.databases.database import db_session,Base
from dailybasis.databases.models import User,Profile
from flask import Flask,render_template, request, jsonify,Blueprint,url_for,redirect,session,g,flash,abort
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask import json
from flask import Response

mod = Blueprint('profiles', __name__,template_folder='templates')

@mod.route('/allprofiles',methods=['POST','GET'])
def allprofiles():
#    profiles = Profile.query.all()
#    values = [profiles.to_json() for profile in profiles]
#    print values
    val2 = db_session.query(Profile).all()
    val3 = map(Profile.to_json,val2)
    print val3
    return jsonify({'devices': val3})
#    return val3
#    return jsonify(val3)
#    resp = Response(val3, status=200, mimetype='application/json')
#    return  resp
#    return json_response(val2)

#    return render_template('/forms/allprofiles.html')


def _todo_response(todo):
    return jsonify(**todo.to_json())


