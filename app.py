from databases.database import db_session
from databases.models import User
from flask import Flask,render_template, request, jsonify

app = Flask(__name__)


@app.route('/milkprofile', methods=['POST','GET'])
def milkprofile():

	return render_template('forms/editscreen.html')

@app.route('/milkprofileForm', methods=['POST','GET'])
def postprofile():
	print "something is comming here"
	contactnoo =  request.form['contactno'];
	print "Value of contactnoo is :",contactnoo,request.form
	print request
	dateval = request.form['dateofdelivery'];
	print "value of date=",
	return 'OK'



@app.route('/abc')
def hello_world():
    u = User('admin', 'admin@localhost')
    db_session.add(u)
    db_session.commit()

    return 'Hello World!'


if __name__ == '__main__':

    app.debug = True
    app.run()

