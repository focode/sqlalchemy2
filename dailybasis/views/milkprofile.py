from dailybasis.databases.database import db_session
from dailybasis.databases.models import User,Profile
from flask import Flask,render_template, request, jsonify,Blueprint,url_for,redirect,session,g,flash,abort


mod = Blueprint('milk', __name__,template_folder='templates')

app = Flask(__name__)

@mod.route('/milkprofile', methods=['POST','GET'])
def milkprofile():

	return render_template('forms/editscreen.html')

@mod.route('/milkprofileForm', methods=['POST','GET'])
def postprofile():

    print request.form
    start_date_time = request.form['start_date']
    start_date_time = '2014-04-02 08:49:43'
    print "start_date:",start_date_time
    All = request.form['All']
    Sunday = request.form['Sunday']
    Monday = request.form['Monday']
    Tuesday = request.form['Tuesday']
    Wednesday = request.form['Wednesday']
    Thursday = request.form['Thursday']
    Friday = request.form['Friday']
    Saturday = request.form['Saturday']

    print "All:",All,"Sunday:",Sunday,"Monday:",Monday,"Tuesday:",Tuesday,"Wednesday:",Wednesday,"Thursday:",Thursday,"Friday:",Friday,"Saturday:",Saturday
    milk_type = request.form['milk_type']
    print "milk_type:",milk_type
    quantity = request.form['quantity']
    print "quantity:",quantity
    brand = request.form['brand']
    print "brand:",brand
    name = request.form['name']
    print "name:",name
    address = request.form['address']
    print "address:",address
    pincode = request.form['pincode']
    print "pincode:",pincode
    contact_no = request.form['contact_no']
    print "contact_no:",contact_no
    profile = Profile(milk_type,quantity,brand,start_date_time,"rtyui",name,address,pincode,contact_no)
    db_session.add(profile)
    db_session.commit()
    return render_template('/forms/allprofiles.html')
#    allprofiles()
#    redirect(url_for('milk.allprofiles'))
#   return render_template('/forms/allprofiles.html', meassage='ok')
#    return  redirect(url_for('milk.allprofiles'))
#    return render_template('/forms/allprofiles.html', meassage='ok')
#    return redirect (url_for('milk.allprofiles'))

@mod.route('/')
def home():
    return render_template('/forms/home.html')




@mod.route('/abc')
def hello_world():
    u = User('admin', 'admin@localhost')
    db_session.add(u)
    db_session.commit()

    return 'Hello World!'


if __name__ == '__main__':

    app.debug = True
    app.run()

