from databases.database import db_session
from databases.models import User,Profile
from flask import Flask,render_template, request, jsonify

app = Flask(__name__)


@app.route('/milkprofile', methods=['POST','GET'])
def milkprofile():

	return render_template('forms/editscreen.html')

@app.route('/milkprofileForm', methods=['POST','GET'])
def postprofile():
    start_date = request.form['start_date']
    delivery_days = request.form['delivery_days']
    milk_type = request.form['milk_type']
    quantity = request.form['quantity']
    brand = request.form['brand']
    name = request.form['name']
    address = request.form['address']
    pincode = request.form['pincode']
    contact_no = request.form['contact_no']
    profile = Profile(milk_type,quantity,brand,start_date,delivery_days,name,address,pincode,contact_no)
    db_session.add(profile)
    db_session.commit()
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

