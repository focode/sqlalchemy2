from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base
from werkzeug.security import generate_password_hash, check_password_hash
import json

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Profile(Base):
    __tablename__ = 'profile'
    idprofile = Column(Integer,primary_key=True)
    milk_type = Column(String(450))
    quantity = Column(Integer)
    brand = Column(String(450))
    start_date_time = Column(TIMESTAMP)
    delivery_days = Column(String(450))
    name = Column(String(450))
    address = Column(String(450))
    pincode = Column(String(450))
    contact_no = Column(String(450))

    def __init__(self,milk_type=None,quantity=None,brand=None,start_date_time=None,delivery_days=None,name=None,address=None,pincode=None,contact_no=None):
        self.milk_type = milk_type
        self.quantity = quantity
        self.brand = brand
        self.start_date_time = start_date_time
        self.delivery_days = delivery_days
        self.name = name
        self.address = address
        self.pincode = pincode
        self.contact_no = contact_no

    def __str__(self):
        """Return the string representation of a mention."""
        return self.text

    def to_json(self):
        return {
                "milk_type": self.milk_type,
                "quantity": str(self.quantity),
                "brand": self.brand,
                "start_date_time": str(self.start_date_time),
                "delivery_days": str(self.delivery_days),
                "name": self.name,
                "address": str(self.address),
                "pincode": str(self.pincode),
                "contact_no": self.contact_no}

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer , primary_key=True)
    username = Column('username', String(20), unique=True , index=True)
    password = Column('password' , String(10))
    email = Column('email',String(50),unique=True , index=True)


    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email

    def set_password(self , password):
        self.password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password , password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)





